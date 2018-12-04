__source__ = 'https://leetcode.com/problems/valid-triangle-number/#/description'
# Time:  O(n^2)
# Space: O(1)
#
# Description: 611. Valid Triangle Number
#
# Given an array consists of non-negative integers,
# your task is to count the number of triplets chosen from the array
# that can make triangles if we take them as side lengths of a triangle.
#
# Example 1:
# Input: [2,2,3,4]
# Output: 3
# Explanation:
# Valid combinations are:
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# Note:
# The length of the given array won't exceed 1000.
# The integers in the given array are in the range of [0, 1000].
# Hide Company Tags Expedia
# Hide Tags Array
# Hide Similar Problems (M) 3Sum Smaller
#
import unittest
import collections

#212ms 53.78%
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        C = collections.Counter(nums)
        C.pop(0, None)
        B = sorted(C.keys())
        P = [0]
        for x in B:
            P.append(P[-1] + C[x])

        ans = 0
        for j, v in enumerate(B):
            k = len(B) - 1
            i = j
            while 0 <= i <= j <= k:
                while k > j and B[i] + B[j] <= B[k]:
                    k -= 1
                if i < j:
                    ans += C[B[i]] * C[B[j]] * (P[k+1] - P[j+1])
                    ans += C[B[i]] * C[B[j]] * (C[B[j]] - 1) / 2
                else:
                    ans += C[B[i]] * (C[B[i]] - 1) / 2 * (P[k+1] - P[j+1])
                    ans += C[B[i]] * (C[B[i]] - 1) * (C[B[i]] - 2) / 6
                i -= 1
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/valid-triangle-number/solution/

# 13ms 99.61%
public class Solution {
    public int triangleNumber(int[] nums) {
        Arrays.sort(nums);
        int count = 0, n = nums.length;
        for (int i = n -1; i >= 0; i--) {
            int l = 0, r = i-1;
            while (l < r) {
                if (nums[l] + nums[r] > nums[i]) {
                    count += r - l;
                    r--;
                }else {
                    l++;
                }
            }
        }
        return count;
    }
}

'''