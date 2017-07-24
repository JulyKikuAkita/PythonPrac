__source__ = 'https://leetcode.com/problems/coin-path/description/'
# Time:  O(nB) all the possible BB positions for every current index considered in the A array.
# Here, A refers to the number of elements in A.
# Space: O(b) dp and nextnext array of size nn are used.
#
# Description: Leetcode # 656. Coin Path
# Given an array A (index starts at 1) consisting of N integers: A1, A2, ..., AN and an integer B.
# The integer B denotes that from any place (suppose the index is i) in the array A,
# you can jump to any one of the place in the array A indexed i+1, i+2,..., i+B if this place can be jumped to.
# Also, if you step on the index i, you have to pay Ai coins.
# If Ai is -1, it means you can't jump to the place indexed i in the array.
#
# Now, you start from the place indexed 1 in the array A,
# and your aim is to reach the place indexed N using the minimum coins.
# You need to return the path of indexes (starting from 1 to N)
# in the array you should take to get to the place indexed N using minimum coins.
#
# If there are multiple paths with the same cost, return the lexicographically smallest such path.
#
# If it's not possible to reach the place indexed N then you need to return an empty array.
#
# Example 1:
# Input: [1,2,4,-1,2], 2
# Output: [1,3,5]
# Example 2:
# Input: [1,2,4,-1,2], 1
# Output: []
# Note:
# Path Pa1, Pa2, ..., Pan is lexicographically smaller than Pb1, Pb2, ..., Pbm,
# if and only if at the first i where Pai and Pbi differ, Pai < Pbi; when no such i exists, then n < m.
# A1 >= 0. A2, ..., AN (if exist) will in the range of [-1, 100].
# Length of A is in the range of [1, 1000].
# B is in the range of [1, 100].
# Companies
# Google
# Related Topics
# Dynamic Programming
# Similar Questions
# House Robber House Robber II
#
import unittest
#455ms
class Solution(object):
    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        if not A or A[0] == -1: return []
        dp = [[float('inf')] for _ in A]
        dp[0] = [A[0], 1]
        for j in range(1, len(A)):
            if A[j] == -1: continue
            dp[j] = min([dp[i][0] + A[j]] + dp[i][1:] + [j + 1] for i in range(max(0, j - B), j))
        return dp[-1][1:] if dp[-1][0] < float('inf') else []

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/coin-path/solution/

The following solution is based on that:

If there are two path to reach n, and they have the same optimal cost, then the longer path is lexicographically smaller.

Proof by contradiction:
Assume path P and Q have the same cost, and P is strictly shorter and P is lexicographically smaller.
Since P is lexicographically smaller, P and Q must start to differ at some point.
In other words, there must be i in P and j in Q such that i < j and len([1...i]) == len([1...j])
P = [1...i...n]
Q = [1...j...n]
Since i is further away from n there need to be no less steps taken to jump from i to n unless j to n is not optimal
So len([i...n]) >= len([j...n])
So len(P) >= len(Q) which contradicts the assumption that P is strictly shorter.

For example:
Input: [1, 4, 2, 2, 0], 2
Path P = [1, 2, 5]
Path Q = [1, 3, 4, 5]
They both have the same cost 4 to reach n
They differ at i = 2 in P and j = 3 in Q
Here Q is longer but not lexicographically smaller.
Why? Because j = 3 to n = 5 is not optimal.
The optimal path should be [1, 3, 5] where the cost is only 2

#61.37% 27ms
public class Solution {
    public List<Integer> cheapestJump(int[] A, int B) {
        int n = A.length;
        int[] c = new int[n]; // cost
        int[] p = new int[n]; // previous index
        int[] l = new int[n]; // length
        Arrays.fill(c, Integer.MAX_VALUE);
        Arrays.fill(p, -1);
        c[0] = 0;
        for (int i = 0; i < n; i++) {
            if (A[i] == -1) continue;
            for (int j = Math.max(0, i - B); j < i; j++) {
                if (A[j] == -1) continue;
                int alt = c[j] + A[i];
                if (alt < c[i] || alt == c[i] && l[i] < l[j] + 1) {
                    c[i] = alt;
                    p[i] = j;
                    l[i] = l[j] + 1;
                }
            }
        }
        List<Integer> path = new ArrayList<>();
        for (int cur = n - 1; cur >= 0; cur = p[cur]) path.add(0, cur + 1);
        return path.get(0) != 1 ? Collections.emptyList() : path;
    }
}

Approach #2 Using Memoization [Accepted]
# 97.21% 22ms
public class Solution {
    public List < Integer > cheapestJump(int[] A, int B) {
        int[] next = new int[A.length];
        Arrays.fill(next, -1);
        long[] memo = new long[A.length];
        jump(A, B, 0, next, memo);
        List < Integer > res = new ArrayList();
        int i;
        for (i = 0; i < A.length && next[i] > 0; i = next[i])
            res.add(i + 1);
        if (i == A.length - 1 && A[i] >= 0)
            res.add(A.length);
        else
            return new ArrayList < Integer > ();
        return res;
    }
    public long jump(int[] A, int B, int i, int[] next, long[] memo) {
        if (memo[i] > 0)
            return memo[i];
        if (i == A.length - 1 && A[i] >= 0)
            return A[i];
        long min_cost = Integer.MAX_VALUE;
        for (int j = i + 1; j <= i + B && j < A.length; j++) {
            if (A[j] >= 0) {
                long cost = A[i] + jump(A, B, j, next, memo);
                if (cost < min_cost) {
                    min_cost = cost;
                    next[i] = j;
                }
            }
        }
        memo[i] = min_cost;
        return min_cost;
    }
}

Approach #3 Using Dynamic Programming [Accepted]

Algorithm

From the solutions discussed above, we can observe that the cost of jumping till the end of the array A
starting from the index ii is only dependent on the elements following the index i and not the ones before it.
This inspires us to make use of Dynamic Programming to solve the current problem.

We again make use of a next array to store the next jump locations.
We also make use of a dp with the same size as that of the given A array.
dp[i] is used to store the minimum cost of jumping till the end of the array A, starting from the index i.
We start with the last index as the current index and proceed backwards for filling the next and dp array.

# 92.49% 23ms
public class Solution {
    public List < Integer > cheapestJump(int[] A, int B) {
        int[] next = new int[A.length];
        long[] dp = new long[A.length];
        Arrays.fill(next, -1);
        List < Integer > res = new ArrayList();
        for (int i = A.length - 2; i >= 0; i--) {
            long min_cost = Integer.MAX_VALUE;
            for (int j = i + 1; j <= i + B && j < A.length; j++) {
                if (A[j] >= 0) {
                    long cost = A[i] + dp[j];
                    if (cost < min_cost) {
                        min_cost = cost;
                        next[i] = j;
                    }
                }
            }
            dp[i] = min_cost;
        }
        int i;
        for (i = 0; i < A.length && next[i] > 0; i = next[i])
            res.add(i + 1);
        if (i == A.length - 1 && A[i] >= 0)
            res.add(A.length);
        else
            return new ArrayList < Integer > ();
        return res;
    }
}

'''