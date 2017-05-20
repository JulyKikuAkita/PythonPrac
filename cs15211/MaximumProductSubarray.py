__author__ = 'July'
# Time:  O(n)
# Space: O(1)
# DP
#
# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.
'''
# http://www.programcreek.com/2014/03/leetcode-maximum-product-subarray-java/
When iterating the array, each element has two possibilities: positive number or negative number.
We need to track a minimum value, so that when a negative number is given, it can also find the maximum value.
We define two local variables, one tracks the maximum and the other tracks the minimum.
'''
# LinkedIn

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        local_min = 1
        local_max = 1
        glo_max = float("-INF")

        for x in nums:
            tmp = local_max
            local_max = max(x, x*local_max, x*local_min)
            local_min = min(x, x * tmp, x*local_min)
            glo_max = max(local_max, glo_max)
        return glo_max

class Solution2:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        global_max, local_max, local_min = float("-inf"), 1, 1
        for x in A:
            local_max = max(1, local_max)
            if x > 0:
                local_max = local_max * x
                local_min = local_min * x
            else:
                local_max = local_min * x
                local_min = local_max
            global_max = max(global_max, local_max)
        return global_max

# Time:  O(n^3)
# Space: O(1)
class Naive:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if not A:
            return 0
        ans = float("-inf")
        for i in xrange(len(A)):
            for j in xrange(len(A)):
                if(i + j) < len(A):
                    product = self.calProduct(A, i, j)
                    ans = max(ans, product)

        return ans

    def calProduct(self, A, i, j):
        result = 1
        for k in xrange(i,j+1):
            result = result * A[k]
        return result

#test
test = SolutionOther()
#print test.maxProduct([2,3,-2,4])

if __name__ == "__main__":
    print Solution().maxProduct([2, 3, -2, 4])
    print Naive().maxProduct([2, 3, -2, 4])
    print Solution2().maxProduct([-4,-3])

#java
js ='''
public class Solution {
    public int maxProduct(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        int max = nums[0];
        int min = nums[0];
        int result = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < 0) {
                int tmp = min;
                min = max;
                max = tmp;
            }
            max = Math.max(nums[i], max * nums[i]);
            min = Math.min(nums[i], min * nums[i]);
            result = Math.max(result, max);
        }
        return result;
    }
}

public class Solution {
    public int maxProduct(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        int max = nums[0];
        int min = nums[0];
        int result = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int curMax = max;
            max = Math.max(nums[i], Math.max(max * nums[i], min * nums[i]));
            min = Math.min(nums[i], Math.min(curMax * nums[i], min * nums[i]));
            result = Math.max(result, max);
        }
        return result;
    }
}
'''