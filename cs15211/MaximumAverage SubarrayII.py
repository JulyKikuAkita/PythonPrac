__source__ = 'https://leetcode.com/problems/maximum-average-subarray-ii/tabs/description'
# Time:  O()
# Space: O()
#
# Description:
# Given an array consisting of n integers, find the contiguous subarray
# whose length is greater than or equal to k that has the maximum average value.
#  And you need to output the maximum average value.
#
# Example 1:
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation:
# when length is 5, maximum average value is 10.8,
# when length is 6, maximum average value is 9.16667.
# Thus return 12.75.
# Note:
# 1 <= k <= n <= 10,000.
# Elements of the given array will be in range [-10,000, 10,000].
# The answer with the calculation error less than 10-5 will be accepted.
# Companies
# Google
# Related Topics
# Binary Search Array
# Similar Questions
# Maximum Average Subarray I
#
import collections
import unittest
# Advanced O(n) solution (Convex Hull Window)
# paper: https://arxiv.org/pdf/cs/0311020.pdf
# Let d(x, y) be the density of segment [x, y], ie. d(x, y) = (A[x]+...+A[y]) / (y-x+1).
# It can be computed quickly with prefix sums.
#
# Now we refer to section 3 of Kai-min Chung, Hsueh-I Lu - An Optimal Algorithm for the Maximum-Density Segment Problem. 2008.
#
# For each ending index j, the current interval for i under consideration, [0, j-K+1]
# (minus parts on the left we have already discarded),
# has been decomposed into minimum density segments of longest length [hull[i], hull[i+1]-1],
# and we discard these segments as appropriate.
# That is, for each i in increasing order, hull[i+1] is the largest index in [hull[i], j-K+1] so that [hull[i],
# hull[i+1]-1] has minimum density.
#
# This is simply a lower hull of candidate points i,
# in a geometric interpretation where d(a, b) = the slope of the line segment (a, P[a]) to (b+1, P[b+1]).
# Then, we can prove that discarding components with lower density than our current candidate d(hull[0], j)
#  must leave us with the highest density option remaining.
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        N = len(nums)
        P = [0]
        for x in nums:
            P.append(P[-1] + x)

        def d(x, y):
            return (P[y+1] - P[x]) / float(y+1-x)

        hull = collections.deque()
        ans = float('-inf')

        for j in xrange(k-1, N):
            while len(hull) >= 2 and d(hull[-2], hull[-1]-1) >= d(hull[-2], j-k):
                hull.pop()
            hull.append(j-k + 1)
            while len(hull) >= 2 and d(hull[0], hull[1]-1) <= d(hull[0], j):
                hull.popleft()
            ans = max(ans, d(hull[0], j))

        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/maximum-average-subarray-ii/
#28% 111 ms
public class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double max_val = Integer.MIN_VALUE;
        double min_val = Integer.MAX_VALUE;
        for (int n: nums) {
            max_val = Math.max(max_val, n);
            min_val = Math.min(min_val, n);
        }
        double prev_mid = max_val, error = Integer.MAX_VALUE;
        while (error > 0.00001) {
            double mid = (max_val + min_val) * 0.5;
            if (check(nums, mid, k))
                min_val = mid;
            else
                max_val = mid;
            error = Math.abs(prev_mid - mid);
            prev_mid = mid;
        }
        return min_val;
    }
    public boolean check(int[] nums, double mid, int k) {
        double sum = 0, prev = 0, min_sum = 0;
        for (int i = 0; i < k; i++)
            sum += nums[i] - mid;
        if (sum >= 0)
            return true;
        for (int i = k; i < nums.length; i++) {
            sum += nums[i] - mid;
            prev += nums[i - k] - mid;
            min_sum = Math.min(prev, min_sum);
            if (sum >= min_sum)
                return true;
        }
        return false;
    }
}

Approach #2 Using Binary Search [Accepted]
Time complexity: O(nlog(max_val - min_val)).
checkcheck takes O(n) time and it is executed O(log(max_val - min_val)) times.
Space complexity :O(1). Constant Space is used

# 97% 27ms
public class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int n = nums.length;
        int[] sum = new int[n + 1];
        int[] conIdx = new int[n+1];

        sum[0] = 0;
        for (int i = 1; i <= n; i++) {
            sum[i] = sum[i-1] + nums[i-1];
        }

        double res = sum[n] / n ;
        int left = 0, right = -1;
        for (int i = k ;i <= n; i++) {
            int oldLeft = i - k;
            while(left < right && avg(conIdx[right], oldLeft, sum) <= avg(conIdx[right - 1], oldLeft, sum)) {
                right--;
            }
            right++;
            conIdx[right] = oldLeft;

            while(left < right && avg(conIdx[left], i, sum) <= avg(conIdx[left + 1], i, sum)) {
                left++;
            }
            double tmp = avg(conIdx[left], i, sum);
            res = Math.max(res, tmp);
        }
        return res;
    }

    private double avg(int left, int right, int sum[]) {
        return (double) (sum[right] - sum[left]) / (right - left);
    }
}
'''