__source__ = 'https://leetcode.com/problems/counting-bits/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/counting-bits.py
# Time:  O(n)
# Space: O(n)
#
# Description: Leetcode # 338. Counting Bits
#
# Given a non negative integer number num. For every numbers i in the range 0 <= i <= num
# calculate the number of 1's in their binary representation and return them as an array.
#
# Example:
# For num = 5 you should return [0,1,1,2,1,2].
#
# Follow up:
#
# It is very easy to come up with a solution with run time O(n*sizeof(integer)).
# But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss?
# Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
#
# Related Topics
# Dynamic Programming Bit Manipulation
# Similar Questions
# Number of 1 Bits
#
import unittest
# 144ms 39.09%
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        for i in xrange(1, num + 1):
            # Number of 1's in i = (i & 1) + number of 1's in (i / 2).
            res.append((i & 1) + res[i >> 1])
        return res

    def countBits2(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        s = [0]
        while len(s) <= num:
            s.extend(map(lambda x: x + 1, s))
        return s[:num + 1]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
    s = Solution()
    r = s.countBits2(5)
    print r

Java = '''
# Thought: https://leetcode.com/problems/counting-bits/solution/

# 1ms 99.16%
class Solution {
    public int[] countBits(int num) {
        int[] ones = new int[num+1];
        for(int i=1; i<=num; i++)
            ones[i]=Integer.bitCount(i);
        return ones;
    }
}

# 1ms 99.16%
class Solution {
    public int[] countBits(int num) {
        int[] res = new int[num + 1];
        for (int i = 1; i <= num; i++) {
            res[i] = res[i >> 1] + (i & 1);
        }
        return res;
    }
}

# DP: https://discuss.leetcode.com/topic/40195/how-we-handle-this-question-on-interview-thinking-process-dp-solution
Thought:
In general, we have the following transition function for popcount P(x):
P(x + b) = P(x) + 1, b = 2^m > x
With this transition function, we can then apply Dynamic Programming to generate all the pop counts starting from 00.

# 1ms 99.16%
class Solution {
    public int[] countBits(int num) {
        int[] res = new int[num + 1];
        int offset = 1;
        for (int i = 1; i <= num; i++) {
            if (offset * 2 == i) {
                offset *= 2;
            }
            res[i] = res[i - offset] + 1;
        }
        return res;
    }
}

# 1ms 99.16%
class Solution {
  public int[] countBits(int num) {
      int[] ans = new int[num + 1];
      for (int i = 1; i <= num; ++i)
        ans[i] = ans[i >> 1] + (i & 1); // x / 2 is x >> 1 and x % 2 is x & 1
      return ans;
  }
}

# 1ms 99.16%
class Solution {
    public int[] countBits(int num) {
        int[] result = new int[num + 1];
        int lastSq = 0;
        for (int i = 1; i <= num; i++) {
            if ((i & (i - 1)) == 0) {
                result[i] = 1;
                lastSq = i;
            } else {
                result[i] = result[lastSq] + result[i - lastSq];
            }
        }
        return result;
    }
}
'''