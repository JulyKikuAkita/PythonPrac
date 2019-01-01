__source__ = 'https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/'
# Time:  O(NLogN)
# Space: O(N)
#
# Description: Leetcode # 987. Vertical Order Traversal of a Binary Tree
#
# Note: When two nodes have the same position (i.e. same X and same Y value),
# 314 asks us to sort them in the result based on X ("from left to right"),
# while 987 asks us to sort them in the result based on the nodes' values.
#
# For each node at position (X, Y),
# its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).
#
# Running a vertical line from X = -infinity to X = +infinity,
# whenever the vertical line touches some nodes,
# we report the values of the nodes in order from top to bottom (decreasing Y coordinates).
#
# If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.
#
# Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.
#
# Example 1:
#
# Input: [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Explanation:
# Without loss of generality, we can assume the root node is at position (0, 0):
# Then, the node with value 9 occurs at position (-1, -1);
# The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
# The node with value 20 occurs at position (1, -1);
# The node with value 7 occurs at position (2, -2).
# Example 2:
#
# Input: [1,2,3,4,5,6,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# Explanation:
# The node with value 5 and the node with value 6 have the same position according to the given scheme.
# However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
#
# Note:
#
# The tree will have between 1 and 1000 nodes.
# Each node's value will be between 0 and 1000.
import unittest
import collections
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 24ms 100%
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        seen = collections.defaultdict(
                  lambda: collections.defaultdict(list))

        def dfs(node, x=0, y=0):
            if node:
                seen[x][y].append(node)
                dfs(node.left, x-1, y+1)
                dfs(node.right, x+1, y+1)

        dfs(root)
        ans = []

        for x in sorted(seen):
            report = []
            for y in sorted(seen[x]):
                report.extend(sorted(node.val for node in seen[x][y]))
            ans.append(report)

        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/solution/
Approach 1: Store Locations
Complexity Analysis
Time Complexity: O(NlogN), where N is the number of nodes in the given tree.
Space Complexity: O(N) 
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
# 4ms 99.17%
class Solution {
    List<Location> locations;
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        // Each location is a node's x position, y position, and value
        locations = new ArrayList();
        dfs(root, 0, 0);
        Collections.sort(locations);

        List<List<Integer>> ans = new ArrayList();
        ans.add(new ArrayList<Integer>());

        int prev = locations.get(0).x;

        for (Location loc: locations) {
            // If the x value changed, it's part of a new report.
            if (loc.x != prev) {
                prev = loc.x;
                ans.add(new ArrayList<Integer>());
            }

            // We always add the node's value to the latest report.
            ans.get(ans.size() - 1).add(loc.val);
        }

        return ans;
    }

    public void dfs(TreeNode node, int x, int y) {
        if (node != null) {
            locations.add(new Location(x, y, node.val));
            dfs(node.left, x-1, y+1);
            dfs(node.right, x+1, y+1);
        }
    }
}

class Location implements Comparable<Location>{
    int x, y, val;
    Location(int x, int y, int val) {
        this.x = x;
        this.y = y;
        this.val = val;
    }

    @Override
    public int compareTo(Location that) {
        if (this.x != that.x)
            return Integer.compare(this.x, that.x);
        else if (this.y != that.y)
            return Integer.compare(this.y, that.y);
        else
            return Integer.compare(this.val, that.val);
    }
}

# DFS
# 49ms 13.01%
class Solution {
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        List<List<Integer>> res = new ArrayList();
        TreeMap<Integer, TreeMap<Integer, PriorityQueue<Integer>>> map = new TreeMap<>();
        dfs(map, 0, 0, root);
        for (TreeMap<Integer, PriorityQueue<Integer>> depMap : map.values()) {
            List<Integer> vals = new LinkedList();
            for (PriorityQueue<Integer> q : depMap.values()) {
                while(!q.isEmpty()) vals.add(0, q.poll());
            }
            res.add(vals);
        }
        return res;
    }
    
    public void dfs(TreeMap<Integer, TreeMap<Integer, PriorityQueue<Integer>>> map, int col, int dep, TreeNode root) {
        if (root == null) return;
        if (map.get(col) == null) map.put(col,new TreeMap());
        if (map.get(col).get(dep) == null) {
            PriorityQueue<Integer> pq = new PriorityQueue<>((x, y) -> Integer.compare(y, x));
            map.get(col).put(dep, pq);
        }
        dfs(map, col - 1, dep - 1, root.left);
        dfs(map, col + 1, dep - 1, root.right);
        map.get(col).get(dep).add(root.val);
    }
}

# BFS
# 4ms 99.17%
class Solution {
    int min = 0, max = 0;
    Map<Integer, List<Integer>> map = new HashMap();
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        List<List<Integer>> res = new ArrayList();
        if(root==null) return res;
        Queue<TreeNode> qNode = new LinkedList();
        Queue<Integer> qIdx = new LinkedList();
        qNode.add(root);
        qIdx.add(0);
        while (!qNode.isEmpty()) {
            int size = qNode.size();
            Map<Integer,List<Integer>> tmp = new HashMap();
            for (int i = 0; i < size; i++) {
                TreeNode cur = qNode.poll();
                int idx = qIdx.poll();
                if (!tmp.containsKey(idx)) tmp.put(idx, new ArrayList());
                tmp.get(idx).add(cur.val);
                if (idx < min) min = idx;
                if (idx > max) max = idx;
                if (cur.left != null) {
                    qNode.add(cur.left);
                    qIdx.add(idx - 1);
                }
                if (cur.right != null) {
                    qNode.add(cur.right);
                    qIdx.add(idx + 1);
                }
            }
            for (int key : tmp.keySet()) {
                if (!map.containsKey(key)) map.put(key, new ArrayList());
                List<Integer> list = tmp.get(key);
                Collections.sort(list);
                map.get(key).addAll(list);
            }
        }
        for (int i = min; i<= max; i++) {
            res.add(map.get(i));
        }
        return res;
    }
}
'''
