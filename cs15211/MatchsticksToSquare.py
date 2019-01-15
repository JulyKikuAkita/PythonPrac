__source__ = 'https://leetcode.com/problems/matchsticks-to-square/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/matchsticks-to-square.py
# Time:  O(n * s * 2^n), s is the number of subset of which sum equals to side length.
# Space: O(n * (2^n + s))
#
# Description: 473. Matchsticks to Square
#
# Remember the story of Little Match Girl? By now, you know exactly
# what matchsticks the little match girl has, please find out a way
# you can make one square by using up all those matchsticks.
# You should not break any stick, but you can link them up,
# and each matchstick must be used exactly one time.
#
# Your input will be several matchsticks the girl has,
# represented with their stick length.
# Your output will either be true or false,
# to represent whether you could make one square using all the matchsticks the little match girl has.
#
# Example 1:
# Input: [1,1,2,2,2]
# Output: true
#
# Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
# Example 2:
# Input: [3,3,3,3,4]
# Output: false
#
# Explanation: You cannot find a way to form a square with all the matchsticks.
# Note:
# The length sum of the given matchsticks is in the range of 0 to 10^9.
# The length of the given matchstick array will not exceed 15.
#
# Rackspace
# Hide Tags Depth-first Search
#
import unittest
# 1376ms 50.37%
class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_len = sum(nums)
        if total_len % 4:
            return False

        side_len = total_len / 4
        fullset = (1 << len(nums)) - 1

        used_subsets = []
        valid_half_subsets = [0] * (1 << len(nums))

        for subset in xrange(fullset+1):
            subset_total_len = 0
            for i in xrange(len(nums)):
                if subset & (1 << i):
                    subset_total_len += nums[i]

            if subset_total_len == side_len:
                for used_subset in used_subsets:
                    if (used_subset & subset) == 0:
                        valid_half_subset = used_subset | subset
                        valid_half_subsets[valid_half_subset] = True
                        if valid_half_subsets[fullset ^ valid_half_subset]:
                            return True
                used_subsets.append(subset)
        return False

class TestMethods(unittest.TestCase):
    def test_Local(self):
        nums = [5969561,8742425,2513572,3352059,9084275,2194427,1017540,2324577,6810719,8936380,7868365,2755770,9954463,9912280,4713511]
        self.assertFalse(Solution().makesquare(nums), False)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/matchsticks-to-square/solution/
#
NP-Hard
#Thought: https://discuss.leetcode.com/topic/72569/java-dfs-solution-with-various-optimizations-sorting-sequential-partition-dp
Java DFS Solution with Explanation
According to https://en.wikipedia.org/wiki/Partition_problem, the partition problem (or number partitioning)
is the task of deciding whether a given multiset S of positive integers can be partitioned
into two subsets S1 and S2 such that the sum of the numbers in S1 equals the sum of the numbers in S2.
The partition problem is NP-complete.

When I trying to think how to apply dynamic programming solution of above problem to this one
(difference is divid S into 4 subsets), I took another look at the constraints of the problem:
The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.

Sounds like the input will not be very large... Then why not just do DFS? In fact, DFS solution passed judges.

1. DFS: 
# 9ms 96.16%
class Solution {
    public boolean makesquare(int[] nums) {
        if (nums == null || nums.length < 4) return false;
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        if (sum % 4 != 0) return false;
        return dfs(nums, 0, new int[4], sum / 4);
    }

    public boolean dfs(int[] nums, int start, int[] perimeter, int target) {
        if (start == nums.length) {
            if (perimeter[0] == target && perimeter[1] == target && perimeter[2] == target && perimeter[3] == target)
                return true;
            return false;
        }

        for ( int i = 0; i < 4 ; i++) {
            if (perimeter[i] + nums[start] > target) continue; //TLE if not do check
            perimeter[i] += nums[start];
            if (dfs(nums, start + 1, perimeter, target)) return true;
            perimeter[i] -= nums[start];
        }
        return false;
    }
}

Thanks @benjamin19890721 for pointing out a very good optimization:
Sorting the input array DESC will make the DFS process run much faster.
Reason behind this is we always try to put the next matchstick in the first subset.
If there is no solution, trying a longer matchstick first will get to negative conclusion earlier.
Following is the updated code. Runtime is improved from more than 1000ms to around 40ms. A big improvement.

2. DFS with sorting desc 
# 23ms 80.55%
//Arrays.sort default ascending
class Solution {
    public boolean makesquare(int[] nums) {
        if (nums == null || nums.length < 4) return false;
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        if (sum % 4 != 0) return false;
        Arrays.sort(nums); //Collections.reverseOrder() not able for primitive type
        return dfs(nums, nums.length - 1, new int[4], sum / 4);
    }

    public boolean dfs(int[] nums, int start, int[] perimeter, int target) {
        if (start == -1) {
            if (perimeter[0] == target && perimeter[1] == target && perimeter[2] == target && perimeter[3] == target)
                return true;
            return false;
        }

        for ( int i = 0; i < 4 ; i++) {
            if (perimeter[i] + nums[start] > target) continue;
            /*
            // switch with below line 98.04%
            // if (perimeter[i] + nums[start] > target || (i > 0 && perimeter[i] == perimeter[i - 1])) continue;
            */
            perimeter[i] += nums[start];
            if (dfs(nums, start - 1, perimeter, target)) return true;
            perimeter[i] -= nums[start];
        }
        return false;
    }
}
'''
