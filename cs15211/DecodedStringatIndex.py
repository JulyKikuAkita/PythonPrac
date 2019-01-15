__source__ = 'https://leetcode.com/problems/decoded-string-at-index/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 880. Decoded String at Index
#
# An encoded string S is given.  To find and write the decoded string to a tape,
# the encoded string is read one character at a time and the following steps are taken:
#
# If the character read is a letter, that letter is written onto the tape.
# If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more times in total.
# Now for some encoded string S, and an index K, find and return the K-th letter (1 indexed) in the decoded string.
#
# Example 1:
#
# Input: S = "leet2code3", K = 10
# Output: "o"
# Explanation:
# The decoded string is "leetleetcodeleetleetcodeleetleetcode".
# The 10th letter in the string is "o".
# Example 2:
#
# Input: S = "ha22", K = 5
# Output: "h"
# Explanation:
# The decoded string is "hahahaha".  The 5th letter is "h".
# Example 3:
#
# Input: S = "a2345678999999999999999", K = 1
# Output: "a"
# Explanation:
# The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".
#
#
# Note:
#
# 2 <= S.length <= 100
# S will only contain lowercase letters and digits 2 through 9.
# S starts with a letter.
# 1 <= K <= 10^9
# The decoded string is guaranteed to have less than 2^63 letters.
#
import unittest
# 20ms 100%
class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        size = 0
        # Find size = length of decoded string
        for c in S:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1

        for c in reversed(S):
            K %= size
            if K == 0 and c.isalpha():
                return c

            if c.isdigit():
                size /= int(c)
            else:
                size -= 1
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/decoded-string-at-index/solution/
Approach 1: Work Backwards
Complexity Analysis
Time Complexity: O(N), where N is the length of S.
Space Complexity: O(1)
Note: Whenever the decoded string would equal some word repeated d times, we can reduce K to K % (word.length).

# 2ms 99.57%
class Solution {
    public String decodeAtIndex(String S, int K) {
        long size = 0;
        int N = S.length();

        // Find size = length of decoded string
        for (int i = 0; i < N; ++i) {
            char c = S.charAt(i);
            if (Character.isDigit(c)) {
                size *= c - '0';
            } else {
                size++;
            }
        }

        for (int i = N - 1; i >= 0; i--) {
            char c = S.charAt(i);
            K %= size;
            if (K == 0 && Character.isLetter(c))
                return Character.toString(c);
            if (Character.isDigit(c)) {
                size /= c - '0';
            } else {
                size--;
            }
        }
        throw null;
    }
}
'''