__source__ = 'https://leetcode.com/problems/find-the-shortest-superstring/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 943. Find the Shortest Superstring
#
# Given an array A of strings,
# find any smallest string that contains each string in A as a substring.
#
# We may assume that no string in A is substring of another string in A.
#
# Example 1:
#
# Input: ["alex","loves","leetcode"]
# Output: "alexlovesleetcode"
# Explanation: All permutations of "alex","loves","leetcode" would also be accepted.
# Example 2:
#
# Input: ["catg","ctaagt","gcta","ttca","atgcatc"]
# Output: "gctaagttcatgcatc"
#
# Note:
#
# 1 <= A.length <= 12
# 1 <= A[i].length <= 20
#
import unittest
# 340ms 77.09%
class Solution(object):
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        N = len(A)

        # Populate overlaps
        overlaps = [[0] * N for _ in xrange(N)]
        for i, x in enumerate(A):
            for j, y in enumerate(A):
                if i != j:
                    for ans in xrange(min(len(x), len(y)), -1, -1):
                        if x.endswith(y[:ans]):
                            overlaps[i][j] = ans
                            break

        # dp[mask][i] = most overlap with mask, ending with ith element
        dp = [[0] * N for _ in xrange(1<<N)]
        parent = [[None] * N for _ in xrange(1<<N)]
        for mask in xrange(1, 1 << N):
            for bit in xrange(N):
                if (mask >> bit) & 1:
                    # Let's try to find dp[mask][bit].  Previously, we had
                    # a collection of items represented by pmask.
                    pmask = mask ^ (1 << bit)
                    if pmask == 0: continue
                    for i in xrange(N):
                        if (pmask >> i) & 1:
                            # For each bit i in pmask, calculate the value
                            # if we ended with word i, then added word 'bit'.
                            value = dp[pmask][i] + overlaps[i][bit]
                            if value > dp[mask][bit]:
                                dp[mask][bit] = value
                                parent[mask][bit] = i

        # Answer will have length sum(len(A[i]) for i) - max(dp[-1])
        # Reconstruct answer:

        # Follow parents down backwards path that retains maximum overlap
        perm = []
        mask = (1<<N) - 1
        i = max(xrange(N), key = dp[-1].__getitem__)
        while i is not None:
            perm.append(i)
            mask, i = mask ^ (1<<i), parent[mask][i]

        # Reverse path to get forwards direction; add all remaining words
        perm = perm[::-1]
        seen = [False] * N
        for x in perm:
            seen[x] = True
        perm.extend([i for i in xrange(N) if not seen[i]])

        # Reconstruct answer given perm = word indices in left to right order
        ans = [A[perm[0]]]
        for i in xrange(1, len(perm)):
            overlap = overlaps[perm[i-1]][perm[i]]
            ans.append(A[perm[i]][overlap:])

        return "".join(ans)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/find-the-shortest-superstring/solution/
Approach 1: Dynamic Programming
Complexity Analysis
Time Complexity: O(N^2 (2^N + W)), where N is the number of words,
and W is the maximum length of each word
Space Complexity: O(N(2^N+W))

# 39ms 48.14%
class Solution {
    public String shortestSuperstring(String[] A) {
        int N = A.length;

        // Populate overlaps
        int[][] overlaps = new int[N][N];
        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j) if (i != j) {
                int m = Math.min(A[i].length(), A[j].length());
                for (int k = m; k >= 0; --k)
                    if (A[i].endsWith(A[j].substring(0, k))) {
                        overlaps[i][j] = k;
                        break;
                    }
            }

