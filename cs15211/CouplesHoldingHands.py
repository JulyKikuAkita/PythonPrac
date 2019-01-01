__source__ = 'https://leetcode.com/problems/couples-holding-hands/'
# Time:  O(N)
# Space: O(N)
# Cyclic swapping
# https://leetcode.com/problems/couples-holding-hands/discuss/113362/JavaC%2B%2B-O(N)-solution-using-cyclic-swapping
#
# Description: Leetcode # 765. Couples Holding Hands
#
# N couples sit in 2N seats arranged in a row and want to hold hands.
# We want to know the minimum number of swaps so that every couple is sitting side by side.
# A swap consists of choosing any two people, then they stand up and switch seats.
#
# The people and seats are represented by an integer from 0 to 2N-1,
# the couples are numbered in order, the first couple being (0, 1),
# the second couple being (2, 3),
# and so on with the last couple being (2N-2, 2N-1).
#
# The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.
#
# Example 1:
#
# Input: row = [0, 2, 1, 3]
# Output: 1
# Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
# Example 2:
#
# Input: row = [3, 2, 0, 1]
# Output: 0
# Explanation: All couples are already seated side by side.
# Note:
#
# len(row) is even and in the range of [4, 60].
# row is guaranteed to be a permutation of 0...len(row)-1.
#
import unittest

# 20ms 100%
class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        N = len(row) / 2

        #couples[x] = [i, j]:
        #x-th couple is at couches i and j
        couples = [[] for _ in xrange(N)]
        for i, x in enumerate(row):
            couples[x/2].append(i/2)
        #adj[x] = [i, j]
        #x-th couch connected to couches i, j by couples
        adj = [[] for _ in xrange(N)]
        for x, y in couples:
            adj[x].append(y)
            adj[y].append(x)
        #Answer is N minus the number of cycles in "adj"
        ans = N
        for start in xrange(N):
            if not adj[start]: continue
            ans -= 1
            x, y = start, adj[start].pop()
            while y != start:
                adj[y].remove(x)
                x, y = y, adj[y].pop()
        return ans

