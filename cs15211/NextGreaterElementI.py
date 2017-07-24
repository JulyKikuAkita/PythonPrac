__source__ = 'https://leetcode.com/problems/next-greater-element-i/#/description'
# Time:  O(m + n)
# Space: O(m + n)
#
# Description:
# You are given two arrays (without duplicates) nums1 and nums2 where nums1's elements are subset of nums2.
# Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
#
# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
# If it does not exist, output -1 for this number.
#
# Example 1:
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
# Output: [-1,3,-1]
# Explanation:
#     For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
#     For number 1 in the first array, the next greater number for it in the second array is 3.
#     For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
#
# Example 2:
# Input: nums1 = [2,4], nums2 = [1,2,3,4].
# Output: [3,-1]
# Explanation:
#     For number 2 in the first array, the next greater number for it in the second array is 3.
#     For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
#
# Note:
# All elements in nums1 and nums2 are unique.
# The length of both nums1 and nums2 would not exceed 1000.
# Related Topics
# Stack
# Similar Questions
# Next Greater Element II Next Greater Element III
#
# 79ms
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        dict = {}
        st = []
        res = []

        for n in nums:
            while len(st) and st[-1] < n:
                dict[st.pop()] = n
            st.append(n)

        for x in findNums:
            res.append(dict.get(x, -1))

        return res

class Solution(object):
    def nextGreaterElement2(self, findNums, nums):
        return [next((y for y in nums[nums.index(x):] if y > x), -1) for x in findNums]

Java = '''
Thought: https://leetcode.com/articles/greater-element-i/

Key observation:
Suppose we have a decreasing sequence followed by a greater number
For example [5, 4, 3, 2, 1, 6] then the greater number 6 is
the next greater element for all previous numbers in the sequence

We use a stack to keep a decreasing sub-sequence, whenever we see a number x greater than stack.peek()
we pop all elements less than x and for all the popped ones, their next greater element is x
For example [9, 8, 7, 3, 2, 1, 6]
The stack will first contain [9, 8, 7, 3, 2, 1] and then we see 6 which is greater than 1
so we pop 1 2 3 whose next greater element should be 6

#36.16% 12ms
public class Solution {
    public int[] nextGreaterElement(int[] findNums, int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        Stack<Integer> stack = new Stack<>();
        for ( int num : nums) {
            while(!stack.isEmpty() && stack.peek() < num) {
                map.put(stack.pop(), num);
            }
            stack.push(num);
        }

        for (int i = 0; i < findNums.length; i++) {
            findNums[i] = map.getOrDefault(findNums[i], -1);
        }
        return findNums;
    }
}

# 47.69% 11ms
public class Solution {
    public int[] nextGreaterElement(int[] findNums, int[] nums) {
        Stack < Integer > stack = new Stack < > ();
        HashMap < Integer, Integer > map = new HashMap < > ();
        int[] res = new int[findNums.length];
        for (int i = 0; i < nums.length; i++) {
            while (!stack.empty() && nums[i] > stack.peek())
                map.put(stack.pop(), nums[i]);
            stack.push(nums[i]);
        }
        while (!stack.empty())
            map.put(stack.pop(), -1);
        for (int i = 0; i < findNums.length; i++) {
            res[i] = map.get(findNums[i]);
        }
        return res;
    }
}

# 92.92% 7ms
public class Solution {
    public int[] nextGreaterElement(int[] findNums, int[] nums) {
        if(findNums == null || nums == null || findNums.length > nums.length)
            return new int[0];
        int[] res = new int[findNums.length];
        Arrays.fill(res, -1);
        // key : nums[i], value : position / index
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            map.put(nums[i], i);
        }

        for(int i = 0; i < res.length; i++){
            int startIndex = map.get(findNums[i]);

            for(int j = startIndex + 1; j < nums.length; j++){
                if(nums[j] > findNums[i]){
                    res[i] = nums[j];
                    break;
                }
            }
        }
        return res;
    }
}
'''