        // dp[mask][i] = most overlap with mask, ending with ith element
        int[][] dp = new int[1<<N][N];
        int[][] parent = new int[1<<N][N];
        for (int mask = 0; mask < (1<<N); ++mask) {
            Arrays.fill(parent[mask], -1);

            for (int bit = 0; bit < N; ++bit) if (((mask >> bit) & 1) > 0) {
                // Let's try to find dp[mask][bit].  Previously, we had
                // a collection of items represented by pmask.
                int pmask = mask ^ (1 << bit);
                if (pmask == 0) continue;
                for (int i = 0; i < N; ++i) if (((pmask >> i) & 1) > 0) {
                    // For each bit i in pmask, calculate the value
                    // if we ended with word i, then added word 'bit'.
                    int val = dp[pmask][i] + overlaps[i][bit];
                    if (val > dp[mask][bit]) {
                        dp[mask][bit] = val;
                        parent[mask][bit] = i;
                    }
                }
            }
        }

        // # Answer will have length sum(len(A[i]) for i) - max(dp[-1])
        // Reconstruct answer, first as a sequence 'perm' representing
        // the indices of each word from left to right.

        int[] perm = new int[N];
        boolean[] seen = new boolean[N];
        int t = 0;
        int mask = (1 << N) - 1;

        // p: the last element of perm (last word written left to right)
        int p = 0;
        for (int j = 0; j < N; ++j)
            if (dp[(1<<N) - 1][j] > dp[(1<<N) - 1][p])
                p = j;

        // Follow parents down backwards path that retains maximum overlap
        while (p != -1) {
            perm[t++] = p;
            seen[p] = true;
            int p2 = parent[mask][p];
            mask ^= 1 << p;
            p = p2;
        }

        // Reverse perm
        for (int i = 0; i < t/2; ++i) {
            int v = perm[i];
            perm[i] = perm[t-1-i];
            perm[t-1-i] = v;
        }

        // Fill in remaining words not yet added
        for (int i = 0; i < N; ++i) if (!seen[i])
            perm[t++] = i;

        // Reconstruct final answer given perm
        StringBuilder ans = new StringBuilder(A[perm[0]]);
        for (int i = 1; i < N; ++i) {
            int overlap = overlaps[perm[i-1]][perm[i]];
            ans.append(A[perm[i]].substring(overlap));
        }

        return ans.toString();
    }
}

# 5ms 100%
class Solution {
    public String shortestSuperstring(String[] A) {
        if (A.length == 0) return "";
        ArrayList<String> alist = new ArrayList<String>();
        for (int i = 0; i < A.length; i++) {
            alist.add(A[i]);
        }
        while (alist.size() > 1) {
            findLargestOverlap(alist);
        }
        return alist.get(0);
    }

    private void findLargestOverlap(ArrayList<String> alist) {
        int overlap = 0, maxOverlap = 0, a = 0, b = 1;
        for (int i = 0; i < alist.size(); i++) {
            for (int j = i + 1; j < alist.size(); j++) {
                overlap = oLap(alist.get(i), alist.get(j));
                if (overlap > maxOverlap) {
                    maxOverlap = overlap;
                    a = i;
                    b = j;
                }
            }
        }

        // a & b are the indices to the max overlap
        String as = alist.get(a);
        String bs = alist.get(b);
        alist.remove(as);
        alist.remove(bs);
        alist.add(myMerge(as, bs));
        return;
    }

    private int oLap(String a, String b) {
        return Math.max(myMatch(a, b), myMatch(b, a));
    }

    private int myMatch(String a, String b) {
        int alen = a.length();
        int blen = b.length();
        if (alen == 0 || blen == 0) return 0;
        int len = Math.min(alen, blen);

        // assume a then b
        int match = len;
        int i = 0;
        for (match = len; match >= 0; match--) { // # of matching characters
            for (i = 0 ; i < match; i++) {
                if (a.charAt(alen - match + i) == b.charAt(i)) continue;
                else break;
            }
            if (i == match) break;
        }
        return match;
    }

    private String myMerge(String a, String b) {
        int match1 = myMatch(a, b);
        int match2 = myMatch(b, a);
        if (match1 < match2) {
            String temp = b;
            b = a;
            a = temp;
            match1 = match2;
        }

        // merge a then b;
        StringBuilder sb = new StringBuilder();
        sb.append(a);
        sb.append(b.substring(match1, b.length()));
        return sb.substring(0);
    }
}
'''