__source__ = 'https://leetcode.com/problems/smallest-good-base/#/description'
# Time:  O(nlogn)
# Space: O(1)
#
# Description:
# # For an integer n, we call k>=2 a good base of n, if all digits of n base k are 1.
#
# Now given a string representing n, you should return the smallest good base of n in string format.
#
# Example 1:
# Input: "13"
# Output: "3"
# Explanation: 13 base 3 is 111.

# Example 2:
# Input: "4681"
# Output: "8"
# Explanation: 4681 base 8 is 11111.

# Example 3:
# Input: "1000000000000000000"
# Output: "999999999999999999"
# Explanation: 1000000000000000000 base 999999999999999999 is 11.
# Note:
# The range of n is [3, 10^18].
# The string representing n is always valid and will not have leading zeros.
# Hide Company Tags Google
# Hide Tags Binary Search Math

import unittest
#
# First things first. Let's see the math behind it.
#
# From given information, we can say one thing- Numbers will be of form-
#
# n = k^m + k^(m-1) + ... + k + 1
# => n-1 = k^m + k^(m-1) + ... + k
# => n-1 = k (k^(m-1) + k^(m-2) + ... + k + 1) ...... [1]
#
# Also, from n = k^m + k^(m-1) + ... + k + 1, we can say,
# n-k^m = k^(m-1) + k^(m-2) + ... + k + 1 ...... [2]
#
# from [1] and [2],
#
# n-1 = k (n - k^m)
# =>k^(m+1) = nk - n + 1
#
# if you shuffle sides you will end up getting following form,
#
# (k^(m+1) - 1)/(k - 1) = n .... [3]
#
# Also from [1] note that, (n - 1) must be divisible by k.
#
# We know that, n = k^m + k^(m-1) + ... + k + 1
#
# => n > k^m
# => m-th root of n > k .... [4]
#
# [EDIT] -->
#
# With inputs from @StefanPochmann we can also say, from binomial thorem, n = k^m + ... + 1 < (k+1)^m .... [5]
# Therefore, k+1 > m-th root of n > k. .... from [4] and [5]
# Thus m-th root of n is the only candidate that needs to be tested. [6]
#
# <--
#
# So our number should satisfy this equation where k will be our base and m will be (number of 1s - 1)
#
# This brings us to the search problem where we need to find k and m.
#
# Linear search from 1 to n does not work. it gives us TLE. So it leaves us with performing some optimization on search space.
#
# From [6] we know that the only candidate that needs to be tested is, m-th root of n
#
# We also know that the smallest base is 2 so we can find our m must be between 2 and log2n else m is (n-1) [7]
import math
class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        n = int(n)
        max_m = int(math.log(n,2)) # Refer [7]
        for m in range(max_m,1,-1):
            k = int(n**m**-1)  # Refer [6]
            if (k**(m+1)-1)//(k-1) == n:
                # Refer [3]
                return str(k)

        return str(n-1)


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
Java Binary Search
public class Solution {
    public String smallestGoodBase(String n) {
        long num = 0;
        for (char c : n.toCharArray()) num = num * 10 + c - '0';

        long x = 1;
        for (int p = 64; p >= 1; p--) {
            if ((x << p) < num) {
                long k = helper(num, p);
                if (k != -1) return String.valueOf(k);
            }
        }
        return String.valueOf(num - 1);
    }

    private long helper(long num, int p) {
        long l = 1, r = (long)(Math.pow(num, 1.0/p) + 1);
        while (l < r) {
            long mid = l + (r - l) / 2;
            long sum = 0, cur = 1;
            for (int i = 0; i <= p; i++) {
                sum += cur;
                cur *= mid;
            }
            if (sum == num) return mid;
            else if (sum > num) r = mid;
            else l = mid + 1;
        }
        return -1;
    }
}
'''