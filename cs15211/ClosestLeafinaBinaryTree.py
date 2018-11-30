__source__ = 'https://leetcode.com/problems/closest-leaf-in-a-binary-tree/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 742. Closest Leaf in a Binary Tree
#
# Given a binary tree where every node has a unique value,
# and a target key k,
# find the value of the nearest leaf node to target k in the tree.
#
# Here, nearest to a leaf means the least number of edges travelled on the binary tree to reach any leaf of the tree.
# Also, a node is called a leaf if it has no children.
#
# In the following examples, the input tree is represented in flattened form row by row.
# The actual root tree given will be a TreeNode object.
#
# Example 1:
#
# Input:
# root = [1, 3, 2], k = 1
# Diagram of binary tree:
#           1
#          / \
#         3   2
#
# Output: 2 (or 3)
#
# Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.
# Example 2:
#
# Input:
# root = [1], k = 1
# Output: 1
#
# Explanation: The nearest leaf node is the root node itself.
# Example 3:
#
# Input:
# root = [1,2,3,4,null,null,null,5,null,6], k = 2
# Diagram of binary tree:
#              1
#             / \
#            2   3
#           /
#          4
#         /
#        5
#       /
#      6
#
# Output: 3
# Explanation: The leaf node with value 3
# (and not the leaf node with value 6) is nearest to the node with value 2.
# Note:
# root represents a binary tree with at least 1 node and at most 1000 nodes.
# Every node has a unique node.val in range [1, 1000].
# There exists some node in the given binary tree for which node.val == k.
#
import unittest

#36ms 100%
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        mapper = dict()
        def dfs(node):
            if not node:
                return None
            if node.val == k:
                return node
            if node.left:
                mapper[node.left.val] = node
            if node.right:
                mapper[node.right.val] = node
            return dfs(node.left) or dfs(node.right)
        knode = dfs(root)
        queue = [knode]
        visited = set()
        visited.add(knode)
        while queue:
            curr = queue.pop(0)
            if not curr.left and not curr.right:
                return curr.val
            if curr.left and curr.left not in visited:
                visited.add(curr.left)
                queue.append(curr.left)
            if curr.right and curr.right not in visited:
                visited.add(curr.right)
                queue.append(curr.right)
            if curr.val in mapper:
                visited.add(mapper[curr.val])
                queue.append(mapper[curr.val])


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/closest-leaf-in-a-binary-tree/solution/

#19ms 47.14%
Approach #1: Convert to Graph [Accepted]
# Complexity Analysis
# Time Complexity: O(N) where N is the number of nodes in the given input tree.
# We visit every node a constant number of times.
# Space Complexity: O(N), the size of the graph.

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
    public int findClosestLeaf(TreeNode root, int k) {
        Map<TreeNode, List<TreeNode>> graph = new HashMap();
        dfs(graph, root, null);

        Queue<TreeNode> queue = new LinkedList();
        Set<TreeNode> seen = new HashSet();

        for (TreeNode node: graph.keySet()) {
            if (node != null && node.val == k) {
                queue.add(node);
                seen.add(node);
            }
        }

        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (node != null) {
                if (graph.get(node).size() <= 1) return node.val;
                for (TreeNode nei : graph.get(node)) {
                    if (!seen.contains(nei)) {
                        seen.add(nei);
                        queue.add(nei);
                    }
                }
            }
        }
        throw null;
    }

    // Convert Tree to Graph
    public void dfs(Map<TreeNode, List<TreeNode>> graph, TreeNode node, TreeNode parent) {
        if (node != null) {
            if (!graph.containsKey(node)) graph.put(node, new LinkedList<TreeNode>());
            if (!graph.containsKey(parent)) graph.put(parent, new LinkedList<TreeNode>());
            graph.get(node).add(parent);
            graph.get(parent).add(node);
            dfs(graph, node.left, node);
            dfs(graph, node.right, node);
        }
    }
}


#12ms 94.82%
Approach #2: Annotate Closest Leaf [Accepted]
Complexity Analysis
Time and Space Complexity: O(N). The analysis is the same as in Approach #1.


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
    public int findClosestLeaf(TreeNode root, int k) {
         //find path from root to target
        List<TreeNode> pathTarget = new ArrayList<>();
        findTargetPath(root, pathTarget, k);

        //find nearest leaf node
        Result result = new Result();
        List<TreeNode> path = new ArrayList<>();
        dfs(root, path, pathTarget, result);
        return result.node.val;
    }

    private boolean findTargetPath(TreeNode node, List<TreeNode> pathTarget, int k){
        pathTarget.add(node);
        if (node.val == k) return true;

        if(node.left != null && findTargetPath(node.left, pathTarget, k)) return true;
        if(node.right != null && findTargetPath(node.right, pathTarget, k)) return true;

        pathTarget.remove(pathTarget.size() - 1);
        return false;
    }

    private void dfs(TreeNode node, List<TreeNode> path, List<TreeNode> pathTarget, Result result){
        //base case
        path.add(node);
        if(node.left == null && node.right == null){
            int dis = getDistance(path, pathTarget);
            if (dis < result.distance) {
                result.node =node;
                result.distance = dis;
            }
        }

        //trace down to lead
        if (node.left != null) dfs(node.left, path, pathTarget, result);
        if (node.right != null) dfs(node.right, path, pathTarget, result);

        path.remove(path.size() - 1);
    }

    private class Result{
        TreeNode node = null;
        int distance = Integer.MAX_VALUE;
    }

    private int getDistance(List<TreeNode> list1, List<TreeNode> list2){
        int i = 0;
        while(i < list1.size() && i < list2.size() && list1.get(i) == list2.get(i)){
            i++;
        }
        return list1.size() - i + list2.size() - i;
    }
}
'''