__source__ = 'https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/verify-preorder-serialization-of-a-binary-tree.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 331. Verify Preorder Serialization of a Binary Tree
#
# One way to serialize a binary tree is to use pre-oder traversal.
# When we encounter a non-null node, we record the node's value.
# If it is a null node, we record using a sentinel value such as #.
#
#      _9_
#     /   \
#   3     2
#   / \   / \
#  4   1  #  6
# / \ / \   / \
# # # # #   # #
# For example, the above binary tree can be serialized to the string
# "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.
#
# Given a string of comma separated values, verify whether it is a
# correct preorder traversal serialization of a binary tree.
# Find an algorithm without reconstructing the tree.
#
# Each comma separated value in the string must be either an integer
# or a character '#' representing null pointer.
#
# You may assume that the input format is always valid, for example
# it could never contain two consecutive commas such as "1,,3".
#
# Example 1:
# "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Return true
#
# Example 2:
# "1,#"
# Return false
#
# Example 3:
# "9,#,#,1"
# Return false
#
# Companies
# Google
# Related Topics
# Stack
#
import unittest
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        def split_iter(s, tok):
            start = 0
            for i in xrange(len(s)):
                if s[i] == tok:
                    yield s[start:i]
                    start = i + 1
            yield s[start:]

        if not preorder:
            return False
        depth = 0
        cnt  = preorder.count(',') + 1
        for tok in split_iter(preorder, ','):
            cnt -= 1
            if tok == '#':
                depth -= 1
                if depth < 0:
                    break
            else:
                depth += 1
        return cnt == 0 and depth < 0

class Solution2(unittest.TestCase):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(',')
        cnt = 0
        for i in xrange(len(nodes)):
            if nodes[i] == "#":
                cnt -= 1
                if cnt < 0:
                    return i == len(nodes) - 1
            else:
                cnt += 1
        return cnt == -1

    def test(self):
        self.assertTrue(self.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 5ms 91.15%
class Solution {
    public boolean isValidSerialization(String preorder) {
        String[] tokens = preorder.split(",");
        int count = 0;
        int index = 0;
        while (index < tokens.length) {
            if (tokens[index++].equals("#")) {
                count--;
                if (count < 0) {
                    break;
                }
            } else {
                count++;
            }
        }
        return count == -1 && index == tokens.length;
    }
}

# 5ms 91.15%
class Solution {
    public boolean isValidSerialization(String preorder) {
        String[] nodes = preorder.split(",");
        int count = 0;
        for (int i = 0; i < nodes.length; i++) {
            if (nodes[i].equals("#")) {
                count--;
                if (count < 0) {
                    return i == nodes.length - 1;
                }
            } else {
                count++;
            }
        }
        return count == -1;
    }
}

# 2ms 98.93%
class Solution {
    public boolean isValidSerialization(String preorder) {
        Deque<Character> stack = new ArrayDeque();
        char[] preArr = preorder.toCharArray();
        for (int i = 0; i < preArr.length - 1; i++) {
            char c = preArr[i];
            if (c == ',') { continue; }
            if (c != '#') {
                stack.push(c);
                while (i < preArr.length - 1 && c != ',') { c = preArr[++i]; }
            } else {
                if (stack.isEmpty()) { return false; }
                stack.pop();
            }
        }

        return stack.isEmpty() && preArr[preArr.length - 1] == '#';
    }
}
'''