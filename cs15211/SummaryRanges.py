__source__ = 'https://leetcode.com/problems/summary-ranges/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/summary-ranges.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 228. Summary Ranges
#
# Given a sorted integer array without duplicates,
# return the summary of its ranges.
#
# For example, given [0,1,2,4,5,7],
# return ["0->2","4->5","7"].
#
# Companies
# Google
# Related Topics
# Array
# Similar Questions
# Missing Ranges Data Stream as Disjoint Intervals
#
import unittest
import re
class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        ranges = []
        if not nums:
            return ranges
        start, end = nums[0], nums[0]
        for i in xrange(1, len(nums) + 1):
            if i < len(nums) and nums[i] == end + 1:
                end = nums[i]
            else:
                interval = str(start)
                if start != end:
                    interval += "->" + str(end)
                ranges.append(interval)

                if i < len(nums):
                    start = end = nums[i]
        return ranges

# Time:  O(n)
# Space: O(n)
import itertools
class Solution2:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        return [re.sub('->.*>', '->', '->'.join(`n` for _, n in g)) for _, g in itertools.groupby(enumerate(nums), lambda(i, n): n - i)]

class Solution3(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        if not nums or len(nums) == 0:
            return res

        i = 0
        while i < len(nums):
            j = i
            while j < len(nums) - 1 and nums[j+1] - nums[j] == 1:
                j += 1
            if i != j:
                res.append("{}->{}".format(nums[i], nums[j]))
            else:
                res.append("{}".format(nums[i]))
            i = j + 1
        return res

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        arr1 = [0,1,2,4,5,7]
        print Solution().summaryRanges(arr1)
        print Solution2().summaryRanges(arr1)
        print Solution3().summaryRanges(arr1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/summary-ranges/solution/
#
# 1ms 100%
class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> summary = new ArrayList<>();
        for (int i, j = 0; j < nums.length; ++j){
            i = j;
            // try to extend the range [nums[i], nums[j]]
            while (j + 1 < nums.length && nums[j + 1] == nums[j] + 1)
                ++j;
            // put the range into the list
            if (i == j)
                summary.add(nums[i] + "");
            else
                summary.add(nums[i] + "->" + nums[j]);
        }
        return summary;
    }
}

# 2ms 42.59%
class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> summary = new ArrayList<>();
        for (int i = 0, j = 0; j < nums.length; ++j) {
            // check if j + 1 extends the range [nums[i], nums[j]]
            if (j + 1 < nums.length && nums[j + 1] == nums[j] + 1)
                continue;
            // put the range [nums[i], nums[j]] into the list
            if (i == j)
                summary.add(nums[i] + "");
            else
                summary.add(nums[i] + "->" + nums[j]);
            i = j + 1;
        }
        return summary;
    }
}

# 1ms 100%
class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> result = new ArrayList<>();
        if (nums.length == 0) {
            return result;
        }
        int start = nums[0];
        int end = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == end + 1) {
                end++;
            } else {
                result.add(convert(start, end));
                start = nums[i];
                end = nums[i];
            }
        }
        result.add(convert(start, end));
        return result;
    }

    private String convert(int start, int end) {
        if (start == end) {
            return Integer.toString(start);
        } else {
            return Integer.toString(start) + "->" + Integer.toString(end);
        }
    }
}
'''
