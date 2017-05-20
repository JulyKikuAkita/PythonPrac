__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/unique-binary-search-trees.py
# Time:  O(n^2)
# Space: O(n)
# DP
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
#explanation: http://fisherlei.blogspot.com/2013/03/leetcode-unique-binary-search-trees.html
# Count[i] = Sigma Count[0...k] * [ k+1....i]     0<=k<i-1

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
if __name__ == "__main__":
    print Solution().generateTrees(2)

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
test = SolutionOther()
# ans = test.generateTrees(4)
# for i in range(len(ans)):
#    print i
#    print test.preorderTraversal1(ans[i])

#java
js = '''
public class Solution {
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
'''