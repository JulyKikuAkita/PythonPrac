__source__ = 'https://leetcode.com/problems/cracking-the-safe/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 753. Cracking the Safe
#
# There is a box protected by a password.
# The password is n digits, where each letter can be one of the first k digits 0, 1, ..., k-1.
#
# You can keep inputting the password, the password will automatically be matched against the last n digits entered.
#
# For example, assuming the password is "345", I can open it when I type "012345", but I enter a total of 6 digits.
#
# Please return any string of minimum length that is guaranteed to open the box after the entire string is inputted.
#
# Example 1:
# Input: n = 1, k = 2
# Output: "01"
# Note: "10" will be accepted too.
# Example 2:
# Input: n = 2, k = 2
# Output: "00110"
# Note: "01100", "10011", "11001" will be accepted too.
#
import unittest

# 44ms 66.25%
class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        seen = set()
        ans = []
        def dfs(node):
            for x in map(str, range(k)):
                nei = node + x
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei[1:])
                    ans.append(x)

        dfs("0" * (n-1))
        return "".join(ans) + "0" * (n-1)

# 24ms 100%
class Solution2(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        M = k**(n-1)
        P = [q*k+i for i in xrange(k) for q in xrange(M)]
        ans = []

        for i in xrange(k**n):
            j = i
            while P[j] >= 0:
                ans.append(str(j / M))
                P[j], j = -1, P[j]

        return "".join(ans) + "0" * (n-1)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/cracking-the-safe/solution/
Approach #1: Hierholzer's Algorithm [Accepted]
https://www.geeksforgeeks.org/hierholzers-algorithm-directed-graph/
Complexity Analysis
Time Complexity: O(n * k^n). We visit every edge once in our depth-first search, and nodes take O(n) space.
Space Complexity: O(n * k^n), the size of seen.

# 10ms 83.60%
class Solution {
    Set<String> seen;
    StringBuilder ans;

    public String crackSafe(int n, int k) {
        if (n == 1 && k == 1) return "0";
        seen = new HashSet();
        ans = new StringBuilder();

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n - 1; i++) {
            sb.append("0");
        }
        String start = sb.toString();

        dfs(start, k);
        ans.append(start);
        return ans.toString();
    }

    private void dfs(String node, int k) {
        for (int x = 0; x < k; ++x) {
            String nei = node + x;
            if (!seen.contains(nei)) {
                seen.add(nei);
                dfs(nei.substring(1), k);
                ans.append(x);
            }
        }
    }
}

Approach #2: Inverse Burrows-Wheeler Transform [Accepted]
Complexity Analysis
Time Complexity: O(k^n). We loop through every possible substring.
Space Complexity: O(k^n), the size of P and ans.
the permutation S'->S [mapping permutation indices (i * k^{n-1} + q) -> (q * k+i)] form the desired Lyndon words.

# 3ms 99.84%
class Solution {
    public String crackSafe(int n, int k) {
        int M = (int) Math.pow(k, n-1);
        int[] P = new int[M * k];

        for (int i = 0; i < k; ++i)
            for (int q = 0; q < M; ++q)
                P[i*M + q] = q*k + i;

        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < M*k; ++i) {
            int j = i;
            while (P[j] >= 0) {
                ans.append(String.valueOf(j / M));
                int v = P[j];
                P[j] = -1;
                j = v;
            }
        }

        for (int i = 0; i < n-1; ++i)
            ans.append("0");
        return new String(ans);
    }
}
'''