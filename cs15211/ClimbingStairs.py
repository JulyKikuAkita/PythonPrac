__source__ = 'https://leetcode.com/problems/climbing-stairs/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/climbing-stairs.py
# Time:  O(n)
# Space: O(1)
# DP
# Description:
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?
# Companies
# Adobe Apple
# Related Topics
# Dynamic Programming
#
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        prev, current = 0, 1
        for i in xrange(n):
            prev, current = current, prev + current
        return current


#fibonacci
class Solution2:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        #initialized Fibonacci number
        f = [1,1]
        while len(f) <= n:
            f.append(f[-1] + f[-2])
        return f[n]

    def fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)

#fibonacci
class SolutionCC150:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        #initialized Fibonacci number
        if n < 0:
            return -1
        if n == 0:
            return 0
        a, b = 1 ,1
        for i in xrange(2, n+1):
            c = a + b
            a = b
            b = c
        return b




#test
# f(n) = f(n-1) +f(n-2)
test = Solution2()
#print test.fibonacci(35)
#print test.climbStairs(5)

if __name__ =='__main__':
    print Solution().climbStairs(5)
    print SolutionCC150().climbStairs(5)

Java = '''
#Thought: https://leetcode.com/problems/climbing-stairs/#/solution
1.
# Time:  O(n)
# Space: O(n)
dp[i]= dp[i - 1]+dp[i-2]

public class Solution {
    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }
}

# Time:  O(n)
# Space: O(2)
public class Solution {
    public int climbStairs(int n) {
        if (n <= 0) {
            return 0;
        }
        int[] dp = new int[2];
        dp[0] = 1;
        dp[1] = 2;
        int index = 0;
        for (int i = 3; i <= n; i++) {
            dp[index] += dp[1 - index];
            index = 1 - index;
        }
        return dp[1 - (n & 1)];
    }
}

# Time:  O(logn)
# Space: O(1)
Approach #6 Fibonacci Formula [Accepted]: see link
public class Solution {
    public int climbStairs(int n) {
        double sqrt5 = Math.sqrt(5);
        double fibn = Math.pow((1 + sqrt5) / 2, n + 1) - Math.pow((1 - sqrt5) / 2, n + 1) ;
        return (int) (fibn /sqrt5);
    }
}
'''

