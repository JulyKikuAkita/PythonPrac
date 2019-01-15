__source__ = 'https://leetcode.com/problems/4-keys-keyboard/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 651. 4 Keys Keyboard
#
# Imagine you have a special keyboard with the following keys:
#
# Key 1: (A): Prints one 'A' on screen.
#
# Key 2: (Ctrl-A): Select the whole screen.
#
# Key 3: (Ctrl-C): Copy selection to buffer.
#
# Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.
#
# Now, you can only press the keyboard for N times (with the above four keys), find out the maximum numbers of 'A' you can print on screen.
#
# Example 1:
# Input: N = 3
# Output: 3
# Explanation:
# We can at most get 3 A's on screen by pressing following key sequence:
# A, A, A
# Example 2:
# Input: N = 7
# Output: 9
# Explanation:
# We can at most get 9 A's on screen by pressing following key sequence:
# A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
# Note:
# 1 <= N <= 50
# Answers will be in the range of 32-bit signed integer.
#
# Companies
# Microsoft Google
# Related Topics
# Math Greedy Dynamic Programming
# Similar Questions
# 2 Keys Keyboard

import unittest

#20ms 100%
class Solution:
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = range(N+1)

        for i in xrange(7, N+1):
            for j in range(3, 6):
                dp[i] = max(dp[i], dp[i-j]*(j-1))
        return dp[N]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
We use i steps to reach maxA(i) then use the remaining n - i steps to reach n - i - 1 copies of maxA(i)

For example:
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
Here we have n = 7 and we used i = 3 steps to reach AAA
Then we use the remaining n - i = 4 steps: Ctrl A, Ctrl C, Ctrl V, Ctrl V, to reach n - i - 1 = 3 copies of AAA

We either don't make copies at all, in which case the answer is just n, or if we want to make copies,
we need to have 3 steps reserved for Ctrl A, Ctrl C, Ctrl V so i can be at most n - 3

#1.89% 911ms
public class Solution {
    public int maxA(int n) {
        int max = n;
        for (int i = 1; i <= n - 3; i++)
            max = Math.max(max, maxA(i) * (n - i - 1));
        return max;
    }
}

#21.41% 6ms
public class Solution {
    public int maxA(int N) {
        int[] dp = new int[N+1];
        for (int i = 0; i <= N; i++) {
            dp[i] = i;
            for (int j = 1; j < i - 3; j++) {
                dp[i] = Math.max(dp[i], dp[j] * (i - j -1));
            }
        }
        return dp[N];
    }
}
This one is O(n), inspired by paulalexis58. We don't have to run the second loop between [3,i).
Instead, we only need to recalculate the last two steps.
It's interesting to observe that dp[i - 4] * 3 and dp[i - 5] * 4 always the largest number in the series.
Welcome to add your mathematics proof here.

#42.19% 5ms
public class Solution {
    public int maxA(int N) {
        if (N <= 6)  return N;
        int[] dp = new int[N + 1];
        for (int i = 1; i <= 6; i++) {
            dp[i] = i;
        }
        for (int i = 7; i <= N; i++) {
            dp[i] = Math.max(dp[i - 4] * 3, dp[i - 5] * 4);
        }
        return dp[N];
    }
}

#Math:
O(1) time O(1) space
Pure math. This problem is to partition number N into 3's and 4's and get their product. n = N / 5 + 1
is to compute the number of factors(the total number of 3's and 4's).
With n, it's easy to know how many out of them are 3's by computing n3 = n * 5 - 1 - N.
We minus 1 here because adding a single factor requires one step more than the factor itself,
e.g. x4 takes 5 steps (select all, copy, paste, paste, paste).
10 is special here because it's the only > 6 number
where there is no enough factors to share cuts from decrement of the number of 3's
which means a 5 has to be introduced.

int maxA(int N) {
    if (N <= 6) return N;
    if (N == 10) return 20;
    int n = N / 5 + 1, n3 = n * 5 - 1 - N; //java: Line 7: error: incompatible types: possible lossy conversion from double to int
    return pow(3, n3) * pow(4, n - n3);
}

'''