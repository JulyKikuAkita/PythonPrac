__source__ = 'https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/convert-sorted-array-to-binary-search-tree.py
# Time:  O(n)
# Space: O(logn)
# Divide and Conquer
#
# Given an array where elements are sorted in ascending order,
# convert it to a height balanced BST.
#
# Topics:
# Tree Depth-first Search
# You might like:
# (M) Convert Sorted List to Binary Search Tree
# Company:
# Airbnb
#
import unittest
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        return self.sortedArrayToBSTRecu(num, 0, len(num) - 1 )

    def sortedArrayToBSTRecu(self, num, start, end):
        if start > end:
            return
        mid = start + (end - start) / 2
        #print "mid = " , mid , "mid - 1 = " , (mid -1)
        node = TreeNode(mid)
        node.left = self.sortedArrayToBSTRecu(num, 0, mid - 1 )
        node.right = self.sortedArrayToBSTRecu(num, mid + 1, end)
        return node

class SolutionOther:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        return self.dfs(0, len(num)-1, num)

    def dfs(self, lint, rint, num):
        if lint > rint:
            return None
        mint = (lint + rint)/2  #ex: (0+3)/2 ->1
        # print mint, lint, rint
        node = TreeNode(num[mint])

        node.left = self.dfs(lint, mint-1, num)
        node.right = self.dfs (mint+1, rint, num)
        return node

    def preorderTraversal1(self, root):
        allnodes = []
        p =root

        def preorder(p, ans):
            if p is None:
                return
            ans += [p.val]
            if p.left != None:
                preorder(p.left, ans)

            if p.right != None:
                preorder(p.right, ans)

        preorder(p,allnodes)
        return allnodes

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        num = [1, 2, 3]
        result = Solution().sortedArrayToBST(num)
        print result.val
        print result.left.val
        print result.right.val

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/contains-duplicate/solution/

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
#11.53% 1ms
public class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        return sortedArrayToBST(nums, 0, nums.length - 1);
    }

    private TreeNode sortedArrayToBST(int[] nums, int start, int end) {
        if (start > end) {
            return null;
        }
        int mid = start + (end - start) / 2;
        TreeNode root = new TreeNode(nums[mid]);
        if (start == end) {
            return root;
        }
        root.left = sortedArrayToBST(nums, start, mid - 1);
        root.right = sortedArrayToBST(nums, mid + 1, end);
        return root;
    }
}

# DFS
#11.53% 1ms
public class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        return binarySearch( nums , 0 , nums.length - 1 );
    }

    public static TreeNode binarySearch( int[] nums , int start , int end )
    {
        if( start > end ) return null;
        int mid = ( start + end ) / 2;
        TreeNode node = new TreeNode( nums[mid] );
        node.left = binarySearch( nums , start , mid - 1 );
        node.right = binarySearch( nums , mid + 1 , end );
        return node;
    }
}

I came up with the recursion solution first and tried to translate it into an iterative solution.
It is very similar to doing a tree inorder traversal, I use three stacks - nodeStack stores the node
I am going to process next, and leftIndexStack and rightIndexStack store the range
where this node need to read from the nums.

# BFS
# 1.13% 9ms
public class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        int len = nums.length;
        if ( len == 0 ) { return null; }

        // 0 as a placeholder
        TreeNode head = new TreeNode(0);

        Deque<TreeNode> nodeStack       = new LinkedList<TreeNode>() {{ push(head); }};
        Deque<Integer>  leftIndexStack  = new LinkedList<Integer>()  {{ push(0); }};
        Deque<Integer>  rightIndexStack = new LinkedList<Integer>()  {{ push(len - 1); }};

        while ( !nodeStack.isEmpty() ) {
            TreeNode cur = nodeStack.pop();
            int left = leftIndexStack.pop();
            int right = rightIndexStack.pop();
            int mid = left + (right - left) / 2;
            cur.val = nums[mid];
            if ( left < mid) {
                cur.left = new TreeNode(0);  // 0 as a placeholder
                nodeStack.push(cur.left);
                leftIndexStack.push(left);
                rightIndexStack.push(mid - 1);
            }
            if (right > mid) {
                cur.right = new TreeNode(0);  // 0 as a placeholder
                nodeStack.push(cur.right);
                leftIndexStack.push(mid + 1);
                rightIndexStack.push(right);
            }
        }
        return head;
    }
}

'''