"""CSC 1001 - Programming Assignment 1: student-written unit tests.

Create at least TWO separate, meaningful unit tests for each function.
The sixteen methods below are ONLY PLACEHOLDERS: they are not real tests.

Replace each self.fail(...) with test inputs, a call to the appropriate
hw1 function, and unittest assertions about its expected output.
Use methods like self.assertEqual(...) or self.assertAlmostEqual(...).

IMPORTANT: The initial test failures are intentional until you write tests
and implement the functions in hw1.py. Do not simply delete the tests.
"""

import unittest

import data
import hw1

from hw1 import vowel_count, short_lists, ascending_pairs, add_prices #import vowel_count, short_lists, ascending pairs, add prices functions

class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        self.assertEqual(0, vowel_count("cmptrscnc")) #lower case without vowels

    def test_vowel_count_empty_string(self):
        self.assertEqual(0, vowel_count("")) #empty string

    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        self.assertEqual([[6,5], [3,1], [0,9]], short_lists([[2,3,5], [6,5], [0,2,2], [3,1], [1,2,3,4], [0,9]])) #list of lists of ints of varying lengths

    def test_short_lists_no_matching_lengths(self):
        self.assertEqual([], short_lists([[2,3,5], [6,5,2], [0,2,2], [3,1,9], [1,2,3,4], [0,9,2,30]])) #list of no matching lengths
        

    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        self.assertEqual([[2,3], [4,5]], ascending_pairs([[3,2],[5,4]])) #two reversed pairs

    def test_ascending_pairs_other_lengths_unchanged(self):
        self.assertEqual([[2,3],[4,5]], ascending_pairs([[2,3], [4,5]])) #unchanged

    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        self.assertEqual(data.Price(5, 23), add_prices(data.Price(4, 10), data.Price(1,13))) #no cents carry

    def test_add_prices_with_cents_carry(self):
        self.assertEqual(data.Price(5, 23), add_prices(data.Price(4, 0), data.Price(0,123))) #cents carried

    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        # TODO: Arrange inputs, call hw1.rectangle_area, and assert the result.
        self.fail("TODO: write the first unit test for rectangle_area")

    def test_rectangle_area_negative_coordinates(self):
        # TODO: Arrange inputs, call hw1.rectangle_area, and assert the result.
        self.fail("TODO: write the second unit test for rectangle_area")

    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        # TODO: Arrange inputs, call hw1.books_by_author, and assert the result.
        self.fail("TODO: write the first unit test for books_by_author")

    def test_books_by_author_no_matches(self):
        # TODO: Arrange inputs, call hw1.books_by_author, and assert the result.
        self.fail("TODO: write the second unit test for books_by_author")

    # Part 7: circle_bound
    def test_circle_bound_square(self):
        # TODO: Arrange inputs, call hw1.circle_bound, and assert the result.
        self.fail("TODO: write the first unit test for circle_bound")

    def test_circle_bound_non_square_rectangle(self):
        # TODO: Arrange inputs, call hw1.circle_bound, and assert the result.
        self.fail("TODO: write the second unit test for circle_bound")

    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        # TODO: Arrange inputs, call hw1.below_pay_average, and assert the result.
        self.fail("TODO: write the first unit test for below_pay_average")

    def test_below_pay_average_empty_list(self):
        # TODO: Arrange inputs, call hw1.below_pay_average, and assert the result.
        self.fail("TODO: write the second unit test for below_pay_average")


if __name__ == '__main__':
    unittest.main()
