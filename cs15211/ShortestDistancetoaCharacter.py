__source__ = 'https://leetcode.com/problems/shortest-distance-to-a-character/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 821. Shortest Distance to a Character
#
# Given a string S and a character C,
# return an array of integers representing the shortest distance from the character C in the string.
#
# Example 1:
#
# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
#
#
# Note:
#
# S string length is in [1, 10000].
# C is a single character, and guaranteed to be in string S.
# All letters in S and C are lowercase.
#
import unittest

# 36ms 91.71%
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        prev = float('-inf')
        ans = []
        for i, x in enumerate(S):
            if x == C: prev = i
            ans.append(i - prev)

        prev = float('inf')
        for i in xrange(len(S) - 1, -1, -1):
            if S[i] == C: prev = i
            ans[i] = min(ans[i], prev - i)
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/shortest-distance-to-a-character/solution/
#
Approach #1: Min Array [Accepted]
Complexity Analysis
Time Complexity: O(N), where N is the length of S. We scan through the string twice.
Space Complexity: O(N), the size of ans.

# 4ms 95.28%
class Solution {
    public int[] shortestToChar(String S, char C) {
        int N = S.length();
        int[] ans = new int[N];
        
        int prev = Integer.MIN_VALUE / 2;
        for (int i = 0; i < N; i++) {
            if (S.charAt(i) == C) prev = i;
            ans[i] = i - prev;
        }
        
        prev = Integer.MAX_VALUE / 2;
        for (int i = N-1; i >= 0; --i) {
            if (S.charAt(i) == C) prev = i;
            ans[i] = Math.min(ans[i], prev - i);
        }
        return ans;
    }
}
'''
