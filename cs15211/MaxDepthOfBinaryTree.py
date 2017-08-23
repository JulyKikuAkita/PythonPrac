__source__ = 'https://leetcode.com/problems/maximum-depth-of-binary-tree/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/maximum-depth-of-binary-tree.py
# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Description: Leetcode # 104. Maximum Depth of Binary Tree
#
# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.
#
# Companies
# LinkedIn Uber Apple Yahoo
# Related Topics
# Tree Depth-first Search
# Similar Questions
# Balanced Binary Tree Minimum Depth of Binary Tree
#
import unittest
# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

class SolutionOther:
    # @param root, a tree node
    # @return an integer
    def maxDepthtoFix1(self, root):
        count =[0]

        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        else:
            def deepestNodeToFix(leafnode):

                if leafnode == None:
                    return
                if leafnode.left == None and leafnode.right == None:
                    return
                else:
                     # balanced tree count needs to -1
                    deepestNodeToFix(leafnode.right)
                    print "mid left", count[0]
                    deepestNodeToFix(leafnode.left)
                    print "mid right", count[0]
                    count[0] += 1
                    print "last", count[0]

                return count[0]

            # need to add root node
        return  deepestNodeToFix(root)+1

    def maxDepthtoFix2(self, root):
        lcount =[0]
        rcount =[0]

        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        else:
            def deepestNode2(leafnode):

                if leafnode== None:
                    return

                if leafnode.left != None:
                    deepestNode2(leafnode.left)
                    lcount[0] += 1
                    print "left" , lcount[0],rcount[0]

                if leafnode.right != None:
                    deepestNode2(leafnode.right)
                    rcount[0] += 1
                    print "right" ,lcount[0],rcount[0]

               # return the deepest leaf count
                if lcount[0] >= rcount[0]:
                    return lcount[0]
                else :
                    return rcount[0]
        return  deepestNode2(root)+1


    def maxDepth(self, root):
        count =[0]
        max=[0]

        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        else:
            def deepestNode(leafnode):

                if count[0] > max[0]:
                    print "cmp", max, count[0]
                    max[0] = count[0]

                if leafnode== None :
                    return

                if leafnode.right != None:
                    count[0] += 1
                    print "start right", count[0]
                    deepestNode(leafnode.right)
                    count[0] -= 1
                    print "mid right", count[0]
                if leafnode.left != None:
                    count[0] += 1
                    print "start left", count[0]
                    deepestNode(leafnode.left)
                    count[0] -= 1
                    print "mid left", count[0]

                print "last", max, count[0]
                return max[0]

        # need to add root node
        return  deepestNode(root)+1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

#DFS: 15.60% 1ms
public class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}

#DFS: 15.60% 1ms
public class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null){ return 0; }
        int l = 1 + maxDepth(root.left);
        int r = 1 + maxDepth(root.right);
        if (l > r){ return l; }
        return r;
    }
}

#BFS: 8.81% 2ms
public class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        int res = 0;
        while (!q.isEmpty()) {
            int len = q.size();
            for (int i = 0; i < len; i++) {
                TreeNode cur = q.poll();
                if (cur.left != null) q.offer(cur.left);
                if (cur.right != null) q.offer(cur.right);
            }
            res++;
        }
        return res;
    }
}

'''