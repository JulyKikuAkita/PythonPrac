__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/lowest-common-ancestor-of-a-binary-tree.py
# Time:  O(h)
# Space: O(h)
#
# Given a binary tree, find the lowest common ancestor (LCA)
# of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia: "The lowest
# common ancestor is defined between two nodes v and w as the
# lowest node in T that has both v and w as descendants (where we
# allow a node to be a descendant of itself)."
#
#         _______3______
#       /              \
#     ___5__          ___1__
#   /      \        /      \
#   6      _2       0       8
#          /  \
#          7   4
# For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3.
# Another example is LCA of nodes 5 and 4 is 5, since a node can be a
# descendant of itself according to the LCA definition.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#  Amazon LinkedIn Apple Facebook Microsoft
# Hide Tags Tree
# Hide Similar Problems (E) Lowest Common Ancestor of a Binary Search Tree


#DFS
class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q):
            return root
        left, right = [self.lowestCommonAncestor(child, p, q) for child in  (root.left, root.right)]

        # 1. If the current subtree contains both p and q,
        #    return their LCA.
        # 2. If only one of them is in that subtree,
        #    return that one of them.
        # 3. If neither of them is in that subtree,
        #    return the node of that subtree.

        return root if left and right else left or right

#BFS
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        parent = {root:None}

        while q not in parent or p not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        ancestor = set()
        while p:
            ancestor.add(p)
            p = parent[p]

        while q not in ancestor:
            q = parent[q]

        return q
    def lowestCommonAncestor2(self, root, p, q):
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q)
                   for kid in (root.left, root.right))
        return root if left and right else left or right

    def lowestCommonAncestor3(self, root, p, q):
        if root in (None, p, q): return root
        subs = [self.lowestCommonAncestor(kid, p, q)
                for kid in (root.left, root.right)]
        return root if all(subs) else max(subs)




# http://algobox.org/lowest-common-ancestor-of-a-binary-tree/
#java
#DFS
js = '''
public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) return root;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        if (left != null && right != null) return root;
        return left == null ? right : left;
    }
}

#BFS

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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        Map<TreeNode, TreeNode> parent = new HashMap<>();
        parent.put(root, null);
        Deque<TreeNode> stack = new ArrayDeque<>();
        stack.push(root);

        while(!parent.containsKey(p) || !parent.containsKey(q)){
            TreeNode node = stack.pop();
            if(node.left != null){
                parent.put(node.left, node);
                stack.push(node.left);
            }

            if(node.right != null){
                parent.put(node.right, node);
                stack.push(node.right);
            }
        }

        Set<TreeNode> ancestors = new HashSet<>();
        while(p != null){
            ancestors.add(p);
            p = parent.get(p);
        }
        while(!ancestors.contains(q)){
            q = parent.get(q);
        }
        return q;
    }
}
'''