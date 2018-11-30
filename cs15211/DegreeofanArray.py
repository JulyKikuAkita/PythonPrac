__source__ = 'https://leetcode.com/problems/degree-of-an-array/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 697. Degree of an Array
#
# Given a non-empty array of non-negative integers nums,
# the degree of this array is defined as the maximum frequency of any one of its elements.
#
# Your task is to find the smallest possible length of a (contiguous) subarray of nums,
# that has the same degree as nums.
#
# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6
# Note:
#
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.
#
import unittest

#52ms 95.48%
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dictionary = {}
        for i,n in enumerate(nums):
            if n not in dictionary:
                dictionary[n] = (1,i,i)
            else:
                (count,lIndex,_) = dictionary[n]
                dictionary[n] = (count+1,lIndex,i)
        minLen = len(nums)
        maxCount = 0
        for key in dictionary:
            (count,lIndex,rIndex) = dictionary[key]
            length = rIndex - lIndex + 1
            if count == maxCount:
                minLen = min(minLen,length)
            if count > maxCount:
                minLen = length
                maxCount = count
        return minLen

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/degree-of-an-array/solution/

# Complexity Analysis
#
# Time Complexity: O(N), where N is the length of nums.
# Every loop is through O(N) items with O(1) work inside the for-block.
# Space Complexity: O(N), the space used by left, right, and count.
#

#37ms 57.91%
class Solution {
    public int findShortestSubArray(int[] nums) {
        Map<Integer, Integer> left = new HashMap(),
                              right = new HashMap(),
                              count = new HashMap();

        for (int i = 0; i < nums.length; i++) {
            int x = nums[i];
            if (left.get(x) == null) left.put(x, i);
            right.put(x, i);
            count.put(x, count.getOrDefault(x, 0) + 1);
        }

        int ans = nums.length;
        int degree = Collections.max(count.values());
        for (int x : count.keySet()) {
            if (count.get(x) == degree) {
                ans = Math.min(ans, right.get(x) - left.get(x) + 1);
            }
        }
        return ans;
    }
}

# 7ms, 99.86%
class Solution {
    public int findShortestSubArray(int[] nums) {
        int max = 0;
        for (int n : nums) max = Math.max(max, n); //we use n as index
        int[] index = new int[max + 1];
        int[] freq = new int[max + 1];
        Arrays.fill(index, -1);
        int res = nums.length, d = 0;

        for (int i = 0; i < nums.length; i++) {
            int n = nums[i];
            if (index[n] < 0) index[n] = i;
            if (++freq[n] > d || freq[n] == d && i - index[n] < res) {
                d = freq[n];
                res = i - index[n];
            }
        }
        return res + 1;
    }
}
'''