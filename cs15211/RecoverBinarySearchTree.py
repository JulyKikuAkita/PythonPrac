__source__ = 'https://leetcode.com/problems/recover-binary-search-tree/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/recover-binary-search-tree.py
# Time:  O(n)
# Space: O(1)
# Tree
#
# Description: Leetcode # 99. Recover Binary Search Tree
#
# Two elements of a binary search tree (BST) are swapped by mistake.
#
# Recover the tree without changing its structure.
#
# Note:
# A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
# Related Topics
# Tree, Depth-first Search
#
import unittest
# http://www.cnblogs.com/zuoyuan/p/3746594.html
# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

     def __repr__(self):
         if self:
             serial = []
             queue = [self]

             while queue:
                 cur = queue[0]

                 if cur:
                     serial.append(cur.val)
                     queue.append(cur.left)
                     queue.append(cur.right)
                 else:
                     serial.append("#")

                 queue = queue[1:]

             while serial[-1] == "#":
                 serial.pop()
             # print "test: ", str(serial), repr(serial) repr() ~= str()
             return repr(serial)
         else:
             return None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        return self.MorrisTraversal(root)

    # as BST inorder
    def MorrisTraversal(self, root):
        if root is None:
            return
        broken = [None, None]
        pre, cur = None, root # cur is pre's right child

        while cur:
            #1) no left child
            if cur.left is None:
                self.detectBroken(broken, pre,cur)
                pre= cur
                cur = cur.right

            #2) left child's right most leaf
            else:
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right

            #3) no right child
                if node.right == None:
                    node.right = cur
                    cur = cur.left

            #4) has right child
                else:
                    self.detectBroken(broken, pre, cur)
                    node.right = None
                    pre = cur
                    cur = cur.right

        broken[0].val, broken[1].val = broken[1].val, broken[0].val
        return root

    def detectBroken(self, broken, pre, cur):
        if pre and pre.val > cur.val:
            if broken[0] is None:
                broken[0] = pre
            broken[1] = cur

