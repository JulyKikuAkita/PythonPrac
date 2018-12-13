source = 'https://leetcode.com/problems/find-mode-in-binary-search-tree/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/find-mode-in-binary-search-tree.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 501. Find Mode in Binary Search Tree
#
# Given a binary search tree (BST) with duplicates,
# find all the mode(s) (the most frequently occurred element) in the given BST.
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
# For example:
# Given BST [1,null,2,2],
#   1
#     \
#      2
#     /
#   2
# return [2].
#
# Note: If a tree has more than one mode, you can return them in any order.
#
# Follow up: Could you do that without using any extra space?
# (Assume that the implicit stack space incurred due to recursion does not count).
# Companies
# Google
# Related Topics
# Tree
# Similar Questions

# Validate Binary Search Tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 80ms 23.06%
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder(root, prev, cnt, max_cnt, result):
            if not root:
                return prev, cnt, max_cnt
    
            prev, cnt, max_cnt = inorder(root.left, prev, cnt, max_cnt, result)
            if prev:
                if root.val == prev.val:
                    cnt += 1
                else:
                    cnt = 1
            if cnt > max_cnt:
                max_cnt = cnt;
                del result[:]
                result.append(root.val)
            elif cnt == max_cnt:
                result.append(root.val)
            return inorder(root.right, root, cnt, max_cnt, result)
        
        if not root:
            return []
        result = []
        inorder(root, None, 1, 0, result);
        return result

Java = '''
Thought:

1. With map: Just travel the tree and count, find the those with max counts. 
Nothing much. Spent 10min on figuring out what is mode....
If using this method (hashmap), inorder/preorder/postorder gives the same result. 
Because essentially you just travel the entire nodes and count. And BST is not necessary. 
This method works for any tree.

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

# 7ms 52.60%
class Solution {
    public int[] findMode(TreeNode root) {
        Map<Integer, Integer> map = new HashMap<>();
        int[] ans = new int[1];
        dfs(root, map, ans);
        List<Integer> res = new ArrayList<>();
        
        for (Map.Entry<Integer,Integer> entry : map.entrySet()) {
            if (entry.getValue() == ans[0]) { //ans[0] is max count
                res.add(entry.getKey());
            }            
        }
        //turns count(value) to key
        ans = new int[res.size()];
        for(int i = 0; i < ans.length; i++) ans[i] = res.get(i);
        return ans;
    }
    
    private void dfs(TreeNode root, Map<Integer, Integer> map, int[] ans){
        if (root == null) return;
        map.put(root.val, map.getOrDefault(root.val, 0) + 1);
        ans[0] = Math.max(ans[0], map.get(root.val));
        dfs(root.left, map, ans);
        dfs(root.right,map, ans);
    }
}

2. No map
# 2ms 99.38%
class Solution {
    Integer prev = null;
    int count = 1;
    int max = 0;
    public int[] findMode(TreeNode root) {
        if (root == null) return new int[0];
        
        List<Integer> list = new ArrayList<>();
        traverse(root, list);
        
        int[] res = new int[list.size()];
        for (int i = 0; i < list.size(); ++i) res[i] = list.get(i);
        return res;
    }
    
    private void traverse(TreeNode root, List<Integer> list) {
        if (root == null) return;
        traverse(root.left, list);
        if (prev != null) {
            if (root.val == prev)
                count++;
            else
                count = 1;
        }
        if (count > max) {
            max = count;
            list.clear();
            list.add(root.val);
        } else if (count == max) {
            list.add(root.val);
        }
        prev = root.val;
        traverse(root.right, list);
    }
}
'''