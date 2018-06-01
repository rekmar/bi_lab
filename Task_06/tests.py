import generate_numbers
import unittest


class Tests(unittest.TestCase):

    res1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 
            7: 49, 8: 64, 9: 81, 10: 100}
    res2 = {1: 1}
    res3 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    def test_result(self):
        self.assertEqual(generate_numbers.generate_numbers(10), self.res1)
        self.assertEqual(generate_numbers.generate_numbers(1), self.res2)
        self.assertEqual(generate_numbers.generate_numbers(5), self.res3)


if __name__ == '__main__':
    unittest.main()
