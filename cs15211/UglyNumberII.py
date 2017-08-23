__source__ = 'https://leetcode.com/problems/ugly-number-ii/#/description'
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
# Related Topics
# Dynamic Programming Heap Math
# Similar Questions
# Merge k Sorted Lists Count Primes Ugly Number Perfect Squares Super Ugly Number
#
import heapq
import unittest
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
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().nthUglyNumber(10)

if __name__ == '__main__':
    unittest.main()

Java = '''
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

#87.11% 8ms
public class Solution {
    public int nthUglyNumber(int n) {
        int[] ugly = new int[n];
        ugly[0] = 1;

        //current index which has been considered for each multiplier
        int index2 = 0;
        int index3 = 0;
        int index5 = 0;
        //ugly candidates, each time choose the smallest one and add it the sequence
        int fac2 = 2;
        int fac3 = 3;
        int fac5 = 5;

        for (int i = 1; i < n; i++) {
            int min = Math.min(fac2, Math.min(fac3, fac5));
            //update, put the smallest candidates
            ugly[i] = min;
            //since the chosen candidates have been used, update it to be a new candidate
            //take care of the duplicates
            if (fac2 == min) {
                index2++;
                fac2 = ugly[index2] * 2; //guarantee each existing ugly number will multiply 2;
            }
            if (fac3 == min) {
                index3++;
                fac3 = ugly[index3] * 3; //guarantee each existing ugly number will multiply 3;
            }
            if (fac5 == min) {
                index5++;
                fac5 = ugly[index5] * 5;
            }
        }

        return ugly[n - 1];
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

#21.95% 51ms
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

#41.86% 12ms
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

#99.58$% 2ms
public class Solution {
    private static int[] uglies = new int[1690];
    private static int valid_index;
    private static int index2 = 0;
    private static int index3 = 0;
    private static int index5 = 0;
    private static final int factor2 = 2;
    private static final int factor3 = 3;
    private static final int factor5 = 5;

    static{
        uglies[0] = 1;
        valid_index = 0;
    }

    public int nthUglyNumber(int n) {
        n --;
        if(n <= valid_index) return uglies[n];
        int next;
        while(valid_index < n){
            next = Math.min(uglies[index2] * factor2, Math.min(uglies[index3] * factor3, uglies[index5] * factor5));
            uglies[++ valid_index] = next;
            if(next == uglies[index2] * factor2)
                index2 ++;
            if(next == uglies[index3] * factor3)
                index3 ++;
            if(next == uglies[index5] * factor5)
                index5 ++;
        }
        return uglies[n];
    }
}
'''
