__source__ = 'https://leetcode.com/problems/complete-binary-tree-inserter/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 919. Complete Binary Tree Inserter
#
# A complete binary tree is a binary tree in which every level,
# except possibly the last, is completely filled, and all nodes are as far left as possible.
#
# Write a data structure CBTInserter that is initialized
#
# with a complete binary tree and supports the following operations:
#
# CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;
# CBTInserter.insert(int v) will insert a TreeNode into the tree with value node.val = v
# so that the tree remains complete, and returns the value of the parent of the inserted TreeNode;
# CBTInserter.get_root() will return the head node of the tree.
#
# Example 1:
#
# Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
# Output: [null,1,[1,2]]
# Example 2:
#
# Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
# Output: [null,3,4,[1,2,3,4,5,6,7,8]]
#
# Note:
#
# The initial given tree is complete and contains between 1 and 1000 nodes.
# CBTInserter.insert is called at most 10000 times per test case.
# Every value of a given or inserted node is between 0 and 5000.
#
import unittest
import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 44ms 96.69%
class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.deque = collections.deque()
        self.root = root
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        node = self.deque[0]
        self.deque.append(TreeNode(v))
        if not node.left:
            node.left = self.deque[-1]
        else:
            node.right = self.deque[-1]
            self.deque.popleft()
        return node.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/complete-binary-tree-inserter/solution/
Approach 1: Deque
Complexity Analysis
Time Complexity: The preprocessing is O(N), where N is the number of nodes in the tree.
Each insertion operation thereafter is O(1)
Space Complexity: O(N cur) space complexity, when the size of the tree during the current insertion operation is Ncur

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

# 69ms 99.08%
class CBTInserter {
    TreeNode root;
    Deque<TreeNode> deque;

    public CBTInserter(TreeNode root) {
        this.root = root;
        deque = new LinkedList();
        Queue<TreeNode> queue = new LinkedList();
        queue.offer(root);
        // BFS to populate deque
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (node.left == null || node.right == null)
                deque.offerLast(node);
            if (node.left != null)
                queue.offer(node.left);
            if (node.right != null)
                queue.offer(node.right);
        }
    }

    public int insert(int v) {
        TreeNode node = deque.peekFirst();
        deque.offerLast(new TreeNode(v));
        if (node.left == null)
            node.left = deque.peekLast();
        else {
            node.right = deque.peekLast();
            deque.pollFirst();
        }

        return node.val;
    }

    public TreeNode get_root() {
        return root;
    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter obj = new CBTInserter(root);
 * int param_1 = obj.insert(v);
 * TreeNode param_2 = obj.get_root();
 */

'''