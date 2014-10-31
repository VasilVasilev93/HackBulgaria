import unittest
from concat import concat
from os import remove


class Test_cat2(unittest.TestCase):
    def setUp(self):
        self.first = 'file.txt'
        self.second = 'file1.txt'
        self.concat = 'concat.txt'
        self.concatenated = """This is some file
And cat is printing it's contents
Second file!
"""
        self.firstContent = """This is some file
And cat is printing it's contents"""

        self.secondContent = """Second file!"""

        with open(self.concat, 'w') as file:
            file.write(self.concatenated)

        with open(self.first, 'w+') as file:
            file.write(self.firstContent)

        with open(self.second, 'w+') as file:
            file.write(self.secondContent)

    def tearDown(self):
        remove(self.concat)

    def test_concat_with_2_files(self):
        actual = concat(["file.txt", "file1.txt", "concat.txt"])
        self.assertEqual(self.concatenated, actual)

if __name__ == '__main__':
    unittest.main()
