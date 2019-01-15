__source__ = 'https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/'
# Time:  O(logK)
# Space: O(logK)
#
# Description: Leetcode # 793. Preimage Size of Factorial Zeroes Function
#
# Let f(x) be the number of zeroes at the end of x!. (x factorial)
# (Recall that x! = 1 * 2 * 3 * ... * x, and by convention, 0! = 1.)
#
# For example, f(3) = 0 because 3! = 6 has no zeroes at the end,
# while f(11) = 2 because 11! = 39916800 has 2 zeroes at the end.
# Given K, find how many non-negative integers x have the property that f(x) = K.
#
# Example 1:
# Input: K = 0
# Output: 5
# Explanation: 0!, 1!, 2!, 3!, and 4! end with K = 0 zeroes.
#
# Example 2:
# Input: K = 5
# Output: 0
# Explanation: There is no x such that x! ends in K = 5 zeroes.
# Note:
#
# K will be an integer in the range [0, 10^9].
#
import unittest
# 32ms 16.67%
class Solution(object):
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        def zeta(x):
            return x/5 + zeta(x/5) if x > 0 else 0

        lo, hi = K, 10*K + 1
        while lo < hi:
            mi = (lo + hi) / 2
            zmi = zeta(mi)
            if zmi == K: return 5
            elif zmi < K: lo = mi + 1
            else: hi = mi
        return 0

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/solution/
Approach #1: Binary Search [Accepted
Complexity Analysis
Time Complexity: O(log(base2)K). Our binary search is O(logK), a
nd in each step of that binary search we do O(logK) work to evaluate the function zeta.
Space Complexity: O(logK), the size of our recursive call stack when calling zeta.
[Wrong ans] when K == 1000000000, should return 5 instead of 0
class Solution {
    public int preimageSizeFZF(int K) {
        int lo = K, hi = 10 * K + 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            int zmi = zeta(mid);
            if (zmi == K) return 5;
            else if (zmi < K) lo = mid + 1;
            else hi = mid;
        }
        return 0;
    }

    private int zeta(int x) {
        if (x == 0) return 0;
        return x / 5 + zeta(x / 5);
    }
}

# 2ms 99.25%
class Solution {
    public int preimageSizeFZF(int K) {
        if (K < 5){
            return 5;
        }

        int d = 1;
        while (d * 5 + 1 <= K){
            d = d * 5 + 1;
        }

        if (K / d == 5){
            return 0;
        }

        return preimageSizeFZF(K % d);
    }
}

'''