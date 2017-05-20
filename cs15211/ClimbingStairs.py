__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/climbing-stairs.py
# Time:  O(n)
# Space: O(1)
# DP
#
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?
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