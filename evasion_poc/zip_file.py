"""Implements the file structure of a zip file"""

from evasion_poc.central_directory_header import CentralDirectoryHeader
from .end_central_dir_header import EndCentralDirectoryHeader
from .utils import get_header_field


class Zip_file:
    """Class that represents the zip file structure"""

    def __init__(self, file_hex) -> None:
        """Splits the provied file_hex into the zip file structure

        Args:
            file_hex (str): The string representation of the files hex
        """
        self._file_hex = file_hex
        self._local_file_headers, self._central_dir, self._end_central_dir = self._split_zip_file_into_sections(
            file_hex)
        self.central_directory_list = self._split_central_dir()

    def get_local_file_headers(self):
        return self._local_file_headers

    def get_central_dir_hex(self):
        """Compiles the hex for the central_dir

        Returns:
            str: the hex for the central directory
        """
        central_dir_hex = ''
        for header in self.central_directory_list:
            central_dir_hex = f'{central_dir_hex}{header.get_header()}'

        return central_dir_hex

    def get_end_central_dir(self):
        return self._end_central_dir

    def get_central_dir_list(self):
        return self.central_directory_list

    def _split_central_dir(self):
        """Splits the central directory hex into the different headers

        creates a list of the central directory headers each one is a 
        CentralDirectoryHeader object

        Returns:
            list(CentralDirectoryHeader): list of all the central directory 
                headers
        """
        split_central_directory_headers = self._central_dir.split('504b0102')
        central_directory_list = []
        # first one is blank so skipped
        # adds the magic number back so the hex is the right length
        for header in split_central_directory_headers[1:]:
            central_directory_list.append(
                CentralDirectoryHeader(f'504b0102{header}'))

        return central_directory_list

    def prepend_file(self, file_hex):
        """Adds a file to the beginning of the local file headers

        After the file is added, adjusts the central directory offsets to
        account for the new file.
        """
        new_file_byte_length = int(len(file_hex)/2)
        self._local_file_headers = f'{file_hex}{self._local_file_headers}'

        for header in self.get_central_dir_list():
            header.shift_relative_local_header_offset(new_file_byte_length)

        self._end_central_dir.shift_start_central_dir_start_offset(
            new_file_byte_length)

    def _split_zip_file_into_sections(self, file_hex):
        """Splits the zip file_hex into the central directory other headers

        Args:
            file_hex (str): The hex code of the file to split

        Returns:
            tuple: (local_files (str): The local files section of the zip,
                    central_directory (str): The central directory of the zip
                    end_central_directory_header (str): The end central directory 
                        header)
        """
        split_end_central_directory_header = file_hex.split('504b0506')
        end_central_directory_header = EndCentralDirectoryHeader(
            f'504b0506{split_end_central_directory_header[-1]}')

        central_directory = get_header_field(
            file_hex, end_central_directory_header.get_offset_start_central_dir_from_start(),
            end_central_directory_header.get_size_central_dir_bytes())

        local_files = file_hex[:end_central_directory_header.get_offset_start_central_dir_from_start(
        )*2]

        return (local_files, central_directory, end_central_directory_header)
