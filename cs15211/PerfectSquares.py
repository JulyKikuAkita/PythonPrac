__source__ = 'https://leetcode.com/problems/perfect-squares/#/description'
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
dp[n] indicates that the perfect squares count of the given n, and we have:

dp[0] = 0
dp[1] = dp[0]+1 = 1
dp[2] = dp[1]+1 = 2
dp[3] = dp[2]+1 = 3
dp[4] = Min{ dp[4-1*1]+1, dp[4-2*2]+1 }
      = Min{ dp[3]+1, dp[0]+1 }
      = 1
dp[5] = Min{ dp[5-1*1]+1, dp[5-2*2]+1 }
      = Min{ dp[4]+1, dp[1]+1 }
      = 2
						.
						.
						.
dp[13] = Min{ dp[13-1*1]+1, dp[13-2*2]+1, dp[13-3*3]+1 }
       = Min{ dp[12]+1, dp[9]+1, dp[4]+1 }
       = 2
						.
						.
						.
dp[n] = Min{ dp[n - i*i] + 1 },  n - i*i >=0 && i >= 1

public class Solution {
    public int numSquares(int n) {
        int[] dp = new int[n + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        int cur = 0;
        for (int j = 1; (cur = j * j) <= n; j++) {
            for (int i = cur; i <= n; i++) {
                dp[i] = Math.min(dp[i], dp[i - cur] + 1);
            }
        }
        return dp[n];
    }
}

#Note
dp arr for n = 5 will be:
0, MAX, MAX, MAX, MAX, MAX
0, 1 , MAX, MAX, MAX, MAX
0, 1, 2, MAX, MAX, MAX
0, 1, 2, 3, MAX, MAX
0, 1, 2, 3, 4, , MAX
0, 1, 2, 3, 4, 2

# recurstion case:
dp[n] = Math.min(dp[n], dp[n - i*i] + 1 ),  n - i*i >=0 && i >= 1

public class Solution {
    public int numSquares(int n) {
        int[] dp = new int[n + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        for (int i = 1; i * i <= n ;i++) {
            int cur = i * i;
            for (int j = cur; j <= n; j++) {
                dp[j] = Math.min(dp[j], dp[j - cur] + 1);
            }
        }
        return dp[n];
    }
}

3.Mathematical Solution: 4ms 98%

public class Solution {

    public int numSquares(int n) {
        //base case
        if(n < 4) return n;

        // If n is a perfect square, return 1.
        if (isSquare(n)) return 1;

        // The result is 4 if and only if n can be written in the
        // form of 4^k*(8*m + 7). Please refer to
        // Legendre's three-square theorem.
        while ((n & 3) == 0) { // n % 4 == 0
            n >>= 2;
        }

        if ((n & 7) == 7) { // n % 8 == 7
            return 4;
        }

        // Check whether 2 is the result.
        int sqrtN = (int)(Math.sqrt(n));
        for(int i = 1; i <= sqrtN; i++) {
            if (isSquare(n - i * i)) return 2;
        }
        return 3;
    }

    public boolean isSquare(int n) {
        int sqrtN = (int)Math.sqrt(n);
        return sqrtN * sqrtN == n;
    }
}

//https://www.cnblogs.com/grandyang/p/4800552.html
//there are only 4 possible result 1,2,3,4
//check if a * a + b * b == n

public class Solution {
    public int numSquares(int n) {
        //base case
        if (n < 4) return n;

        // The result is 4 if and only if n can be written in the
        // form of 4^k*(8*m + 7). // Legendre's three-square theorem.
        while (n % 4 == 0) n /= 4;  //to make it smaller
        if (n % 8 == 7) return 4;
        int a, b;
        for (int i = 0; i < n; i++) {
            a = i;
            b = (int) Math.sqrt(n - a * a);
            if (a * a + b * b == n) //perfect square -> a or b == 0
                return a == 0 || b == 0 ? 1 : 2;
        }
        return 3;
    }
}
'''