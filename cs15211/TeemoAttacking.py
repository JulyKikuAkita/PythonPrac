__source__ = 'https://leetcode.com/problems/teemo-attacking/#/description'
# Time:  O(n)
# Space: O(1)
#
# Description: 495. Teemo Attacking
#
# In LLP world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition.
# Now, given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration
# per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.
#
# You may assume that Teemo attacks at the very beginning of a specific time point,
# and makes Ashe be in poisoned condition immediately.
#
# Example 1:
# Input: [1,4], 2
# Output: 4
# Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned immediately.
# This poisoned status will last 2 seconds until the end of time point 2.
# And at time point 4, Teemo attacks Ashe again, and causes Ashe to be in poisoned status for another 2 seconds.
# So you finally need to output 4.
# Example 2:
# Input: [1,2], 2
# Output: 3
# Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned.
# This poisoned status will last 2 seconds until the end of time point 2.
# However, at the beginning of time point 2, Teemo attacks Ashe again who is already in poisoned status.
# Since the poisoned status won't add up together, though the second poisoning attack will still work at time point 2,
# it will stop at the end of time point 3.
# So you finally need to output 3.
# Note:
# You may assume the length of given time series array won't exceed 10000.
# You may assume the numbers in the Teemo's attacking time series and his poisoning time duration per attacking
# are non-negative integers, which won't exceed 10,000,000.
# Hide Company Tags Riot Games
# Hide Tags Array
# Hide Similar Problems (M) Merge Intervals (E) Can Place Flowers

import unittest

# 60ms 40.45%
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        ans = duration * len(timeSeries)
        for i in range(1, len(timeSeries)):
            ans -= max(0, duration - (timeSeries[i] - timeSeries[i-1]))
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
O(n) Java Solution using same idea of merge intervals
The same idea as https://leetcode.com/problems/merge-intervals/
Algorithm:

Use two variable to record current start and end point.
If the start of new interval is greater than current end, meaning NO overlapping,
we can sum the current interval length to result and then update start and end.
Otherwise just update the current end;

# 3ms 100%
class Solution {
    public int findPosisonedDuration(int[] timeSeries, int duration) {
        if (timeSeries == null || timeSeries.length == 0 || duration == 0) return 0;

        int result = 0, start = timeSeries[0], end = timeSeries[0] + duration;
        for (int i = 1; i < timeSeries.length; i++) {
            if (timeSeries[i] > end) {
                result += end - start;
                start = timeSeries[i];
            }
            end = timeSeries[i] + duration;
        }
        result += end - start;

        return result;
    }
}

# Math
# 4ms 98.40%
class Solution {
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        int ans = duration * timeSeries.length;
        for (int i = 1; i < timeSeries.length; i++) {
            ans -= Math.max(0, duration - (timeSeries[i] - timeSeries[i-1]));
        }
        return ans;
    }
}
'''