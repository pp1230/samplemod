# -*- coding: utf-8 -*-

import context

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(context.core.hmm())


if __name__ == '__main__':
    unittest.main()
