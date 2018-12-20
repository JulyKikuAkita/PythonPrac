__source__ = 'https://leetcode.com/problems/remove-9/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 660. Remove 9
#
# Start from integer 1, remove any integer that contains 9 such as 9, 19, 29...
#
# So now, you will have a new integer sequence: 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, ...
#
# Given a positive integer n, you need to return the n-th integer after removing. Note that 1 will be the first integer.
#
# Example 1:
# Input: 9
# Output: 10
# Hint: n will not exceed 9 x 10^8.
#
# Companies
# Houzz
# Related Topics
# Math
#
import unittest

# Thought: The set of numbers without 9s is the same as the set of base-9 numbers,
# and they occur in the same order. The answer is therefore just the n-th base-9 number.
#
# 20ms 100%
class Solution(object):
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = ''
        while n:
            ans = str(n%9) + ans
            n /= 9
        return int(ans)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/remove-9/solution/
#
# 3ms 100%
class Solution {
    public int newInteger(int n) {
        return Integer.parseInt(Integer.toString(n, 9));
    }
}

# 5ms 31.25%
class Solution {
    public int newInteger(int n) {
        int res = 0, base = 1;
        while (n > 0) {
            res += n % 9  * base;
            n /= 9;
            base *= 10;
        }
        return res;
    }
}
'''
