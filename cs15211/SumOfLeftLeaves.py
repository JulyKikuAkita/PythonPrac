__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/sum-of-left-leaves.py

# Time:  O(n)
# Space: O(h)

# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#     3
#   / \
#   9  20
#     /  \
#   15   7
#
# There are two left leaves in the binary tree,
# with values 9 and 15 respectively. Return 24.
#  Facebook
# Hide Tags Tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sumOfLeftLeavesHelper(root, is_left):
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val if is_left else 0
            return sumOfLeftLeavesHelper(root.left, True) + \
                   sumOfLeftLeavesHelper(root.right, False)

        return sumOfLeftLeavesHelper(root, False)

jav = '''
Java iterative and recursive solutions
Recursive method. For given node we check whether its left child is a leaf. If it is the case,
we add its value to answer, otherwise recursively call method on left child.
For right child we call method only if it has at least one nonnull child.
public class Solution {
    public int sumOfLeftLeaves(TreeNode root) {
        return helper(root, false);
    }

    public int helper(TreeNode root, boolean isLeft) {
        if (root == null) return 0;
        if (root.left == null && root.right == null) {
            return isLeft ? root.val : 0;
        }
        return helper(root.left, true) + helper(root.right, false);
    }
}

public int sumOfLeftLeaves(TreeNode root) {
    if(root == null) return 0;
    int ans = 0;
    if(root.left != null) {
        if(root.left.left == null && root.left.right == null) ans += root.left.val;
        else ans += sumOfLeftLeaves(root.left);
    }
    ans += sumOfLeftLeaves(root.right);

    return ans;
}
Iterative method. Here for each node in the tree we check whether its left child is a leaf.
If it is true, we add its value to answer, otherwise add left child to the stack to process it later.
For right child we add it to stack only if it is not a leaf.

public int sumOfLeftLeaves(TreeNode root) {
    if(root == null) return 0;
    int ans = 0;
    Stack<TreeNode> stack = new Stack<TreeNode>();
    stack.push(root);

    while(!stack.empty()) {
        TreeNode node = stack.pop();
        if(node.left != null) {
            if (node.left.left == null && node.left.right == null)
                ans += node.left.val;
            else
                stack.push(node.left);
        }
        if(node.right != null) {
            if (node.right.left != null || node.right.right != null)
                stack.push(node.right);
        }
    }
    return ans;
}

public class Solution {
    public int sumOfLeftLeaves(TreeNode root) {
        if(root == null || root.left == null && root.right == null) return 0;

        int res = 0;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while(!queue.isEmpty()) {
            TreeNode curr = queue.poll();

            if(curr.left != null && curr.left.left == null && curr.left.right == null) res += curr.left.val;
            if(curr.left != null) queue.offer(curr.left);
            if(curr.right != null) queue.offer(curr.right);
        }
        return res;
    }
}
'''