# coding=utf-8
__source__ = 'https://leetcode.com/problems/all-possible-full-binary-trees/'
# Time:  O(2 ^N)
# Space: O(2 ^ N)
#
# Description: Leetcode # 894. All Possible Full Binary Trees
#
# A full binary tree is a binary tree where each node has exactly 0 or 2 children.
#
# Return a list of all possible full binary trees with N nodes.
# Each element of the answer is the root node of one possible tree.
#
# Each node of each tree in the answer must have node.val = 0.
#
# You may return the final list of trees in any order.
#
# Example 1:
#
# Input: 7
# Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],
# [0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# Explanation: (see pic at source link)
# Note:
#
# 1 <= N <= 20
#
import unittest

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#128ms 97.57%
class Solution(object):
    memo = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N not in Solution.memo:
            ans = []
            for x in xrange(N):
                y = N - 1 - x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right
                        ans.append(bns)
            Solution.memo[N] = ans

        return Solution.memo[N]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/all-possible-full-binary-trees/solution/
Approach 1: Recursion
Complexity Analysis

Time Complexity: O(2^N) For odd N, let N = 2k + 1 Then, ∣FBT(N)∣=Ck, the k-th catalan number;
and ∑ Ck
(the complexity involved in computing intermediate results required) is bounded by O(2^N).
However, the proof is beyond the scope of this article.
Space Complexity: O(2^N)

# 4ms 90.42%
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
    Map<Integer, List<TreeNode>> memo = new HashMap();
    public List<TreeNode> allPossibleFBT(int N) {
        if (!memo.containsKey(N)) {
            List<TreeNode> ans = new LinkedList();
            if (N == 1) ans.add(new TreeNode(0));
            else if (N % 2 == 1){
                for (int x = 0; x < N; ++x) {
                    int y = N - 1 -x;
                    for (TreeNode left : allPossibleFBT(x)) {
                        for (TreeNode right : allPossibleFBT(y)) {
                            TreeNode bns = new TreeNode(0);
                            bns.left = left;
                            bns.right = right;
                            ans.add(bns);
                        }
                    }
                }
            }
            memo.put(N, ans);
        }
        return memo.get(N);
    }
}


# 2ms 100%
class Solution {
    public static HashMap<Integer, List<TreeNode>> store = new HashMap<>();

    public List<TreeNode> allPossibleFBT(int N) {
        if (store.containsKey(N)) {
            return store.get(N);
        }
        List<TreeNode> result = new ArrayList();
        if (N == 1) {
            TreeNode ans = new TreeNode(0);
            result.add(ans);
            store.put(1, result);
            return result;
        } else if (N == 0 || N == 2) {
            return result;
        }
        for (int i = 1; i <= N; i++) {
            List<TreeNode> leftResult = allPossibleFBT(i - 1);
            List<TreeNode> rightResult = allPossibleFBT(N - i);
            if (leftResult.size() > 0 && rightResult.size() > 0) {
                for (int li = 0; li < leftResult.size(); li ++) {
                    for (int ri = 0; ri < rightResult.size(); ri ++ ) {
                        TreeNode root = new TreeNode(0);
                        root.left = leftResult.get(li);
                        root.right = rightResult.get(ri);
                        result.add(root);
                    }
                }

            }
        }
        store.put(N, result);
        return result;
    }
}
'''