__source__ = 'https://leetcode.com/problems/push-dominoes/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 838. Push Dominoes
#
# There are N dominoes in a line, and we place each domino vertically upright.
#
# In the beginning, we simultaneously push some of the dominoes either to the left or to the right.
#
#
#
# After each second, each domino that is falling to the left pushes the adjacent domino on the left.
#
# Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.
#
# When a vertical domino has dominoes falling on it from both sides,
# it stays still due to the balance of the forces.
#
# For the purposes of this question,
# we will consider that a falling domino expends no additional force to a falling or already fallen domino.
#
# Given a string "S" representing the initial state. S[i] = 'L',
# if the i-th domino has been pushed to the left; S[i] = 'R',
# if the i-th domino has been pushed to the right; S[i] = '.',
# if the i-th domino has not been pushed.
#
# Return a string representing the final state.
#
# Example 1:
#
# Input: ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."
# Example 2:
#
# Input: "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second domino.
# Note:
#
# 0 <= N <= 10^5
# String dominoes contains only 'L', 'R' and '.'
#
import unittest

# 272ms 61.98%
class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]

        ans = list(dominoes)
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                for k in xrange(i+1, j):
                    ans[k] = x
            elif x > y: #RL
                for k in xrange(i+1, j):
                    ans[k] = '.LR'[cmp(k-i, j-k)]
        return "".join(ans)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/push-dominoes/solution/
Approach #1: Adjacent Symbols [Accepted]
Complexity Analysis
Time and Space Complexity: O(N), where N is the length of dominoes.

# 12ms 78.05%
class Solution {
    public String pushDominoes(String dominoes) {
        int N = dominoes.length();
        int[] indexes = new int[N+2];
        char[] symbols = new char[N+2];
        int len = 1;
        indexes[0] = -1;
        symbols[0] = 'L';

        for (int i = 0; i < N; ++i)
            if (dominoes.charAt(i) != '.') {
                indexes[len] = i;
                symbols[len++] = dominoes.charAt(i);
            }

        indexes[len] = N;
        symbols[len++] = 'R';

        char[] ans = dominoes.toCharArray();
        for (int index = 0; index < len - 1; ++index) {
            int i = indexes[index], j = indexes[index+1];
            char x = symbols[index], y = symbols[index+1];
            char write;
            if (x == y) {
                for (int k = i+1; k < j; ++k)
                    ans[k] = x;
            } else if (x > y) { // RL
                for (int k = i+1; k < j; ++k)
                    ans[k] = k-i == j-k ? '.' : k-i < j-k ? 'R' : 'L';
            }
        }

        return String.valueOf(ans);
    }
}

Approach #2: Calculate Force [Accepted]
Complexity Analysis
Time and Space Complexity: O(N)

# 29ms 21.46%
class Solution {
    public String pushDominoes(String dominoes) {
        char[] A = dominoes.toCharArray();
        int N = A.length;
        int[] forces = new int[N];

        // Populate forces going from left to right
        int force = 0;
        for (int i = 0; i < N; ++i) {
            if (A[i] == 'R') force = N;
            else if (A[i] == 'L') force = 0;
            else force = Math.max(force - 1, 0);
            forces[i] += force;
        }

        // Populate forces going from right to left
        force = 0;
        for (int i = N-1; i >= 0; --i) {
            if (A[i] == 'L') force = N;
            else if (A[i] == 'R') force = 0;
            else force = Math.max(force - 1, 0);
            forces[i] -= force;
        }

        StringBuilder ans = new StringBuilder();
        for (int f: forces)
            ans.append(f > 0 ? 'R' : f < 0 ? 'L' : '.');
        return ans.toString();
    }
}

# 7ms 99.51%
class Solution {
    public String pushDominoes(String dominoes) {
        dominoes = "L" + dominoes + "R";
		char[] arr = dominoes.toCharArray();
		int left = 0, right = 0;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] == 'L' || arr[i] == 'R') {
                right = i;
                updateBetweenTwo(left, right, arr);
                left = i;
            }
        }
        return new String(arr).substring(1, arr.length - 1);
    }

    private void updateBetweenTwo(int left, int right, char[] arr) {
        if (arr[left] == 'L' && arr[right] == 'L') {
            for (; left < right; left++) {
                arr[left] = 'L';
            }
        } else if (arr[left] == 'R' && arr[right] == 'R') {
            for (; left < right; left++) {
                arr[left] = 'R';
            }
        } else if (arr[left] == 'R' && arr[right] == 'L') {
            for (; left < right; left++, right--) {
                arr[left] = 'R';
                arr[right] = 'L';
            }
        }
    }
}
'''