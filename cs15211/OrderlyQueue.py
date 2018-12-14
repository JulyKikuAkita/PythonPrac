__source__ = 'https://leetcode.com/problems/orderly-queue/'
# Time:  O(N^2)
# Space: O(N^2)
#
# Description: Leetcode # 899. Orderly Queue
#
# A string S of lowercase letters is given.  Then, we may make any number of moves.
#
# In each move, we choose one of the first K letters (starting from the left),
# remove it, and place it at the end of the string.
#
# Return the lexicographically smallest string we could have after any number of moves.
#
# Example 1:
#
# Input: S = "cba", K = 1
# Output: "acb"
# Explanation:
# In the first move, we move the 1st character ("c") to the end, obtaining the string "bac".
# In the second move, we move the 1st character ("b") to the end, obtaining the final result "acb".
# Example 2:
#
# Input: S = "baaca", K = 3
# Output: "aaabc"
# Explanation:
# In the first move, we move the 1st character ("b") to the end, obtaining the string "aacab".
# In the second move, we move the 3rd character ("c") to the end, obtaining the final result "aaabc".
#
# Note:
#
# 1 <= K <= S.length <= 1000
# S consists of lowercase letters only.
#
import unittest

# 20ms 100%
class Solution(object):
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if K == 1:
            return min(S[i:] + S[:i] for i in range(len(S)))
        return "".join(sorted(S))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
Approach 1: Mathematical
Complexity Analysis
Time Complexity: O(N^2), where N is the length of S.
Space Complexity: O(N^2)

Note: 2-kick moves allow any permutation of the string.
If K = 1, only rotations of S are possible, and the answer is the smallest rotation.
If K > 1, any permutation of S is possible, and the answer is the letters of S written in lexicographic order.

# 10ms 48.89%
class Solution {
    public String orderlyQueue(String S, int K) {
        if (K == 1) {
            String ans = S;
            for (int i = 0; i < S.length(); i++) {
                String T = S.substring(i) + S.substring(0, i);
                if (T.compareTo(ans) < 0) ans = T;
            }
            return ans;
        } else {
            char[] ca = S.toCharArray();
            Arrays.sort(ca);
            return new String(ca);
        }
    }
}

# 8ms 65.19%
class Solution {
    public String orderlyQueue(String S, int K) {
        char[] cs = S.toCharArray();
        if (K > 1) {
            Arrays.sort(cs);
        } else {
            int m = 0;
            for (int i = 1; i < cs.length; i++) {
                if (compare(cs, m, i) > 0) {
                    m = i;
                }
            }
            if (m != 0) {
                char[] ncs = new char[cs.length];
                System.arraycopy(cs, m, ncs, 0, cs.length - m);
                System.arraycopy(cs, 0, ncs, cs.length - m, m);
                cs = ncs;
            }
        }
        return new String(cs);
    }

    private int compare(char[] cs, int i, int j) {
        int x;
        for (int d = 0; d < cs.length; d++) {
            x = cs[i + d >= cs.length ? i + d - cs.length : i + d] -
                    cs[j + d >= cs.length ? j + d - cs.length : j + d];
            if (x != 0) {
                return x;
            }
        }
        return 0;
    }
}
'''