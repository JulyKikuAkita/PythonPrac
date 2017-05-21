__source__ = ''
# https://github.com/kamyu104/LeetCode/blob/master/Python/perfect-squares.py

# Time:  O(n * sqrt(n))
# Space: O(n)
#
# Given a positive integer n, find the least number of perfect
# square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4;
# given n = 13, return 2 because 13 = 4 + 9.
#
#  Google
# Hide Tags Dynamic Programming Breadth-first Search Math
# Hide Similar Problems (E) Count Primes (M) Ugly Number II
#

#dp
# http://bookshadow.com/weblog/2015/09/09/leetcode-perfect-squares/
# O(n * sqrt n)
# @Not getting dp yet
class Solution(object):
    _num = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = self._num
        while len(num) <= n:
            num += min(num[-i*i] for i in xrange(1, int(len(num)**0.5+1))) + 1,
            #print num
        return num[n]

# java solution
# http://www.cnblogs.com/grandyang/p/4800552.html
#Recursion
class Solution2(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: in
        """
        num, a, b, res = 2, 0, 0, n
        while num * num <= n:
            a = n / (num *  num)
            b = n % (num *  num)
            res = min(res, a + self.numSquares(b))
            num += 1
        return res

# Lagrange's Four-Square Theorem
# http://bookshadow.com/weblog/2015/09/09/leetcode-perfect-squares/
# O (sqrt n )
import math
class Solution3(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: in
        """
        while n % 4  == 0:
            n /= 4
        if n % 8 == 7:
            return 4

        a = 0
        while a*a <= n:
            b = math.sqrt( n - a * a)
            if ( a*a + b*b == n):
                return ~~a + ~~b  # no logical expression in python
                break
            a += 1
        return 3

class SolutionDFS(object):
    def __init__(self):
        self.cnt = 0xF7777777

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1

        self.dfs(n, 0, [], 1)
        return self.cnt

    def dfs(self, n, sum, tmp, idx):
        if sum > n or idx * idx > n :
            return
        if sum == n:
            self.cnt = min(self.cnt, len(tmp))
            return
        while idx * idx <= n:
            tmp.append(idx)
            self.dfs(n, sum + idx * idx, tmp, idx)
            tmp.pop()
            idx += 1
            print tmp, idx, self.cnt, sum

class SolutionDP(object):

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1

        dp = [ 0xF7777777 for i in xrange(n+1)]
        for i in xrange(n):
            if i * i <= n:
                dp[i * i] = 1

        for i in xrange(n+1):
            for j in xrange(1, n - i):
                if j * j + i <= n:
                    dp[ j * j + i ] = min(dp[ j * j + i ], dp[i] + 1)
        return dp[n]
if __name__ == "__main__":
    #print Solution().numSquares(12)
    #print Solution2().numSquares(12)
    print Solution3().numSquares(12)
    print SolutionDFS().numSquares(10)

#java
java = '''
thought: https://leetcode.com/problems/perfect-squares/#/solutions
public class Solution {
    public int numSquares(int n) {
        int[] dp = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            int sqrt = (int) Math.sqrt(i);
            if (sqrt * sqrt == i) {
                dp[i] = 1;
                continue;
            }
            int min = Integer.MAX_VALUE;
            for (int j = 1; j <= sqrt; j++) {
                min = Math.min(min, dp[i - j * j] + 1);
            }
            dp[i] = min;
        }
        return dp[n];
    }
}

public class Solution {
    public int numSquares(int n) {
        int[] dp = new int[n+1];
        Arrays.fill(dp, Integer.MAX_VALUE);

        for(int i = 0; i * i <= n; i++){
            dp[i*i] = 1;
        }

        for(int a = 0; a <= n; a++){
            for(int b = 0 ; a + b * b <= n; b++){
                dp[a + b*b] = Math.min(dp[a+b*b], dp[a] +1);
            }
        }
        return dp[n];
    }
}
'''