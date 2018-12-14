# coding=utf-8
__source__ = 'https://leetcode.com/problems/pyramid-transition-matrix/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 756. Pyramid Transition Matrix
#
# We are stacking blocks to form a pyramid.
# Each block has a color which is a one letter string, like `'Z'`.
#
# For every block of color `C` we place not in the bottom row,
# we are placing it on top of a left block of color `A` and right block of color `B`.
# We are allowed to place the block there only if `(A, B, C)` is an allowed triple.
#
# We start with a bottom row of bottom, represented as a single string.
# We also start with a list of allowed triples allowed.
# Each allowed triple is represented as a string of length 3.
#
# Return true if we can build the pyramid all the way to the top, otherwise false.
#
# Example 1:
# Input: bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]
# Output: true
# Explanation:
# We can stack the pyramid like this:
#     A
#    / \
#   D   E
#  / \ / \
# X   Y   Z
#
# This works because ('X', 'Y', 'D'), ('Y', 'Z', 'E'), and ('D', 'E', 'A') are allowed triples.
# Example 2:
# Input: bottom = "XXYX", allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]
# Output: false
# Explanation:
# We can't stack the pyramid to the top.
# Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.
# Note:
# bottom will be a string with length in range [2, 8].
# allowed will have length in range [0, 200].
# Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E', 'F', 'G'}.
#
import unittest
import collections
# 24ms 90.95%
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        T = collections.defaultdict(set)
        for u, v, w in allowed:
            T[u, v].add(w)

        #Comments can be used to cache intermediate results
        #seen = set()
        def solve(A):
            if len(A) == 1: return True
            #if A in seen: return False
            #seen.add(A)
            return any(solve(cand) for cand in build(A, []))

        def build(A, ans, i = 0):
            if i + 1 == len(A):
                yield "".join(ans)
            else:
                for w in T[A[i], A[i+1]]:
                    ans.append(w)
                    for result in build(A, ans, i+1):
                        yield result
                    ans.pop()

        return solve(bottom)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/pyramid-transition-matrix/solution/
Approach #1: State to State Transition [Wrong Answer]
Complexity Analysis
Time Complexity: O(2^2A*A+N^2), where N is the length of bottom, A is the length of allowed,
and A is the size of the alphabet.
Space Complexity: O(2^2A) in additional space complexity.

At the end, applying these transitions is straightforward.
However, this approach is not correct, because the transitions are not independent.
If for example we have states in a row A, {B or C}, A, and allowed triples (A, B, D), (C, A, D),
then regardless of the choice of {B or C} we cannot create the next row of the pyramid.

[Wrong Answer]
class Solution {
    public boolean pyramidTransition(String bottom, List<String> allowed) {
        int[][] T = new int[1 << 7][1 << 7];
        for (String triple: allowed) {
            int u = 1 << (triple.charAt(0) - 'A');
            int v = 1 << (triple.charAt(1) - 'A');
            int w = 1 << (triple.charAt(2) - 'A');
            for (int b1 = 0; b1 < (1 << 7); ++b1) if ((u & b1) > 0)
                for (int b2 = 0; b2 < (1 << 7); ++b2) if ((v & b2) > 0)
                    T[b1][b2] |= w;
        }

        int[] state = new int[bottom.length()];
        int t = 0;
        for (char c: bottom.toCharArray())
            state[t++] = 1 << (c - 'A');
        while (t-- > 1)
            for (int i = 0; i < t; ++i)
                state[i] = T[state[i]][state[i+1]];
        return state[0] > 0;
    }
}



