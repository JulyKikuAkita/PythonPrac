import collections

__source__ = 'https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 863. All Nodes Distance K in Binary Tree
#
# We are given a binary tree (with root node root),
# a target node, and an integer value K.
#
# Return a list of the values of all nodes that have a distance K from the target node.
# The answer can be returned in any order.
#
# Example 1:
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
#
# Output: [7,4,1]
#
# Explanation:
# The nodes that are a distance 2 from the target node (with value 5)
# have values 7, 4, and 1.
#
# Note that the inputs "root" and "target" are actually TreeNodes.
# The descriptions of the inputs above are just serializations of these objects.
#
#
# Note:
#
# The given tree is non-empty.
# Each node in the tree has unique values 0 <= node.val <= 500.
# The target node is a node in the tree.
# 0 <= K <= 1000.
#
import unittest

#24ms 100%
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        def dfs(node, par = None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        queue = collections.deque([(target, 0)])
        seen = {target}
        while queue:
            if queue[0][1] == K:
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d+1))
        return []

#32ms 32.93%
class Solution2(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        ans = []
        # Return distance from node to target if exists, else -1
        def dfs(node):
            if not node:
                return -1
            elif node is target:
                subtree_add(node, 0)
                return 1
            else:
                L, R = dfs(node.left), dfs(node.right)
                if L != -1:
                    if L == K: ans.append(node.val)
                    subtree_add(node.right, L + 1)
                    return L + 1
                elif R != -1:
                    if R == K: ans.append(node.val)
                    subtree_add(node.left, R + 1)
                    return R + 1
                else:
                    return -1

        # Add all nodes 'K - dist' from the node to answer.
        def subtree_add(node, dist):
            if not node:
                return
            elif dist == K:
                ans.append(node.val)
            else:
                subtree_add(node.left, dist + 1)
                subtree_add(node.right, dist + 1)

        dfs(root)
        return ans


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/solution/
Approach 1: Annotate Parent
Complexity Analysis
Time Complexity: O(N), where N is the number of nodes in the given tree.
Space Complexity: O(N)

# 1ms 100%
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<Integer> distanceK(TreeNode root, TreeNode target, int K) {
        List<TreeNode> path = new ArrayList<>();
		//1.find the path of target
        findPath(root, target, path);

        //2.do bfs for every node in the path
        path.add(null);
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < path.size() - 1; i++) {
            if (path.size() -2 - i <= K) {
                TreeNode node = path.get(i);
                //turn the node's children into null if they are the next node in the path
                TreeNode child = path.get(i + 1);
				TreeNode leftChild = node.left;
				TreeNode rightChild = node.right;
                if (leftChild == child) {
					node.left = null;
				} else if (rightChild == child) {
					node.right = null;
				}
                //do bfs
                bfs(node, K - (path.size() - 2 - i), result);

                //turn children back
                if (leftChild == child) {
					node.left = child;
				} else if (rightChild == child) {
					node.right = child;
				}
            }
        }
        return result;
    }

   	private void bfs(TreeNode root, int k, List<Integer> result) {
        Queue<TreeNode> queue = new LinkedList<>();
		queue.add(root);
		int level = 0;
        while (!queue.isEmpty()) {
            final int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.remove();
                if (level == k) result.add(node.val);
                if (level < k && node.left != null) queue.add(node.left);
                if (level < k && node.right != null) queue.add(node.right);
            }
            level++;
        }
    }


    //find the target's path
	private boolean findPath(TreeNode node, TreeNode target, List<TreeNode> path) {
        path.add(node);
        if (node == target) return true;
        if (node.left != null && findPath(node.left, target, path)) {
            return true;
        }
        if (node.right != null && findPath(node.right, target, path)) {
            return true;
        }
        path.remove(path.size() - 1);
        return false;
    }
}

Approach 2: Percolate Distance
Complexity Analysis
Time Complexity: O(N), where N is the number of nodes in the given tree.
Space Complexity: O(N)

# 1ms 100%

class Solution {
    List<Integer> ans;
    TreeNode target;
    int K;
    public List<Integer> distanceK(TreeNode root, TreeNode target, int K) {
        ans = new LinkedList();
        this.target = target;
        this.K = K;
        dfs(root);
        return ans;
    }

    // Return distance from node to target if exists, else -1
    public int dfs(TreeNode node) {
        if (node == null)
            return -1;
        else if (node == target) {
            subtree_add(node, 0);
            return 1;
        } else {
            int L = dfs(node.left), R = dfs(node.right);
            if (L != -1) {
                if (L == K) ans.add(node.val);
                subtree_add(node.right, L + 1);
                return L + 1;
            } else if (R != -1) {
                if (R == K) ans.add(node.val);
                subtree_add(node.left, R + 1);
                return R + 1;
            } else {
                return -1;
            }
        }
    }

    // Add all nodes 'K - dist' from the node to answer.
    public void subtree_add(TreeNode node, int dist) {
        if (node == null) return;
        if (dist == K)
            ans.add(node.val);
        else {
            subtree_add(node.left, dist + 1);
            subtree_add(node.right, dist + 1);
        }
    }
}
'''