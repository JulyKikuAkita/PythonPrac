__source__ = 'https://leetcode.com/problems/closest-binary-search-tree-value-ii/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/closest-binary-search-tree-value-ii.py
# Time:  O(h + k)
# Space: O(h)
#
# Description: Leetcode # 272. Closest Binary Search Tree Value II
#
# Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.
#
# Note:
# Given target value is a floating point.
# You may assume k is always valid, that is: k <= total nodes.
# You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
# Follow up:
# Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
#
# Companies
# Google
# Related Topics
# Tree Stack
# Similar Questions
# Binary Tree Inorder Traversal Closest Binary Search Tree Value
#
import unittest
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        # Helper to make a stack to the next node.
        def nextNode(stack, child1, child2):
            if stack:
                if child2(stack):
                    stack.append(child2(stack))
                    while child1(stack):
                        stack.append(child1(stack))
                else:
                    child = stack.pop()
                    while stack and child is child2(stack):
                        child = stack.pop()

        # The forward or backward iterator.
        backward = lambda stack: stack[-1].left
        forward = lambda stack: stack[-1].right

        # Build the stack to the closest node.
        stack = []
        while root:
            stack.append(root)
            root = root.left if target < root.val else root.right
        dist = lambda node: abs(node.val - target)
        forward_stack = stack[:stack.index(min(stack, key = dist)) + 1]

        # Get the stack to the next smaller node.
        backward_stack = list(forward_stack)
        nextNode(backward_stack, backward, forward)

        # Get the closest k values by advancing the iterators of the stacks.
        result = []
        for _ in xrange(k):
            if not backward_stack or \
            forward_stack and dist(forward_stack[-1]) < dist(backward_stack[-1]):
                result.append(forward_stack[-1].val)
                nextNode(forward_stack, forward, backward)
            elif not forward_stack or \
                forward_stack and dist(backward_stack[-1]) <= dist(forward_stack[-1]):
                    result.append(backward_stack[-1].val)
                    nextNode(backward_stack, backward, forward)
        return result

