__source__ = 'https://leetcode.com/problems/ugly-number-ii/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/ugly-number-ii.py
#
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
#  Dynamic Programming Heap Math
# Hide Similar Problems (H) Merge k Sorted Lists (E) Count Primes (E) Ugly Number (M) Perfect Squares (M) Super Ugly Number
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
java = '''
The idea of this solution is from this page: http://www.geeksforgeeks.org/ugly-numbers/

The ugly-number sequence is 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15,
because every number can only be divided by 2, 3, 5, one way to look at the sequence
is to split the sequence to three groups as below:

(1) 1x2, 2x2, 3x2, 4x2, 5x2, ...
(2) 1x3, 2x3, 3x3, 4x3, 5x3, ...
(3) 1x5, 2x5, 3x5, 4x5, 5x5, ...

We can find that every subsequence is the ugly-sequence itself (1, 2, 3, 4, 5, ...) multiply 2, 3, 5.
Then we use similar merge method as merge sort, to get every ugly number from the three subsequence.
Every step we choose the smallest one, and move one step after,including nums with same value.

public class Solution {
    public int nthUglyNumber(int n) {
        int[] ugly = new int[n];
        ugly[0] = 1;
        int index2 = 0, index3 = 0, index5 = 0;
        int factor2 = 2, factor3 = 3, factor5 = 5;
        for(int i=1;i<n;i++){
            int min = Math.min(Math.min(factor2,factor3),factor5);
            ugly[i] = min;
            if(factor2 == min)
                factor2 = 2*ugly[++index2];
            if(factor3 == min)
                factor3 = 3*ugly[++index3];
            if(factor5 == min)
                factor5 = 5*ugly[++index5];
        }
        return ugly[n-1];
    }
}

-> a general idea: from super ugly number
public class Solution {
    public int nthSuperUglyNumber(int n, int[] primes) {
        int[] ugly = new int[n];
        ugly[0] = 1;
        int[] index = new int[primes.length];

        int next = Integer.MAX_VALUE;
        for (int i = 1; i < n ;i++) {
            ugly[i] = next;

            for (int j = 0; j < primes.length; j++) {
                ugly[i] = Math.min(ugly[i], primes[j] * ugly[index[j]]);
            }

            //slip duplicate
            for (int j = 0; j < primes.length; j++) {
                while(ugly[i] >= primes[j] * ugly[index[j]]) index[j]++;
            }
        }
        return ugly[n -1];
    }
}

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

'''
