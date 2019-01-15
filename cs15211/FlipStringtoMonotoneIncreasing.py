__source__ = 'https://leetcode.com/problems/flip-string-to-monotone-increasing/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 926. Flip String to Monotone Increasing
#
# A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0),
# followed by some number of '1's (also possibly 0.)
#
# We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.
#
# Return the minimum number of flips to make S monotone increasing.
#
# Example 1:
#
# Input: "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.
# Example 2:
#
# Input: "010110"
# Output: 2
# Explanation: We flip to get 011111, or alternatively 000111.
# Example 3:
#
# Input: "00011000"
# Output: 2
# Explanation: We flip to get 00000000.
#
#
# Note:
#
# 1 <= S.length <= 20000
# S only consists of '0' and '1' characters.
#
import unittest

# 96ms 40.55%
class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        P = [0]
        for x in S:
            P.append(P[-1] + int(x))

        return min(P[j] + len(S)-j-(P[-1]-P[j])
                   for j in xrange(len(P)))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/flip-string-to-monotone-increasing/solution/
Approach 1: Prefix Sums
Complexity Analysis
Time Complexity: O(N), where N is the length of S.
Space Complexity: O(N)

# 7ms 93.28%
class Solution {
    public int minFlipsMonoIncr(String S) {
        int N = S.length();
        int[] P = new int[N + 1];
        for (int i = 0; i < N; ++i) {
            P[i+1] = P[i] + (S.charAt(i) == '1' ? 1 : 0);
        }

        int ans = Integer.MAX_VALUE;
        for (int j = 0; j <= N; ++j) {
            ans = Math.min(ans, P[j] + N - j - (P[N] - P[j]));
        }

        return ans;
    }
}

'''