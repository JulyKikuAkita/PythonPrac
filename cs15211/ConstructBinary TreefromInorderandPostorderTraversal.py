__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/construct-binary-tree-from-preorder-and-inorder-traversal.py
# Time:  O(n)
# Space: O(n)
# divide and conquer
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
# root = preorder[0]
# root = inorder[mid]
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# Microsoft



# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        lookup = {}
        for i, num in enumerate(inorder):
            lookup[num] = i
        return self.buildTreeRecu(lookup, postorder, inorder, len(postorder), 0, len(inorder))

    def buildTreeRecu(self, lookup, postorder, inorder, post_end, in_start, in_end):
        #base case
        if in_start == in_end:
            return None
        node = TreeNode(postorder[post_end - 1])
        i = lookup[postorder[post_end - 1]]
        node.left = self.buildTreeRecu(lookup, postorder, inorder, post_end - 1 - (in_end - i - 1), in_start, i)
        node.right = self.buildTreeRecu(lookup, postorder, inorder, post_end  - 1, i  + 1, in_end )
        return node


#OT
class SolutionOther:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0 :
            return None
        root = TreeNode(postorder[-1])
        rootPos = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[: rootPos], postorder[:rootPos])
        root.right = self.buildTree(inorder[rootPos+1:], postorder[rootPos:-1])
        return root

    def inorderTraversal1(self, root):
        ans = []
        p =root

        def inorder(p, ans):
            if p is None:
                return
            if p.left != None:
                inorder(p.left, ans)
            ans += [p.val]
            if p.right != None:
                inorder(p.right, ans)

        inorder(p,ans)
        return ans
#test
test = SolutionOther()
newRoot = test.buildTree([-1], [-1])
print test.inorderTraversal1(newRoot)

if __name__ ==  "__main__":
    preorder = [1, 2, 3]
    inorder = [2, 1, 3]
    result = Solution().buildTree(preorder, inorder)
    print result.val
    print result.left.val
    print result.right.val

#java
js = '''
public class Solution {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        return buildTree(inorder, 0, inorder.length - 1, postorder, 0, postorder.length - 1);
    }

    private TreeNode buildTree(int[] inorder, int inStart, int inEnd, int[] postorder, int postStart, int postEnd) {
        if (postStart > postEnd) {
            return null;
        }
        TreeNode root = new TreeNode(postorder[postEnd]);
        int inIndex = find(inorder, postorder[postEnd], inStart, inEnd);
        root.left = buildTree(inorder, inStart, inIndex - 1, postorder, postStart, postEnd - inEnd + inIndex - 1);
        root.right = buildTree(inorder, inIndex + 1, inEnd, postorder, postEnd - inEnd + inIndex, postEnd - 1);
        return root;
    }

    private int find(int[] arr, int target, int start, int end) {
        for (int i = start; i <= end; i++) {
            if (arr[i] == target) {
                return i;
            }
        }
        return -1;
    }
}
'''