__source__ = 'https://leetcode.com/problems/triangle/description/'
# Time:  O(m * n)
# Space: O(n)
# DP
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
#
# Related Topics
# Array Dynamic Programming

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    # top-down
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        cur = triangle[0] + [float("inf")]

        for i in xrange(1, len(triangle)):
            next = []
            next.append(triangle[i][0] + cur[0]) # first element of every level
            for j in xrange(1, i+1):
                next.append(triangle[i][j] + min(cur[j - 1], cur[j]))
                print i, j, next, cur
            cur = next + [float("inf")]
        return reduce(min, cur)

class Solution2:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        ans = triangle[::] # does modified the original triangle

        #print ans
        # iterate from bottom up so ans[0][0] is the only answer
        #if from top to down, need to find the min at ans[last_row][:]
        for i in range(len(triangle)-2, -1, -1 ):
            for j in range(0, i+1):
                ans[i][j] +=  min(triangle[i+1][j], triangle[i+1][j+1])
        return ans[0][0]

# http://www.programcreek.com/2013/01/leetcode-triangle-java/
    def minimumTotal_B_U(self, triangle):
        size = len(triangle)

        ans = [ c for c in triangle[size-1]]

        for i in reversed(xrange(size - 1)):
            for j in xrange(len(triangle[i + 1]) - 1): # same as for j in xrange(i+1)
                ans[j] = triangle[i][j] + min(ans[j], ans[j+1])
        return ans[0]

# java solution
# http://www.programcreek.com/2013/01/leetcode-triangle-java/

#test
tri1 = \
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

tri2 = [[-10]]
tri3 = [[1],[2,3]]
test = Solution2()
#print test.minimumTotal(tri1)  # modified the original tri value
#print tri1
print test.minimumTotal_B_U(tri1)

#if __name__ == "__main__":
    #print Solution().minimumTotal([[-1], [2, 3], [1, -1, -3]])
    #print Solution().minimumTotal(tri1)
#Java
Java = '''
Thought: This problem is quite well-formed in my opinion. The triangle has a tree-like structure,
which would lead people to think about traversal algorithms such as DFS. However, if you look closely,
you would notice that the adjacent nodes always share a 'branch'. In other word, there are overlapping subproblems.
Also, suppose x and y are 'children' of k. Once minimum paths from x and y to the bottom are known,
the minimum path starting from k can be decided in O(1), that is optimal substructure. Therefore, dynamic programming would be the best solution to this problem in terms of time complexity.

What I like about this problem even more is that the difference
between 'top-down' and 'bottom-up' DP can be 'literally' pictured in the input triangle.
For 'top-down' DP, starting from the node on the very top, we recursively find the minimum path sum of each node.
When a path sum is calculated, we store it in an array (memoization);
the next time we need to calculate the path sum of the same node, just retrieve it from the array.
However, you will need a cache that is at least the same size as the input triangle itself to store the pathsum,
which takes O(N^2) space. With some clever thinking,
it might be possible to release some of the memory that will never be used after a particular point,
but the order of the nodes being processed is not straightforwardly seen in a recursive solution,
so deciding which part of the cache to discard can be a hard job.

'Bottom-up' DP, on the other hand, is very straightforward: we start from the nodes on the bottom row;
the min pathsums for these nodes are the values of the nodes themselves.
From there, the min pathsum at the ith node on the kth row would be the lesser of the pathsums
of its two children plus the value of itself, i.e.:

minpath[k][i] = min( minpath[k+1][i], minpath[k+1][i+1]) + triangle[k][i];
Or even better, since the row minpath[k+1] would be useless after minpath[k] is computed,
we can simply set minpath as a 1D array, and iteratively update itself:

For the kth level:
minpath[i] = min( minpath[i], minpath[i+1]) + triangle[k][i];

#DP Bottom-up
#62.86% 8ms
public class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int[] A = new int[triangle.size()+1];
        for(int i=triangle.size()-1;i>=0;i--){
            for(int j=0;j<triangle.get(i).size();j++){
                A[j] = Math.min(A[j],A[j+1])+triangle.get(i).get(j);
            }
        }
        return A[0];
    }
}

# 97.20% 6ms top-down
public class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int depth = triangle.size();
        if (depth == 0) {
            return 0;
        }
        int[] dp = new int[depth];
        dp[0] = triangle.get(0).get(0);
        for (int i = 1; i < depth; i++) {
            List<Integer> cur = triangle.get(i);
            int size = cur.size();
            dp[size - 1] = dp[size - 2] + cur.get(size - 1);
            for (int j = size - 2; j > 0; j--) {
                dp[j] = Math.min(dp[j - 1], dp[j]) + cur.get(j);
            }
            dp[0] += cur.get(0);
        }
        int result = dp[0];
        for (int i = 1; i < depth; i++) {
            result = Math.min(result, dp[i]);
        }
        return result;
    }
}
'''