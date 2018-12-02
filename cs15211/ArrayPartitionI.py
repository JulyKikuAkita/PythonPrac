__source__ = 'https://leetcode.com/problems/array-partition-i/'
# Time:  O(nlogn)
# Space: O(1)
#
# Description: Leetcode # 561. Array Partition I
#
# Given an array of 2n integers, your task is to group these integers into n pairs of integer,
# say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi)
# for all i from 1 to n as large as possible.
#
# Example 1:
# Input: [1,4,3,2]
#
# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4.
# The goal is to get the largest possible sum of MIN of the pair.
# So for the example [1, 2, 3, 4], the best pairs are (1, 2) and (3, 4).
# min(1, 2) + min(3, 4) = 1 + 3 = 4
# Note:
# n is a positive integer, which is in the range of [1, 10000].
# All the integers in the array will be in the range of [-10000, 10000].
# Adobe,Bloomberg,Google
#

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])


if __name__ == "__main__":
    print Solution().arrayPairSum([1,4,3,2])

Java = '''
#Thought: https://leetcode.com/problems/array-partition-i/solution/

Approach #2 Using Sorting [Accepted]
Complexity Analysis
Time complexity : O(nlog(n)). Sorting takes O(nlog(n)) time. We iterate over the array only once.
Space complexity : O(1) Constant extra space is used.

#19ms 93.36%
class Solution {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int ans = 0;
        for (int i = 0; i < nums.length; i += 2) {
            ans += nums[i];
        }
        return ans;
    }
}

Approach #3 Using Extra Array [Accepted]
Complexity Analysis
Time complexity : O(n). The whole hashmap arrarr of size nn is traversed only once.
Space complexity : O(n). A hashmap arrarr of size nn is used.

# 9ms 98.40%
class Solution {
    public int arrayPairSum(int[] nums) {
        int[] arr = new int[20001];
        int lim = 10000;
        for (int num: nums)
            arr[num + lim]++;
        int d = 0, sum = 0;
        for (int i = -10000; i <= 10000; i++) {
            sum += (arr[i + lim] + 1 - d) / 2 * i;
            d = (2 + arr[i + lim] - d) % 2;
        }
        return sum;
    }
}
'''