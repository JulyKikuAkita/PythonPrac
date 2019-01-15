__source__ = 'https://leetcode.com/problems/walls-and-gates/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/walls-and-gates.py
# Time:  O(m * n)
# Space: O(g)
#
# Description: Leetcode # 286. Walls and Gates
#
# You are given a m x n 2D grid initialized with these three possible values.
#
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room.
#
# We use the value 231 - 1 = 2147483647 to represent INF
# as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate.
# If it is impossible to reach a gate, it should be filled with INF.
#
# For example, given the 2D grid:
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# After running your function, the 2D grid should be:
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4
#
# Companies
# Google Facebook
# Related Topics
# Breadth-first Search
# Similar Questions
# Surrounded Regions Number of Islands Shortest Distance from All Buildings

import unittest
#BFS
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """

        for i in xrange(len(rooms)):
            for j in xrange(len(rooms[0])):
                if rooms[i][j] == 0:
                    stack = [
                        (i+1, j, 1),
                        (i-1, j, 1),
                        (i, j+1, 1),
                        (i, j-1, 1)
                    ]
                    while stack:
                        ii, jj, dist = stack.pop()
                        if ii < 0 or jj < 0  or ii >= len(rooms) or jj >= len(rooms[0]) or rooms[ii][jj] < dist:
                            continue
                        rooms[ii][jj] = dist
                        stack.append((ii+1, jj, dist + 1))
                        stack.append((ii-1, jj, dist + 1))
                        stack.append((ii, jj+1, dist + 1))
                        stack.append((ii, jj-1, dist + 1))

#BFS -2
class Solution2(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        m = len(rooms)
        n = len(rooms[0])
        stack = []

        for i in xrange(m):
            for j in xrange(n):
                if rooms[i][j] == 0:
                    stack.append([i*n +j, 0])

        cube = [0, 1, 0, -1, 0]
        while stack:
            digit, dis = stack.pop()
            x = digit / n
            y = digit % n
            for k in xrange(4):
                p = x + cube[k]
                q = y + cube[k+1]
                if p >= 0 and p < m and q >= 0 and q < n and rooms[p][q] > dis + 1:
                    rooms[p][q] = dis + 1
                    stack.append([p*n+q, dis+1])

#DFS
class Solution3(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        m = len(rooms)
        n = len(rooms[0])
        padding = [ 0, 1, 0, -1, 0]
        for i in xrange(m):
            for j in xrange(n):
                if rooms[i][j] == 0:
                    self.dfs(rooms, m, n, i, j, padding)

    def dfs(self, rooms, m, n, i, j, padding):
        for k in xrange(4):
            p = i + padding[k]
            q = j + padding[k+1]

            if p >= 0 and q >= 0 and p < m and q < n and rooms[p][q] > rooms[i][j] + 1:
                rooms[p][q] = rooms[i][j] + 1
                self.dfs(rooms, m, n, p, q, padding)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/walls-and-gates/solution/
# DFS
# 99.31% 4ms
class Solution {
    public static final int[][] DIRECTIONS = new int[][] {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public void wallsAndGates(int[][] rooms) {
        int m = rooms.length;
        int n = m == 0 ? 0 : rooms[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (rooms[i][j] == 0) {
                    dfs(rooms, m, n, i, j, 1);
                }
            }
        }
    }

    private void dfs(int[][] rooms, int m, int n, int i, int j, int steps) {
        for (int[] direction : DIRECTIONS) {
            int newI = i + direction[0];
            int newJ = j + direction[1];
            if (newI >= 0 && newI < m && newJ >= 0 && newJ < n && rooms[newI][newJ] > steps) {
                rooms[newI][newJ] = steps;
                dfs(rooms, m, n, newI, newJ, steps + 1);
            }
        }
    }
}

# DFS
# 99.31% 4ms
public class Solution {
    private static int[] dir = {0, 1, 0, -1, 0};
    public void wallsAndGates(int[][] rooms) {
        for (int i = 0; i < rooms.length; i++) {
            for (int j = 0; j < rooms[0].length; j++) {
                if (rooms[i][j] == 0) dfs(rooms, i, j);
            }
        }
    }

    public void dfs(int[][] rooms, int i, int j) {
        for (int k = 0; k < 4; k++) {
            int p = i + dir[k], q = j + dir[k+1];
            if ( 0 <= p && p < rooms.length && 0 <= q && q < rooms[0].length && rooms[p][q] > rooms[i][j] + 1) {
                rooms[p][q] = rooms[i][j] + 1;
                dfs(rooms, p, q);
            }
        }
    }
}

# BFS
# 59.16% 9ms
public class Solution {
    //The Multi End BFS solution used is this
    public static final int[] d = {0, 1, 0, -1, 0};

    public void wallsAndGates(int[][] rooms) {
        if (rooms.length == 0) return;
        int m = rooms.length, n = rooms[0].length;

        Deque<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < m ; i++) {
            for (int j = 0; j < n; j++) {
                if (rooms[i][j] == 0){
                    queue.offer(i *n + j);                }
            }
        }

        while(!queue.isEmpty()){
            int x = queue.poll();
            int i = x / n, j = x % n;
            for (int k = 0; k < 4; k++) {
                int p = i + d[k], q = j + d[k+1];
                if (0 <= p && p < m && 0 <= q && q < n && rooms[p][q] == Integer.MAX_VALUE) {
                    rooms[p][q] = rooms[i][j] + 1;
                    queue.offer(p * n + q);
                }
            }
        }
    }

    private void bfs(int[][] rooms, int i, int j) {
        int m = rooms.length, n = rooms[0].length;
        Deque<Integer> queue = new ArrayDeque<>();
        queue.offer(i * n + j); // Put gate in the queue
        while (!queue.isEmpty()) {
            int x = queue.poll();
            i = x / n; j = x % n;
            for (int k = 0; k < 4; ++k) {
               int p = i + d[k], q = j + d[k+1];
               if (0 <= p && p < m && 0 <= q && q < n && rooms[p][q] > rooms[i][j] + 1) {
                   rooms[p][q] = rooms[i][j] + 1;
                   queue.offer(p * n + q);
               }
            }
        }
    }
}

# BFS2
# 32.38% 13ms
class Solution {
    //The Multi End BFS solution used is this
    public static final int[] d = {0, 1, 0, -1, 0};

    public void wallsAndGates(int[][] rooms) {
        if (rooms.length == 0) return;
        int m = rooms.length, n = rooms[0].length;

        Deque<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < m ; i++) {
            for (int j = 0; j < n; j++) {
                if (rooms[i][j] == 0){
                    queue.offer(i * n + j);
                    bfs(rooms, i, j);  //naive BFS solution
                }
            }
        }
    }

    private void bfs(int[][] rooms, int i, int j) {
        int m = rooms.length, n = rooms[0].length;
        Deque<Integer> queue = new ArrayDeque<>();
        queue.offer(i * n + j); // Put gate in the queue
        while (!queue.isEmpty()) {
            int x = queue.poll();
            i = x / n; j = x % n;
            for (int k = 0; k < 4; ++k) {
               int p = i + d[k], q = j + d[k+1];
               if (0 <= p && p < m && 0 <= q && q < n && rooms[p][q] > rooms[i][j] + 1) {
                   rooms[p][q] = rooms[i][j] + 1;
                   queue.offer(p * n + q);
               }
            }
        }
    }
}
'''