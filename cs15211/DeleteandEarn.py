__source__ = 'https://leetcode.com/problems/delete-and-earn/'
# Time:  O(N + W)
# Space: O(W)
#
# Description: Leetcode # 740. Delete and Earn
#
# Given an array nums of integers, you can perform operations on the array.
#
# In each operation, you pick any nums[i] and delete it to earn nums[i] points.
# After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.
#
# You start with 0 points. Return the maximum number of points you can earn by applying such operations.
#
# Example 1:
# Input: nums = [3, 4, 2]
# Output: 6
# Explanation:
# Delete 4 to earn 4 points, consequently 3 is also deleted.
# Then, delete 2 to earn 2 points. 6 total points are earned.
# Example 2:
# Input: nums = [2, 2, 3, 3, 3, 4]
# Output: 9
# Explanation:
# Delete 3 to earn 3 points, deleting both 2's and the 4.
# Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
# 9 total points are earned.
# Note:
#
# The length of nums is at most 20000.
# Each element nums[i] is an integer in the range [1, 10000].
#
import unittest
import collections
# Complexity Analysis
# Time Complexity (Python): O(NlogN), where N is the length of nums.
# We make a single pass through the sorted keys of N, and the complexity is dominated by the sorting step.
# Space Complexity (Python): O(N), the size of our count.

# 28ms 84.46%
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        prev = None
        avoid = using = 0
        for k in sorted(count):
            if k - 1 != prev:
                avoid, using = max(avoid, using), k * count[k] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), k * count[k] + avoid
            prev = k
        return max(avoid, using)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/delete-and-earn/solution/

Approach #1: Dynamic Programming [Accepted]
Complexity Analysis
Time Complexity (Java): We performed a radix sort instead,
so our complexity is O(N+W) where W is the range of allowable values for nums[i].
Space Complexity (Java): O(W), the size of our count.

# 3ms 100%
class Solution {
    public int deleteAndEarn(int[] nums) {
        int[] count = new int[10001];
        for (int x: nums) count[x]++;
        int avoid = 0, using = 0, prev = -1;

        for (int k = 0; k <= 10000; ++k) {
            if (count[k] > 0) {
                int m = Math.max(avoid, using);
                if (k - 1 != prev) {
                    using = k * count[k] + m;
                    avoid = m;
                } else {
                    using = k * count[k] + avoid;
                    avoid = m;
                }
                prev = k;
            }

        }
        return Math.max(avoid, using);
    }
}

# 5ms 83.47%
class Solution {
    public int deleteAndEarn(int[] nums) {
        int n = nums.length;
        int[] arr = new int[10001];
        for (int num : nums)
            arr[num] += num;
        int take = 0, skip = 0;
        for (int num : arr) {
            int takei = skip + num;
            int skipi = Math.max(skip, take);
            take = takei;
            skip = skipi;
        }

        return Math.max(take, skip);
    }
}

# 5ms 83.47%
class Solution {
    public int deleteAndEarn(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int n = 10001;
        int[] values = new int[n];
        for (int num: nums) values[num] += num;
        for (int i = 2; i < n; i++) {
            values[i] = Math.max(values[i] + values[i - 2],  values[i-1]);
        }
        return Math.max(values[n - 1], values[n - 2]);
    }
}


'''