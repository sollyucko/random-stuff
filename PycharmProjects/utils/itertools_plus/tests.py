import unittest
from itertools import islice
from typing import Iterator, Optional

from itertools_plus import *


class Utils(unittest.TestCase):
    def assertIteratorsEqual(self, a: Iterator, b: Iterator, item_count: Optional[int] = None) -> None:
        self.assertEqual(list(islice(a, item_count)), list(islice(b, item_count)))


class RangeTest(Utils):
    def test_default(self):
        self.assertIteratorsEqual(Range(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
    
    def test_default_repr(self):
        self.assertEqual(repr(Range()), 'Range(0, inf, 1, True, False)')


if __name__ == '__main__':
    unittest.main()
