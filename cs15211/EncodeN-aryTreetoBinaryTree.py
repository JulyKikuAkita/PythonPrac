__source__ = 'https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 431. Encode N-ary Tree to Binary Tree
#
# Design an algorithm to encode an N-ary tree into a binary tree and
# decode the binary tree to get the original N-ary tree.
# An N-ary tree is a rooted tree in which each node has no more than N children.
# Similarly, a binary tree is a rooted tree in which each node has no more than 2 children.
# There is no restriction on how your encode/decode algorithm should work.
# You just need to ensure that an N-ary tree can be encoded to a binary tree
# and this binary tree can be decoded to the original N-nary tree structure.
#
# For example, you may encode the following 3-ary tree to a binary tree in this way:
#
# Note that the above is just an example which might or might not work.
# You do not necessarily need to follow this format,
# so please be creative and come up with different approaches yourself.
#
# Note:
#
# N is in the range of [1, 1000]
# Do not use class member/global/static variables to store states.
# Your encode and decode algorithms should be stateless.
#
#
import unittest
# Thought:
# https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/discuss/151772/Python-left-child-for-children-right-child-for-siblings
#
# Python - left child for children, right child for siblings
# The left child of a binary node is the subtree
# encoding all the children of the corresponding n-ary node.
# The right child of a binary node is a chain of the binary root nodes
# encoding each sibling of the n-ary node.
# Hence the root node has no right binary child,
# because the root has no sibilings.
#
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.

        :type root: Node
        :rtype: TreeNode
        """
        if not root:
            return None

        binary = TreeNode(root.val)                 # create a binary root
        if not root.children:
            return binary

        binary.left = self.encode(root.children[0]) # left child of binary is the encoding of all n-ary children,
        node = binary.left                          #     starting with the first child.
        for child in root.children[1:]:             # other children of n-ary root are right child of previous child
            node.right = self.encode(child)
            node = node.right

        return binary

    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.

        :type data: TreeNode
        :rtype: Node
        """
        if not data:
            return None

        nary = Node(data.val, [])                   # create n-ary root
        node = data.left                            # move to first child of n-ary root
        while node:                                 # while more children of n-ary root
            nary.children.append(self.decode(node)) # append to list
            node = node.right                       # and move to next child

        return nary

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/discuss/153061/Java-Solution-(Next-Level-greater-left-Same-Level-greater-right)

#2ms 93.48%
class Codec {
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val,List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Codec {

    // Encodes an n-ary tree to a binary tree.
    public TreeNode encode(Node root) {
        if (root == null) return null;
        TreeNode res = new TreeNode(root.val);
        if (root.children.size() > 0) res.left = encode(root.children.get(0));
        TreeNode cur = res.left;
        for (int i = 1; i < root.children.size(); i++) {
            cur.right = encode(root.children.get(i));
            cur = cur.right;
        }
        return res;
    }

    // Decodes your binary tree to an n-ary tree.
    public Node decode(TreeNode root) {
        if (root == null) return null;
        Node res = new Node(root.val, new LinkedList<>());
        TreeNode cur = root.left;
        while (cur != null) {
            res.children.add(decode(cur));
            cur = cur.right;
        }
        return res;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(root));
'''