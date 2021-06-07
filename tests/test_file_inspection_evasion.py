from exploit import central_directory_header
import unittest
import exploit.file_inspection_evasion as fie


class TestCreateNewFilePath(unittest.TestCase):

    def test_create_new_file_path_file_in_same_folder(self):
        file_loc = 'test.txt'
        new_path = fie._create_new_file_path(file_loc)
        self.assertEqual(new_path, 'flags_test.txt')

    def test_create_new_file_path_file_in_subfolder(self):
        file_loc = 'test_docs/test.txt'
        new_path = fie._create_new_file_path(file_loc)
        self.assertEqual(new_path, 'test_docs\\flags_test.txt')

# if __name__ == '__main__':
#     unittest.main()
