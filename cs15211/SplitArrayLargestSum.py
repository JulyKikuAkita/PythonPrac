__source__ = 'https://leetcode.com/problems/split-array-largest-sum/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/split-array-largest-sum.py
# Time:  O(nlogs), s is the sum of nums
# Space: O(1)
#
# Description: Leetcode # 410. Split Array Largest Sum
#
# Given an array which consists of non-negative integers and an integer m,
# you can split the array into m non-empty continuous subarrays.
# Write an algorithm to minimize the largest sum among these m subarrays.
#
# Note:
# Given m satisfies the following constraint: 1 <= m <= length(nums) <= 14,000.
#
# Examples:
#
# Input:
# nums = [7,2,5,10,8]
# m = 2
#
# Output:
# 18
#
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
#
# Companies
# Facebook Baidu
# Related Topics
# Binary Search Dynamic Programming
#
#38ms
import unittest
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def canSplit(nums, m, s):
            cnt, curr_sum = 1, 0
            for num in nums:
                curr_sum += num
                if curr_sum > s:
                    curr_sum = num
                    cnt += 1
            return cnt <= m

        left, right = 0, 0
        for num in nums:
            left = max(left, num)
            right += num

        while left <= right:
            mid = left + (right - left) / 2;
            if canSplit(nums, m, mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
#46.84% 4ms
public class Solution {
    public int splitArray(int[] nums, int m) {
        int max = 0; long sum = 0;
        for (int num : nums) {
            max = Math.max(num, max);
            sum += num;
        }
        if (m == 1) return (int)sum;
        //binary search
        long l = max; long r = sum;
        while (l <= r) { //don't use left + 1 < right, not index
            long mid = (l + r)/ 2;
            if (valid(mid, nums, m)) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return (int)l;
    }
    public boolean valid(long target, int[] nums, int m) {
        int count = 1;
        long total = 0;
        for(int num : nums) {
            total += num;
            if (total > target) {
                total = num;
                count++;
                if (count > m) {
                    return false;
                }
            }
        }
        return true;
    }
}

#46.84% 4ms
public class Solution {
    public int splitArray(int[] nums, int m) {
        int lo = 0, hi = 0;
        for(int n: nums) {
            lo = Math.max(lo, n);
            hi += n;
        }

        while(lo <= hi) {
            int mid = (hi-lo)/2+lo;

            if(canSplit(nums, m, mid))
                lo = mid+1;
            else
                hi = mid-1;
        }
        return lo;
    }

    private boolean canSplit(int[] nums, int m, int sum) {
        int s = 0;
        int cnt = 1;

        for(int i = 0; i < nums.length; i++) {
            s += nums[i];

            if(s > sum) {
                s = nums[i];
                cnt++;
            }
        }

        return cnt > m;
    }
}


DP solution. This is obviously not as good as the binary search solutions; but it did pass OJ.

dp[s,j] is the solution for splitting subarray n[j]...n[L-1] into s parts.

dp[s+1,i] = min{ max(dp[s,j], n[i]+...+n[j-1]) }, i+1 <= j <= L-s

This solution does not take advantage of the fact that the numbers are non-negative
(except to break the inner loop early). That is a loss.
(On the other hand, it can be used for the problem containing arbitrary numbers)

# 24.49% 11ms
class Solution {
    public int splitArray(int[] nums, int m) {
        int L = nums.length;
        int[] S = new int[L + 1];
        S[0] = 0;
        for (int i = 0; i < L ; i++) {
            S[i + 1] = S[i] + nums[i];
        }

        int[] dp = new int[L];
        for (int i = 0; i < L; i++) {
            dp[i] = S[L] - S[i];
        }

        for (int s = 1; s < m; s++) {
            for( int i = 0; i < L - s; i++) {
                dp[i] = Integer.MAX_VALUE;
                for (int j = i + 1; j <= L - s; j++) {
                    int t = Math.max(dp[j], S[j] - S[i]);
                    if (t <= dp[i]) dp[i] = t;
                    else break;
                }
            }
        }
        return dp[0];
    }
}
'''