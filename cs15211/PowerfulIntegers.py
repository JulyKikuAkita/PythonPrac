__source__ = 'https://leetcode.com/problems/powerful-integers/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 970. Powerful Integers
#
# Given two non-negative integers x and y,
# an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.
#
# Return a list of all powerful integers that have value less than or equal to bound.
#
# You may return the answer in any order.  In your answer, each value should occur at most once.
#
#
#
# Example 1:
#
# Input: x = 2, y = 3, bound = 10
# Output: [2,3,4,5,7,9,10]
# Explanation:
# 2 = 2^0 + 3^0
# 3 = 2^1 + 3^0
# 4 = 2^0 + 3^1
# 5 = 2^1 + 3^1
# 7 = 2^2 + 3^1
# 9 = 2^3 + 3^0
# 10 = 2^0 + 3^2
# Example 2:
#
# Input: x = 3, y = 5, bound = 15
# Output: [2,4,6,8,10,14]
#
#
# Note:
#
# 1 <= x <= 100
# 1 <= y <= 100
# 0 <= bound <= 10^6
import unittest
# 36ms 66.67%
class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        ans = set()
        # 2**18 > bound
        for i in xrange(18):
            for j in xrange(18):
                v = x**i + y**j
                if v <= bound:
                    ans.add(v)
        return list(ans)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/powerful-integers/solution/
# Approach 1: Brute Force
# Complexity Analysis
# Time Complexity: O(log^2 bound).
# Space Complexity: O(log^2 bound). 
#
// 18 due to bound is up to 10^6 and is approximately equal to (2^3)^6, 
// so maximum power should be 18. Because after raising to a power bigger than 18, 
// all numbers will be more than 10^6
# 5ms 98.80%
class Solution {
    public List<Integer> powerfulIntegers(int x, int y, int bound) {
        Set<Integer> seen = new HashSet();
        for (int i = 0; i < 18 && Math.pow(x, i) <= bound; ++i)
            for (int j = 0; j < 18 && Math.pow(y, j) <= bound; ++j) {
                int v = (int) Math.pow(x, i) + (int) Math.pow(y, j);
                if (v <= bound)
                    seen.add(v);
            }

        return new ArrayList(seen);
    }
}

# https://leetcode.com/problems/powerful-integers/discuss/214197/Java-straightforward-try-all-combinations
# 5ms 98.90%
class Solution {
    public List<Integer> powerfulIntegers(int x, int y, int bound) {
        Set<Integer> result = new HashSet<>();
        for (int a = 1; a < bound; a *= x) {
            for (int b = 1; a + b <= bound; b *= y) {
                result.add(a + b);
                if (y == 1) {
                    break;
                }
            }
            if (x == 1) {
                break;
            }
        }
        return new ArrayList<>(result);
    }
}
'''
