__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/gas-station.py
# Time:  O(n)
# Space: O(1)
# Greedy
#
# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).
# You begin the journey with an empty tank at one of the gas stations.
#
# Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
#
# Note:
# The solution is guaranteed to be unique.
#
# Greedy
import unittest
class Solution(unittest.TestCase):
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        start, total_sum, current_sum = 0, 0, 0
        for i in xrange(len(gas)):
            diff = gas[i] - cost[i]
            current_sum += diff
            total_sum += diff
            if current_sum < 0:
                start = i + 1
                current_sum = 0
        if total_sum >= 0:
            return start
        return -1

    def test(self):
        self.assertEqual(self.canCompleteCircuit([1, 2, 3], [3, 2, 1]), 1)
        self.assertEqual(self.canCompleteCircuit([1, 2, 3], [1, 2, 4]), -1)
        self.assertEqual(Solution2().canCompleteCircuit([1, 2, 3], [3, 2, 1]), 1)
        self.assertEqual(Solution2().canCompleteCircuit([1, 2, 3], [1, 2, 4]), -1)



class Solution2:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost) :
            return -1

        diff = 0
        stationIndex = 0
        for i in range(len(gas)):
            if gas[i] + diff < cost[i]:
                stationIndex = i+1;
                diff =0
            else:
                diff += gas[i]-cost[i]
        return stationIndex

if __name__ == "__main__":
    print Solution().canCompleteCircuit([1, 2, 3], [3, 2, 1])
    print Solution().canCompleteCircuit([1, 2, 3], [2, 2, 2])
    print Solution().canCompleteCircuit([1, 2, 3], [1, 2, 3])
    print Solution().canCompleteCircuit([1, 2, 3], [1, 2, 4])

# Java
js = '''
public class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int total = 0;
        int cur = 0;
        int start = 0;
        for (int i = 0; i < gas.length; i++) {
            int diff = gas[i] - cost[i];
            total += diff;
            cur += diff;
            if (cur < 0) {
                start = i + 1;
                cur = 0;
            }
        }
        return total < 0 ? -1 : start;
    }
}
'''