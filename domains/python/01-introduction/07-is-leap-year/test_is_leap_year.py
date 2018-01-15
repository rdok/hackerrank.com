import os
import subprocess
import unittest

from ddt import ddt

import is_leap_year


@ddt
class TestLeapYear(unittest.TestCase):
    def test_is_evenly_dived(self):
        self.assertTrue(is_leap_year.check(2000))
        self.assertTrue(is_leap_year.check(1992))
        self.assertTrue(is_leap_year.check(1904))
        self.assertFalse(is_leap_year.check(1901))
        self.assertFalse(is_leap_year.check(1900))
        self.assertTrue(is_leap_year.check(2400))

    def test_is_evenly_dived_by_4(self):
        self.assertTrue(is_leap_year.dividable_by_four(2000))  # divided by all
        self.assertTrue(
            is_leap_year.dividable_by_four(1904)
        )  # not divided by 100 or 400

    def test_is_not_evenly_divided_by_4(self):
        self.assertFalse(is_leap_year.dividable_by_four(1901))

    def test_is_evenly_dived_by_100(self):
        self.assertTrue(
            is_leap_year.dividable_by_hundred(2000)
        )  # divided by 4, 100, and 400
        self.assertTrue(
            is_leap_year.dividable_by_hundred(1900))  # not divided by 400

    def test_is_not_evenly_divided_by_100_but_divided_by_400(self):
        self.assertFalse(is_leap_year.dividable_by_hundred(1901))

    def test_is_evenly_dived_by_400(self):
        self.assertTrue(is_leap_year.dividable_by_four_hundred(2400))

    def test_is_not_evenly_dived_by_400(self):
        self.assertFalse(is_leap_year.dividable_by_four_hundred(2500))

    def test_prints_expected_outpout(self):
        script = os.path.dirname(
            os.path.realpath(__file__)) + "/is_leap_year.py"

        self.process = subprocess.Popen(["python", script],
                                        stdout=subprocess.PIPE,
                                        stdin=subprocess.PIPE,
                                        stderr=subprocess.STDOUT)

        actual_output = self.process.communicate(input='1990')[0]

        self.assertEquals('False\n', actual_output)


if __name__ == '__main__':
    unittest.main()
