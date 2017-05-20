__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/ugly-number-ii.py

# Time:  O(n)
# Space: O(1)
#
# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors
# only include 2, 3, 5. For example,
# 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the
# first 10 ugly numbers.
#
# Note that 1 is typically treated as an ugly number.
#
# Hint:
#
# The naive approach is to call isUgly for every number
# until you reach the nth one. Most numbers are not ugly.
# Try to focus your effort on generating only the ugly ones.
#

import heapq

class Solution:
    # @param {integer} n
    # @return {integer}
    def nthUglyNumber(self, n):
        ugly_number = 0

        heap = []
        heapq.heappush(heap, 1)
        for i in xrange(n):
            ugly_number = heapq.heappop(heap)
            if ugly_number % 2 == 0:
                heapq.heappush(heap, ugly_number * 2)
            elif ugly_number % 3 == 0:
                heapq.heappush(heap, ugly_number * 2)
                heapq.heappush(heap, ugly_number * 3)
            else:
                heapq.heappush(heap, ugly_number * 2)
                heapq.heappush(heap, ugly_number * 3)
                heapq.heappush(heap, ugly_number * 5)
        return ugly_number

#test
if __name__ == "__main__":
    print Solution().nthUglyNumber(10)

#java
js = '''
public class Solution {
    public int nthUglyNumber(int n) {
        List<Integer> list = new ArrayList<>();
        list.add(1);
        int cur = 1;
        int idx2 =0, idx3=0, idx5=0;
        for(int i = 1; i < n; i++){
            cur = Math.min(list.get(idx2) * 2 ,(Math.min(list.get(idx3) *3, list.get(idx5) * 5)));
            list.add(cur);
            // if to eliminate dulplicate
            if(cur == list.get(idx2) * 2){
                idx2 ++;
            }
            if(cur == list.get(idx3) * 3){
                idx3 ++;
            }
            if(cur == list.get(idx5) * 5){
                idx5 ++;
            }
        }
        return cur;
    }
}

public class Solution {
    public int nthUglyNumber(int n) {
        if (n <= 0) {
            return 0;
        }
        int[] dp = new int[n];
        dp[0] = 1;
        int[] indices = new int[3];
        int[] nums = new int[3];
        nums[0] = 2;
        nums[1] = 3;
        nums[2] = 5;
        for (int i = 1; i < n; i++) {
            dp[i] = Math.min(Math.min(nums[0], nums[1]), nums[2]);
            nums[0] = nums[0] == dp[i] ? dp[++indices[0]] * 2 : nums[0];
            nums[1] = nums[1] == dp[i] ? dp[++indices[1]] * 3 : nums[1];
            nums[2] = nums[2] == dp[i] ? dp[++indices[2]] * 5 : nums[2];
        }
        return dp[n - 1];
    }
}

#OT

'''