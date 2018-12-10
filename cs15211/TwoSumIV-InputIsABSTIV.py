__source__ = 'https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/'
# Time:  O(n)
# Space: O(n)
#
# Description: Leetcode # 653. Two Sum IV - Input is a BST
#
# Given a Binary Search Tree and a target number, return true
# if there exist two elements in the BST such that their sum is equal to the given target.
#
# Example 1:
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 9
#
# Output: True
# Example 2:
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 28
#
# Output: False
#
# Companies
# Facebook Samsung
# Related Topics
# Tree
# Similar Questions
# Two Sum Two Sum II - Input array is sorted Two Sum III - Data structure design
#
#
import unittest
# 49ms
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/solution/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

# Approach #1 Using HashSet[Accepted]
# 14ms 92.62%
class Solution {
    public boolean findTarget(TreeNode root, int k) {
        Set < Integer > set = new HashSet();
        return find(root, k, set);
    }
    public boolean find(TreeNode root, int k, Set < Integer > set) {
        if (root == null)
            return false;
        if (set.contains(k - root.val))
            return true;
        set.add(root.val);
        return find(root.left, k, set) || find(root.right, k, set);
    }
}

# Approach #2 Using BFS and HashSet [Accepted]
# 15ms 85.29%
class Solution {
    public boolean findTarget(TreeNode root, int k) {
        Set < Integer > set = new HashSet();
        Queue < TreeNode > queue = new LinkedList();
        queue.add(root);
        while (!queue.isEmpty()) {
            if (queue.peek() != null) {
                TreeNode node = queue.remove();
                if (set.contains(k - node.val))
                    return true;
                set.add(node.val);
                queue.add(node.right);
                queue.add(node.left);
            } else
                queue.remove();
        }
        return false;
    }
}

# Approach #3 Using BST [Accepted] + inorder
# 20ms 47.57%
class Solution {
    public boolean findTarget(TreeNode root, int k) {
        List < Integer > list = new ArrayList();
        inorder(root, list);
        int l = 0, r = list.size() - 1;
        while (l < r) {
            int sum = list.get(l) + list.get(r);
            if (sum == k)
                return true;
            if (sum < k)
                l++;
            else
                r--;
        }
        return false;
    }
    public void inorder(TreeNode root, List < Integer > list) {
        if (root == null)
            return;
        inorder(root.left, list);
        list.add(root.val);
        inorder(root.right, list);
    }
}

# 14ms 92.62%
class Solution {
    Set<Integer> num = new HashSet<>();
    public boolean findTarget(TreeNode root, int k) {
        if(root == null) return false;
        if(num.contains(k - root.val)) return true;
        num.add(root.val);
        return findTarget(root.left, k) || findTarget(root.right, k);
    }
}

# Time Complexity: O(nlogn), Space Complexity: O(h).
# h is the height of the tree, which is logn at best case, and n at worst case.
# Binary search
# 20ms 47.57%
class Solution {
    public boolean findTarget(TreeNode root, int k) {
        return dfs(root, root,  k);
    }

    public boolean dfs(TreeNode root,  TreeNode cur, int k){
        if(cur == null)return false;
        return search(root, cur, k - cur.val) || dfs(root, cur.left, k) || dfs(root, cur.right, k);
    }

    public boolean search(TreeNode root, TreeNode cur, int value){
        if(root == null)return false;
        return (root.val == value) && (root != cur)
            || (root.val < value) && search(root.right, cur, value)
                || (root.val > value) && search(root.left, cur, value);
    }
}
'''