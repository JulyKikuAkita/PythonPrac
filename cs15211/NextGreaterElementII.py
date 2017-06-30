# https://leetcode.com/problems/next-greater-element-ii/#/description
# Given a circular array (the next element of the last element is the first element of the array),
# print the Next Greater Number for every element. The Next Greater Number of a number x is
# the first greater number to its traversing-order next in the array, which means you could search circularly
# to find its next greater number. If it doesn't exist, output -1 for this number.
#
# Example 1:
# Input: [1,2,1]
# Output: [2,-1,2]
#
# Explanation: The first 1's next greater number is 2;
# The number 2 can't find next greater number;
# The second 1's next greater number needs to search circularly, which is also 2.
# Note: The length of given array won't exceed 10000.
#
# Hide Company Tags Google
# Hide Tags Stack
# Hide Similar Problems (E) Next Greater Element I (M) Next Greater Element III
#
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack, res = [], [-1] * len(nums)
        for i in range(len(nums)) * 2:
            while stack and (nums[stack[-1]] < nums[i]):
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res

java = '''
public class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] next = new int[n];
        Arrays.fill(next, -1);
        Stack<Integer> stack = new Stack<>(); //index stack
        for (int i = 0; i < n * 2 ; i++) {
            int num = nums[i % n];
            while (!stack.isEmpty() && nums[stack.peek()] < num) {
                next[stack.pop()] = num;
            }
            if (i < n) stack.push(i);
        }
        return next;
    }
}
'''