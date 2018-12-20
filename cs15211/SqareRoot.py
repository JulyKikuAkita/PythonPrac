__source__ = 'https://leetcode.com/problems/sqrtx/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/sqrtx.py
# Time:  O(logn)
# Space: O(1)
# Binary Search
#
# Description: Leetcode # 69. Sqrt(x)
#
# Implement int sqrt(int x).
#
# Compute and return the square root of x.
#
# Companies
# Bloomberg Apple Facebook
# Related Topics
# Binary Search Math
# Similar Questions
# Pow(x, n) Valid Perfect Square
#
import unittest
class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x < 2:
            return x

        low, high = 1, x /2
        while low <= high:
            mid = (low + high) / 2
            if x / mid < mid:
                high = mid - 1
            else:
                low = mid + 1
        return high
    # 34ms
    def mySqrt(self, x):
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return r

# y1= 1/2*(y0+x/y0)
class SolutionOther:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        y, ans, isNeg =0 ,1, False
        if x < 0:
            isNeg = True
        if x == 0:
            return 0
        while ans != y and x >0:
            y = ans
            ans = 1.0/2 *(y +x/y)
            #print y, ans
        return int(ans) if isNeg == False else int(ans * -1)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().sqrt(10)
        print Solution().sqrt(6)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 15ms 98.71%
class Solution {
    public int mySqrt(int x) {
        if (x <= 0) {
            return 0;
        }
        long start = 1;
        long end = x;
        while (start + 1 < end) {
            long mid = start + ((end - start) >> 1);
            if (mid * mid < x) {
                start = mid;
            } else {
                end = mid;
            }
        }
        return (int) (end * end <= x ? end : start);
    }
}

# 15ms 98.71%
class Solution {
    public int mySqrt(int x) {
        long r = x;
        while (r*r > x)
            r = (r + x/r) / 2;
        return (int) r;
    }
}

# 16ms 88.96%
class Solution {
    public int mySqrt(int x) {
        return (int)Math.sqrt(x);
    }
}

'''
