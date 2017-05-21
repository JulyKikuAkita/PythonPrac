__source__ = 'https://leetcode.com/problems/symmetric-tree/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/symmetric-tree.py
# Time:  O(n)
# Space: O(h), h is height of binary tree
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# Stack
#
# For example, this binary tree is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.
#
# LinkedIn Bloomberg Microsoft
# Hide Tags Tree Depth-first Search Breadth-first Search
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Iterative solution
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is None:
            return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)

        while stack:
            left ,right = stack.pop(), stack.pop()

            if left is None and right is None:
                continue
            if left is None or right is None or left.val != right.val:
                return False

            stack.append(left.left)
            stack.append(right.right)

            stack.append(left.right)
            stack.append(right.left)

        return True

if __name__ == "__main__":
    root = TreeNode(1)
    root.left, root.right = TreeNode(2), TreeNode(2)
    root.left.left, root.right.right = TreeNode(3), TreeNode(3)
    root.left.right, root.right.left = TreeNode(4), TreeNode(4)
    print Solution().isSymmetric(root)



class SolutionRecu:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
         if root == None:
             return True
         return self.checkSymmetric(root.left, root.right)

    def checkSymmetric(self, left, right):
        if left == right == None:
            return True

        # if either left or right node not exist
        if not (left and right):
            return False

        if left.val != right.val:
            return False

        return self.checkSymmetric(left.left, right.right ) and self.checkSymmetric(left.right, right.left)

# inorder won't work
# ex: [1,2,3,3,null,2,null]
class Wrong(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        ans = []
        self.inOrder( ans, root)

        for i in xrange((len(ans)/ 2)+1):
            if ans[i] != ans[-(i+1)]:
                print ans[i], ans[-i]
                return False
            else:
                print ans, i, -i, ans[i], ans[-i]
                return True


    def inOrder(self, res, root):
        if not root:
            return
        if root.left:
            self.inOrder(res, root.left)
        res.append(root.val)
        if root.right:
            self.inOrder(res, root.right)



#test
#############test
#creating BST tree ####
root0=TreeNode(0)
tree1=TreeNode(1)
tree2=TreeNode(2)
tree3=TreeNode(3)
tree4=TreeNode(4)
tree5=TreeNode(5)
tree6=TreeNode(6)
root0.left=tree1
root0.right=tree2
tree1.left=tree3
tree1.right=tree4
tree2.left=tree5
tree2.right=tree6
#end of creating BST tree ####

#creating BST tree ####
qroot0=TreeNode(0)
qtree1=TreeNode(1)
qtree2=TreeNode(1)
qtree3=TreeNode(2)
qtree4=TreeNode(2)
qtree5=TreeNode(2)
qtree6=TreeNode(2)
qroot0.left=qtree1
qroot0.right=qtree2
qtree1.left=qtree3
qtree1.right=qtree4
qtree2.left=qtree5
qtree2.right=qtree6
#end of creating BST tree ####
#test = Solutioniter()
#print test.isSymmetric(qroot0)

java = '''
Thought:  https://leetcode.com/articles/symmetric-tree/
# DFS
public boolean isSymmetric(TreeNode root) {
    return isMirror(root, root);
}

public boolean isMirror(TreeNode t1, TreeNode t2) {
    if (t1 == null && t2 == null) return true;
    if (t1 == null || t2 == null) return false;
    return (t1.val == t2.val)
        && isMirror(t1.right, t2.left)
        && isMirror(t1.left, t2.right);
}
private boolean isMirror2(TreeNode t1, TreeNode t2){
    if(t1==null || t2==null)
        return t1==t2;
    if(t1.val!=t2.val)
        return false;
    return isMirror2(t1.left, t2.right) && isMirror2(t1.right, t2.left);
}

# BFS
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
    public boolean isSymmetric(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        if(root == null) return true;
        q.add(root);
        q.add(root);
        while(!q.isEmpty()) {
            TreeNode t1 = q.poll();
            TreeNode t2 = q.poll();
            if ( t1 == null && t2 == null) continue;
            if ( t1 == null || t2 == null) return false;
            if ( t1.val != t2.val) return false;
            q.offer(t1.left);
            q.offer(t2.right);
            q.offer(t1.right);
            q.offer(t2.left);
        }
        return true;
    }
}
'''