__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/verify-preorder-serialization-of-a-binary-tree.py
# Time:  O(n)
# Space: O(1)

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
#
# Google
# Stack
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

#java
js = '''
public class Solution {
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
'''