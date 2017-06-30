__source__ = 'https://leetcode.com/problems/sum-of-square-numbers/#/description'
# Time:  O(sqrt(c) * log(c))
# Space: O(1)
#
# Description:
# Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.
#
# Example 1:
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
# Example 2:
# Input: 3
# Output: False
#
# Companies
# LinkedIn
# Related Topics
# Math
# Similar Questions
# Valid Perfect Square
#
import unittest
# Without loss of generality, let's consider only a, b >= 0.
# This is because if say, a < 0, then we may also find a solution using abs(a).
#
# Now, a*a = c - b*b <= c, because b*b >= 0, and 0 <= a <= sqrt(c) is a necessary condition for a solution.
#
# Let's try each 0 <= a <= sqrt(c). For each choice of a, we must have b*b = c - a*a.
# There will be a solution if and only if the right-hand-side is a perfect square.
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        def is_square(N):
            return int(N**.5)**2 == N

        return any(is_square(c - a*a)
                for a in xrange(int(c**.5) + 1))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/sum-of-square-numbers/

1.
Time complexity : O(c).
The total number of times the sumsum is updated is: 1+2+3+...(sqrt(c) times) = sqrt(c) * (sqrt(c)+1)/2 = O(c)
Space complexity : O(1). Constant extra space is used.

Now, to determine, if the number c - a^2 is a perfect square or not, we can make use of the following theorem:
"The square of n^th positive integer can be represented as a sum of first n odd positive integers."
Or in mathematical terms:
n^2 = 1 + 3 + 5 + ... + (2 * n - 1)

public class Solution {
    public boolean judgeSquareSum(int c) {
        for (long a = 0; a * a <= c; a++) {
            int b =  c - (int)(a * a);
            int i = 1, sum = 0;
            while (sum < b) {
                sum += i;
                i += 2;
            }
            if (sum == b)
                return true;
        }
        return false;
    }
}

2. Sqrt 44%
Time complexity : O(sqrt(c) * log(c)).
Space complexity : O(1).
public class Solution {
    public boolean judgeSquareSum(int c) {
        for (long a = 0; a * a <= c; a++) {
            double b = Math.sqrt(c - a * a);
            if (b == (int) b)
                return true;
        }
        return false;
    }
}

3. Using Binary Search 15.75%
Time complexity : O(sqrt(c) * log(c)).
Space complexity : O(log(c)).

public class Solution {
    public boolean judgeSquareSum(int c) {
        for (long a = 0; a * a <= c; a++) {
            int b = c - (int)(a * a);
            if (binary_search(0, b, b))
                return true;
        }
        return false;
    }
    public boolean binary_search(long s, long e, int n) {
        if (s > e)
            return false;
        long mid = s + (e - s) / 2;
        if (mid * mid == n)
            return true;
        if (mid * mid > n)
            return binary_search(s, mid - 1, n);
        return binary_search(mid + 1, e, n);
    }
}

4. Two pointers 81%
public class Solution {
    public boolean judgeSquareSum(int c) {
        int lo = 0, hi = (int)Math.sqrt(c);
        while (lo <= hi) {
            int sum = lo * lo + hi * hi;
            if (sum == c) return true;
            if (sum < c) lo++;
            else hi--;
        }
        return false;
    }
}
'''