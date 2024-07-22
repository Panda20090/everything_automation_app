import unittest
import os
from list_files_and_directories import list_files_and_directories, save_file_list

class TestListFilesAndDirectories(unittest.TestCase):

    def test_list_files_and_directories(self):
        root_directory = "C:\\Users\\GunPr\\OneDrive\\Documents\\GitHub\\everything_automation_app"
        result = list_files_and_directories(root_directory)
        self.assertIn('files', result)
        self.assertIn('directories', result)

    def test_save_file_list(self):
        root_directory = "C:\\Users\\GunPr\\OneDrive\\Documents\\GitHub\\everything_automation_app"
        output_file = "test_file_list.txt"
        save_file_list(root_directory, output_file)
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)

if __name__ == '__main__':
    unittest.main()
