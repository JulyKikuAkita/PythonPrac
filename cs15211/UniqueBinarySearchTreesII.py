__source__ = 'https://leetcode.com/problems/unique-binary-search-trees-ii/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/unique-binary-search-trees.py
# Time:  O(n^2)
# Space: O(n)
# DP
#
# Description: Leetcode # 95. Unique Binary Search Trees II
#
# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
#
# For example,
# Given n = 3, there are a total of 5 unique BST's.
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#
# (Catalan_number: combination C(m,n) ex: C5(3,2) = 5*4*3/3*2*1)
# http://en.wikipedia.org/wiki/Catalan_number#Applications_in_combinatorics
# explanation: http://fisherlei.blogspot.com/2013/03/leetcode-unique-binary-search-trees.html
# Count[i] = Sigma Count[0...k] * [ k+1....i]     0<=k<i-1
#
# Related Topics
# Tree Dynamic Programming
# Similar Questions
# Unique Binary Search Trees Different Ways to Add Parentheses
#
import unittest
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

            while serial[-1] == '#':
                serial.pop()
            return repr(serial)
        else:
            return None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        return self.generateTreesRecu(1, n)

    def generateTreesRecu(self, low, high):
        result = []
        if low > high:
            result.append(None)
        for i in xrange(low, high + 1):
            left = self.generateTreesRecu(low, i - 1)
            right = self.generateTreesRecu(i + 1, high)
            for j in left:
                for k in right:
                    cur = TreeNode(i)
                    cur.left = j
                    cur.right = k
                    result.append(cur)
        return result

class SolutionOther:
    treelist = None
    # @return a list of tree node
    def generateTrees(self, n):
        return self.dfs(0,n)

    def dfs(self, lnode , rnode):
        ans = []
        if lnode == rnode:
            ans.append(None)
            return ans
        for i in range(lnode, rnode):
            lb, rb = self.dfs(lnode,i), self.dfs(i+1, rnode)
            for lc in lb:
                for rc in rb:
                    node = TreeNode(i+1)
                    node.left =lc
                    node.right =rc
                    ans.append(node)
        return ans

    def preorderTraversal1(self, root):
        allnodes = []
        p =root

        def preorder(p, ans):
            if p is None:
                return
            ans += [p.val]
            if p.left != None:
                preorder(p.left, ans)

            if p.right != None:
                preorder(p.right, ans)

        preorder(p,allnodes)
        return allnodes

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().generateTrees(2)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/unique-binary-search-trees-ii/solution/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */


1. Divide-and-conquer. F(i) = G(i-1) * G(n-i)

# 2ms 91.34%
class Solution {
    public List<TreeNode> generateTrees(int n) {
        if (n <= 0) {
            return new ArrayList<>();
        }
        return(generateTrees(1, n));
    }

    private List<TreeNode> generateTrees(int start, int end) {
        List<TreeNode> result = new ArrayList<>();
        if (start > end) {
            result.add(null);
            return result;
        }
        for (int i = start; i <= end; i++) {
            List<TreeNode> lefts = generateTrees(start, i - 1);
            List<TreeNode> rights = generateTrees(i + 1, end);
            for (TreeNode left : lefts) {
                for (TreeNode right : rights) {
                    TreeNode root = new TreeNode(i);
                    root.left = left;
                    root.right = right;
                    result.add(root);
                }
            }
        }
        return result;
    }
}

#2 
I start by noting that 1..n is the in-order traversal for any BST with nodes 1 to n. 
So if I pick i-th node as my root, the left subtree will contain elements 1 to (i-1), 
and the right subtree will contain elements (i+1) to n. 
I use recursive calls to get back all possible trees for left and right subtrees 
and combine them in all possible ways with the root.

# 2ms 91.34%
class Solution {
    public List<TreeNode> generateTrees(int n) {
        if ( n < 1) return new ArrayList<TreeNode>();
        return genTrees(1, n);
    }
    
    public List<TreeNode> genTrees(int start, int end){
        List<TreeNode> res = new ArrayList<TreeNode>();
        if (start > end) {
            res.add(null);
            return res;
        }
        
        if (start == end) {
            res.add(new TreeNode(start));
            return res;
        }
        
        List<TreeNode> leftTree, rightTree;
        for (int i = start; i <= end; i++) {
            leftTree = genTrees(start, i - 1);
            rightTree = genTrees(i + 1, end);
            for (TreeNode leftNode : leftTree) {
                for (TreeNode rightNode : rightTree) {
                    TreeNode root = new TreeNode(i);
                    root.left = leftNode;
                    root.right = rightNode;
                    res.add(root);
                }
            }
        }
        return res;
    }
}

# 1ms 100%
class Solution {
    public List<TreeNode> generateTrees(int n) {
        // List<TreeNode> res = new ArrayList<>();
        List<TreeNode>[][] memo = new ArrayList[n+1][n+1];
        if (n == 0) return new ArrayList<>();
        return divideConquer(1, n, memo);
    }
    private List<TreeNode> divideConquer(int start, int end, List[][] memo) {
        List<TreeNode> res = new ArrayList<>();
        if (start > end) {
            res.add(null); return res;
        }
        if (memo[start][end] != null) return memo[start][end];
        for (int mid = start; mid <= end; mid++) {
            List<TreeNode> left = divideConquer(start, mid-1, memo);
            List<TreeNode> right = divideConquer(mid+1, end, memo);
            for (TreeNode l : left) {
                for (TreeNode r : right) {
                    TreeNode root = new TreeNode(mid);
                    root.left = l;
                    root.right = r;
                    res.add(root);
                }
            }
        }
        memo[start][end] = res;
        return res;
    }
}

#2ms 91.34%
class Solution {
    public List<TreeNode> generateTrees(int n) {
        if (n <= 0) {
            return new ArrayList<>();
        }
        return generateTrees(1, n, n + 1, new HashMap<>());
    }

    private List<TreeNode> generateTrees(int start, int end, int base, Map<Long, List<TreeNode>> cache) {
        List<TreeNode> result = new ArrayList<>();
        if (start > end) {
            result.add(null);
            return result;
        }
        long key = hash(base, start, end);
        if (cache.containsKey(key)) {
            return cache.get(key);
        }
        for (int i = start; i <= end; i++) {
            List<TreeNode> lefts = generateTrees(start, i - 1, base, cache);
            List<TreeNode> rights = generateTrees(i + 1, end, base, cache);
            for (TreeNode left : lefts) {
                for (TreeNode right : rights) {
                    TreeNode root = new TreeNode(i);
                    root.left = left;
                    root.right = right;
                    result.add(root);
                }
            }
        }
        cache.put(key, result);
        return result;
    }

    private long hash(int base, int... nums) {
        long result = 0;
        for (int num : nums) {
            result = result * base + num;
        }
        return result;
    }
}
'''