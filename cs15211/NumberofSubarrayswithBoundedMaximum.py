__source__ = 'https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 795. Number of Subarrays with Bounded Maximum
#
# We are given an array A of positive integers, and two positive integers L and R (L <= R).
# Return the number of (contiguous, non-empty) subarrays
# such that the value of the maximum array element in that subarray
# is at least L and at most R.
#
# Example :
# Input:
# A = [2, 1, 4, 3]
# L = 2
# R = 3
# Output: 3
# Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
#
# Note:
#
# L, R  and A[i] will be an integer in the range [0, 10^9].
# The length of A will be in the range of [1, 50000].
#
import unittest

# 100ms 35%
class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        def count(bound):
            ans = cur = 0
            for x in A :
                cur = cur + 1 if x <= bound else 0
                ans += cur
            return ans

        return count(R) - count(L - 1)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/solution/
#
Approach #1: Counting [Accepted]
Complexity Analysis
Time Complexity: O(N), where N is the length of A.
Space Complexity: O(1).
As we only care about whether each element is less than, between, 
or greater than the interval [L, R], let's pretend each element is either 0 if it is less than L; 
1 if it is between L and R; or 2 if it is greater than R.
Then, we want the number of subarrays with no 2 and at least one 1. 
The 2s split the array into groups of arrays with only 0s and 1s.
Say count(B) is the number of subarrays that have all elements less than or equal to B. 
From the above reasoning, 
the answer is count(R) - count(L-1).

# 6ms 73.53%
class Solution {
    public int numSubarrayBoundedMax(int[] A, int L, int R) {
        return count(A, R) - count(A, L - 1);
    }
    
    private int count(int[] A, int bound) {
        int ans = 0, cur = 0;
        for (int x : A) {
            cur = x <= bound ? cur + 1 : 0;
            ans += cur;
        }
        return ans;
    }
}

# 7ms 58.82%
class Solution {
    public int numSubarrayBoundedMax(int[] A, int L, int R) {
        int j = 0, count = 0, res = 0;
        for (int i = 0; i < A.length; i++) {
            if (A[i] >= L && A[i] <= R) {
                res += i - j + 1;
                count = i - j + 1;
            } else if (A[i] < L) {
                res += count;
            } else {
                count = 0;
                j = i + 1;
            }
        }
        return res;
    }
}
'''
