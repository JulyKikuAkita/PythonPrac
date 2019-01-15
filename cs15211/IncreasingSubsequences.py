__source__ = 'https://leetcode.com/problems/increasing-subsequences/#/description'
# Time:  O(n!) [4,3,2,1] and return []
# Space: O(1) stack
#
# Description: 491. Increasing Subsequences
#
# Given an integer array, your task is to find all the different possible increasing subsequences
# of the given array, and the length of an increasing subsequence should be at least 2 .
#
# Example:
# Input: [4, 6, 7, 7]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
# Note:
# The length of the given array will not exceed 15.
# The range of integer in the given array is [-100,100].
# The given array may contain duplicates, and two equal integers should also be considered
# as a special case of increasing sequence.
#
# Hide Company Tags Yahoo
# Hide Tags Depth-first Search
#
import unittest
# 644ms 18.67%
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subs = {()}
        for num in nums:
            subs |= {sub + (num,) for sub in subs if not sub or sub[-1] <= num}
        return [sub for sub in subs if len(sub) >= 2]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
#dfs template 93%
#if nums has duplicate, use set, otherwise get duplicated result
#remember when to have i start with 0 or start; use 0 if can reuse nums[i]

# 12ms 87.80%
class Solution {
    public List<List<Integer>> findSubsequences(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        backtracking(res, new ArrayList<>(), nums, 0);
        return res;
    }

    public void backtracking(List<List<Integer>> res, ArrayList<Integer> tmp, int[] nums, int start) {
        if (tmp.size() > 1) {
            res.add(new ArrayList<>(tmp));
        }
        Set<Integer> set = new HashSet<>();
        for (int i = start; i < nums.length; i++) {
            if (set.contains(nums[i])) continue;
            if (tmp.size() > 0 && nums[i] < tmp.get(tmp.size() - 1)) continue;
                tmp.add(nums[i]);
                set.add(nums[i]);
                backtracking(res, tmp, nums, i + 1);
                tmp.remove(tmp.size() - 1);
        }
    }
}

'''