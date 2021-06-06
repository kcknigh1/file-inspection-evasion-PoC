"""The test file for the end central dir header class"""

import unittest
import exploit.end_central_dir_header as end_central_header


class TestEndCentralDirHeaderInit(unittest.TestCase):
    def test_end_central_dir_header(self):
        header_hex = '504b050600000000010001005b000000278e00000000'
        end_header = end_central_header.EndCentralDirectoryHeader(header_hex)
        self.assertEqual(end_header._header_hex, header_hex)
        self.assertEqual(end_header._num_central_dir_records, 1)
        self.assertEqual(
            end_header._offset_start_central_dir_from_start, 36391)
        self.assertEqual(end_header._comment_length, 0)
# class TestEndCentralDirHeaderGetNum(unittest.TestCase):