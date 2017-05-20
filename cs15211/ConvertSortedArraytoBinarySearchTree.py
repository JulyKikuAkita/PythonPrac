__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/convert-sorted-array-to-binary-search-tree.py
# Time:  O(n)
# Space: O(logn)
# Divide and Conquer
#
# Given an array where elements are sorted in ascending order,
# convert it to a height balanced BST.
#

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

if __name__ == "__main__":
    num = [1, 2, 3]
    result = Solution().sortedArrayToBST(num)
    print result.val
    print result.left.val
    print result.right.val




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
test = SolutionOther()
node = test.sortedArrayToBST([0,1,2,3])
#node = test.sortedArrayToBST([0,1,2,3,4,5,6])
#print test.preorderTraversal1(node)

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
'''