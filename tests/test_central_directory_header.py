import unittest
import exploit.central_directory_header as central_directory_header


class TestHexToInt(unittest.TestCase):
    #  TODO update test names and add docs
    def test_hex_to_int_0900(self):
        num = central_directory_header._hex_to_int('0900')
        self.assertEqual(num, 9)

    def test_hex_to_int_efbe(self):
        num = central_directory_header._hex_to_int('efbe')
        self.assertEqual(num, 48879)

    def test_hex_to_int_abdcea0d(self):
        num = central_directory_header._hex_to_int('abdcea0d')
        self.assertEqual(num, 233495723)

    def test_hex_to_int_b1d8a7(self):
        num = central_directory_header._hex_to_int('b1d8a7')
        self.assertEqual(num, 10999985)

    def test_hex_to_int_1e000000(self):
        num = central_directory_header._hex_to_int('1e000000')
        self.assertEqual(num, 30)


class TestHexToStr(unittest.TestCase):

    def test_hex_to_str_hello(self):
        string = central_directory_header._hex_to_str('68656c6c6f')
        self.assertEqual(string, 'hello')

    def test_hex_to_str_hello_world(self):
        string = central_directory_header._hex_to_str(
            '68656c6c6f20776f726c64')
        self.assertEqual(string, 'hello world')

    def test_hex_to_str_numbers_and_letters(self):
        string = central_directory_header._hex_to_str('7131773265337234')
        self.assertEqual(string, 'q1w2e3r4')


class TestGetHeaderField(unittest.TestCase):
    header = ('504b01023f000a00000000000581c2521591b5fb1e0000001e00000009'
              '002400000000000000200000000000000066696c65312e7478740a0020'
              '000000000001001800de973a63f357d70159f6f1fc8d58d701a1b18f58'
              'f357d701')

    def test_get_header_field_get_first_field(self):
        field = central_directory_header._get_header_field(self.header, 0, 4)
        self.assertEqual(field, '504b0102')

    def test_get_header_field_get_middle_field(self):
        field = central_directory_header._get_header_field(self.header, 46, 9)
        self.assertEqual(field, '66696c65312e747874')

    # def test_get_header_field_get_end_field(self):
    #     field = central_directory_header._get_header_field(
    #         self.header, 46, 600)
    #     self.assertEqual(field, '66696c65312e747874')


if __name__ == '__main__':
    unittest.main()
