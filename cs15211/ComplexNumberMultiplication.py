__source__ = 'https://leetcode.com/problems/complex-number-multiplication/'
# Time:  O(1)
# Space: O(1)
#
# Description: Leetcode # 537. Complex Number Multiplication
#
# Given two strings representing two complex numbers.
# https://en.wikipedia.org/wiki/Complex_number
#
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

# 20ms 98.88%
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
Java = '''

# Thought: https://leetcode.com/problems/complex-number-multiplication/solution/

Java 3-liner
This solution relies on the fact that (a+bi)(c+di) = (ac - bd) + (ad+bc)i.
Approach #1 Simple Solution[Accepted]
Complexity Analysis
Time complexity : O(1). Here splitting takes constant time as length of the string is very small (<20).
Space complexity : O(1). Constant extra space is used.

# 7ms 34.32%
public class Solution {
    public String complexNumberMultiply(String a, String b) {
        String x[] = a.split("\\+|i");
        String y[] = b.split("\\+|i");
        int a_real = Integer.parseInt(x[0]);
        int a_img = Integer.parseInt(x[1]);
        int b_real = Integer.parseInt(y[0]);
        int b_img = Integer.parseInt(y[1]);
        return (a_real * b_real - a_img * b_img) + "+" + (a_real * b_img + a_img * b_real) + "i";
    }
}


# 51ms 3.37%
public class Solution {
    public String complexNumberMultiply(String a, String b) {
        int[] coefs1 = Stream.of(a.split("\\+|i")).mapToInt(Integer::parseInt).toArray(),
              coefs2 = Stream.of(b.split("\\+|i")).mapToInt(Integer::parseInt).toArray();
              return (coefs1[0]*coefs2[0] - coefs1[1]*coefs2[1]) + "+"
                    + (coefs1[0]*coefs2[1] + coefs1[1]*coefs2[0]) + "i";
    }
}

# 2ms 100%
class Solution {

    String[] split(String a) {
        String[] ans = new String[2];
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) == '+') {
                ans[0] = a.substring(0, i);
                ans[1] = a.substring(i + 1, a.length() - 1);
                break;
            }
        }
        return ans;
    }

    public String complexNumberMultiply(String a, String b) {
        String[] str = split(a);
        int al = Integer.valueOf(str[0]), ar = Integer.valueOf(str[1]);
        str = split(b);
        int bl = Integer.valueOf(str[0]), br = Integer.valueOf(str[1]);
        int l = al * bl - ar * br;
        int r = al * br + ar * bl;
        StringBuilder sb = new StringBuilder();
        sb.append(l);
        sb.append("+");
        sb.append(r);
        sb.append("i");
        return sb.toString();
    }
}
'''