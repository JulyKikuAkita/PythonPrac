__source__ = 'https://leetcode.com/problems/partition-labels/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 763. Partition Labels
#
# A string S of lowercase letters is given.
# We want to partition this string into as many parts as possible
# so that each letter appears in at most one part,
# and return a list of integers representing the size of these parts.
#
# Example 1:
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
# Note:
#
# S will have length in range [1, 500].
# S will consist of lowercase letters ('a' to 'z') only.
#
import unittest

# 28ms 95.82%
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/partition-labels/solution/
Approach #1: Greedy [Accepted]
Complexity Analysis
Time Complexity: O(N), where N is the length of SS.
Space Complexity: O(N)

# 7ms 96.23%
class Solution {
    public List<Integer> partitionLabels(String S) {
        int[] last = new int[26];
        for (int i = 0; i < S.length(); ++i)
            last[S.charAt(i) - 'a'] = i;
        int j = 0, anchor = 0;
        List<Integer> ans = new ArrayList();
        for (int i = 0; i < S.length(); ++i) {
            j = Math.max(j, last[S.charAt(i) - 'a']);
            if (i == j) {
                ans.add(i - anchor + 1);
                anchor = i + 1;
            }
        }
        return ans;
    }
}

'''