# Created by Kiku on 5/21/17
# https://leetcode.com/problems/complex-number-multiplication/#/description
# Given two strings representing two complex numbers.
# https://en.wikipedia.org/wiki/Complex_number
# A complex number is a number that can be expressed in the form a + bi,
# where a and b are real numbers and i is the imaginary unit
#
# You need to return a string representing their multiplication. Note i2 = -1 according to the definition.
#
# Example 1:
# Input: "1+1i", "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
# Example 2:
# Input: "1+-1i", "1+-1i"
# Output: "0+-2i"
# Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
# Note:
#
# The input strings will not have extra blank.
# The input strings will be given in the form of a+bi,
# where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.
# Hide Company Tags Amazon
# Hide Tags Math String

import unittest

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1, a2 = map(int, a[:-1].split('+'))
        b1, b2 = map(int, b[:-1].split('+'))
        return '%d+%di' % (a1 * b1 - a2 * b2, a1 * b2 + a2 * b1)


class FooTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setupDown(self):
        pass

    def tearDown(self):
        pass

    def test_foo(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    # run all tests
    unittest.main()

    # run one test
    #unittest.main(defaultTest='FooTest.test_foo', warnings='ignore')
java = '''
Java 3-liner
This solution relies on the fact that (a+bi)(c+di) = (ac - bd) + (ad+bc)i.

public String complexNumberMultiply(String a, String b) {
    int[] coefs1 = Stream.of(a.split("\\+|i")).mapToInt(Integer::parseInt).toArray(),
          coefs2 = Stream.of(b.split("\\+|i")).mapToInt(Integer::parseInt).toArray();
    return (coefs1[0]*coefs2[0] - coefs1[1]*coefs2[1]) + "+" + (coefs1[0]*coefs2[1] + coefs1[1]*coefs2[0]) + "i";
}
'''