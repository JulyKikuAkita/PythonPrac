__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/binary-tree-longest-consecutive-sequence.py

'''
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
   2
    \
     3
    /
   2
  /
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
Hide Company Tags Google
'''

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# google
#http://algobox.org/binary-tree-longest-consecutive-sequence/

#Python Iterative Breadth-First Search
from collections import deque
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = 0
        dq = deque([[root,1]]) # [[]] otherwise tree obj not iterable err

        while dq:
            node, length = dq.popleft()
            res = max( res, length)
            for child in [node.left, node.right]:
                if child:
                    l = length + 1 if child.val == node.val + 1 else 1
                    dq.append([child,l])
        return res

# Python Iterative Depth-First Search
class Solution2(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = 0
        stack = [[root, 1]]

        while stack:
            node, length = stack.pop()
            res = max(res, length)
            for child in [node.left, node.right]:
                if child:
                    l = length +1 if child.val == node.val + 1 else 1
                    stack.append([child,l])
        return res

class Solution3(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_len = 0

        def longestConsecutiveHelper(root):
            if not root:
                return 0

            left_len = longestConsecutiveHelper(root.left)
            right_len = longestConsecutiveHelper(root.right)

            cur_len = 1
            if root.left and root.left.val == root.val + 1:
                cur_len = max(cur_len, left_len + 1);
            if root.right and root.right.val == root.val + 1:
                cur_len = max(cur_len, right_len + 1)

            self.max_len = max(self.max_len, cur_len, left_len, right_len)

            return cur_len

        longestConsecutiveHelper(root)
        return self.max_len

#java
js = '''
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
    public int longestConsecutive(TreeNode root) {
        if(root == null) return 0;
        int [] res = new int[1];
        dfs(root, res, 0, 0);
        return res[0];
    }

    private void dfs(TreeNode root, int[] res, int candidate, int target){
        if(root == null) return;

        candidate = root.val == target? candidate + 1 : 1;
        if(root.val == target){
            candidate +=1;
        }else{
            candidate = 1;
        }
        dfs(root.left, res, candidate, root.val + 1);
        dfs(root.right, res, candidate, root.val + 1);
        res[0] = Math.max(res[0], candidate);

    }
}


public class Solution {
    public int longestConsecutive(TreeNode root) {
        int[] result = new int[1];
        longestConsecutive(root, result);
        return result[0];
    }

    private int longestConsecutive(TreeNode root, int[] result) {
        if (root == null) {
            return 0;
        }
        int leftLen = longestConsecutive(root.left, result);
        int rightLen = longestConsecutive(root.right, result);
        int curLen = 0;
        if (root.left != null && root.left.val == root.val + 1) {
            curLen = Math.max(curLen, leftLen);
        }
        if (root.right != null && root.right.val == root.val + 1) {
            curLen = Math.max(curLen, rightLen);
        }
        curLen++;
        result[0] = Math.max(result[0], curLen);
        return curLen;
    }
}
'''