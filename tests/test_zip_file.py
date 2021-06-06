import unittest
import exploit.zip_file as zf
# @unittest.skip("Not implemented yet")


class TestSplitCentralDirectory(unittest.TestCase):

    # def test_split_central_directroy_not_zip_file(self):
    #     # test_docs/file1.txt
    #     file_hex = '546869732069732074686520636f6e74656e7473206f662066696c65312e'
    #     central_directory, other_contents = fie._split_zip_file_into_sections(
    #         file_hex)
    #     self.assertEqual(central_directory, '12121')
    #     self.assertEqual(other_contents, '12121')

    # @unittest.skip("Not implemented yet")
    def test_split_central_directroy_zip_with_one_file(self):
        # test_docs/file1.zip
        file_hex = ('504b03040a00000000000581c2521591b5fb1e0000001e0000000900'
                    '000066696c65312e747874546869732069732074686520636f6e7465'
                    '6e7473206f662066696c65312e504b01023f000a00000000000581c2'
                    '521591b5fb1e0000001e000000090024000000000000002000000000'
                    '00000066696c65312e7478740a0020000000000001001800de973a63'
                    'f357d70159f6f1fc8d58d701a1b18f58f357d701504b050600000000'
                    '010001005b000000450000000000')
        local_files, central_directory, end_central_directory = zf._split_zip_file_into_sections(
            file_hex)
        self.assertEqual(
            local_files, ('504b03040a00000000000581c2521591b5fb1e0000001e00000'
                          '00900000066696c65312e747874546869732069732074686520'
                          '636f6e74656e7473206f662066696c65312e'))
        self.assertEqual(
            central_directory, ('504b01023f000a00000000000581c2521591b5fb1e0000'
                                '001e000000090024000000000000002000000000000000'
                                '66696c65312e7478740a0020000000000001001800de97'
                                '3a63f357d70159f6f1fc8d58d701a1b18f58f357d701'))
        self.assertEqual(end_central_directory._header_hex,
                         '504b050600000000010001005b000000450000000000')

    # @unittest.skip("Not implemented yet")
    def test_split_central_directroy_zip_with_multiple_file(self):
        # test_docs/files.zip
        file_hex = ('504b03040a00000000000581c2521591b5fb1e0000001e00000009000'
                    '00066696c65312e747874546869732069732074686520636f6e74656e'
                    '7473206f662066696c65312e504b03040a00000000000f81c252d6c29'
                    '8d01e0000001e0000000900000066696c65322e747874546869732069'
                    '732074686520636f6e74656e7473206f662066696c65322e504b01023'
                    'f000a00000000000581c2521591b5fb1e0000001e0000000900240000'
                    '0000000000200000000000000066696c65312e7478740a00200000000'
                    '00001001800de973a63f357d701b79f25478e58d701a1b18f58f357d7'
                    '01504b01023f000a00000000000f81c252d6c298d01e0000001e00000'
                    '009002400000000000000200000004500000066696c65322e7478740a'
                    '0020000000000001001800fb016d6ff357d701b79f25478e58d701878'
                    'b6868f357d701504b05060000000002000200b60000008a0000000000')
        local_files, central_directory, end_central_directory = zf._split_zip_file_into_sections(
            file_hex)
        self.assertEqual(local_files, ('504b03040a00000000000581c2521591b5fb1e'
                                       '0000001e0000000900000066696c65312e7478'
                                       '74546869732069732074686520636f6e74656e'
                                       '7473206f662066696c65312e504b03040a0000'
                                       '0000000f81c252d6c298d01e0000001e000000'
                                       '0900000066696c65322e747874546869732069'
                                       '732074686520636f6e74656e7473206f662066'
                                       '696c65322e'))
        self.assertEqual(central_directory,
                         ('504b01023f000a00000000000581c2521591b5fb1e0000001e0'
                          '0000009002400000000000000200000000000000066696c6531'
                          '2e7478740a0020000000000001001800de973a63f357d701b79'
                          'f25478e58d701a1b18f58f357d701504b01023f000a00000000'
                          '000f81c252d6c298d01e0000001e00000009002400000000000'
                          '000200000004500000066696c65322e7478740a002000000000'
                          '0001001800fb016d6ff357d701b79f25478e58d701878b6868f'
                          '357d701'))
        self.assertEqual(end_central_directory._header_hex,
                         '504b05060000000002000200b60000008a0000000000')


if __name__ == '__main__':
    unittest.main()
