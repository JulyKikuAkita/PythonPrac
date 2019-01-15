# coding=utf-8
__source__ = 'https://leetcode.com/problems/bus-routes/'
# Time:  O(N^2)
# Space: O(N^2)
#
# Description: Leetcode # 815. Bus Routes
#
# We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever.
# For example if routes[0] = [1, 5, 7],
# this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.
#
# We start at bus stop S (initially not on a bus), and we want to go to bus stop T.
# Travelling by buses only, what is the least number of buses we must take to reach our destination?
# Return -1 if it is not possible.
#
# Example:
# Input:
# routes = [[1, 2, 7], [3, 6, 7]]
# S = 1
# T = 6
# Output: 2
# Explanation:
# The best strategy is take the first bus to the bus stop 7,
# then take the second bus to the bus stop 6.
# Note:
#
# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 500.
# 0 <= routes[i][j] < 10 ^ 6.
#
import unittest

#912ms 22.55%
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T: return 0
        routes = map(set, routes)
        graph = collections.defaultdict(set)
        for i, r1 in enumerate(routes):
            for j in xrange(i+1, len(routes)):
                r2 = routes[j]
                if any(r in r2 for r in r1):
                    graph[i].add(j)
                    graph[j].add(i)

        seen, targets = set(), set()
        for node, route in enumerate(routes):
            if S in route: seen.add(node)
            if T in route: targets.add(node)

        queue = [(node, 1) for node in seen]
        for node, depth in queue:
            if node in targets: return depth
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1

#104ms 99.63%
from collections import deque
class Solution2(object):
    def numBusesToDestination(self, routes, S, T):
        if S == T: return 0

        # You need to record all the buses you can take at each stop so that you can find out all
        # of the stops you can reach when you take one time of bus.
        # the key is stop and the value is all of the buses you can take at this stop.
        stopBoard = {}
        for bus, stops in enumerate(routes):
            for stop in stops:
                if stop not in stopBoard:
                    stopBoard[stop] = [bus]
                else:
                    stopBoard[stop].append(bus)

        # The queue is to record all of the stops you can reach when you take one time of bus.
        queue = deque([S])
        # Using visited to record the buses that have been taken before, because you needn't to take them again.
        visited = set()

        res = 0
        while queue:
            # take one time of bus.
            res += 1
            # In order to traverse all of the stops you can reach for this time, you have to traverse
            # all of the stops you can reach in last time.
            pre_num_stops = len(queue)
            for _ in range(pre_num_stops):
                curStop = queue.popleft()
                # Each stop you can take at least one bus, you need to traverse all of the buses at this stop
                # in order to get all of the stops can be reach at this time.
                for bus in stopBoard[curStop]:
                    # if the bus you have taken before, you needn't take it again.
                    if bus in visited: continue
                    visited.add(bus)
                    for stop in routes[bus]:
                        if stop == T: return res
                        queue.append(stop)
        return -1
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/bus-routes/solution/
Approach #1: Breadth First Search [Accepted]
Complexity Analysis

Time Complexity: Let N denote the number of buses, and bi be the number of stops on the iith bus.
To create the graph, in Python we do O(∑(N−i)bi) work
(we can improve this by checking for which of r1, r2 is smaller),
while in Java we did a O(∑bilogbi) sorting step, plus our searches are O(N∑bi) work.
Our (breadth-first) search is on N nodes, and each node could have NN edges, so it is O(N^2)
Space Complexity: O(N2 +∑bi) additional space complexity, the size of graph and routes.
In Java, our space complexity is O(N^2) because we do not have an equivalent of routes.
Dual-pivot quicksort (as used in Arrays.sort(int[])) is an in-place algorithm,
so in Java we did not increase our space complexity by sorting.

# 95ms 46.91%
import java.awt.Point; //abstract window toolkit
class Solution {
    public int numBusesToDestination(int[][] routes, int S, int T) {
        if (S == T) return 0;
        int N = routes.length;

        List<List<Integer>> graph = new ArrayList();
        for (int i = 0; i < N; ++i) {
            Arrays.sort(routes[i]);
            graph.add(new ArrayList());
        }

        Set<Integer> seen = new HashSet();
        Set<Integer> targets = new HashSet();
        Queue<Point> queue = new ArrayDeque();

        // Build the graph.  Two buses are connected if
        // they share at least one bus stop.
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                if (intersect(routes[i], routes[j])) {
                    graph.get(i).add(j);
                    graph.get(j).add(i);
                }
            }
        }

        // Initialize seen, queue, targets.
        // seen represents whether a node has ever been enqueued to queue.
        // queue handles our breadth first search.
        // targets is the set of goal states we have.
        for (int i = 0; i < N; i++) {
            if (Arrays.binarySearch(routes[i], S) >= 0) {
                seen.add(i);
                queue.offer(new Point(i, 0));
            }
            if (Arrays.binarySearch(routes[i], T) >= 0) {
                targets.add(i);
            }
        }

        while (!queue.isEmpty()) {
            Point info = queue.poll();
            int node = info.x, depth = info.y;
            if (targets.contains(node)) return depth + 1;
            for (Integer nei : graph.get(node)) {
                if (!seen.contains(nei)) {
                    seen.add(nei);
                    queue.offer(new Point(nei, depth + 1));
                }
            }
        }
        return -1;
    }

    private boolean intersect(int[] A, int[] B) {
        int i = 0, j = 0;
        while (i < A.length && j < B.length) {
            if (A[i] == B[j]) return true;
            if (A[i] < B[j]) i++;
            else j++;
        }
        return false;
    }
}

#9ms 99.83% #Brilliant
class Solution {
     public int numBusesToDestination(int[][] routes, int S, int T) {
        int maxStop = 0;
        for (int[] route : routes) {
            for (int stop : route) {
                maxStop = Math.max(stop, maxStop);
            }
        }

        maxStop++;
        int[] counts = new int[maxStop];
        Arrays.fill(counts, maxStop);
        counts[S] = 0;

        boolean changed = true;
        for (int i = 0; changed && i < routes.length; i++) {
            changed = false;
            for (int[] route : routes) {
                int min = maxStop - 1;
                for (int stop : route) {
                    min = Math.min(min, counts[stop]);
                }
                min += 1;
                for (int stop : route) {
                    if (counts[stop] > min) {
                        counts[stop] = min;
                        changed = true;
                    }
                }
            }
        }

        return counts[T] == maxStop ? -1 : counts[T];
    }
}
'''