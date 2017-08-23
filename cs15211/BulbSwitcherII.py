__source__ = 'https://leetcode.com/problems/bulb-switcher-ii/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/bulb-switcher-ii.py
# Time:  O(1)
# Space: O(1)
#
# Description: Leetcode # 672. Bulb Switcher II
#
# There is a room with n lights which are turned on initially and 4 buttons on the wall.
# After performing exactly m unknown operations towards buttons,
# you need to return how many different kinds of status of the n lights could be.
#
# Suppose n lights are labeled as number [1, 2, 3 ..., n], function of these 4 buttons are given below:
#
# Flip all the lights.
# Flip lights with even numbers.
# Flip lights with odd numbers.
# Flip lights with (3k + 1) numbers, k = 0, 1, 2, ...
# Example 1:
# Input: n = 1, m = 1.
# Output: 2
# Explanation: Status can be: [on], [off]
# Example 2:
# Input: n = 2, m = 1.
# Output: 3
# Explanation: Status can be: [on, off], [off, on], [off, off]
# Example 3:
# Input: n = 3, m = 1.
# Output: 4
# Explanation: Status can be: [off, on, off], [on, off, on], [off, off, off], [off, on, on].
# Note: n and m both fit in range [0, 1000].
#
# Companies
# Microsoft
# Related Topics
# Math
# Similar Questions
# Bulb Switcher
#
import unittest
import itertools
#39ms
class Solution(object):
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        seen = set()
        for cand in itertools.product((0, 1), repeat = 4):
            if sum(cand) % 2 == m % 2 and sum(cand) <= m:
                A = []
                for i in xrange(min(n, 3)):
                    light = 1
                    light ^= cand[0]
                    light ^= cand[1] and i % 2
                    light ^= cand[2] and i % 2 == 0
                    light ^= cand[3] and i % 3 == 0
                    A.append(light)
                seen.add(tuple(A))
        return len(seen)

class Solution2(object):
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if m == 0:            return 1
        if n == 1:            return 2
        if m == 1 and n == 2: return 3
        if m == 1 or  n == 2: return 4
        if m == 2:            return 7
        return 8

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
We only need to consider special cases which n<=2 and m < 3. When n >2 and m >=3, the result is 8.
The four buttons:

Flip all the lights.
Flip lights with even numbers.
Flip lights with odd numbers.
Flip lights with (3k + 1) numbers, k = 0, 1, 2, ...
If we use button 1 and 2, it equals to use button 3.
Similarly...

1 + 2 --> 3, 1 + 3 --> 2, 2 + 3 --> 1
So, there are only 8 cases.

All_on, 1, 2, 3, 4, 1+4, 2+4, 3+4

And we can get all the cases, when n>2 and m>=3.

#66.09% 6ms
class Solution {
    public int flipLights(int n, int m) {
        if(m == 0) return 1;
        if (n == 1) return 2;
        if (n == 2 && m == 1) return 3;
        if (n == 2) return 4;
        if (m == 1) return 4;
        if (m == 2) return 7;
        return 8;
    }
}

Thought:
1: light is on
0: light is off
n == 1

Only 2 possibilities: 1 and 0.

n == 2

After one operation, it has only 3 possibilities: 00, 10 and 01.
After two and more operations, it has only 4 possibilities: 11, 10, 01 and 00.

n == 3

After one operation, it has only 4 possibilities: 000, 101, 010 and 011.
After two operations, it has 7 possibilities: 111,101,010,100,000,001 and 110.
After three and more operations, it has 8 possibilities, plus 011 on above case.

n >= 4

After one operation, it has only 4 possibilities: 0000, 1010, 0101 and 0110.
After two or more operations: it has 8 possibilities, 1111,1010,0101,0111,0000,0011, 1100 and 1001.

#66.09% 6ms
class Solution {
    public int flipLights(int n, int m) {
        if (m == 0) return 1;
        if (n <= 0 || m < 0) return 0;

        if (n == 1) return 2;
        else if (n == 2) return (m == 1) ? 3 : 4;
        else return (m == 1) ? 4 : ((m == 2) ? 7 : 8);
    }
}
'''