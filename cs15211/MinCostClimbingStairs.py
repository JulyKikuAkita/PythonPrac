__source__ = 'https://leetcode.com/problems/min-cost-climbing-stairs/'
# Time:  O(N)
# Space: O(1)
# DP:  the final cost f[i] to climb the staircase from some step i is
# f[i] = cost[i] + min(f[i+1], f[i+2])
#
# Description: Leetcode # 746. Min Cost Climbing Stairs
#
# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
#
# Once you pay the cost, you can either climb one or two steps.
# You need to find minimum cost to reach the top of the floor,
# and you can either start from the step with index 0, or the step with index 1.
#
# Example 1:
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
# Example 2:
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
# Note:
# cost will have a length in the range [2, 1000].
# Every cost[i] will be an integer in the range [0, 999].
#
import unittest
#24ms 100%
class SolutionTopDown(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        f1 = f2 = 0
        for x in reversed(cost):
            f1, f2 = x  + min(f1, f2), f1
        return min(f1, f2)

#81.10% 28ms
class SolutionBottomUp(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if cost == [] or None: return
        if len(cost) == 1: return cost[0]
        a = cost[1]
        b = cost[0]
        for i in xrange(2, len(cost)):
            c = min(cost[i] + b, cost[i] + a)
            b = a
            a = c
        return min(a, b)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/min-cost-climbing-stairs/solution/
# Approach #1: Dynamic Programming [Accepted]
# Complexity Analysis
# Time Complexity: O(N) where N is the length of cost.
# Space Complexity: O(1), the space used by f1, f2.
# 100% 9ms
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int f1 = 0, f2 = 0;
        for (int i = cost.length - 1; i >= 0; --i) {
            int f0 = cost[i] + Math.min(f1, f2);
            f2 = f1;
            f1 = f0;
        }
        return Math.min(f1, f2);
    }
}

# 8ms 99.37%
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int step0 = cost[0], step1 = cost[1], res;
        for (int i = 2; i < cost.length; i++) {
            res = cost[i] + Math.min(step0, step1);
            step0 = step1;
            step1 = res;    
        }
        return Math.min(step0, step1);
    }
}

# 8ms 99.37%
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        for (int i = 2; i < cost.length; i++) {
            cost[i] += Math.min(cost[i -1], cost[i -2]);
        }
        return Math.min(cost[cost.length - 1], cost[cost.length - 2]);
    }
}
'''