# 20ms 100%
class Solution2(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        ans = 0
        for i in xrange(0, len(row), 2):
            x = row[i]
            if row[i+1] == x^1: continue
            ans += 1
            for j in xrange(i+1, len(row)):
                if row[j] == x^1:
                    row[i+1], row[j] = row[j], row[i+1]
                    break
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/couples-holding-hands/solution/
Approach #1: Backtracking [Time Limit Exceeded]
Complexity Analysis
Time Complexity: O(N * 2^N), where N is the number of couples,
as for each couch we check up to two complete possibilities.
The N factor is from searching for jx and jy;
this factor can be removed with a more efficient algorithm that keeps track of where pairs[j][k]
is x as we swap elements through pairs.
Space Complexity: O(N).

# TLE
class Solution {
    int N;
    int[][] pairs;

    public int minSwapsCouples(int[] row) {
        N = row.length / 2;
        pairs = new int[N][2];
        for (int i = 0; i < N; ++i) {
            pairs[i][0] = row[2*i] / 2;
            pairs[i][1] = row[2*i+1] / 2;
        }

        return solve(0);
    }

    public void swap(int a, int b, int c, int d) {
        int t = pairs[a][b];
        pairs[a][b] = pairs[c][d];
        pairs[c][d] = t;
    }

    public int solve(int i) {
        if (i == N) return 0;
        int x = pairs[i][0], y = pairs[i][1];
        if (x == y) return solve(i+1);

        int jx=0, kx=0, jy=0, ky=0; // Always gets set later
        for (int j = i+1; j < N; ++j) {
            for (int k = 0; k <= 1; ++k) {
                if (pairs[j][k] == x) {jx = j; kx = k;}
                if (pairs[j][k] == y) {jy = j; ky = k;}
            }
        }

        swap(i, 1, jx, kx);
        int ans1 = 1 + solve(i+1);
        swap(i, 1, jx, kx);

        swap(i, 0, jy, ky);
        int ans2 = 1 + solve(i+1);
        swap(i, 0, jy, ky);

        return Math.min(ans1, ans2);
    }
}

Approach #2: Cycle Finding [Accepted]
Complexity Analysis
Time Complexity: O(N), where N is the number of couples.
Space Complexity: O(N), the size of adj and associated data structures.
//Construct a cyclic graph

#4ms 34.77%
class Solution {
    public int minSwapsCouples(int[] row) {
        int N = row.length / 2;
        //couples[x] = {i, j} means that
        //couple #x is at couches i and j (1 indexed)
        int[][] couples = new int[N][2];

        for (int i = 0; i < row.length; ++i)
            add(couples[row[i]/2], i/2 + 1);

        //adj[x] = {i, j} means that
        //x-th couch connected to couches i, j (all 1 indexed) by couples
        int[][] adj = new int[N+1][2];
        for (int[] couple: couples) {
            add(adj[couple[0]], couple[1]);
            add(adj[couple[1]], couple[0]);
        }

        // The answer will be N minus the number of cycles in adj.
        int ans = N;
        // For each couch (1 indexed)
        for (int r = 1; r <= N; ++r) {
            // If this couch has no people needing to be paired, continue
            if (adj[r][0] == 0 && adj[r][1] == 0)
                continue;

            // Otherwise, there is a cycle starting at couch r.
            // We will use two pointers x, y with y faster than x by one turn.
            ans--;
            int x = r, y = pop(adj[r]);
            // When y reaches the start 'r', we've reached the end of the cycle.
            while (y != r) {
                // We are at some couch with edges going to 'x' and 'new'.
                // We remove the previous edge, since we came from x.
                rem(adj[y], x);

                // We update x, y appropriately: y becomes new and x becomes y.
                x = y;
                y = pop(adj[y]);
            }
        }
        return ans;
    }

    // Replace the next zero element with x.
    public void add(int[] pair, int x) {
        pair[pair[0] == 0 ? 0 : 1] = x;
    }

    // Remove x from pair, replacing it with zero.
    public void rem(int[] pair, int x) {
        pair[pair[0] == x ? 0 : 1] = 0;
    }

    // Remove the next non-zero element from pair, replacing it with zero.
    public int pop(int[] pair) {
        int x = pair[0];
        if (x != 0) {
            pair[0] = 0;
        } else {
            x = pair[1];
            pair[1] = 0;
        }
        return x;
    }
}

# cyclic swapping O(N^2)
# 3ms 85.25%
class Solution {
    public int minSwapsCouples(int[] row) {
        int res = 0;
        for (int i = 0; i < row.length; i += 2) {
            int target = row[i] % 2 == 0 ? row[i] + 1 : row[i] - 1;
            if (row[i + 1] == target) continue;
            for (int j = i + 2; j < row.length; j++) {
                if (row[j] == target) {
                    swap(row, i + 1, j);
                    res++;
                }
            }
        }
        return res;
    }
    
    private void swap(int[] row, int i, int j) {
        int t = row[i];
        row[i] = row[j];
        row[j] = t;
    }
}

# Proof
# https://leetcode.com/problems/couples-holding-hands/discuss/113369/Formal-proof-of-the-optimality-of-greedy-algorithm
# By defining nodes as n pairs of seats, it suffices to show that it takes n - m swaps to form m circles from n isolated nodes.
Approach #3: Greedy [Accepted]
Complexity Analysis
Time Complexity: O(N^2), where N is the number of couples.
Space Complexity: O(1) additional complexity: the swaps are in place.
# 4ms 34.77%
class Solution {
    public int minSwapsCouples(int[] row) {
        int ans = 0;
        for (int i = 0; i < row.length; i += 2) {
            int x = row[i];
            if (row[i + 1] == (x ^ 1)) continue; // == x + 1
            ans ++;
            for (int j = i + 1; j < row.length; j++) {
                if (row[j] == (x ^ 1)) {
                    row[j] = row[i + 1];
                    row[i + 1] = x ^ 1;
                    break;
                }
            }
        }
        return ans;
    }
}

# UnionFind
# 3ms 78.32%
class Solution {
    public int minSwapsCouples(int[] row) {
        int n = row.length/ 2;
        UnionFind uf = new UnionFind(n);
        for (int i = 0; i < n; i++) {
            int a = row[2 * i];
            int b = row[2 * i + 1];
            uf.union(a/2, b/2);
        }
        return n - uf.count;
    }

    class UnionFind {
        int[] parent;
        int count;
        UnionFind(int n) {
            parent = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
            }
            count = n;
        }

        public int find(int x) {
            while (x != parent[x]) {
                x = parent[parent[x]];
            }
            return x;
        }

        public void union(int x, int y){
            x = find(x);
            y = find(y);
            if (x == y) return;
            parent[x] = y;
            count--;
        }
    }
}
# https://leetcode.com/problems/couples-holding-hands/discuss/160104/Union-find-understand-in-60-seconds-beats-99.6
# Quick Union 0(n^2)
# 2ms 100% 
class Solution {
    public int minSwapsCouples(int[] row) {
        int len = row.length;
        int[] parent = new int[len];
        for (int i = 0; i < len / 2; i++) {
            parent[2 * i] = i;
            parent[2 * i + 1] = i;
        }
        
        int cnt = 0;
        for (int i = 0; i < len / 2; i++) {    
            if (row[2 * i] / 2 != row[2 * i + 1] / 2) {
               if (find(parent, row[2 * i]) != find(parent, row[2 * i + 1])) {
                    union(parent, row[2 * i], row[2 * i + 1]);
                    cnt++;
                } 
            }
        }
        return cnt;
    }
    
    public int find(int[] root, int x) {
        return root[x];
    }
    
    public void union(int[] root, int x, int y) {
        int group = root[x];
        for (int i = 0; i < root.length; i++) {
            if (group == root[i]) root[i] = root[y];
        }
    }   
}
'''
