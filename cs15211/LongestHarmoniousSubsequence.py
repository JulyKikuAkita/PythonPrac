__source__ = 'https://leetcode.com/problems/longest-harmonious-subsequence/'
# Time:  O()
# Space: O()
#
# Description: https://leetcode.com/problems/longest-harmonious-subsequence/solution/
#
# We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.
#
# Now, given an integer array,
# you need to find the length of its longest harmonious subsequence among all its possible subsequences.
#
# Example 1:
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# Note: The length of the input array will not exceed 20,000.
#
# Hide Company Tags LiveRamp
# Hide Tags Hash Table

# Let count[x] be the number of x's in our array.
# Suppose our longest subsequence B has min(B) = x and max(B) = x+1.
# Evidently, it should use all occurrences of x and x+1 to maximize it's length, so len(B) = count[x] + count[x+1].
# Additionally, it must use x and x+1 atleast once, so count[x] and count[x+1] should both be positive.

import unittest
import collections
# 104ms 73.,79%
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        res = 0
        for x in count:
            if x + 1 in count:
                res = max (res, count[x] + count[x+1])
        return res;

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/longest-harmonious-subsequence/solution/

The idea is to keep a count of all the numbers, and eventually for each of the numbers,
check if there's any adjacent number. If it's present, then add the count of both -
since these two numbers form subsequence in the array.

# 67ms 37.91%
class Solution {
    public int findLHS(int[] nums) {
        Map<Long, Integer> map = new HashMap<>();
        for (long num : nums) {
            map.put(num, map.getOrDefault(num,0) + 1);
        }

        int res = 0;
        for (long key : map.keySet()) {
            if (map.containsKey(key + 1)) {
                res = Math.max(res, map.get(key+1) + map.get(key));
            }
        }
        return res;
    }
}
'''
