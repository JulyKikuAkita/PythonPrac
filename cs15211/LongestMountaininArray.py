__source__ = 'https://leetcode.com/problems/longest-mountain-in-array/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 845. Longest Mountain in Array
#
# Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:
#
# B.length >= 3
# There exists some 0 < i < B.length - 1
# such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
# (Note that B could be any subarray of A, including the entire array A.)
#
# Given an array A of integers, return the length of the longest mountain.
#
# Return 0 if there is no mountain.
#
# Example 1:
#
# Input: [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
# Example 2:
#
# Input: [2,2,2]
# Output: 0
# Explanation: There is no mountain.
# Note:
#
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000
# Follow up:
#
# Can you solve it using only one pass?
# Can you solve it in O(1) space?
#
import unittest

# 48ms 77.66%
class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        ans = base = 0

        while base < N:
            end = base
            if end + 1 < N and A[end] < A[end + 1]: #if base is a left-boundary
                #set end to the peak of this potential mountain
                while end+1 < N and A[end] < A[end+1]:
                    end += 1

                if end + 1 < N and A[end] > A[end + 1]: #if end is really a peak..
                    #set 'end' to right-boundary of mountain
                    while end+1 < N and A[end] > A[end+1]:
                        end += 1
                    #record candidate answer
                    ans = max(ans, end - base + 1)
            base = max(end, base + 1)
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/longest-mountain-in-array/solution/
#
Approach #1: Two Pointer [Accepted]
Complexity Analysis
Time Complexity: O(N), where N is the length of A.
Space Complexity: O(1)

# 5ms 96.82%
class Solution {
    public int longestMountain(int[] A) {
        int N = A.length;
        int ans = 0, base = 0;
        while (base < N) {
            int end = base;
            // if base is a left-boundary
            if (end + 1 < N && A[end] < A[end + 1]) {
                // set end to the peak of this potential mountain
                while (end + 1 < N && A[end] < A[end + 1]) end++;

                // if end is really a peak..
                if (end + 1 < N && A[end] > A[end + 1]) {
                    // set end to the right-boundary of mountain
                    while (end + 1 < N && A[end] > A[end + 1]) end++;
                    // record candidate answer
                    ans = Math.max(ans, end - base + 1);
                }
            }
            base = Math.max(end, base + 1);
        }
        return ans;
    }
}

# 5ms 96.82%
class Solution {
    public int longestMountain(int[] A) {
        int res = 0;
        for (int i = 1; i < A.length - 1; i++) {
            if (A[i - 1] < A[i] && A[i] > A[i + 1]) {
                int left = i - 1;
                int right = i + 1;
                while (left > 0 && A[left - 1å < A[left]) left--;
                while (right < A.length - 1 && A[right + 1] < A[right]) right++;
                res = Math.max(res, right - left + 1);
            }
        }
        return res;
    }
}
'''
