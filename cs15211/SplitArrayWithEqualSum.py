__source__ = 'https://leetcode.com/problems/split-array-with-equal-sum/#/description'
# Time:  O(n^2)
# Space: O(n^2)
#
# Description:
# Given an array with n integers, you need to find if there are triplets (i, j, k) which satisfies following conditions:
# 0 < i, i + 1 < j, j + 1 < k < n - 1
# Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.
# where we define that subarray (L, R) represents a slice of the original array starting
# from the element indexed L to the element indexed R.
# Example:
# Input: [1,2,1,2,1,2,1]
# Output: True
# Explanation:
# i = 1, j = 3, k = 5.
# sum(0, i - 1) = sum(0, 0) = 1
# sum(i + 1, j - 1) = sum(2, 2) = 1
# sum(j + 1, k - 1) = sum(4, 4) = 1
# sum(k + 1, n - 1) = sum(6, 6) = 1
# Note:
# 1 <= n <= 2000.
# Elements in the given array will be in range [-1,000,000, 1,000,000].
# Hide Company Tags Alibaba
# Hide Tags Array

import unittest

# Let A be the array. As in most problems involving querying the sum of contiguous elements of an array,
# let P[x] = sum(A[:x]) be the prefix sums of A, which can be found in linear time.
#
# Then the sums in question are P[i] = P[j] - P[i+1] = P[k] - P[j+1] = P[-1] - P[k+1].
# For every j < k, P[i] = P[-1] - P[k+1] is a necessary requirement to choose i,
# so let's iterate over those indices first.
# This gives us the advantage that since we are iterating over a sorted list of candidate indices i,
# we can break when i >= j.
class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        P = [0]
        for x in nums:
            P.append(P[-1] + x)

        N = len(nums)
        Pinv = collections.defaultdict(list)
        for i, u in enumerate(P):
            Pinv[u].append(i)

        for j in xrange(1, N - 1):
            for k in xrange(j + 1, N -1):
                for i in Pinv[P[-1] - P[k+1]]:
                    if i >= j:
                        break
                    if P[i] == P[j] - P[i+1] == P[k] - P[j+1]:
                        return True
        return False

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/split-array-with-equal-sum/
public class Solution {
    public boolean splitArray(int[] nums) {
        if (nums.length < 7)
            return false;
        int[] sum = new int[nums.length];
        sum[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            sum[i] = sum[i - 1] + nums[i];
        }
        for (int j = 3; j < nums.length - 3; j++) {
            HashSet < Integer > set = new HashSet < > ();
            for (int i = 1; i < j - 1; i++) {
                if (sum[i - 1] == sum[j - 1] - sum[i])
                    set.add(sum[i - 1]);
            }
            for (int k = j + 2; k < nums.length - 1; k++) {
                if (sum[nums.length - 1] - sum[k] == sum[k - 1] - sum[j] && set.contains(sum[k - 1] - sum[j]))
                    return true;
            }
        }
        return false;
    }
}
'''