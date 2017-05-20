__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/binary-tree-preorder-traversal.py
# Time:  O(n)
# Space: O(1)
# Tree
#
# Given a binary tree, return the preorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].
#
# Note: Recursive solution is trivial, could you do it iteratively?
#

# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

# Morris Traversal Solution
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        result, prev, cur = [], None, root
        while cur:
            #1) no left child
            if cur.left is None:
                result.append(cur.val)
                #prev = cur
                cur = cur.right
            else:
                node = cur.left
                #2) go to left child's righest most child
                while node.right and node.right != cur:
                    node = node.right

                #3) no right child : node.right = cur and cur= cur.left
                if node.right is None:
                    result.append(cur.val)
                    node.right = cur
                    #prev = cur
                    cur = cur.left
                else:
                #3) has right child : node.right = None and cur = cur.right
                    node.right = None
                    cur = cur.right
        return result




# Time:  O(n)
# Space: O(n)
# Stack Solution
class Solution2:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        result, stack, current, last_traversed = [], [], root, None
        while current or stack:
            if current:
                result.append(current.val)
                stack.append(current)
                current = current.left
            else:
                parent = stack[-1]

                if parent.right in (None, last_traversed):
                    last_traversed = stack.pop()
                else:
                    current = parent.right
        return result




class Solution3:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        result, stack , current, last_traversed = [], [], root, None
        while stack or current:
            if current:
                result.append(current.val)
                stack.append(current)
                current = current.left
            else:
                current = stack[-1]
                stack.pop()
                current = current.right
        return result

# http://www.programcreek.com/2012/12/leetcode-solution-for-binary-tree-preorder-traversal-in-java/
class javaSolution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        result, stack  = [], [root]
        if not root:
            return result
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

class SolutionOther:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal1(self, root):
        ans = []
        p =root

        def preorder(p, ans):
            if p is None:
                return
            ans += [p.val]
            if p.left != None:
                preorder(p.left, ans)

            if p.right != None:
                preorder(p.right, ans)

        preorder(p,ans)
        return ans

    def preorderTraversal3(self, root):
        s= []
        ans = []
        p =root

        while (p != None or len(s) != 0):

            if p != None:
                ans += [p.val]
                if p.right != None:
                    s.append(p.right)
                p = p.left
            else:
                p = s.pop()

        return ans



#create tree
root1=TreeNode(0)
root2=TreeNode(1)
root3=TreeNode(2)
root4=TreeNode(4)
root5=TreeNode(5)

tree2=TreeNode(2)
tree31=TreeNode(3)
tree32=TreeNode(3)
tree41=TreeNode(4)
tree411=TreeNode(4)
tree4111=TreeNode(4)
tree51=TreeNode(1)
tree52=TreeNode(2)
tree511=TreeNode(3)
tree522=TreeNode(4)
tree5221=TreeNode(5)
tree52212=TreeNode(6)

root2.left=tree2

root3.left=tree31
root3.right=tree32

root4.right =tree41
tree41.right=tree411
tree411.right=tree4111

root5.left=tree51
root5.right=tree52
tree51.left=tree511
tree52.right=tree522
tree522.left=tree5221
tree5221.right=tree52212

my_test=SolutionOther()
print my_test.preorderTraversal1(root5)
print my_test.preorderTraversal3(root2)

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    result1 = javaSolution().preorderTraversal(root)
    result2 = Solution2().preorderTraversal(root)
    result3 = Solution3().preorderTraversal(root)
    print result1
    print result2
    print result3

#java
js = '''
public class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        preorder(root, result);
        return result;
    }

    private void preorder(TreeNode root, List<Integer> result) {
        if (root == null) {
            return;
        }
        result.add(root.val);
        preorder(root.left, result);
        preorder(root.right, result);
    }
}

public class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode cur = stack.pop();
            result.add(cur.val);
            if (cur.right != null) {
                stack.push(cur.right);
            }
            if (cur.left != null) {
                stack.push(cur.left);
            }
        }
        return result;
    }
}
'''