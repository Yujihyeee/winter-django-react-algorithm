from django.test import TestCase
import unittest
from admin.sorting.models import MySum, Palindrome


class TestMySum(unittest.TestCase):

    def test_one_to_ten_sum_1(self):
        instance = MySum()
        instance.start_number = 1
        instance.end_number = 11
        res = instance.one_to_ten_sum_2()
        print(f'My Expected Value is {res}')
        self.assertEqual(res, 55)


class TestPalindrome(unittest, TestCase):

    def test_str_to_list(self):
        instance = Palindrome()
        instance.input_string = ''
        res1 = instance.isPalindrome()
        self.assertEqual(res1, {"RESULT": False})

    def test_reverse_string(self):
        instance = Palindrome()
        instance.input_string = ''
        res2 = instance.reverse_string()
        self.assertEqual(res2, [])


if __name__ == '__main__':
    unittest.main()
