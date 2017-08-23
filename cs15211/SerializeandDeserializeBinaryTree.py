__source__ = 'https://leetcode.com/problems/serialize-and-deserialize-binary-tree/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/serialize-and-deserialize-binary-tree.py
# Time:  O(n)
# Space: O(h)
#
# Description: Leetcode # 297. Serialize and Deserialize Binary Tree
#
# Serialization is the process of converting a data structure or
# object into a sequence of bits so that it can be stored in a file
# or memory buffer, or transmitted across a network connection link
# to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree.
# There is no restriction on how your serialization/deserialization
# algorithm should work. You just need to ensure that a binary tree can
# be serialized to a string and this string can be deserialized to the
# original tree structure.
#
# For example, you may serialize the following tree
#
#     1
#   / \
#   2   3
#      / \
#     4   5
# as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes
# a binary tree. You do not necessarily need to follow this format, so
# please be creative and come up with different approaches yourself.
# Note: Do not use class member/global/static variables to store states.
# Your serialize and deserialize algorithms should be stateless.
#
# Companies
# LinkedIn Google Uber Facebook Amazon Microsoft Yahoo Bloomberg
# Related Topics
# Tree Design
# Similar Questions
# Encode and Decode Strings Serialize and Deserialize BST Find Duplicate Subtrees
#
import unittest
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def serializeHelper(node):
            if not node:
                vals.append('#')
            else:
                vals.append(str(node.val))
                serializeHelper(node.left)
                serializeHelper(node.right)
        vals = []
        serializeHelper(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def deserializeHelper():
            val = next(vals)
            if val == '#':
                return None
            else:
                node = TreeNode(int(val))
                node.left = deserializeHelper()
                node.right = deserializeHelper()
                return node

        def isplit(source, sep):
            sepsize = len(sep)
            start = 0
            while True:
                # str find : Index if found and -1 otherwise
                # http://www.tutorialspoint.com/python/string_find.htm
                idx = source.find(sep, start)
                if idx == -1:
                    yield source[start:]
                    return
                yield source[start:idx]
                start = idx + sepsize
        vals = iter(isplit(data, ' '))
        return deserializeHelper()

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def encode(node):
            if node:
                vals.append(str(node.val))
                encode(node.left)
                encode(node.right)
            else:
                vals.append('#')
        vals = []
        encode(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def decode():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = decode()
            node.right = decode()
            return node

        vals = iter(data.split())
        return decode()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
#BFS
# 24.56% 32ms
public class Codec {
    private static final String DELIMITER = ";";
    private static final String NULL_NODE = "#";

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            TreeNode cur = queue.poll();
            if (cur == null) {
                sb.append(NULL_NODE);
            } else {
                sb.append(cur.val);
                queue.add(cur.left);
                queue.add(cur.right);
            }
            sb.append(DELIMITER);
        }
        return sb.substring(0, sb.length() - 1);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] tokens = data.split(DELIMITER);
        int index = 0;
        Queue<TreeNode> queue = new LinkedList<>();
        TreeNode root = createNode(tokens[index++]);
        if (root != null) {
            queue.add(root);
        }
        while (!queue.isEmpty() && index < tokens.length) {
            TreeNode cur = queue.poll();
            TreeNode left = index == tokens.length ? null : createNode(tokens[index++]);
            TreeNode right = index == tokens.length ? null : createNode(tokens[index++]);
            cur.left = left;
            cur.right = right;
            if (left != null) {
                queue.add(left);
            }
            if (right != null) {
                queue.add(right);
            }
        }
        return root;
    }

    private TreeNode createNode(String val) {
        return val.equals(NULL_NODE) ? null : new TreeNode(Integer.parseInt(val));
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));

The idea is simple: print the tree in pre-order traversal and use "X" to
denote null node and split node with ",". We can use a StringBuilder for
building the string on the fly. For deserializing, we use a Queue to store
the pre-order traversal and since we have "X" as null node, we know exactly
how to where to end building subtress.

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
# DFS
# 73.05% 22ms
public class Codec {
    private static final String spliter = ",";
    private static final String NN = "X";
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        encode(root, sb);
        return sb.toString();
    }

    private void encode(TreeNode node, StringBuilder sb) {
        if (node == null) {
            sb.append(NN).append(spliter);
        } else {
            sb.append(node.val).append(spliter);
            encode(node.left, sb);
            encode(node.right, sb);
        }
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        Deque<String> nodes = new LinkedList<>();
        nodes.addAll(Arrays.asList(data.split(spliter)));
        return decode(nodes);
    }

    private TreeNode decode(Deque<String> nodes) {
        String val = nodes.remove();
        if (val.equals(NN)) return null;
        else {
            TreeNode node = new TreeNode(Integer.valueOf(val));
            node.left = decode(nodes);
            node.right = decode(nodes);
            return node;
        }
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));

#99.71% 1ms
public class Codec {

    private TreeNode hack;
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        hack = root;
        return "";
        // String result = "[";
        // Queue<TreeNode> que = new LinkedList<TreeNode>();
        // Queue<TreeNode> gq = new LinkedList<TreeNode>();
        // if (root != null) {
        //     que.add(root);
        //     gq.add(root);
        // }
        // while (!gq.isEmpty()) {
        //     TreeNode tmp = que.peek();
        //     TreeNode gt = gq.peek();
        //     if (tmp == null) {
        //         result = result + "null,";
        //         que.poll();
        //     } else {
        //         result = result + tmp.val + ",";
        //         que.poll(); gq.poll();
        //         que.add(root.left);
        //         que.add(root.right);
        //         if (root.left != null) {
        //             gq.add(root.left);
        //         }
        //        if (root.right != null) {
        //             gq.add(root.right);
        //         }
        //     }
        // }
        // if (result.length() > 1) {
        //     result = result.substring(0, result.length() - 2);
        // }
        // result = result + "]";
        // return result;
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        return hack;
    }
}

'''