class Solution2(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        # Helper class to make a stack to the next node.
        class BSTIterator:
            # @param root, a binary search tree's root node
            def __init__(self, stack, child1, child2):
                self.stack = list(stack)
                self.cur = self.stack.pop()
                self.child1 = child1
                self.child2 = child2

            # @return an integer, the next node
            def next(self):
                node = None
                if self.cur and self.child1(self.cur):
                    self.stack.append(self.cur)
                    node = self.child1(self.cur)
                    while self.child2(node):
                        self.stack.append(node)
                        node = self.child2(node)
                elif self.stack:
                    prev = self.cur
                    node = self.stack.pop()
                    while node:
                        if self.child2(node) is prev:
                            break
                        else:
                            prev = node
                            node = self.stack.pop() if self.stack else None
                self.cur = node
                return node
         # Build the stack to the closet node.
        stack = []
        while root:
            stack.append(root)
            root = root.left if target < root.val else root.right
        dist = lambda node: abs(node.val - target) if node else float("inf")
        stack = stack[:stack.index(min(stack, key = dist) + 1)]

        # The forward or backward iterator.
        backward = lambda node: node.left
        forward = lambda node: node.right
        smaller_it, larger_it = BSTIterator(stack, backward, forward), BSTIterator(stack, forward, backward)
        smaller_node, larger_node = smaller_it.next(), larger_it.next()

        # Get the closest k values by advancing the iterators of the stacks.
        result = [stack[-1].val]
        for _ in xrange(k - 1):
            if dist(smaller_node) < dist(larger_node):
                result.append(smaller_node.val)
                smaller_node = smaller_it.next()
            else:
                result.append(larger_node.val)
                larger_node = larger_it.next()
        return result

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
# 0ms 100%
class Solution {
    public List<Integer> closestKValues(TreeNode root, double target, int k) {
        LinkedList<Integer> res = new LinkedList<>();
        inOrder(root, target, k, res);
        return res;
    }

    private void inOrder(TreeNode root, double target, int k, LinkedList<Integer> res) {
        if (root == null) return;
        inOrder(root.left, target, k, res);
        if (res.size() == k) {
            if (Math.abs(root.val - target) < Math.abs(res.peekFirst() - target)) {
                res.removeFirst();
            } else { //early termination. maintain the window size k
                return;
            }
        }
        res.add(root.val);
        inOrder(root.right, target, k, res);
    }
}

# Preorder
#2ms 71.22%
class Solution {
    public List<Integer> closestKValues(TreeNode root, double target, int k) {
        List<Integer> result = new ArrayList<>();
        if (root == null || k <= 0) {
            return result;
        }
        Stack<Integer> pre = new Stack<>();
        Stack<Integer> post = new Stack<>();
        preOrder(root, target, pre);
        preOrderReversed(root, target, post);
        for (int i = 0; i < k; i++) {
            if (pre.isEmpty()) {
                result.add(post.pop());
            } else if (post.isEmpty()) {
                result.add(pre.pop());
            } else if (target - pre.peek() < post.peek() - target) {
                result.add(pre.pop());
            } else {
                result.add(post.pop());
            }
        }
        return result;
    }

    private void preOrder(TreeNode root, double target, Stack<Integer> stack) {
        if (root == null) {
            return;
        }
        preOrder(root.left, target, stack);
        if (root.val >= target) {
            return;
        }
        stack.push(root.val);
        preOrder(root.right, target, stack);
    }

    private void preOrderReversed(TreeNode root, double target, Stack<Integer> stack) {
        if (root == null) {
            return;
        }
        preOrderReversed(root.right, target, stack);
        if (root.val < target) {
            return;
        }
        stack.push(root.val);
        preOrderReversed(root.left, target, stack);
    }
}

# 0ms 100%
class Solution {
    int k = 0;
    double target;
    LinkedList<Integer> list = new LinkedList<>();
    public List<Integer> closestKValues(TreeNode root, double target, int k) {
        this.target = target;
        this.k = k;
        traverse(root);
        return list;
    }

    private void traverse(TreeNode root) {
        if (root == null) return;
        traverse(root.left);
        if (list.size() < k) {
            list.addLast(root.val);
        } else {
            double diffFirst = target - (double)list.peekFirst();
            diffFirst = diffFirst < 0 ? -diffFirst : diffFirst;
            double diff = target - (double)root.val;
            diff = diff < 0 ? -diff : diff;
        //    System.out.println(diffFirst +" "+ diff);

            if (diffFirst > diff) {
                list.removeFirst();
                list.addLast(root.val);
            } else {
                return;
            }
        }
        traverse(root.right);
    }
}

Thought:
The idea is to compare the predecessors and successors of the closest node to the target,
we can use two stacks to track the predecessors and successors, then like what we do in merge sort,
we compare and pick the closest one to the target and put it to the result list.

As we know, inorder traversal gives us sorted predecessors, whereas reverse-inorder traversal gives us sorted successors.

We can use iterative inorder traversal rather than recursion, but to keep the code clean, here is the recursion version.

# 3ms 45.77%
class Solution {
    public List<Integer> closestKValues(TreeNode root, double target, int k) {
        List<Integer> result = new ArrayList<>();
        if (root == null || k == 0) {
            return result;
        }
        Stack<TreeNode> preStack = new Stack<>();
        Stack<TreeNode> sucStack = new Stack<>();

        initPreStack(root, preStack, target);
        initSucStack(root, sucStack, target);
        if (!preStack.isEmpty() && !sucStack.isEmpty() && preStack.peek().val == sucStack.peek().val) {
            getNextSuc(sucStack);
        }
        while (k-- > 0) {
            if (preStack.isEmpty()) {
                result.add(sucStack.peek().val);
                getNextSuc(sucStack);
            } else if (sucStack.isEmpty()) {
                result.add(preStack.peek().val);
                getNextPre(preStack);
            } else if (Math.abs(preStack.peek().val - target) <= Math.abs(sucStack.peek().val - target)) {
                result.add(preStack.peek().val);
                getNextPre(preStack);
            } else {
                result.add(sucStack.peek().val);
                getNextSuc(sucStack);
            }
        }
        return result;
    }

    private void initPreStack(TreeNode root, Stack<TreeNode> stack, double target) {
        while (root != null) {
            if (root.val < target) {
                stack.push(root);
                root = root.right;
            } else if (root.val > target) {
                root = root.left;
            } else {
                stack.push(root);
                return;
            }
        }
    }

    private void initSucStack(TreeNode root, Stack<TreeNode> stack, double target) {
        while (root != null) {
            if (root.val < target) {
                root = root.right;
            } else if (root.val > target) {
                stack.push(root);
                root = root.left;
            } else {
                stack.push(root);
                return;
            }
        }
    }

    private void getNextPre(Stack<TreeNode> stack) {
        TreeNode cur = stack.pop().left;
        while (cur != null) {
            stack.push(cur);
            cur = cur.right;
        }
    }

    private void getNextSuc(Stack<TreeNode> stack) {
        TreeNode cur = stack.pop().right;
        while (cur != null) {
            stack.push(cur);
            cur = cur.left;
        }
    }
}
'''

