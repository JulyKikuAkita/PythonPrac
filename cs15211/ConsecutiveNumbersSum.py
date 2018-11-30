# coding=utf-8
__source__ = 'https://leetcode.com/problems/consecutive-numbers-sum/'
# Time:  O(sqrt(N)
# Space: O(1)
#
# Description: Leetcode # 829. Consecutive Numbers Sum
#
# Given a positive integer N,
# how many ways can we write it as a sum of consecutive positive integers?
#
# Example 1:
#
# Input: 5
# Output: 2
# Explanation: 5 = 5 = 2 + 3
# Example 2:
#
# Input: 9
# Output: 3
# Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
# Example 3:
#
# Input: 15
# Output: 4
# Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
# Note: 1 <= N <= 10 ^ 9.
#
import unittest

#24ms 100%
class Solution(object):
    def consecutiveNumbersSum(self, N):
        while N & 1 == 0:
            N >>= 1

        ans = 1
        d = 3
        while d * d <= N:
            e = 0
            while N % d == 0:
                N /= d
                e += 1
            ans *= e + 1
            d += 2

        if N > 1: ans *= 2
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/consecutive-numbers-sum/solution/
Approach #1: Brute Force [Time Limit Exceeded]
Complexity Analysis
Time Complexity: O(N^2)
Space Complexity: O(1)

class Solution {
    public int consecutiveNumbersSum(int N) {
        int ans = 0;
        for (int start = 1; start <= N; ++ start) {
            int target = N, x = start;
            while (target > 0) {
                target -= x++;
            }
            if (target == 0) ans++;
        }
        return ans;
    }
}


Approach #2: Mathematical (Naive) [Time Limit Exceeded]
 N = (x+1) + (x+2) + \cdots + (x+k)N=(x+1)+(x+2)+⋯+(x+k).
 2∗N=k(2∗x+k+1).

Approach #3: Mathematical (Fast) [Accepted]
-> the number of ways to factor the odd part of NN.

Complexity Analysis

Time Complexity: O(sqrt(N)
Space Complexity: O(1)



#6ms 99.20%
class Solution {
    public int consecutiveNumbersSum(int N) {
        while ((N & 1) == 0) N >>= 1;
        int ans = 1, d = 3;

        while (d * d <= N) {
            int e = 0;
            while (N % d == 0) {
                N /= d;
                e++;
            }
            ans *= e + 1;
            d += 2;
        }

        if (N > 1) ans <<= 1;
        return ans;
    }
}

# math explanation:
https://leetcode.com/problems/consecutive-numbers-sum/discuss/128946/Short-Math-Solution-with-explanation
The goal is to looking for the number of arithmetic sequences whos summation is N. Let the starting number of a sequence be i and the length of the sequence be n. From the summation equation, we know

(i+i+n-1)*n/2 = N  (1)
rearrange the equation we obtaion

i = (2*N-n(n-1))/(2*n) (2)
If there exist such i, the denominator should satisfy

0=<2*N-n(n-1) <=2*N-n*n
Therefore, the length of the sequence cannot exceed sqrt(2N)
From equation (2), we know i must be a interger,
so when (2N-n(n-1))%(2*n) == 0, the i satisfies the requirement. The code is simple

# 9ms 91.82%
class Solution {
    public int consecutiveNumbersSum(int N) {
        int count = 0;
        for (int i = 1; i <= (int) Math.sqrt(2*N); i++) {
            if ( (2 * N - i * (i - 1)) % (2 * i) == 0) count++;
        }
        return count;
    }
}
'''