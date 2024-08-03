import unittest
from med import min_edit_distance


class TestMinEditDistance(unittest.TestCase):

    def test_identical_strings(self):
        self.assertEqual(min_edit_distance("kitten", "kitten"), 0)

    def test_insertion(self):
        self.assertEqual(min_edit_distance("kitten", "kittena"), 1)
        self.assertEqual(min_edit_distance("kitten", "akitten"), 1)

    def test_deletion(self):
        self.assertEqual(min_edit_distance("kitten", "kiten"), 1)
        self.assertEqual(min_edit_distance("kitten", "itten"), 1)

    def test_substitution(self):
        self.assertEqual(min_edit_distance("intention", "execution"), 8)

    def test_completely_different_strings(self):
        self.assertEqual(min_edit_distance("kitten", "sitting"), 5)

    def test_empty_source(self):
        self.assertEqual(min_edit_distance("", "kitten"), 6)

    def test_empty_strings(self):
        self.assertEqual(min_edit_distance("", ""), 0)

    def test_empty_target(self):
        self.assertEqual(min_edit_distance("kitten", ""), 6)

    def test_some_common_characters(self):
        self.assertEqual(min_edit_distance("kitten", "kitchen"), 3)

    def test_case_sensitivity(self):
        self.assertEqual(min_edit_distance("Kitten", "kitten"), 2)

    def test_special_characters(self):
        self.assertEqual(min_edit_distance("kitten!", "kitten"), 1)
        self.assertEqual(min_edit_distance("kitten", "kitten!"), 1)

    def test_numbers(self):
        self.assertEqual(min_edit_distance("kitten123", "kitten"), 3)
        self.assertEqual(min_edit_distance("123kitten", "kitten"), 3)

    def test_long_strings(self):
        self.assertEqual(min_edit_distance("a" * 1000, "b" * 1000), 2000)

    def test_strings_with_spaces(self):
        self.assertEqual(min_edit_distance("kitten", "kit ten"), 1)
        self.assertEqual(min_edit_distance("kit ten", "kitten"), 1)

    def test_substrings(self):
        self.assertEqual(min_edit_distance("kitten", "kit"), 3)
        self.assertEqual(min_edit_distance("kit", "kitten"), 3)


if __name__ == '__main__':
    unittest.main()
