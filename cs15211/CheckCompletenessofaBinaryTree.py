__source__ = 'https://leetcode.com/problems/check-completeness-of-a-binary-tree/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 958. Check Completeness of a Binary Tree
#
# Given a binary tree, determine if it is a complete binary tree.
#
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last,
# is completely filled, and all nodes in the last level are as far left as possible.
# It can have between 1 and 2h nodes inclusive at the last level h.
#
# Example 1:
#
# Input: [1,2,3,4,5,6]
# Output: true
# Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}),
# and all nodes in the last level ({4, 5, 6}) are as far left as possible.
#
# Example 2:
#
# Input: [1,2,3,4,5,null,7]
# Output: false
# Explanation: The node with value 7 isn't as far left as possible.
#
# Note:
#
#     The tree will have between 1 and 100 nodes.
#
import unittest

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 40ms 37.14%
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodes = [(root, 1)]
        i = 0
        while i < len(nodes):
            node, v = nodes[i]
            i += 1
            if node:
                nodes.append((node.left, 2*v))
                nodes.append((node.right, 2*v+1))

        return  nodes[-1][1] == len(nodes)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/check-completeness-of-a-binary-tree/solution/
#
Approach 1: Breadth First Search
Complexity Analysis
Time Complexity: O(N), where N is the number of nodes in the tree.
Space Complexity: O(N)

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
 
# 12ms 4.73%
class Solution {
    public boolean isCompleteTree(TreeNode root) {
        List<ANode> nodes = new ArrayList();
        nodes.add(new ANode(root, 1));
        int i = 0;
        while (i < nodes.size()) {
            ANode anode = nodes.get(i++);
            if (anode.node != null) {
                nodes.add(new ANode(anode.node.left, anode.code * 2));
                nodes.add(new ANode(anode.node.right, anode.code * 2 + 1));
            }
        }

        return nodes.get(i-1).code == nodes.size();
    }
}

class ANode {  // Annotated Node
    TreeNode node;
    int code;
    ANode(TreeNode node, int code) {
        this.node = node;
        this.code = code;
    }
}

# 9ms 24.55%
class Solution {
    public boolean isCompleteTree(TreeNode root) {
        if (root == null) return true;
        Queue<TreeNode> queue = new LinkedList<>();
        boolean flag = false;
        queue.offer(root);
        while (!queue.isEmpty()){
            TreeNode cur = queue.poll();
            if (cur.left == null) flag = true;
            else if (flag) return false;
            else queue.offer(cur.left);
            if (cur.right == null) flag = true;
            else if (flag) return false;
            else queue.offer(cur.right);
        }
        return true;
    }
}
'''
