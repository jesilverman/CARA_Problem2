import re,os
import unittest
from writeKVFiles import main as write_main

class TestWriteFile(unittest.TestCase):
    def setUp(self):
        pass

    def test_file_format(self):
        write_main
        with open("keyValuefile_0.kv", "r") as test_file:
            for line in test_file.readlines():
               self.assertEqual(re.match(line, ".+=.+")

    def test_number_files(self):
        write_main
        list=os.listdir("*.kv")
        self.assertEqual(len(list), numFiles)


if name == "__main__":
    unittest.main()

