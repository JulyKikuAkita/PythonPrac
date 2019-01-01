__source__ = 'https://leetcode.com/problems/reach-a-number/'
# Time:  O(target^(1/2))
# Space: O(1)
#
# Description: Leetcode # 754. Reach a Number
#
# You are standing at position 0 on an infinite number line.
# There is a goal at position target.
#
# On each move, you can either go left or right.
# During the n-th move (starting from 1), you take n steps.
#
# Return the minimum number of steps required to reach the destination.
#
# Example 1:
#
# Input: target = 3
# Output: 2
# Explanation:
# On the first move we step from 0 to 1.
# On the second step we step from 1 to 3.
#
# Example 2:
#
# Input: target = 2
# Output: 3
# Explanation:
# On the first move we step from 0 to 1.
# On the second move we step  from 1 to -1.
# On the third move we step from -1 to 2.
#
# Note:
# target will be a non-zero integer in the range [-10^9, 10^9].
import unittest

# 60ms 62.88%
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k
        return k if target % 2 == 0 else k + 1 + k % 2

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/reach-a-number/solution/
#
Approach #1: Mathematical [Accepted]
Complexity Analysis
Time Complexity: O(target^(1/2))
Our while loop needs this many steps, as 1 + 2 + ... + k = (k + 1) * k / 2
Space Complexity: O(1)

# 4ms 91.30%
class Solution {
    public int reachNumber(int target) {
        target = Math.abs(target);
        int k = 0;
        while (target > 0) 
            target -= ++k;
        return target % 2 == 0 ? k : k + 1 + k % 2;
    }
}

# 3ms 97.97%
class Solution {
    public int reachNumber(int target) {
        target = Math.abs(target);
        int k = (int) Math.sqrt(target * 2);
        while (sum(k) < target)  k++;
        int d = sum(k) - target;
        if (d % 2 == 0) return k;
        return k + 1 + k % 2;
    }
    
    private int sum(int k) {
        return k * (k + 1) / 2;
    }
}

# 2ms 100%
class Solution {
    public int reachNumber(int target) {
        if (target == 0) return 0;
        if (target < 0) target = -target;
        int n = (int) (Math.sqrt(0.25 + 2 * target) - 0.5);
        while (true) {
            long num = n * (n + 1) / 2 - target;
            if (num >= 0 && num % 2 == 0) return n;
            n++;
        }   
    }
}
'''
