__source__ = 'https://leetcode.com/problems/print-binary-tree/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 655. Print Binary Tree
#
# Print a binary tree in an m*n 2D string array following these rules:
#
# The row number m should be equal to the height of the given binary tree.
# The column number n should always be an odd number.
# The root node's value (in string format) should be put in the exactly middle of the first row it can be put.
# The column and the row where the root node belongs will separate the rest space into two parts
# (left-bottom part and right-bottom part).
# You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part.
# The left-bottom part and the right-bottom part should have the same size.
# Even if one subtree is none while the other is not,
# you don't need to print anything for the none subtree
# but still need to leave the space as large as that for the other subtree.
# However, if two subtrees are none, then you don't need to leave space for both of them.
#
# Each unused space should contain an empty string "".
# Print the subtrees following the same rules.
# Example 1:
# Input:
#      1
#     /
#    2
# Output:
# [["", "1", ""],
#  ["2", "", ""]]
# Example 2:
# Input:
#      1
#     / \
#    2   3
#     \
#      4
# Output:
# [["", "", "", "1", "", "", ""],
#  ["", "2", "", "", "", "3", ""],
#  ["", "", "4", "", "", "", ""]]
# Example 3:
# Input:
#       1
#      / \
#     2   5
#    /
#   3
#  /
# 4
# Output:
#
# [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
#  ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
#  ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
#  ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
# Note: The height of binary tree is in the range of [1, 10].
#
# Companies
# Poynt
# Related Topics
# Tree
#

import unittest

#42ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root: return [""]

        def depth(root):
            if not root: return 0
            return max(depth(root.left), depth(root.right)) + 1

        d = depth(root)
        self.res = [[""] * (2**d - 1) for _ in xrange(d)]

        def helper(node, d, pos):
            self.res[-d - 1][pos] = str(node.val)
            if node.left: helper(node.left, d - 1, pos - 2**(d - 1))
            if node.right: helper(node.right, d - 1, pos + 2**(d - 1))

        helper(root, d - 1, 2**(d - 1) - 1)
        return self.res

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/print-binary-tree/solution/
# 57.48% 8ms
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List<List<String>> printTree(TreeNode root) {
        List<List<String>> res = new LinkedList<>();
        int height = root == null ? 1 : getHeight(root);
        int row = height;
        int col = (1 << height) - 1; // Math.pow(2, height) - 1
        List<String> list = new ArrayList<>();
        for (int i = 0; i < col; i++) list.add("");
        for (int i = 0; i < row ; i++) res.add(new ArrayList<>(list));
        fillColumn(root, res, 0, row, 0, col - 1);
        return res;
    }

    public void fillColumn(TreeNode root,  List<List<String>> res, int row, int totalRows, int start, int end) {
        if (row == totalRows || root == null) return;
        int mid = (int) start + (end - start) / 2;
        res.get(row).set(mid, root.val + "");
        fillColumn(root.left, res, row + 1, totalRows, start, mid - 1);
        fillColumn(root.right, res, row + 1, totalRows, mid + 1, end);
    }

    public int getHeight(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(getHeight(root.left), getHeight(root.right));
    }
}

Approach #2 Using queue(BFS)[Accepted]
#3.44% 14ms
public class Solution {
    class Params {
        Params(TreeNode n, int ii, int ll, int rr) {
            root = n;
            i = ii;
            l = ll;
            r = rr;
        }
        TreeNode root;
        int i, l, r;
    }
    public List<List<String>> printTree(TreeNode root) {
        int height = getHeight(root);
        String[][] res = new String[height][(1 << height) - 1];
        for (String[] arr: res) Arrays.fill(arr, "");
        List<List<String>> ans = new ArrayList<>();
        fill(res, root, 0, 0, res[0].length);
        for (String[] arr: res) ans.add(Arrays.asList(arr));
        return ans;
    }
    public void fill(String[][] res, TreeNode root, int i, int l, int r) {
        Queue<Params> queue = new LinkedList();
        queue.add(new Params(root, 0, 0, res[0].length));
        while (!queue.isEmpty()) {
            Params p = queue.remove();
            res[p.i][(p.l + p.r) / 2] = "" + p.root.val;
            if (p.root.left != null)
                queue.add(new Params(p.root.left, p.i + 1, p.l, (p.l + p.r) / 2));
            if (p.root.right != null)
                queue.add(new Params(p.root.right, p.i + 1, (p.l + p.r + 1) / 2, p.r));
        }
    }
    public int getHeight(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList();
        queue.add(root);
        int height = 0;
        while (!queue.isEmpty()) {
            height++;
            Queue<TreeNode> temp = new LinkedList();
            while (!queue.isEmpty()) {
                TreeNode node = queue.remove();
                if (node.left != null)
                    temp.add(node.left);
                if (node.right != null)
                    temp.add(node.right);
            }
            queue = temp;
        }
        return height;
    }
}
'''