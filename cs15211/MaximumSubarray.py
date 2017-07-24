__source__ = 'https://leetcode.com/problems/maximum-subarray/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/maximum-subarray.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 53. Maximum Subarray
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
#
# click to show more practice.
#
# More practice:
# If you have figured out the O(n) solution,
# try coding another solution using the divide and conquer approach, which is more subtle.
#
# Companies
# LinkedIn Bloomberg Microsoft
# Related Topics
# Array Dynamic Programming Divide and Conquer
# Similar Questions
# Best Time to Buy and Sell Stock Maximum Product Subarray
#
import unittest
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        global_max, local_max = float("-inf"), 0
        for x in A:
            local_max = max(x + local_max, x)
            global_max = max(global_max, local_max)
        return global_max

# http://www.programcreek.com/2013/02/leetcode-maximum-subarray-java/
class WrongAns:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        global_max, local_max = float("-inf"), 0
        for x in A:
            local_max = max(x + local_max, 0)  # fails if A = [-1]
            global_max = max(global_max, local_max)
        return global_max

# The changing condition for dynamic programming is
# "We should ignore the sum of the previous n-1 elements if nth element is greater than the sum."
class OneD_DP:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if not A or len(A) == 0:
            return 0
        sum = [ 0 for i in xrange(len(A))]
        sum[0], ans = A[0], A[0]
        for i in xrange(1, len(A)):
            sum[i] = max(sum[i-1] + A[i], A[i] )
            ans = max(ans, sum[i])
        return ans

class SolutionOther:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        ans, sum = A[0] ,A[0]

        for i in range(1,len(A)):
            if (sum < 0):
                sum = A[i]
            else:
                sum += A[i]

            ans = max(ans,sum)
        return ans

test = SolutionOther()
arr = [-2,1,-3,4,-1,2,1,-5,4]
arr1 = [-1] #ans should be -1 not 0
#print test.maxSubArray(arr)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().maxSubArray(arr)
        print Solution().maxSubArray(arr1)
        print
        print OneD_DP().maxSubArray(arr)
        print OneD_DP().maxSubArray(arr1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/contains-duplicate/solution/
this problem was discussed by Jon Bentley (Sep. 1984 Vol. 27 No. 9 Communications of the ACM P885)

the paragraph below was copied from his paper (with a little modifications)

algorithm that operates on arrays: it starts at the left end (element A[1]) and
scans through to the right end (element A[n]), keeping track of the maximum sum subvector seen so far.
The maximum is initially A[0]. Suppose we've solved the problem for A[1 .. i - 1];
how can we extend that to A[1 .. i]? The maximum
sum in the first I elements is either the maximum sum in the first i - 1 elements
(which we'll call MaxSoFar), or it is that of a subvector that ends in position i (which we'll call MaxEndingHere).

MaxEndingHere is either A[i] plus the previous MaxEndingHere, or just A[i], whichever is larger.

# 24.67% 17ms
public class Solution {
    public int maxSubArray(int[] A) {
        int maxSoFar=A[0], maxEndingHere=A[0];
        for (int i=1;i<A.length;++i){
        	maxEndingHere= Math.max(maxEndingHere+A[i],A[i]);
        	maxSoFar=Math.max(maxSoFar, maxEndingHere);
        }
        return maxSoFar;
    }
}

#10.39% 19ms
public class Solution {
    public int maxSubArray(int[] nums) {
        int result = Integer.MIN_VALUE;
        int cur = 0;
        for (int i = 0; i < nums.length; i++) {
            cur += nums[i];
            result = Math.max(result, cur);
            cur = Math.max(cur, 0);
        }
        return result;
    }
}

#40.66% 16ms
public class Solution {
    public int maxSubArray(int[] nums) {
        int max = Integer.MIN_VALUE;
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            if (sum < 0)
                sum = nums[i];
            else
                sum += nums[i];
            if (sum > max)
                max = sum;
        }
        return max;
    }
}

2. DP
Analysis of this problem:
Apparently, this is a optimization problem, which can be usually solved by DP.
So when it comes to DP, the first thing for us to figure out is the format of the sub problem
(or the state of each sub problem).
The format of the sub problem can be helpful when we are trying to come up with the recursive relation.

At first, I think the sub problem should look like: maxSubArray(int A[], int i, int j),
which means the maxSubArray for A[i: j]. In this way,
our goal is to figure out what maxSubArray(A, 0, A.length - 1) is.
However, if we define the format of the sub problem in this way,
it's hard to find the connection from the sub problem to the original problem(at least for me).
In other words, I can't find a way to divided the original problem into the sub problems and use the solutions
of the sub problems to somehow create the solution of the original one.

So I change the format of the sub problem into something like: maxSubArray(int A[], int i),
which means the maxSubArray for A[0:i ] which must has A[i] as the end element.
Note that now the sub problem's format is less flexible and less powerful than the previous one
because there's a limitation that A[i] should be contained in that sequence and we have to keep track of
 each solution of the sub problem to update the global optimal value. However, now the connect
 between the sub problem & the original one becomes clearer:

maxSubArray(A, i) = maxSubArray(A, i - 1) > 0 ? maxSubArray(A, i - 1) : 0 + A[i];
And here's the code

#24.67% 17ms
public int maxSubArray(int[] A) {
        int n = A.length;
        int[] dp = new int[n];//dp[i] means the maximum subarray ending with A[i];
        dp[0] = A[0];
        int max = dp[0];

        for(int i = 1; i < n; i++){
            dp[i] = A[i] + (dp[i - 1] > 0 ? dp[i - 1] : 0);
            max = Math.max(max, dp[i]);
        }

        return max;
}
'''