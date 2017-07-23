__source__ = 'https://leetcode.com/problems/binary-tree-inorder-traversal/#/description'
#https://github.com/kamyu104/LeetCode/blob/master/Python/binary-tree-inorder-traversal.py
# Time:  O(n)
# Space: O(1)
# tree
#
# Given a binary tree, return the inorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#   1
#    \
#     2
#    /
#   3
# return [1,3,2].
#
# Note: Recursive solution is trivial, could you do it iteratively?
# Company:
# Microsoft
# Topics:
# Tree Hash Table Stack
# You might like:
# (M) Validate Binary Search Tree (M) Binary Tree Preorder Traversal (H) Binary Tree Postorder Traversal
# (M) Binary Search Tree Iterator (M) Kth Smallest Element in a BST (H) Closest Binary Search Tree Value II
# (M) Inorder Successor in BST
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
    def inorderTraversal(self, root):
        result, prev, cur = [], None, root
        while cur:

            #1) no left child
            if cur.left == None:
                result.append(cur.val)
                prev = cur
                cur = cur.right
            else:
                #2) go to left child's rightmost leaf
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right

                #3) no right child: node.right = cur and cur = cur.left
                if node.right is None:
                    node.right = cur
                    cur = cur.left

                #4) has right child : node.right = None and cur = cur.left
                else:
                    result.append(cur.val)
                    node.right = None
                    prev = cur
                    cur = cur.right
        return result



# Time:  O(n)
# Space: O(n)
# Stack Solution
class Solution2:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        result, stack, current, last_traversed = [], [], root, None
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                parent = stack[-1]
                if parent.right in (None, last_traversed):  # last_traversed does not have effect to me
                    if parent.right == None:
                        result.append(parent.val)
                    last_traversed = stack.pop()
                else:
                    result.append(parent.val)
                    current = parent.right

class Solution3:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        result, stack, current, last_traversed = [], [], root, None
        while stack or current:
            # if it is not null, push to stack
            # and go down the tree to left
            if current:
                stack.append(current)
                current = current.left
            # if no left child
            # pop stack, process the node
            # then let p point to the right
            else:
                current = stack[-1]
                result.append(current.val)
                stack.pop()
                current = current.right
        return result


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

my_test=Solution()
#print my_test.inorderTraversal1(root2)
#print my_test.inorderTraversal3(root2)

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print Solution().inorderTraversal(root)
    print Solution3().inorderTraversal(root)

#Java
Java = '''
# DFS 37%
public class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        dfs(root, res);
        return res;
    }

    private void dfs(TreeNode root, List<Integer> res ) {
        if (root == null) return;
        dfs(root.left, res);
        res.add(root.val);
        dfs(root.right, res);
    }
}

#BFS
4.33%
public class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode p = root;
        while(!stack.isEmpty() || p != null) {
            if ( p != null) {
                stack.push(p);
                p = p.left;
            } else {
                TreeNode node = stack.pop();
                result.add(node.val);
                p = node.right;
            }
        }
        return result;
    }
}

#37.89%
public class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        while(root != null) {
            stack.push(root);
            root = root.left;
        }
        
        while(!stack.isEmpty()) {
            TreeNode cur = stack.pop();
            res.add(cur.val);
            cur = cur.right;
            while( cur != null) {
                stack.push(cur);
                cur = cur.left;
            }
        }
        return res;
    }
}

     # PostOrder
     public List<Integer> postorderBFS(TreeNode root) {
        LinkedList<Integer> result = new LinkedList<>();
        Deque<TreeNode> stack = new ArrayDeque<>();
        while(!stack.isEmpty() || root != null) {
            if (root != null) {
                stack.push(root);
                result.addFirst(root.val); // Reverse the process of preorder
                root = root.right; // Reverse the process of preorder
            } else {
                TreeNode node = stack.pop();
                root = node.left; // Reverse the process of preorder
            }
        }
        return result;
     }

     # Pre Order Traverse
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode p = root;
        while(!stack.isEmpty() || p != null) {
            if(p != null) {
                stack.push(p);
                result.add(p.val);  // Add before going to children
                p = p.left;
            } else {
                TreeNode node = stack.pop();
                p = node.right;
            }
        }
        return result;
    }
'''
