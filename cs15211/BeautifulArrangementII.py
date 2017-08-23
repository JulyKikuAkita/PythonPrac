__source__ = 'https://leetcode.com/problems/beautiful-arrangement-ii/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 667. Beautiful Arrangement II
#
# Given two integers n and k, you need to construct a list
# which contains n different positive integers ranging from 1 to n and obeys the following requirement:
# Suppose this list is [a1, a2, a3, ... , an],
# then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.
#
# If there are multiple answers, print any of them.
#
# Example 1:
# Input: n = 3, k = 1
# Output: [1, 2, 3]
# Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3,
# and the [1, 1] has exactly 1 distinct integer: 1.
# Example 2:
# Input: n = 3, k = 2
# Output: [1, 3, 2]
# Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3,
# and the [2, 1] has exactly 2 distinct integers: 1 and 2.
#
# Companies
# Google
# Related Topics
# Array
# Similar Questions
# Beautiful Arrangement
#
import unittest
class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
if you have n number, the maximum k can be n - 1;
if n is 9, max k is 8.
This can be done by picking numbers interleavingly from head and tail,

// start from i = 1, j = n;
// i++, j--, i++, j--, i++, j--

1   2   3   4   5
  9   8   7   6
out: 1 9 2 8 3 7 6 4 5
dif:  8 7 6 5 4 3 2 1
This is a case where k is exactly n - 1
When k is less than that, simply lay out the rest (i, j) in incremental
order(all diff is 1). Say if k is 5:

i++, j--, i++, j--, i++, i++, i++ ...
1   9   2   8    3 4 5 6 7
  8   7   6   5    1 1 1 1

#24.12% 7ms
class Solution {
    public int[] constructArray(int n, int k) {
        int[] res = new int[n];
        for (int i = 0, l = 1, r = n; l <= r; i++)
            res[i] = k > 1 ? (k-- % 2 != 0 ? l++ : r--) : (k % 2 != 0? l++ : r--);
        return res;
    }
}
'''