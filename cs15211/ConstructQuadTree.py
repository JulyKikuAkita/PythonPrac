__source__ = 'https://leetcode.com/problems/construct-quad-tree/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 427. Construct Quad Tree
#
# We want to use quad trees to store an N x N boolean grid.
# Each cell in the grid can only be true or false.
# The root node represents the whole grid.
# For each node, it will be subdivided into four children nodes
# until the values in the region it represents are all the same.
#
# Each node has another two boolean attributes : isLeaf and val.
# isLeaf is true if and only if the node is a leaf node.
# The val attribute for a leaf node contains the value of the region it represents.
#
# Your task is to use a quad tree to represent a given grid.
# The following example may help you understand the problem better:
#
# Given the 8 x 8 grid below, we want to construct the corresponding quad tree:
#
# It can be divided according to the definition above:
#
# The corresponding quad tree should be as following,
# where each node is represented as a (isLeaf, val) pair.
#
# For the non-leaf nodes, val can be arbitrary, so it is represented as *.
# Note:
#
# N is less than 1000 and guaranteened to be a power of 2.
# If you want to know more about the quad tree, you can refer to its wiki.
#
import unittest

# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

#1155ms 99.30%
class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        if not grid:
            return None

        if self.isLeaf(grid):
            return Node(grid[0][0] == 1, True, None, None, None, None)
        n = len(grid)
        return Node('*',
                   False,
                   self.construct([row[:n/2] for row in grid[:n/2]]),
                   self.construct([row[n/2:] for row in grid[:n/2]]),
                   self.construct([row[:n/2] for row in grid[n/2:]]),
                   self.construct([row[n/2:] for row in grid[n/2:]])
                   )
    def isLeaf(self, grid):
        vals = set()
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                vals.add(grid[i][j])
                if len(vals) > 1:
                    return False
        return True
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:

/*
// Definition for a QuadTree node.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;

    public Node() {}

    public Node(boolean _val,boolean _isLeaf,Node _topLeft,Node _topRight,Node _bottomLeft,Node _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};
*/

# 2ms 100%
class Solution {
    public Node construct(int[][] grid) {
        return helper(grid, 0, 0, grid.length);
    }

    private Node helper(int[][] grid, int i, int j, int len) {
        if (len == 1) return new Node(grid[i][j] == 1, true, null, null, null, null);
        int next_len = len >> 1;
        Node tl = helper(grid, i, j, next_len);
        Node tr = helper(grid, i, j + next_len, next_len);
        Node bl = helper(grid, i + next_len, j, next_len);
        Node br = helper(grid, i + next_len, j + next_len, next_len);
        if (tl.isLeaf && tr.isLeaf && bl.isLeaf && br.isLeaf
            && (tl.val && tr.val && bl.val && br.val ||
                !tl.val && !tr.val && !bl.val && !br.val)) return new Node(tl.val, true, null, null, null, null);
        else {
            return new Node(false, false, tl, tr, bl, br);
        }
    }
}

# 2ms 100%
class Solution {
    public Node construct(int[][] grid) {
        return construct(0, grid.length - 1, 0, grid.length - 1, grid);
    }

    Node construct(int r1, int r2, int c1, int c2, int[][] grid) {
        if (r1 > r2 || c1 > c2) return null;
        boolean isLeaf = true;
        int val = grid[r1][c1];
        for (int i = r1; i <= r2; i++) {
            for (int j = c1; j <= c2; j++) {
                if (grid[i][j] != val) {
                    isLeaf = false;
                    break;
                }
            }
        }
        if (isLeaf) {
            return new Node(val == 1, true, null, null, null, null);
        }
        int rowMid = (r1 + r2) / 2;
        int colMid = (c1 + c2) / 2;
        return new Node(false, false,
            construct(r1, rowMid, c1, colMid, grid),
            construct(r1, rowMid, colMid + 1, c2, grid),
            construct(rowMid + 1, r2, c1, colMid, grid),
            construct(rowMid + 1, r2, colMid + 1, c2, grid));
    }
}
'''