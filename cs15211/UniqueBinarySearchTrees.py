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
# Count[i] = sum( Count[0...k] * [ k+1....i] )    0<=k<i-1


class Solution:
    # @return an integer
    def numTrees(self, n):
        counts = [1, 1]
        for i in xrange(2, n+1):
            count = 0
            for j in xrange(i):
                #print i, j, counts, i-j-1, count
                count += counts[j] * counts[i - j - 1]
            counts.append(count)
        return counts[-1]

if __name__ == "__main__":
    for i in xrange(7):
        print Solution().numTrees(i)

class SolutionOther2:
    # @return an integer
    def numTrees(self, n):
        answer = 0

        if n <= 0 :
            return 0

        dp = [ -1 for i in range(n+1) ]


        for i in range (2):
            dp[i] = 1

        return self.dpit(dp, n)

    def dpit(self, dparr, nodenum ):
        if dparr[nodenum] != -1 :
            return dparr[nodenum]

        dparr[nodenum] = 0

        for j in range(nodenum):
            dparr[nodenum] += self.dpit(dparr,j) * self.dpit(dparr, nodenum-j-1)
            #print j, dparr,  nodenum ,dparr[nodenum]
        return dparr[nodenum]

#test
test =  Solution()
print test.numTrees(2)
#print test.numTrees(-1)
#print test.numTrees(5)

#java
js = '''
Fantastic Clean Java DP Solution with Detail Explaination
First note that dp[k] represents the number of BST trees built from 1....k;

Then assume we have the number of the first 4 trees: dp[1] = 1 ,dp[2] =2 ,dp[3] = 5, dp[4] =14 ,
how do we get dp[5] based on these four numbers is the core problem here.

The essential process is: to build a tree, we need to pick a root node,
then we need to know how many possible left sub trees and right sub trees can be held under that node,
finally multiply them.

To build a tree contains {1,2,3,4,5}. First we pick 1 as root, for the left sub tree, there are none;
for the right sub tree, we need count how many possible trees are there constructed from {2,3,4,5},
apparently it's the same number as {1,2,3,4}. So the total number of trees under "1"
picked as root is dp[0] * dp[4] = 14. (assume dp[0] =1). Similarly, root 2 has dp[1]*dp[3] = 5 trees.
root 3 has dp[2]*dp[2] = 4, root 4 has dp[3]*dp[1]= 5 and root 5 has dp[0]*dp[4] = 14.
Finally sum the up and it's done.

Now, we may have a better understanding of the dp[k],
which essentially represents the number of BST trees with k consecutive nodes.
It is used as database when we need to know how many left sub trees are possible for k nodes when picking (k+1) as root.

 public int numTrees(int n) {
    int [] dp = new int[n+1];
    dp[0]= 1;
    dp[1] = 1;
    for(int level = 2; level <=n; level++)
        for(int root = 1; root<=level; root++)
            dp[level] += dp[level-root]*dp[root-1];
    return dp[n];
}
public class Solution {
    public int numTrees(int n) {
        if (n <= 0) {
            return 0;
        }
        int[] dp = new int[n + 1];
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                dp[i] += dp[j] * dp[i - 1 - j];
            }
        }
        return dp[n];
    }
}
'''