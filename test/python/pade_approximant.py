#!/usr/bin/env python

import unittest

from PadeApproximants import PadeApproximant

import numpy as np

class test_pade(unittest.TestCase):

    def test_basic(self):

        x = np.arange(1, 10, dtype=np.complex)
        y = 1. / x

        fun = PadeApproximant(x, y)

        print fun(100.)
        self.assertLess(abs(fun(100.) - 0.01), 1e-9)


if __name__ == '__main__':
    unittest.main()
