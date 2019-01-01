__source__ = 'https://leetcode.com/problems/3sum-smaller/'
# Time:  O(n^2)
# Space: O(1)
#
# Description: Leetcode # 259. 3Sum Smaller
#
# Given an array of n integers nums and a target, find the number of index triplets i, j, k
# with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
#
# For example, given nums = [-2, 0, 1, 3], and target = 2.
#
# Return 2. Because there are two triplets which sums are less than 2:
#
# [-2, 0, 1]
# [-2, 0, 3]
# Follow up:
# Could you solve it in O(n2) runtime?
#
# Companies
# Google
# Related Topics
# Array Two Pointers
# Similar Questions
# 3Sum 3Sum Closest Valid Triangle Number
#
import unittest
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumSmaller(self, nums, target):
        nums.sort()
        n = len(nums)

        count, k = 0, 2
        while k < n:
            i, j = 0, k-1
            while i < j: # Two Pointers, linear time.
                if nums[i] + nums[j] + nums[k] >= target:
                    j -= 1
                else:
                    count += (j - i)
                    i += 1
            k += 1
        return count

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/3sum-smaller/solution/
We sort the array first. Then, for each element,
we use the two pointer approach to find the number of triplets that meet the requirements.

Let me illustrate how the two pointer technique works with an example:

target = 2

  i  lo    hi
[-2, 0, 1, 3]

We use a for loop (index i) to iterate through each element of the array.
For each i, we create two pointers, lo and hi, where lo is initialized as the next element of i,
and hi is initialized at the end of the array. If we know that nums[i] + nums[lo] + nums[hi] < target,
then we know that since the array is sorted, we can replace hi with any element from lo+1 to nums.length-1,
and the requirements will still be met. Just like in the example above, we know that since -2 + 0 + 3 < 2,
we can replace hi (3) with 1, and it would still work. Therefore, we can just add hi - lo to the triplet count.
# No need to skip duplicats, those count as one triplet
# 99.60% 3ms
class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        int result = 0;
        if (nums == null || nums.length < 3) {
            return result;
        }
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 2; i++) {
            int start = i + 1;
            int end = nums.length - 1;
            int max = target - nums[i];
            while (start < end) {
                int sum = nums[start] + nums[end];
                if (sum < max) {
                    result += end - start;
                    start++;
                } else {
                    end--;
                }
            }
        }
        return result;
    }
}

# 41.45% 5ms
class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        Arrays.sort(nums);
        int sum = 0;

        for(int i = 0; i < nums.length - 2; i++) {
            sum += twoSumSmaller(nums, i + 1, target - nums[i]);
        }

        return sum;
    }

    private int twoSumSmaller(int[] nums, int start, int target) {
        int sum = 0;
        int left = start;
        int right = nums.length - 1;

        while(left < right) {
            if(nums[left] + nums[right] < target) {
                sum += right - left;
                left++;
            } else
                right--;
        }

        return sum;
    }
}
'''
