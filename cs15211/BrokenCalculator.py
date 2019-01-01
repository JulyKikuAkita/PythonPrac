__source__ = 'https://leetcode.com/problems/broken-calculator/'
# Time:  O(logY)
# Space: O(1)
#
# Description: Leetcode # 991. Broken Calculator
#
# On a broken calculator that has a number showing on its display, we can perform two operations:
#
# Double: Multiply the number on the display by 2, or;
# Decrement: Subtract 1 from the number on the display.
# Initially, the calculator is displaying the number X.
#
# Return the minimum number of operations needed to display the number Y.
#
#
#
# Example 1:
#
# Input: X = 2, Y = 3
# Output: 2
# Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.
# Example 2:
#
# Input: X = 5, Y = 8
# Output: 2
# Explanation: Use decrement and then double {5 -> 4 -> 8}.
# Example 3:
#
# Input: X = 3, Y = 10
# Output: 3
# Explanation:  Use double, decrement and double {3 -> 6 -> 5 -> 10}.
# Example 4:
#
# Input: X = 1024, Y = 1
# Output: 1023
# Explanation: Use decrement operations 1023 times.
#
# Note:
#
# 1 <= X <= 10^9
# 1 <= Y <= 10^9
#
import unittest
# 20ms 98.82%
class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        ans = 0
        while Y > X:
            ans += 1
            if Y%2: Y += 1
            else: Y /= 2

        return ans + X-Y

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/broken-calculator/solution/
# https://leetcode.com/problems/broken-calculator/discuss/234484/JavaC%2B%2BPython-Change-Y-to-X-in-1-Line

# Approach 1: Work Backwards
# Complexity Analysis
# Time Complexity: O(logY).
# Space Complexity: O(1). 
# 3ms 100%
class Solution {
    public int brokenCalc(int X, int Y) {
        int res = 0;
        while (Y > X) {
            Y = Y % 2 > 0 ? Y + 1 : Y / 2;
            res++;
        }
        return res + X - Y;
    }
}
'''
