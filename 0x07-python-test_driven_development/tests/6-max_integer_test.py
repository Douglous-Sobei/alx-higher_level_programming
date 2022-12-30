import unittest

def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

class TestMaxInteger(unittest.TestCase):
    def test_max_integer_with_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_max_integer_with_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_max_integer_with_multiple_elements(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([1, 3, 2]), 3)

if __name__ == '__main__':
    unittest.main()