class SolutionOther:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        self.n1 = self.n2 = None
        self.prev = None
        self.findTwoNodes(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val
        return root


    def findTwoNodes(self, root):
        if root:
            self.findTwoNodes(root.left)
            if self.prev and self.prev.val > root.val:
                self.n2 = root
                if self.n1 == None:
                    self.n1 = self.prev
            self.prev = root
            self.findTwoNodes(root.right)


    def inorder(self, root, list, listp):
        if root:
            self.inorder(root.left, list, listp)
            list.append(root.val)
            listp.append(root)
            self.inorder(root.right, list, listp)

    def recoverTreeON(self, root):
        list = []
        listp = []
        self.inorder(root, list, listp)
        list.sort()
        for i in range(len(list)):
            listp[i].val = list[i]
        return root

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().containsDuplicate([12344555,12344555])

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

Let's start by writing the in order traversal:

private void traverse (TreeNode root) {
   if (root == null)
      return;
   traverse(root.left);
   // Do some business
   traverse(root.right);
}

So when we need to print the node values in order, we insert System.out.println(root.val) in the place of 
"Do some business".

What is the business we are doing here?
We need to find the first and second elements that are not in order right?

How do we find these two elements? For example, we have the following tree that is printed as in order traversal:

6, 3, 4, 5, 2

We compare each node with its next one and we can find out that 6 is the first element 
to swap because 6 > 3 and 2 is the second element to swap because 2 < 5.

Really, what we are comparing is the current node and its previous node in the "in order traversal".

Let us define three variables, firstElement, secondElement, and prevElement. 
Now we just need to build the "do some business" logic as finding the two elements. See the code below:

# 23ms 98.56%
class Solution {
    TreeNode firstElement = null;
    TreeNode secondElement = null;
    // The reason for this initialization is to avoid null pointer exception 
    //in the first comparison when prevElement has not been initialized
    TreeNode prevElement = new TreeNode(Integer.MIN_VALUE);
    
    public void recoverTree(TreeNode root) {
        
        // In order traversal to find the two elements
        traverse(root);
        
        // Swap the values of the two nodes
        int temp = firstElement.val;
        firstElement.val = secondElement.val;
        secondElement.val = temp;
    }
    
    private void traverse(TreeNode root) {
        
        if (root == null)
            return;
            
        traverse(root.left);
        
        // Start of "do some business", 
        // If first element has not been found, assign it to prevElement (refer to 6 in the example above)
        if (firstElement == null && prevElement.val >= root.val) {
            firstElement = prevElement;
        }
    
        // If first element is found, assign the second element to the root (refer to 2 in the example above)
        if (firstElement != null && prevElement.val >= root.val) {
            secondElement = root;
        }        
        prevElement = root;

        // End of "do some business"

        traverse(root.right);
    }
}

# 38ms 32.97%
class Solution {
    private TreeNode pre = null;
    private TreeNode first = null, second = null;
    public void recoverTree(TreeNode root) {
        dfs(root);
        final int temp = first.val;
        first.val = second.val;
        second.val = temp;
    }

    public void dfs(TreeNode root) {
        if (root == null) return;
        dfs(root.left);
        if (pre != null) {
            if (root.val < pre.val) {
                if (first == null) {
                    first = pre;
                }
                second = root;
            }
        }
        pre = root;
        dfs(root.right);
    }
}

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
# 31ms 56.25%
class Solution {
    private TreeNode err1;
    private TreeNode err2;
    private TreeNode prev;
    
    public void recoverTree(TreeNode root) {
        inorderTraverse(root);
        if (err1 != null) {
            swap(err1, err2);
        }
    }
    
    private void inorderTraverse(TreeNode root) {
        if (root == null) {
            return;
        }
        inorderTraverse(root.left);
        if (prev != null && prev.val >= root.val) {
            if (err1 == null) {
                err1 = prev;
            }
            err2 = root;
        }
        prev = root;
        inorderTraverse(root.right);
    }
    
    private void swap(TreeNode node1, TreeNode node2) {
        int tmp = node1.val;
        node1.val = node2.val;
        node2.val = tmp;
    }
}

# Morris:
Thought: https://discuss.leetcode.com/topic/9305/detail-explain-about-how-morris-traversal-finds-two-incorrect-pointer
Below is a standard Inorder Morris Traversal, 
referred from http://www.cnblogs.com/AnnieKim/archive/2013/06/15/morristraversal.html
When they are not consecutive, the first time we meet pre.val > root.val 
ensure us the first node is the pre node, since root should be traversal ahead of pre, 
pre should be at least at small as root. 
The second time we meet pre.val > root.val ensure us the second node is the root node, 
since we are now looking for a node to replace with out first node, which is found before.

When they are consecutive, which means the case pre.val > cur.val will appear only once. 
We need to take case this case without destroy the previous analysis. 
So the first node will still be pre, and the second will be just set to root. 
Once we meet this case again, the first node will not be affected.

# 41ms 25.12%
class Solution {
    public void recoverTree(TreeNode root) {
        TreeNode pre = null;
        TreeNode err1 = null, err2 = null;
        //Morris Traversal
        TreeNode tmp = null;
        while (root != null) {
            if (root.left != null) {
                // connect threading for root
                tmp = root.left;
                while (tmp.right != null && tmp.right != root) {
                    tmp = tmp.right;
                }
                // the threading already exists
                if (tmp.right != null) {
                    if (pre != null && pre.val > root.val) {
                        if (err1 == null) {
                            err1 = pre;
                            err2 = root;
                        } else {
                            err2 = root;
                        }
                    }
                    pre = root;
                    
                    tmp.right = null;
                    root = root.right;
                } else {
                    // construct the threading
                    tmp.right = root;
                    root = root.left;
                }
            } else {
                if (pre != null && pre.val > root.val) {
                    if (err1 == null) {
                        err1 = pre;
                        err2 = root;
                    } else {
                        err2 = root;
                    }            
                }
                pre = root;
                root = root.right;
            }
        }
        //swap err node val
        if (err1 != null && err2 != null) {
            int t = err1.val;
            err1.val = err2.val;
            err2.val = t;
        }
    }
}

'''
