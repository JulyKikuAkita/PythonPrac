__source__ = 'https://leetcode.com/problems/array-nesting/#/description'
# Time:  O(N)
# Space: O(1)
#
# Description:
# A zero-indexed array A consisting of N different integers is given.
# The array contains all integers in the range [0, N - 1].
#
# Sets S[K] for 0 <= K < N are defined as follows:
#
# S[K] = { A[K], A[A[K]], A[A[A[K]]], ... }.
#
# Sets S[K] are finite for each K and should NOT contain duplicates.
#
# Write a function that given an array A consisting of N integers,
# return the size of the largest set S[K] for this array.
#
# Example 1:
# Input: A = [5,4,0,3,1,6,2]
# Output: 4
# Explanation:
# A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.
#
# One of the longest S[K]:
# S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
# Note:
# N is an integer within the range [1, 20,000].
# The elements of A are all distinct.
# Each element of array A is an integer within the range [0, N-1].
# Hide Company Tags Apple
# Hide Tags Array
# Hide Similar Problems (E) Nested List Weight Sum (M) Flatten Nested List Iterator (M) Nested List Weight Sum II
#
import unittest
#
# Basically this problem means find the biggest cycle.
# One thing we shall notice is once i has been visited in previous different cycle,
# it must not in current cycle and we can ignore it.
#
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, step, n = 0, 0, len(nums)
        seen = [False] * n
        for i in range(n):
            while not seen[i]:
                seen[i] = True
                i, step = nums[i], step + 1
            ans = max(ans, step)
            step = 0
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/array-nesting/
The idea is to, start from every number, find circles in those index-pointer-chains,
every time you find a set (a circle) mark every number as visited (-1)
so that next time you won't step on it again.

public class Solution {
    public int arrayNesting(int[] nums) {
        int maxsize = 0;
        for (int i = 0; i < nums.length; i++) {
            int size = 0;
            for (int k = i; nums[k] >= 0; size++) {
                int tmp = nums[k];
                nums[k] = -1; // mark a[k] as visited;
                k = tmp;
            }
            maxsize = Math.max(maxsize, size);
        }
        return maxsize;
    }
}
'''