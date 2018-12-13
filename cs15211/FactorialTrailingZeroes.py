__source__ = 'https://leetcode.com/problems/factorial-trailing-zeroes/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/factorial-trailing-zeroes.py
# http://bookshadow.com/weblog/2014/12/30/leetcode-factorial-trailing-zeroes/
# Time:  O(logn)
# Space: O(1)
# Math
#
# Description: Leetcode # 172. Factorial Trailing Zeroes
#
# Given an integer n, return the number of trailing zeroes in n!.  (5 * 2) = 10
#
# Note: Your solution should be in logarithmic time complexity.
# Companies
# Bloomberg
# Related Topics
# Math
# Similar Questions
# Number of Digit One
import unittest
#
class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        result = 0
        while n > 0:
            result += n / 5
            n /= 5
        return result

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().trailingZeroes(99)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
10 is the product of 2 and 5. In n!, we need to know how many 2 and 5,
and the number of zeros is the minimum of the number of 2 and the number of 5.

Since multiple of 2 is more than multiple of 5, the number of zeros is dominant by the number of 5.

Here we expand

  2147483647!
=2 * 3 * ...* 5 ... *10 ... 15* ... * 25 ... * 50 ... * 125 ... * 250...
=2 * 3 * ...* 5 ... * (5^1*2)...(5^1*3)...*(5^2*1)...*(5^2*2)...*(5^3*1)...*(5^3*2)... (Equation 1)
We just count the number of 5 in Equation 1.

Multiple of 5 provides one 5, multiple of 25 provides two 5 and so on.

Note the duplication: multiple of 25 is also multiple of 5, so multiple of 25 only provides one extra 5.

Here is the basic solution:

return n/5 + n/25 + n/125 + n/625 + n/3125+...;


# 18ms 33.06%
class Solution {
    public int trailingZeroes(int n) {
        return n == 0 ? 0 : n / 5 + trailingZeroes(n / 5);
    }
}

# 17ms 45.06%
class Solution {
    public int trailingZeroes(int n) {
        int result = 0;
        while (n > 0) {
            int next = n / 5;
            result += next;
            n = next;
        }
        return result;
    }
}
'''