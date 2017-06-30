__source__ = 'https://github.com/kamyu104/LeetCode/blob/master/Python/132-pattern.py'
# Time:  O(n)
# Space: O(n)

# Given a sequence of n integers a1, a2, ..., an,
# a 132 pattern is a subsequence ai, aj, ak such that i < j < k and
# ai < ak < aj. Design an algorithm that takes a list of n numbers as
# input and checks whether there is a 132 pattern in the list.
#
# Note: n will be less than 15,000.
#
# Example 1:
# Input: [1, 2, 3, 4]
#
# Output: False
#
# Explanation: There is no 132 pattern in the sequence.
# Example 2:
# Input: [3, 1, 4, 2]
#
# Output: True
#
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
# Example 3:
# Input: [-1, 3, 2, 0]
#
# Output: True
#
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

import unittest

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ak = float("-inf")
        st = []
        for i in reversed(xrange(len(nums))):
            if nums[i] < ak:
                return True
            else:
                while st and nums[i] > st[-1]:
                    ak = st.pop()
            st.append(nums[i])
        return False

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
The idea is that we can use a stack to keep track of previous min-max intervals.

Here is the principle to maintain the stack:

For each number num in the array

If stack is empty:

push a new Pair of num into stack
If stack is not empty:

if num < stack.peek().min, push a new Pair of num into stack

if num >= stack.peek().min, we first pop() out the peek element, denoted as last

if num < last.max, we are done, return true;

if num >= last.max, we merge num into last, which means last.max = num.
Once we update last, if stack is empty, we just push back last.
However, the crucial part is:
If stack is not empty, the updated last might:

Entirely covered stack.peek(),
i.e. last.min < stack.peek().min (which is always true) && last.max >= stack.peek().max,
in which case we keep popping out stack.peek().
Form a 1-3-2 pattern, we are done ,return true
So at any time in the stack, non-overlapping Pairs are formed in descending order by their min value,
which means the min value of peek element in the stack is always the min value globally.

public class Solution {
    public boolean find132pattern(int[] nums) {
        Stack<Pair> stack = new Stack<>();
        for (int n : nums) {
            if (stack.isEmpty() || n < stack.peek().min) stack.push(new Pair(n, n));
            else if (n > stack.peek().min) {
                Pair last = stack.pop();
                if (n < last.max) return true;
                else {
                    last.max = n;
                    while (!stack.isEmpty() && n >= stack.peek().max) stack.pop();
                    // At this time, n < stack.peek().max (if stack not empty)
                    if (!stack.isEmpty() && stack.peek().min < n) return true;
                    stack.push(last);
                }
            }
        }
        return false;
    }

    class Pair{
        int min, max;
        public Pair(int min, int max) {
            this.min = min;
            this.max = max;
        }
    }
}
'''