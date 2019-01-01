__source__ = 'https://leetcode.com/problems/minimum-number-of-refueling-stops/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 871. Minimum Number of Refueling Stops
#
# A car travels from a starting position to a destination which is target miles east of the starting position.
#
# Along the way, there are gas stations.
# Each station[i] represents a gas station that is station[i][0] miles east of the starting position,
#  and has station[i][1] liters of gas.
#
# The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.
# It uses 1 liter of gas per 1 mile that it drives.
#
# When the car reaches a gas station, it may stop and refuel,
# transferring all the gas from the station into the car.
#
# What is the least number of refueling stops the car must make in order to reach its destination?
# If it cannot reach the destination, return -1.
#
# Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.
# If the car reaches the destination with 0 fuel left, it is still considered to have arrived.
#
# Example 1:
#
# Input: target = 1, startFuel = 1, stations = []
# Output: 0
# Explanation: We can reach the target without refueling.
# Example 2:
#
# Input: target = 100, startFuel = 1, stations = [[10,100]]
# Output: -1
# Explanation: We can't reach the target (or even the first gas station).
# Example 3:
#
# Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
# Output: 2
# Explanation:
# We start with 10 liters of fuel.
# We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
# Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
# and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
# We made 2 refueling stops along the way, so we return 2.
#
#
# Note:
#
# 1 <= target, startFuel, stations[i][1] <= 10^9
# 0 <= stations.length <= 500
# 0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] < target
#
import unittest

# 652ms 32.89%
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        dp = [startFuel] + [0] * len(stations)
        for i, (location, capacity) in enumerate(stations):
            for t in xrange(i, -1, -1):
                if dp[t] >= location:
                    dp[t+1] = max(dp[t+1], dp[t] + capacity)
        for i, d in enumerate(dp):
            if d >= target: return i
        return -1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/minimum-number-of-refueling-stops/solution/
#
Approach 1: Dynamic Programming
Complexity Analysis
Time Complexity: O(N^2), where N is the length of stations.
Space Complexity: O(N), the space used by dp. 

# 36ms 29.80%
class Solution {
    public int minRefuelStops(int target, int startFuel, int[][] stations) {
        int N = stations.length;
        long[] dp = new long[N + 1];
        dp[0] = startFuel;
        
        for (int i = 0; i < N; i++) {
            for (int t = i; t >= 0; t--) {
                if (dp[t] >= stations[i][0]) {
                    dp[t + 1] = Math.max(dp[t + 1], dp[t] + (long)stations[i][1]);
                }
            }
        }
        
        for (int i = 0; i <= N; i++) {
            if (dp[i] >= target) return i;
        }
        return -1;
    }
}

Approach 2: Heap
Complexity Analysis
Time Complexity: O(NlogN), where N is the length of stations.
Space Complexity: O(N), the space used by pq. 

# 12ms 77.65%
class Solution {
    public int minRefuelStops(int target, int startFuel, int[][] stations) {
        // pq is a maxheap of gas station capacities
        PriorityQueue<Integer> pq = new PriorityQueue(Collections.reverseOrder());
        int ans = 0, prev = 0;
        for (int[] station : stations) {
            int location = station[0];
            int capacity = station[1];
            startFuel -= location - prev;
            while (!pq.isEmpty() && startFuel < 0) { // must refuel in past
                startFuel += pq.poll();
                ans++;
            }
            if (startFuel < 0) return -1;
            pq.offer(capacity);
            prev = location;
        }
        
        // Repeat body for station = (target, inf)
        startFuel -= target - prev;
        while (!pq.isEmpty() && startFuel < 0) {
            startFuel += pq.poll();
            ans++;
        }
        if (startFuel < 0) return -1;
        return ans;
    }
}

# Greedy
# 9ms 100%
class Solution {
    public int minRefuelStops(int target, int startFuel, int[][] stations) {
        int res = 0;
        int i = 0;
        int reach = startFuel;
        Queue<Integer> queue = new PriorityQueue<>();
        while (reach < target) {
            while (i < stations.length && stations[i][0] <= reach) {
                queue.offer(-stations[i++][1]);
            }
            if (queue.isEmpty()) return -1;
            res++;
            reach += -queue.poll();
        }
        return res;
    }
}
'''