Approach #2: Depth-First Search [Accepted]
Complexity Analysis
Time Complexity: O(A^N), where N is the length of bottom, and A is the size of the alphabet,
and assuming we cache intermediate results.
We might try every sequence of letters for each row.
[The total complexity is because O(∑ A^k) is a geometric series equal to O(A^(n+1)−1 / (A−1)]
Without intermediate caching, this would be O(A^N^2)
Space Complexity: O(N^2)  additional space complexity.

# 6ms 84.55%
class Solution {
    int[][] T;
    Set<Long> seen;

    public boolean pyramidTransition(String bottom, List<String> allowed) {
        T = new int[7][7];
        for (String a: allowed)
            T[a.charAt(0) - 'A'][a.charAt(1) - 'A'] |= 1 << (a.charAt(2) - 'A');

        seen = new HashSet();
        int N = bottom.length();
        int[][] A = new int[N][N];
        int t = 0;
        for (char c: bottom.toCharArray())
            A[N-1][t++] = c - 'A';
        return solve(A, 0, N-1, 0);
    }

    //A[i] - the ith row of the pyramid
    //R - integer representing the current row of the pyramid
    //N - length of current row we are calculating
    //i - index of how far in the current row we are calculating
    //Returns true iff pyramid can be built
    public boolean solve(int[][] A, long R, int N, int i) {
        if (N == 1 && i == 1) { // If successfully placed entire pyramid
            return true;
        } else if (i == N) {
            if (seen.contains(R)) return false; // If we've already tried this row, give up
            seen.add(R); // Add row to cache
            return solve(A, 0, N-1, 0); // Calculate next row
        } else {
            // w's jth bit is true iff block #j could be
            // a parent of A[N][i] and A[N][i+1]
            int w = T[A[N][i]][A[N][i+1]];
            // for each set bit in w...
            for (int b = 0; b < 7; ++b) if (((w >> b) & 1) != 0) {
                A[N-1][i] = b; //set parent to be equal to block #b
                //If rest of pyramid can be built, return true
                //R represents current row, now with ith bit set to b+1
                // in base 8.
                if (solve(A, R * 8 + (b+1), N, i+1)) return true;
            }
            return false;
        }
    }
}

# backtracking with map
# 10ms 48.17%
class Solution {
    public boolean pyramidTransition(String bottom, List<String> allowed) {
            Map<String, List<String>> map = new HashMap<>();
            for (String s : allowed) {
                String key = s.substring(0,2);
                if (!map.containsKey(key)) map.put(key, new ArrayList<String>());
                map.get(key).add(s.substring(2));
            }

            return helper(bottom, map);
        }

    private boolean helper(String bottom, Map<String, List<String>> map) {
        if( bottom.length() == 1) return true;
        for (int i = 0; i < bottom.length() - 1; i++) {
            if (!map.containsKey(bottom.substring(i, i + 2))) return false;
        }
        List<String> ls = new ArrayList<>();
        getList(bottom, 0, new StringBuilder(), ls, map);
        for (String s : ls) {
            if (helper(s, map)) return true;
        }
        return false;
    }

    private void getList(String bottom, int idx, StringBuilder sb, List<String> ls, Map<String, List<String>> map) {
        if (idx == bottom.length() - 1) {
            ls.add(sb.toString());
            return;
        }
        for (String s : map.get(bottom.substring(idx, idx + 2))) {
            sb.append(s);
            getList(bottom, idx + 1, sb, ls, map);
            sb.deleteCharAt(sb.length()-1);
        }
    }
}

# Same idea use bit
# 5ms 93.50%
class Solution {
    public boolean pyramidTransition(String bottom, List<String> allowed) {
        int[][] pair = new int[26][26];
        for (String s : allowed) {
            pair[s.charAt(0) - 'A'][s.charAt(1) - 'A'] |= 1 << (s.charAt(2) - 'A');
        }
        int n = bottom.length();
        int[][] pyramid = new int[n][n];
        char[] cs = bottom.toCharArray();
        for (int i = 0; i < n; ++i) {
            pyramid[n - 1][i] = cs[i] - 'A';
        }
        return dfs(pyramid, n - 1, n - 1, pair);
    }

    private boolean dfs(int[][] pyramid, int col, int row, int[][] pair) {
        if (0 == col && row == 0) return true;
        if (0 == col) return dfs(pyramid, row - 1, row - 1, pair);
        int mask = pair[pyramid[row][col - 1]][pyramid[row][col]];
        for (int i = 0; i < 26; ++i) {
            if (1 == ((mask >> i) & 1)) {
                pyramid[row - 1][col - 1] = i;
                if (dfs(pyramid, col - 1, row, pair)) return true;
            }
        }
        return false;
    }
}
'''