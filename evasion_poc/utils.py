"""This consists of some helper functions"""


def hex_to_int(hex):
    """Converts hex to int

    Args:
        hex (str): string representation of hex value

    Returns:
        int: the value of the hex in int format
    """
    hex_bytes = bytearray.fromhex(hex)
    hex_bytes.reverse()
    hex_str = ''.join(format(x, '02x') for x in hex_bytes)
    num = int(hex_str, 16)
    return num


def int_to_hex(num, len_bytes):
    """Converts int to hex

    Args: 
        num (int): number to convert

    Returns:
        str: string version of int
    """
    hex_str = hex(num)
    # remove the prefix 0x
    hex_str = hex_str[2:]
    if len(hex_str) % 2:
        hex_str = f'0{hex_str}'
    hex_bytes = bytearray.fromhex(hex_str)
    hex_bytes.reverse()
    hex_str = ''.join(format(x, '02x') for x in hex_bytes)
    while len(hex_str) < len_bytes*2:
        hex_str = f'{hex_str}0'
    return hex_str


def hex_to_str(hex) -> str:
    """Converts the hex to he ascii values of the bytes

    Args:
        hex (str): The hex value to be converted in string format 

    Returns:
        str: The ascii representation of the hex
    """
    return bytearray.fromhex(hex).decode()


def get_header_field(header, start_offset, length_in_bytes) -> str:
    """Gets a field from the header

    Gets a section of the bytes from the header that represents a field

    Args:
        header (str): The header containing the fields in bytes
        start_offset (int): The offset from th start of the header to the
                            start of the field
        length_in_bytes (int): Length of the field in bytes

    Returns:
        str: The field selected from the header
    """
    # have to multiple by to because one byte is 2 chars
    return header[start_offset*2:start_offset*2 + length_in_bytes*2]
