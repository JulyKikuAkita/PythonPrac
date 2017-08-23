__source__ = 'https://leetcode.com/problems/shortest-distance-from-all-buildings/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/shortest-distance-from-all-buildings.py
# Time:  O(k * m * n), k is the number of the buildings
# Space: O(m * n)
#
# Description: Leetcode # 317. Shortest Distance from All Buildings
#
# You want to build a house on an empty land which reaches all buildings in the shortest amount of distance.
# You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:
#
# Each 0 marks an empty land which you can pass by freely.
# Each 1 marks a building which you cannot pass through.
# Each 2 marks an obstacle which you cannot pass through.
# For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):
#
# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
# So return 7.
#
# Note:
# There will be at least one building. If it is not possible to build such house according to the above rules,
# return -1.
#
# Companies
# Google Zenefits
# Related Topics
# Breadth-first Search
# Similar Questions
# Walls and Gates Best Meeting Point
#
import unittest
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def bfs(grid, dists, cnts, x, y):
            dist, m, n = 0, len(grid), len(grid[0])
            visited = [[False for _ in xrange(n)] for _ in xrange(m)]

            pre_level = [(x, y)]
            visited[x][y] = True
            while pre_level:
                dist += 1
                cur_level = []
                for i, j in pre_level:
                    for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        I, J = i+dir[0], j+dir[1]
                        if 0 <= I < m and 0 <= J < n and grid[I][J] == 0 and not visited[I][J]:
                            cnts[I][J] += 1
                            dists[I][J] += dist
                            cur_level.append((I, J))
                            visited[I][J] = True
                pre_level = cur_level

        m, n, cnt = len(grid),  len(grid[0]), 0
        dists = [[0 for _ in xrange(n)] for _ in xrange(m)]
        cnts = [[0 for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    cnt += 1
                    bfs(grid, dists, cnts, i, j)

        shortest = float("inf")
        for i in xrange(m):
            for j in xrange(n):
                if dists[i][j] < shortest and cnts[i][j] == cnt:
                    shortest = dists[i][j]

        return shortest if shortest != float("inf") else -1
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
Traverse the matrix. For each building, use BFS to compute the shortest distance from each '0' to
this building. After we do this for all the buildings, we can get the sum of shortest distance
from every '0' to all reachable buildings. This value is stored in 'distance[][]'.
For example, if grid[2][2] == 0, distance[2][2] is the sum of shortest distance from this block to all reachable buildings.
Time complexity: O(number of 1)O(number of 0) ~ O(m^2n^2)

We also count how many building each '0' can be reached. It is stored in reach[][].
This can be done during the BFS.
We also need to count how many total buildings are there in the matrix, which is stored in 'buildingNum'.

Finally, we can traverse the distance[][] matrix to get the point having shortest distance to all buildings. O(m*n)

The total time complexity will be O(m^2*n^2), which is quite high!.

# 79.57% 14ms
public class Solution {
    private static final int[][] DIRECTIONS = new int[][] {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};

    public int shortestDistance(int[][] grid) {
        int m = grid.length;
        int n = m == 0 ? 0 : grid[0].length;
        if (m == 0 || n == 0) {
            return 0;
        }
        int[][] distances = new int[m][n];
        int[][] reachable = new int[m][n];
        int numBuildings = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    bfs(grid, distances, reachable, i, j, m, n, numBuildings);
                    numBuildings++;
                }
            }
        }
        int result = Integer.MAX_VALUE;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0 && reachable[i][j] == numBuildings) {
                    result = Math.min(result, distances[i][j]);
                }
            }
        }
        return result == Integer.MAX_VALUE ? -1 : result;
    }

    private void bfs(int[][] grid, int[][] distances, int[][] reachable, int i, int j, int m, int n, int numBuildings) {
        Queue<Integer> queue = new LinkedList<>();
        boolean[][] visited = new boolean[m][n];
        int distance = 0;
        reachable[i][j]++;
        queue.add(i * n + j);
        visited[i][j] = true;
        while (!queue.isEmpty()) {
            distance++;
            int size = queue.size();
            while (size-- > 0) {
                int cur = queue.poll();
                int curI = cur / n;
                int curJ = cur % n;
                for (int[] direction : DIRECTIONS) {
                    int newI = curI + direction[0];
                    int newJ = curJ + direction[1];
                    if (newI >= 0 && newI < m && newJ >= 0 && newJ < n && !visited[newI][newJ] && grid[newI][newJ] == 0 && reachable[newI][newJ] == numBuildings) {
                        distances[newI][newJ] += distance;
                        reachable[newI][newJ]++;
                        queue.add(newI * n + newJ);
                        visited[newI][newJ] = true;
                    }
                }
            }
        }
    }
}

#74.79% 17ms
public class Solution {
    private static final int[][] DIRECTIONS = new int[][] {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public int shortestDistance(int[][] grid) {
        int m = grid.length;
        int n = m == 0 ? 0 : grid[0].length;
        if (m == 0 || n == 0) {
            return 0;
        }
        int[][] distances = new int[m][n];
        int[][] reachable = new int[m][n];
        int buildings = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    bfs(grid, m, n, i, j, distances, reachable, buildings);
                    buildings++;
                }
            }
        }
        int result = Integer.MAX_VALUE;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0 && reachable[i][j] == buildings) {
                    result = Math.min(result, distances[i][j]);
                }
            }
        }
        return result == Integer.MAX_VALUE ? -1 : result;
    }

    private void bfs(int[][] grid, int m, int n, int i, int j, int[][] distances, int[][] reachable, int buildings) {
        Queue<Integer> rowQueue = new LinkedList<>();
        Queue<Integer> colQueue = new LinkedList<>();
        boolean[][] visited = new boolean[m][n];
        int path = 1;
        rowQueue.add(i);
        colQueue.add(j);
        visited[i][j] = true;
        while (!rowQueue.isEmpty()) {
            int size = rowQueue.size();
            for (int k = 0; k < size; k++) {
                int curRow = rowQueue.poll();
                int curCol = colQueue.poll();
                for (int[] direction : DIRECTIONS) {
                    int nextRow = curRow + direction[0];
                    int nextCol = curCol + direction[1];
                    if (nextRow >= 0 && nextRow < m && nextCol >= 0 && nextCol < n && grid[nextRow][nextCol] == 0 && !visited[nextRow][nextCol] && reachable[nextRow][nextCol] == buildings) {
                        rowQueue.add(nextRow);
                        colQueue.add(nextCol);
                        distances[nextRow][nextCol] += path;
                        visited[nextRow][nextCol] = true;
                        reachable[nextRow][nextCol]++;
                    }
                }
            }
            path++;
        }
    }
}
'''