__source__ = 'https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 428. Serialize and Deserialize N-ary Tree
#
# Serialization is the process of converting a data structure or object into a sequence of bits
# so that it can be stored in a file or memory buffer,
# or transmitted across a network connection link to be reconstructed later in the same
# or another computer environment.
#
# Design an algorithm to serialize and deserialize an N-ary tree.
# An N-ary tree is a rooted tree in which each node has no more than N children.
# There is no restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that an N-ary tree can be serialized to a string
# and this string can be deserialized to the original tree structure.
#
# For example, you may serialize the following 3-ary tree
#
# as [1 [3[5 6] 2 4]]. You do not necessarily need to follow this format,
# so please be creative and come up with different approaches yourself.
#
# Note:
#
# N is in the range of [1, 1000]
# Do not use class member/global/static variables to store states.
# Your serialize and deserialize algorithms should be stateless.
#
import unittest

class Solution(object):
    pass  # your function here

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
#
# Template for N-Ray tree vs binary tree
# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/discuss/190318/Serialize-and-Deserialize-Binary-and-N-ary-Tree-Summary

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

# 13ms 65.42%
class Codec {
    String NN = "X";
    String spliter = ",";

    // Encodes a tree to a single string.
    public String serialize(Node root) {
        StringBuilder sb = new StringBuilder();
        buildString(root, sb);
        return sb.toString();
    }

    private void buildString(Node node, StringBuilder sb) {
        if (node == null) {
            sb.append(NN);
            sb.append(spliter);
        } else {
            sb.append(node.val);
            sb.append(spliter);
            sb.append(node.children.size());
            sb.append(spliter);
            for (Node child : node.children) {
                buildString(child, sb);
            }
        }
    }

    // Decodes your encoded data to tree.
    public Node deserialize(String data) {
        Deque<String> deque = new ArrayDeque<>(Arrays.asList(data.split(spliter)));
        return buildTree(deque);
    }

    private Node buildTree(Deque<String> deque) {
        String s1 = deque.removeFirst();
        if (s1.equals(NN)) return null;

        int rootVal = Integer.valueOf(s1);
        int childrenNumber = Integer.valueOf(deque.removeFirst());

        Node root = new Node(rootVal);
        root.children = new ArrayList();
        for (int i = 0; i < childrenNumber; i++) {
            root.children.add(buildTree(deque));
        }
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));

# Java BFS using queue
# 12ms 72.48%
class Codec {
    // Encodes a tree to a single string.
    public String serialize(Node root) {
        if (root == null) return "0,-1";

        Queue<Node> queue = new LinkedList();
        StringBuilder res = new StringBuilder();
        queue.add(root);
        while(!queue.isEmpty()) {
            Node cur = queue.remove();
            res.append(cur.val + "," + cur.children.size() + ",");
            for (Node child: cur.children) queue.add(child);
        }
        return res.toString();
    }

    // Decodes your encoded data to tree.
    public Node deserialize(String data) {
        String[] strs = data.split(",");
        if (strs[1].equals("-1")) return null;

        Queue<Node> q_node = new LinkedList();
        Queue<Integer> q_len = new LinkedList();

        Node root = new Node(Integer.valueOf(strs[0]));
        root.children = new ArrayList();
        q_node.add(root);
        q_len.add(Integer.valueOf(strs[1]));
        int index = 2;
        while (index < strs.length) {
            Node cur = q_node.remove();
            int len = q_len.remove();
            for (int i = 0; i < len; i++) {
                int val = Integer.valueOf(strs[index + i * 2]);
                Node child = new Node(val);
                q_node.add(child);
                q_len.add(Integer.valueOf(strs[index + i * 2 + 1]));
                child.children = new ArrayList();
                cur.children.add(child);
            }
            index += len * 2;
        }
        return root;
    }
}

'''
