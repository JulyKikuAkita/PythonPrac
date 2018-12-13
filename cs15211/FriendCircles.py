__source__ = 'https://leetcode.com/problems/friend-circles/'
# Time:  O(n^2)
# Space: O(n)
#
# Description: 547. Friend Circles
#
# There are N students in a class. Some of them are friends, while some are not.
# Their friendship is transitive in nature. For example, if A is a direct friend of B,
# and B is a direct friend of C, then A is an indirect friend of C.
# And we defined a friend circle is a group of students who are direct or indirect friends.
#
# Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1,
# then the ith and jth students are direct friends with each other, otherwise not.
# And you have to output the total number of friend circles among all the students.
#
# Example 1:
# Input:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
# The 2nd student himself is in a friend circle. So return 2.
# Example 2:
# Input:
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
# so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
# Note:
# N is in range [1,200].
# M[i][i] = 1 for all students.
# If M[i][j] = 1, then M[j][i] = 1.
#
# Hide Company Tags Two Sigma
# Hide Tags Depth-first Search Union Find
# Hide Similar Problems (M) Number of Connected Components in an Undirected Graph

import unittest
import scipy.sparse
import numpy as np
class Solution(object):
    # 108ms 21.53%
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        return scipy.sparse.csgraph.connected_components(M)[0]

    # 176ms 11.49%
    def findCircleNum2(self, M):
        return len(set(map(tuple, (np.matrix(M, dtype='bool')**len(M)).A)))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/friend-circles/solution/
unionfind, different from island

# DFS
# 5ms 98.23%
class Solution {
    public int findCircleNum(int[][] M) {
        int[] visited = new int[M.length];
        int count = 0;
        for (int i = 0; i < M.length; i++) {
            if (visited[i] == 0) {
                dfs(M, visited, i);
                count++;
            }
        }
        return count;
    }

    public void dfs(int[][] M, int[] visited, int index) {
        for (int j = 0; j < M.length; j++) {
            if (M[index][j] == 1 && visited[j] == 0) {
                visited[j] = 1;
                dfs(M, visited, j);
            }
        }
    }
}

2. This is a typical Union Find problem.
I abstracted it as a standalone class.
Remember the template, you will be able to use it later.

# 6ms 84.19%
class Solution {
    public int findCircleNum(int[][] M) {
        UnionFind uf = new UnionFind(M.length);
        for (int i = 0; i < M.length - 1; i++) {
            for (int j = i + 1; j < M.length; j++) {
                if (M[i][j] == 1) {
                    uf.union(i, j);
                }
            }
        }
        return uf.count();
    }

    class UnionFind {
        private int mCount = 0;
        private int[] mParent, mRank;

        public UnionFind(int n) {
            mCount = n;
            mParent = new int[n];
            mRank = new int[n];
            for (int i = 0; i < n; i++) {
                mParent[i] = i;
            }
        }

        public int find(int p) {
        	while(p != mParent[p]) {
        	    // path compression by halving
        	    mParent[p] = mParent[mParent[p]];
        	    p = mParent[p];
        	}
        	return p;
        }

        public void union(int p, int q) {
            int rootP = find(p);
            int rootQ = find(q);
            if (rootP == rootQ) return;
            if (mRank[rootQ] > mRank[rootP]) {
                mParent[rootP] = rootQ;
            } else {
                mParent[rootQ] = rootP;
                if (mRank[rootQ] == mRank[rootP]) {
                    mRank[rootQ]++;
                }
            }
            mCount--;
        }

        public int count() {
            return mCount;
        }
    }
}
'''