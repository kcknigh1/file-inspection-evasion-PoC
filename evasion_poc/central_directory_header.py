"""This is the implementation of the central directory header

This implements the central directory class and methods
"""
from . import utils


class CentralDirectoryHeader:
    """ A class used to represent a Central Directory Header

    This class is built from the string representation of a central directory 
    header in hex format. It allows access to diffrent fields in string for
    reading and writing.

    """

    def __init__(self, header_hex) -> None:
        """Stores the hex representation of the central directory header

        Args:
            header_hex (str): The original version of this header in hex
                format
        """
        self._header_hex = header_hex

    def get_file_name_length(self):
        """Get the length of the file name as int

        Returns:
            int: length of file name
        """
        return utils.hex_to_int(utils.get_header_field(self._header_hex, 28, 2))

    def get_file_name(self):
        """Get the name of the file

        Returns:
            str: file name
        """
        return utils.hex_to_str(
            utils.get_header_field(self._header_hex, 46,
                                   self.get_file_name_length()))

    def get_relative_local_header_offset(self):
        return utils.hex_to_int(utils.get_header_field(self._header_hex, 42, 4))

    def get_header(self):
        return self._header_hex

    def shift_relative_local_header_offset(self, shift_by):
        """Shifts the relative offset of local file header

        The relative offset is the number of bytes from the start of the file to
        the start of the local file header. This function is used to shift that 
        number to account for something being prepended to the file before the 
        local file header.

        Args:
            shift_by (int): the number of bytes to shift the offset by. Should
            be the size of what ever was prepended.  
        """
        new_offset = self.get_relative_local_header_offset() + shift_by
        # splices in the new offset. Have to multiply the indexes by 2 to
        # account for the byte size.
        self._header_hex = (f'{self._header_hex[:42*2]}'
                            f'{utils.int_to_hex(new_offset, 4)}'
                            f'{self._header_hex[46*2:]}')
