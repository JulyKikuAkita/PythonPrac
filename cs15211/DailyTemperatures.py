__source__ = 'https://leetcode.com/problems/daily-temperatures/'
# Time:  O(N)
# Space: O(W) The size of the stack is bounded as it represents strictly increasing temperatures.
#
# Description: Leetcode # 739. Daily Temperatures
#
# Given a list of daily temperatures T, return a list such that,
# for each day in the input, tells you how many days you would have to wait until a warmer temperature.
# If there is no future day for which this is possible, put 0 instead.
#
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
# your output should be [1, 1, 4, 2, 1, 1, 0, 0].
#
# Note: The length of temperatures will be in the range [1, 30000].
# Each temperature will be an integer in the range [30, 100].
#
import unittest

# 308ms 97.44%
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        if not T:
            return []
        stk = []
        res = [0] * len(T)
        for i in range(len(T)):
            while stk and T[stk[-1]] < T[i]:
                t = stk.pop()
                res[t] = i - t
            stk.append(i)      # top is the current min
        return res

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/daily-temperatures/solution/
# Approach #1: Next Array [Accepted]
# Complexity Analysis
# Time Complexity: O(NW), where N is the length of T and W is the number of allowed values for T[i].
Since W=71, we can consider this complexity O(N).
# Space Complexity: O(N + W), the size of the answer and the next array.

# 92.71% 11ms
class Solution {
    public int[] dailyTemperatures(int[] T) {
        int[] ans = new int[T.length];
        int[] next = new int[101];
        Arrays.fill(next, Integer.MAX_VALUE);

        for (int i = T.length - 1; i >= 0; i--) {
            int warmer_index = Integer.MAX_VALUE;
            for (int t = T[i] + 1; t <= 100; ++t) {
                if (next[t] < warmer_index) warmer_index = next[t];
            }

            if (warmer_index < Integer.MAX_VALUE) ans[i] = warmer_index - i;
            next[T[i]] = i;
        }
        return ans;
    }
}

Approach #2: Stack [Accepted]
#66ms 52.63%

class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> stack = new Stack<>();
         int[] res = new int[temperatures.length];

        //Start from backward, mainin a increasing order in stack
        for (int i = temperatures.length -1; i >= 0; i--) {
            while(!stack.isEmpty() && temperatures[stack.peek()] <= temperatures[i]) {
                stack.pop();
            }
            if (!stack.isEmpty()) res[i] = stack.peek() - i;
            stack.push(i);
        }
        return res;
    }
}

#58ms 64.22%
class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> stack = new Stack<>();
         int[] res = new int[temperatures.length];

        //Start from index 0, maintaining a decreasing order in stack
        for (int i = 0; i < temperatures.length; ++i) {
            while(!stack.isEmpty() && temperatures[stack.peek()] < temperatures[i]) {
                res[stack.peek()] = i - stack.pop();
            }
            stack.push(i);
        }
        return res;
    }
}
'''