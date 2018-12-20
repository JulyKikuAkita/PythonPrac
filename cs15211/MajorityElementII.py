__source__ = 'https://leetcode.com/problems/majority-element-ii/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/majority-element-ii.py
# Time:  O(n)
# Space: O(1)
# Boyer-Moore Majority Vote algorithm
#
# Description: Leetcode # 229. Majority Element II
#
# Given an integer array of size n,
# find all elements that appear more than [n/3] times.
# The algorithm should run in linear time and in O(1) space.
#
# Companies
# Zenefits
# Related Topics
# Array
# Similar Questions
# Majority Element
#
import unittest
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        k, n, hash = 3, len(nums), {}

        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        # Detecting k items in hash, at least one of them must have exactly
        # one in it. We will discard those k items by one for each.
        # This action keeps the same mojority numbers in the remaining numbers.
        # Because if x / n  > 1 / k is true, then (x - 1) / (n - k) > 1 / k is also true.

        if len(hash) == k:
            for i in hash.keys():
                if hash[i] == 0:
                    del hash[i]

        # Resets hash for the following counting.
        for i in hash.keys():
            hash[i] = 0

        # Counts the occurrence of each candidate integer.
        for i in nums:
            if i in hash:
                hash[i] += 1

        # Selects the integer which occurs > [n / k] times.
        ret = []
        for i in hash.keys():
            if hash[i] > n / k:
                ret.append(i)

        return ret

    def majorityElement2(self, nums):
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2)
                        if nums.count(n) > len(nums) // 3]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().containsDuplicate([12344555,12344555])

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

For those who aren't familiar with Boyer-Moore Majority Vote algorithm,
I found a great article (http://goo.gl/64Nams) that helps me to understand this fantastic algorithm!!
Please check it out!

The essential concepts is you keep a counter for the majority number X. 
If you find a number Y that is not X,
the current counter should deduce 1. The reason is that if there is 5 X and 4 Y, 
there would be one (5-4) more X than Y.
This could be explained as "4 X being paired out by 4 Y".

And since the requirement is finding the majority for more than ceiling of [n/3],
the answer would be less than or equal to two numbers.
So we can modify the algorithm to maintain two counters for two majorities.

# 1ms 100%
class Solution {
    public List<Integer> majorityElement(int[] nums) {
    	if (nums == null || nums.length == 0)
    		return new ArrayList<Integer>();
    	List<Integer> result = new ArrayList<Integer>();
    	int number1 = nums[0], number2 = nums[0], count1 = 0, count2 = 0, len = nums.length;
    	for (int i = 0; i < len; i++) {
    		if (nums[i] == number1)
    			count1++;
    		else if (nums[i] == number2)
    			count2++;
    		else if (count1 == 0) {
    			number1 = nums[i];
    			count1 = 1;
    		} else if (count2 == 0) {
    			number2 = nums[i];
    			count2 = 1;
    		} else {
    			count1--;
    			count2--;
    		}
    	}
    	count1 = 0;
    	count2 = 0;
    	for (int i = 0; i < len; i++) {
    		if (nums[i] == number1)
    			count1++;
    		else if (nums[i] == number2)
    			count2++;
    	}
    	if (count1 > len / 3)
    		result.add(number1);
    	if (count2 > len / 3)
    		result.add(number2);
    	return result;
    }
}
'''

