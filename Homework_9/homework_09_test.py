
import unittest
from homework_9_1.functions import *



class MyTest(unittest.TestCase):
    def test_sum_1(self):
        result: int = sum_number(7, 10)
        self.assertEqual(result, 17)

    def test_sum_2(self):
        result: bool = sum_number(-1.5, 7.8)
        self.assertEqual(result, 6.3)

    def test_increase_1(self):
        result: bool = increase_in_bananas(8)
        self.assertEqual(result, 32)

    def test_increase_2(self):
        result: bool = increase_in_bananas(-4)
        self.assertEqual(result, -16)

    def test_amount_1(self):
        result: bool = amount_on_credit(4, 1100.5)
        self.assertEqual(result, 4402)

    def test_amount_2(self):
        result: bool = amount_on_credit(0, 1999.99)
        self.assertEqual(result, 0)

    def test_longest_word_1(self):
        result: str = longest_word(['flover', 'ocean', 'apples'])
        self.assertEqual(result, 'flover', 'apples')

    def test_longest_word_2(self):
        result: str = longest_word(['dolphin', 'column', 'mouse'])
        self.assertEqual(result, 'dolphin')


    def test_find_substring_1(self):
        result: int = find_substring("Instantly generate clear, compelling writing while maintaining your unique voice.",  "clear")
        self.assertEqual(result, 19)

    def test_find_substring_2(self):
        result: int = find_substring("Instantly generate clear, compelling writing while maintaining your unique voice.",  "word")
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()
