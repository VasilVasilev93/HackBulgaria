from os import remove
import unittest
from cat import cat


class Test_Cat(unittest.TestCase):

    def setUp(self):
        self.filename = 'test.txt'
        self.content = """This is some file
And cat is printing it's contents"""
        with open(self.filename, 'w') as file:
            file.write(self.content)

    def tearDown(self):
        remove(self.filename)

    def test_cat_with_existing_file(self):
        actual = cat(self.filename)
        self.assertEqual(self.content, actual)

if __name__ == '__main__':
    unittest.main()
