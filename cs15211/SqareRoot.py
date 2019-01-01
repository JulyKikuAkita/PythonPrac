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
# https://leetcode.com/problems/sqrtx/discuss/25198/3-JAVA-solutions-with-explanation
# Binary Search: Time complexity = O(lg(x)) = O(32)=O(1)
# use long incase of overflow when mid * mid
# 17ms 73.08%
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
# use mid > x / mid to avoid overflow
# 21ms 47.08%
class Solution {
    public int mySqrt(int x) {
        if (x == 0) return 0;
        int start = 1, end = x;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (mid <= x / mid && (mid + 1) > x / (mid + 1)) return mid;
            else if (mid > x / mid) end = mid;
            else start = mid;
        }
        return end * end < x ? end : start;
    }
}

# Newton Solution: 
# Time complexity = O(lg(x))
# 15ms 98.71%
class Solution {
    public int mySqrt(int x) {
        long r = x;
        while (r*r > x)
            r = (r + x/r) / 2;
        return (int) r;
    }
}

# Brute force
# Look for the critical point: i * i <= x && (i+1)(i+1) > x
# A little trick is using i <= x / i for comparison, instead of i * i <= x, to avoid exceeding integer upper limit.
# 112ms 3.64%
class Solution {
    public int mySqrt(int x) {
        if (x == 0) return 0;
        for (int i = 1; i <= x / i; i++) {
            if (i <= x / i && (i + 1) > x / (i + 1)) { // Look for the critical point: i*i <= x && (i+1)(i+1) > x
                return i;
            }
        }
        return -1;
    }
}

# https://leetcode.com/problems/sqrtx/discuss/25048/Share-my-O(log-n)-Solution-using-bit-manipulation
# Bit Manipulation
# 18ms 59.46%
class Solution {
     public int mySqrt(int x) {
        int res = 0;
        for (int mask = 1 << 15; mask != 0; mask >>>= 1) {
            int next = res | mask; //set bit
            if (next <= x / next) res = next;
        }
        return res;
    }
}

# 16ms 90.05%
class Solution {
    public int mySqrt(int x) {
        int ans = 0; // no need to define as "long"
        int bit = 1 << 15; // no need to define as "long"
        while (bit > 0) {
            ans |= bit;
            // the original condition is "ans * ans > x" or "((long)ans) * ((long)ans) > x", this is revised version.
            if (ans > x / ans) {
                // if ans * ans > x, then ans = (ans | bit) ^ bit = ans | (bit ^ bit) = ans (the "previous" ans).
                ans ^= bit; 
            }
            bit >>= 1;
        }
        return ans;
    }
}

# 16ms 88.96%
class Solution {
    public int mySqrt(int x) {
        return (int)Math.sqrt(x);
    }
}

'''
