__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/construct-binary-tree-from-inorder-and-postorder-traversal.py#L8
# Time:  O(n)
# Space: O(n)
# divide and conquer
#
# Given inorder and postorder traversal of a tree, construct the binary tree.
# root = postorder[-1]
# root = inorder[mid index]

# Note:
# You may assume that duplicates do not exist in the tree.
#
# Bloomberg


# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        lookup = {}
        for i, num in enumerate(inorder):
            lookup[num] = i
        return self.buildTreeRecu(lookup, preorder, inorder, 0, 0, len(inorder))

    def buildTreeRecu(self, lookup, preorder, inorder, pre_start, in_start, in_end):
        # base case
        if in_start == in_end:
            return None
        node = TreeNode(preorder[pre_start])
        i = lookup[preorder[pre_start]]
        node.left = self.buildTreeRecu(lookup, preorder, inorder, pre_start + 1, in_start, i )
        node.right = self.buildTreeRecu(lookup, preorder, inorder, pre_start + 1 + (i - in_start), i + 1, in_end)
        return node

class SolutionOther:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    #http://jelices.blogspot.com/2014/05/leetcode-python-construct-binary-tree.html  explanation
    def buildTree(self, preorder, inorder):
        if len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        rootPos = inorder.index(preorder[0]) # return the corresponding index of array given any value
        print inorder.index(-1)
        root.left = self.buildTree(preorder[1 : 1+rootPos], inorder[ : rootPos])
        root.right = self.buildTree(preorder[rootPos +1:], inorder[rootPos+1:])
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
newTreeRoot = test.buildTree([-1],[-1])
#print test.inorderTraversal1(newTreeRoot)

if __name__ ==  "__main__":
    inorder = [2, 1, 3]
    postorder = [2, 3, 1]
    result = Solution().buildTree(inorder, postorder)
    print result.val
    print result.left.val
    print result.right.val

# java
js = '''
public class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder.length != inorder.length) {
            return null;
        }
        return buildTree(preorder, 0, preorder.length - 1, inorder, 0, inorder.length - 1);
    }

    private TreeNode buildTree(int[] preorder, int preStart, int preEnd, int[] inorder, int inStart, int inEnd) {
        if (preStart > preEnd) {
            return null;
        }
        TreeNode root = new TreeNode(preorder[preStart]);
        int inIndex = find(inorder, preorder[preStart], inStart, inEnd);
        if (inIndex == -1) {
            return root;
        }
        root.left = buildTree(preorder, preStart + 1, preStart + inIndex - inStart, inorder, inStart, inIndex - 1);
        root.right = buildTree(preorder, preStart + inIndex - inStart + 1, preEnd, inorder, inIndex + 1, inEnd);
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