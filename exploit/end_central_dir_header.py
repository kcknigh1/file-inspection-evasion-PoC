"""This is the implementation of the end of central directory header
"""
from . import utils


class EndCentralDirectoryHeader:
    """Class that represents the end central directory header

    This class is built from the string representation of the end of the central
    directory header in hex format. It allows access to diffrent fields in
    string for reading and writing.
    """

    def __init__(self, header_hex) -> None:
        """Stores the hex representation of the end of central directory header

        Args:
            header_hex (str): The string version of the header in hex

        """
        self._header_hex = header_hex

    def get_header_hex(self):
        return self._header_hex

    def get_num_central_dir_records(self):
        return utils.hex_to_int(utils.get_header_field(self._header_hex, 8, 2))

    def get_size_central_dir_bytes(self):
        return utils.hex_to_int(utils.get_header_field(self._header_hex, 12, 4))

    def get_offset_start_central_dir_from_start(self):
        return utils.hex_to_int(utils.get_header_field(self._header_hex, 16, 4))

    def shift_start_central_dir_start_offset(self, shift_by):
        """Shifts the start of central directory value

        The start central directory value is the number of bytes from the start 
        of the file to the start of the central directory. This function is used
        to shift that number to account for something being prepended to the
        file before the the central directory.

        Args:
            shift_by (int): the number of bytes to shift the start by. Should
            be the size of what ever was prepended.  
        """
        new_offset = self.get_offset_start_central_dir_from_start() + shift_by
        # splices in the new offset. Have to multiply the indexes by 2 to
        # account for the byte size.
        self._header_hex = (f'{self._header_hex[:16*2]}'
                            f'{utils.int_to_hex(new_offset, 4)}'
                            f'{self._header_hex[20*2:]}')
