"""pick the middle number of certain block"""
import numpy as np
import statistics

# Creator: Jiacheng Li
# Email: lij31@tcd.ie
# Contact me if anything breaks
x = [5, 6, 7, 8, 9, 9, 9, 9]
d = 3


def mid_filter(x, d):
    """take several numbers, return several middle numbers
    
    Args:
        x: an array of several numbers
        d: a natural number

    Returns: 
        output: returns the array of several numbers

    
    
    """
    filter_x = np.zeros((1, len(x)))
    if d % 2 == 0:
        return 'incorrect d'

    else:
        output = []
        for i in range (0, len(x) - 1):
            x_block = x[i : (d + i)]
            x_block = sorted(x_block)
            if (d // 2 == 0):
                filter_x[0, i] = (x[(d // 2) + i] + x[(d  // 2) + 1 + i]) / 2
            else: 
                middle = x[(d // 2) + i]
                output.append(middle)
    return output
print(mid_filter(x,d))

import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_upper(self):
        x = [5, 6, 7, 8, 9, 9, 9, 9]
        d = 3
        result = [6, 7, 8, 9, 9, 9, 9]
        self.assertEqual(result, mid_filter(x, d))

    def test_isupper(self):
        x = [5, 6, 7, 8, 9, 9, 9, 9]
        d = 4
        result = 'incorrect d'
        self.assertEqual(result, mid_filter(x, d))


if __name__ == '__main__':
    print('test begin')
    x = [5, 6, 7, 8, 9, 9, 9, 9]
    d = 3
    output = mid_filter(x, d)
    print(output)
    unittest.main()