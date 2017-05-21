__source__ = 'https://github.com/kamyu104/LeetCode/blob/master/Python/valid-word-square.py'
# Time:  O(m * n)
# Space: O(1)
#
# Description:
#Given a sequence of words, check whether it forms a valid word square.
# A sequence of words forms a valid word square if the kth row and column read the exact same string,
# where 0 <= k < max(numRows, numColumns).
#
# Note:
# The number of words given is at least 1 and does not exceed 500.
# Word length will be at least 1 and does not exceed 500.
# Each word contains only lowercase English alphabet a-z.
# Example 1:
#
# Input:
# [
#   "abcd",
#   "bnrt",
#   "crmy",
#   "dtye"
# ]
#
# Output:
# true
#
# Explanation:
# The first row and first column both read "abcd".
# The second row and second column both read "bnrt".
# The third row and third column both read "crmy".
# The fourth row and fourth column both read "dtye".
#
# Therefore, it is a valid word square.
# Example 2:
#
# Input:
# [
#   "abcd",
#   "bnrt",
#   "crm",
#   "dt"
# ]
#
# Output:
# true
#
# Explanation:
# The first row and first column both read "abcd".
# The second row and second column both read "bnrt".
# The third row and third column both read "crm".
# The fourth row and fourth column both read "dt".
#
# Therefore, it is a valid word square.
# Example 3:
#
# Input:
# [
#   "ball",
#   "area",
#   "read",
#   "lady"
# ]
#
# Output:
# false
#
# Explanation:
# The third row reads "read" while the third column reads "lead".
#
# Therefore, it is NOT a valid word square.
# Hide Company Tags Google
# Hide Similar Problems (H) Word Squares

import unittest

# Explanation:
#
# The map(None, ...) transposes the "matrix", filling missing spots with None. For example:
#
# ["abc",           [('a', 'd', 'f'),
#  "de",     =>      ('b', 'e', None),
#  "f"]              ('c', None, None)]
# And then I just need to check whether transposing it once more changes it.
class Solution(object):
    def validWordSquare2(self, words):
        t = map(None, *words)
        return t == map(None, *t)

    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        for i in xrange(len(words)):
            for j in xrange(len(words[i])):
                if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True


# your function here

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
public class Solution {
    public boolean validWordSquare(List<String> words) {
        if (words == null || words.size() == 0) return true;
        int n = words.size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < words.get(i).length(); j++) {
                if ( j >= n || words.get(j).length() <= i || words.get(j).charAt(i) != words.get(i).charAt(j)) {
                    return false;
                }
            }
        }
        return true;
    }
}
'''