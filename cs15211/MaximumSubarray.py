__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/maximum-subarray.py
# Time:  O(n)
# Space: O(1)
#
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
#
# click to show more practice.
#
# More practice:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
# Linkedln

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

if __name__ == "__main__":
    print Solution().maxSubArray(arr)
    print Solution().maxSubArray(arr1)
    print
    print OneD_DP().maxSubArray(arr)
    print OneD_DP().maxSubArray(arr1)