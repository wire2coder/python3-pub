import unittest
import util_functions 

class TestArrayFunc(unittest.TestCase):
    def test_combine(self):
        array1 = [1, 2, 3]
        array2 = [4, 5, 6]
        expected = [1, 2, 3, 4, 5, 6]

        combined1 = util_functions.UtilFunctions.combine(array1, array2)
        self.assertEqual(expected, combined1)

    def test_reverse(self):
        string = 'hello'
        expected = 'olleh'

        reversed_string = util_functions.UtilFunctions.reverse_string(string)
        self.assertEqual(expected, reversed_string)

    def test_anagram(self):
        string1 = 'hello'
        string2 = 'olleh'
        expected = True

        util_functions.UtilFunctions.anagram_checker(string1, string2)
        self.assertEqual(expected, True)

if __name__ == '__main__':
    unittest.main()