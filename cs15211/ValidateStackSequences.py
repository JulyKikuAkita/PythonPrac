__source__ = 'https://leetcode.com/problems/validate-stack-sequences/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 946. Validate Stack Sequences
#
# Given two sequences pushed and popped with distinct values,
# return true if and only if this could have been the result of a sequence of push and pop operations
# on an initially empty stack.
#
# Example 1:
#
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
# Example 2:
#
# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.
#
#
# Note:
#
# 0 <= pushed.length == popped.length <= 1000
# 0 <= pushed[i], popped[i] < 1000
# pushed is a permutation of popped.
# pushed and popped have distinct values.
#

import unittest

# 28ms 88.40%
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        j = 0
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return j == len(popped)
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/validate-stack-sequences/solution/
Approach 1: Greedy
Complexity Analysis
Time Complexity: O(N), where N is the length of pushed and popped.
Space Complexity: O(N)).

# 9ms 86.82%
class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        int N = pushed.length;
        Stack<Integer> stack = new Stack();

        int j = 0;
        for (int x : pushed) {
            stack.push(x);
            while (!stack.isEmpty() && j < N && stack.peek() == popped[j]) {
                stack.pop();
                j++;
            }
        }
        return j == N;
    }
}

# use array
# 5ms 99.91%
class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        int[] stack = new int[pushed.length];
        int index = 0, pIndex = 0;

        for (int i = 0; i < pushed.length; i++) {
            stack[index++] = pushed[i];
            while (index != 0 && stack[index - 1] == popped[pIndex]) {
                index--;
                pIndex++;
            }
        }

        while (index != 0 && stack[index - 1] == popped[pIndex]) {
            index--;
            pIndex++;
        }

        return index == 0 && pIndex == popped.length;
    }
}
'''