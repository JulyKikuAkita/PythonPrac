__source__ = 'https://leetcode.com/problems/minimize-max-distance-to-gas-station/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 774. Minimize Max Distance to Gas Station
#
# On a horizontal number line,
# we have gas stations at positions stations[0], stations[1], ..., stations[N-1], where N = stations.length.
#
# Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized.
#
# Return the smallest possible value of D.
#
# Example:
#
# Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
# Output: 0.500000
# Note:
#
# stations.length will be an integer in range [10, 2000].
# stations[i] will be an integer in range [0, 10^8].
# K will be an integer in range [1, 10^6].
# Answers within 10^-6 of the true value will be accepted as correct.
#
import unittest

# 612ms 12.10%
class Solution(object):
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        def possible(D):
            return sum(int((stations[i+1] - stations[i]) / D) for i in xrange(len(stations) - 1)) <= K

        lo, hi = 0, 10 **8
        while hi - lo > 1e-6: # 1e-6 == 1 * 10^(-6) == 0.000001 #better than judge if a ~= 0
            mi = (lo + hi) / 2.0
            if possible(mi):
                hi = mi
            else:
                lo = mi
        return lo

# 96ms 100%
class SolutionHeapq(object):
    def minmaxGasDist(self, stations, k):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        diff = max(stations) - min(stations)
        avg = diff * 1.0 / (k + 1)
        import heapq
        import math
        heap = []
        for i in xrange(1, len(stations)):
            diff = (stations[i] - stations[i-1]) * 1.0
            if diff > avg:
                count = int(math.ceil(diff / avg))
                k -= count - 1
                heapq.heappush(heap, (-diff / count, diff, count))
            else :
                heapq.heappush(heap, (-diff, diff, 1))

        for i in xrange(k):
            cur, totalDiff, count = heapq.heappop(heap)
            heapq.heappush(heap, (-totalDiff / (count + 1), totalDiff, count + 1))
        return -heap[0][0]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/minimize-max-distance-to-gas-station/solution/

Approach #1: Dynamic Programming [Memory Limit Exceeded]
Complexity Analysis
Time Complexity: O(N K^2), where N is the length of stations.
Space Complexity: O(NK), the size of dp.


Approach #2: Brute Force [Time Limit Exceeded]
Complexity Analysis
Time Complexity: O(NK), where NN is the length of stations.
Space Complexity: O(N), the size of deltas and count.

Approach #3: Heap [Time Limit Exceeded]
Complexity Analysis
Time Complexity: O(KlogN), where NN is the length of stations.
Space Complexity: O(N), the size of deltas and count.

# TLE
class Solution {
    public double minmaxGasDist(int[] stations, int K) {
        int N = stations.length;
        PriorityQueue<int[]> pq = new PriorityQueue<int[]>((a, b) ->
            (double)b[0] / b[1] < (double)a[0] / a[1] ? -1 : 1
        );

        for (int i = 0; i < N - 1; i++) {
            pq.add(new int[]{stations[i + 1] - stations[i], 1});
        }

        for (int k = 0; k < K; ++k) {
            int[] node = pq.poll();
            node[1]++;
            pq.add(node);
        }

        int[] node = pq.poll();
        return (double) node[0] / node[1];
    }
}

Approach #4: Binary Search [Accepted]
Complexity Analysis
Time Complexity: O(NlogW), where N is the length of stations, and W = 10^{14},
is the range of possible answers (10^8),
divided by the acceptable level of precision (10^{-6}.
Space Complexity: O(1) in additional space complexity.

# 21ms 73.60%
class Solution {
    public double minmaxGasDist(int[] stations, int K) {
        double lo = 0, hi = 1e8;
        while (hi - lo > 1e-6) { // 1 * 10 ^ (-6)
            double mi = (lo + hi) / 2.0;
            if (possible(mi, stations, K))
                hi = mi;
            else
                lo = mi;
        }
        return lo;
    }

    public boolean possible(double D, int[] stations, int K) {
        int used = 0;
        for (int i = 0; i < stations.length - 1; ++i)
            used += (int) ((stations[i+1] - stations[i]) / D);
        return used <= K;
    }
}


'''
