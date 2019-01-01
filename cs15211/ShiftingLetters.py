__source__ = 'https://leetcode.com/problems/shifting-letters/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 848. Shifting Letters
#
# We have a string S of lowercase letters, and an integer array shifts.
#
# Call the shift of a letter, the next letter in the alphabet,
# (wrapping around so that 'z' becomes 'a').
#
# For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
#
# Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.
#
# Return the final string after all such shifts to S are applied.
#
# Example 1:
#
# Input: S = "abc", shifts = [3,5,9]
# Output: "rpl"
# Explanation:
# We start with "abc".
# After shifting the first 1 letters of S by 3, we have "dbc".
# After shifting the first 2 letters of S by 5, we have "igc".
# After shifting the first 3 letters of S by 9, we have "rpl", the answer.
#
# Note:
#     1 <= S.length = shifts.length <= 20000
#     0 <= shifts[i] <= 10 ^ 9
#
import unittest
# 100ms 32.85%
class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        ans = []
        X = sum(shifts) % 26
        for i, c in enumerate(S):
            index = ord(c) - ord('a')
            ans.append(chr(ord('a') + (index + X) % 26))
            X = (X - shifts[i]) % 26
        return "".join(ans)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/shifting-letters/solution/
#
Approach #1: Prefix Sum [Accepted]
Complexity Analysis
Time Complexity: O(N), where N is the length of S (and shifts).
Space Complexity: O(N), the space needed to output the answer.
In general, we need to do X -= shifts[i] to maintain the correct value of X as we increment i.

# 13ms 29.84%
class Solution {
    public String shiftingLetters(String S, int[] shifts) {
        StringBuilder ans = new StringBuilder();
        int X = 0;
        for (int shift: shifts)
            X = (X + shift) % 26;

        for (int i = 0; i < S.length(); ++i) {
            int index = S.charAt(i) - 'a';
            ans.append((char) ((index + X) % 26 + 97));
            X = Math.floorMod(X - shifts[i], 26);
        }

        return ans.toString();
    }
}

# 8ms 63.17%
class Solution {
    public String shiftingLetters(String S, int[] shifts) {
        int shift = 0;
        char[] chars = S.toCharArray();
        
        // start from last letter
        for (int i = S.length() - 1; i >= 0; i--) {
            shift = (shift + shifts[i]) % 26;
            chars[i] = (char) ((chars[i] - 'a' + shift) % 26 + 'a');
        }
        return new String(chars);
    }
}
'''
