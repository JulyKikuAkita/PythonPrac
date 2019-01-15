__source__ = 'https://leetcode.com/problems/cheapest-flights-within-k-stops/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 787. Cheapest Flights Within K Stops
#
# There are n cities connected by m flights.
# Each fight starts from city u and arrives at v with a price w.
#
# Now given all the cities and flights,
# together with starting city src and the destination dst,
# your task is to find the cheapest price from src to dst with up to k stops.
# If there is no such route, output -1.
#
# Example 1:
# Input:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation:
# The graph looks like this:
#
#
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
# Example 2:
# Input:
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The graph looks like this:
#
#
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
# Note:
#
# The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
# The size of flights will be in range [0, n * (n - 1) / 2].
# The format of each flight will be (src, dst, price).
# The price of each flight will be in the range [1, 10000].
# k is in the range of [0, n - 1].
# There will not be any duplicated flights or self cycles.
#
import unittest
import collections
# 73,45% 44ms
from heapq import *
class SolutionDijkstra(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        minCost=None
        graph=collections.defaultdict(list)
        for i in flights:
            graph[i[0]].append((i[1],i[2]))
        if src not in graph:
            return -1
        visited={}
        heap=[]
        heappush(heap,(0,src,0))
        while heap:
            price,des,stop=heappop(heap)
            if des==dst:
                return price
            visited[des]=1
            if stop<K+1:
                for i in graph[des]:
                    if i[0] not in visited:
                        heappush(heap,(i[1]+price,i[0],stop+1))
        return minCost if minCost else -1

#96ms 22.03%
class Solution2(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        dist = [[float('inf')] * n for _ in xrange(2)]
        dist[0][src] = dist[1][src] = 0

        for i in xrange(K + 1):
            for u, v, w in flights:
                dist[i&1][v] = min(dist[i&1][v], dist[~i&1][u] + w)
        return dist[K&1][dst] if dist[K&1][dst] < float('inf') else -1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/cheapest-flights-within-k-stops/solution/
# Approach #1: Maintain Cheapest To Target [Accepted]
# Complexity Analysis
# Time Complexity: O(E * K), where E is the length of flights.
# Space Complexity: O(n), the space used to store dis and pre.

# 6ms 100%
class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K) {
        int[][] dist = new int[2][n];
        int INF = Integer.MAX_VALUE / 2;
        Arrays.fill(dist[0], INF);
        Arrays.fill(dist[1], INF);
        dist[0][src] = dist[1][src] = 0;

        for (int i = 0; i <= K; ++i)
            for (int[] edge: flights)
                dist[i&1][edge[1]] = Math.min(dist[i&1][edge[1]], dist[~i&1][edge[0]] + edge[2]);

        return dist[K&1][dst] < INF ? dist[K&1][dst] : -1;
    }
}

#
# Approach #2: Dijkstra's [Accepted]
# Complexity Analysis
# Time Complexity: O(E+nlogn), where E is the total number of flights.
# Space Complexity: O(n), the size of the heap.
#

# 4ms 100%
class Solution {
    private class City implements Comparable<City>{
        int id;
        int costFromSrc;
        int stopFromSrc;

        public City(int id, int costFromSrc, int stopFromSrc){
            this.id = id;
            this.costFromSrc = costFromSrc;
            this.stopFromSrc = stopFromSrc;
        }

        public boolean equals(City c){
            if (c instanceof City) return this.id == c.id;
            return false;
        }

        public int compareTo(City c){
            return this.costFromSrc - c.costFromSrc;
        }
    }

    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K) {
        int[][] srcToDst = new int[n][n];
        for (int i = 0; i < flights.length; i++) {
            srcToDst[flights[i][0]][flights[i][1]] = flights[i][2];
        }

        PriorityQueue<City> minHeap = new PriorityQueue();
        minHeap.offer(new City(src,0,0));

        int[] cost = new int[n];
        Arrays.fill(cost, Integer.MAX_VALUE);
        cost[src] = 0;
        int[] stop = new int[n];
        Arrays.fill(stop, Integer.MAX_VALUE);
        stop[src] = 0;

        while(!minHeap.isEmpty()){
            City curCity = minHeap.poll();
            if (curCity.id == dst) return curCity.costFromSrc;
            if (curCity.stopFromSrc == K + 1) continue;
            int[] nexts = srcToDst[curCity.id];
            for (int i = 0; i < n; i++) {
                if (nexts[i] != 0) {
                    int newCost = curCity.costFromSrc + nexts[i];
                    int newStop = curCity.stopFromSrc + 1;
                    if (newCost < cost[i]) {
                        minHeap.offer(new City(i, newCost, newStop));
                        cost[i] = newCost;
                    } else if (newStop < stop[i]){
                        minHeap.offer(new City(i, newCost, newStop));
                        stop[i] = newStop;
                    }
                }
            }
        }
        return cost[dst] == Integer.MAX_VALUE? -1:cost[dst];
    }
}
'''