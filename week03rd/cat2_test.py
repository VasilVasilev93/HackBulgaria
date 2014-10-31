import unittest
from cat2 import cat2
from os import remove


class Test_cat2(unittest.TestCase):
    def setUp(self):
        self.single = 'file.txt'
        self.multiple = 'ghostfile.txt'
        self.multipleContets = """This is some file
And cat is printing it's contentsSecond file!
"""

        self.singleContents = """This is some file
And cat is printing it's contents"""

        with open(self.multiple, 'w+') as file:
            file.write(self.multipleContets)

        with open(self.single, 'w+') as file:
            file.write(self.singleContents)

    def tearDown(self):
        remove(self.multiple)

    def test_cat2_with_single_file(self):
        actual = cat2(['file.txt'])
        self.assertEqual(self.singleContents, actual)

    def test_cat2_with_multiple_files(self):
        actual = cat2(['file.txt', 'file1.txt'])
        self.assertEqual(self.multipleContets, actual)

if __name__ == '__main__':
    unittest.main()
