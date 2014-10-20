import unittest
from reducepath import reduce_file_path


class Test_reducepath(unittest.TestCase):
    def test_reduce_file_path_with_empty_path(self):
        input = ""
        output = ""
        result = reduce_file_path(input)
        self.assertEqual(result, output)

    def test_reduce_file_path_with_single_character_path(self):
        input = "a"
        output = "a"
        result = reduce_file_path(input)
        self.assertEqual(result, output)

    def test_reduce_file_path_with_2_characters_path(self):
        input = "ab"
        output = "ab"
        result = reduce_file_path(input)
        self.assertEqual(result, output)

    def test_reduce_file_path_with_slash_only(self):
        input = "/"
        output = "/"
        result = reduce_file_path(input)
        self.assertEqual(result, output)

    def test_reduce_file_path_with_2slashes(self):
        input = "//"
        output = "/"
        result = reduce_file_path(input)
        self.assertEqual(result, output)

    def test_reduce_file_path_with_more_slashes(self):
        input = "//////////////////////////////////////"
        output = "/"
        result = reduce_file_path(input)
        self.assertEqual(result, output)

    def test_reduce_file_path_with_path_with_slashes_between(self):
        input = "///etc///etc////"
        output = "/etc/etc"
        result = reduce_file_path(input)
        self.assertEqual(result, output)

    def test_reduce_file_path_with_path_with_slashes_and_single_dots_between(self):
        input = "/srv/./././././"
        output = "/srv"
        result = reduce_file_path(input)
        self.assertEqual(result, output)

    def test_reduce_file_path_with_path_with_slashes_and_double_dots_between(self):
        input = "/etc/../etc/../etc/../"
        output = "/"
        result = reduce_file_path(input)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
