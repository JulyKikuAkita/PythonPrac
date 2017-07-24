__source__ = 'https://leetcode.com/problems/flatten-binary-tree-to-linked-list/#/description'
# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Given a binary tree, flatten it to a linked list in-place.
#
# For example,
# Given
#
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
#
#
# Definition for a  binary tree node
# Related Topics
# Tree, Depth-first Search
# Companies
# Microsoft
#
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        return self.flattenRecu(root, None)

    def flattenRecu(self, root, list_head):
        if root != None:
            list_head = self.flattenRecu(root.right, list_head)
            list_head = self.flattenRecu(root.left, list_head)
            root.right = list_head
            root.left = None
            return root
        else:
            return list_head


class Solution2:
    list_head = None
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root != None:
            self.flatten(root.right)
            self.flatten(root.left)
            root.right = self.list_head
            root.left = None
            self.list_head = root
            return root

# http://www.programcreek.com/2013/01/leetcode-flatten-binary-tree-to-linked-list/
# Go down through the left, when right is not null, push right to stack.
class javaSolution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        p, stack = root, []
        while p or stack:
            if p.right != None:
                stack.append(p.right)
            if p.left != None:
                p.right = p.left
                p.left = None
            elif stack:
                p.right = stack.pop()
            p = p.right



if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    result = Solution().flatten(root)
    print result.val
    print result.right.val
    print result.right.right.val
    print result.right.right.right.val
    print result.right.right.right.right.val
    print result.right.right.right.right.right.val

    #print javaSolution().flatten(root)

# http://www.cnblogs.com/zuoyuan/p/3721157.html
class SolutionOther:
    # @param root, a tree node
    # @return nothing, do it in place

    def flatten(self, root):
        if root == None:
            return root
        self.flatten(root.left)
        self.flatten(root.right)

        if root.left == None:
            return
        else:
            p = root.left
            while p.right != None:
                p = p.right

            p.right = root.right
            root.right =root.left
            root.left = None

        return

############test
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
#test
test = SolutionOther()
#test.flatten(root0)

#Java
Java = '''
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
    public void flatten(TreeNode root) {
        dfs_flatten(root, null);
    }

    #25.77%
    private TreeNode dfs_flatten(TreeNode root, TreeNode prev) {
        if (root == null) {
            return prev;
        }
        prev = dfs_flatten(root.right, prev);
        prev = dfs_flatten(root.left, prev);
        root.right = prev;
        root.left = null;
        return root;
    }
    
    #25.77%
    private void bfs_flatten(TreeNode root) {
        TreeNode cur = root;
        while (cur != null) {
            if (cur.left != null) {
                //Find current node's prenode that links to current node's right subtree
                TreeNode pre = cur.left;
                while (pre.right != null) pre = pre.right;
                pre.right = cur.right;
                //Use current node's left subtree to replace its right subtree(original right 
                //subtree is already linked by current node's prenode
                cur.right = cur.left;
                cur.left = null;
            }
            cur = cur.right;
        }
    }
}
'''