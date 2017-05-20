__author__ = 'July'

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
#java
js = '''
public class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        if(triangle.size() == 0){
            return 0;
        }

        int[] dp = new int[triangle.size()];

        for(int i = 0 ; i < triangle.size() ; i++){
            dp[i] = triangle.get(triangle.size() - 1).get(i);
        }

        for(int i = triangle.size() - 2; i >= 0; i--){
            for(int j = 0; j < i + 1 ; j++){
                dp[j] = triangle.get(i).get(j) + Math.min(dp[j],dp[j+1]);
            }
        }
        return dp[0];
    }
}

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