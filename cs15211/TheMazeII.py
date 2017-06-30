__source__ = 'https://leetcode.com/problems/the-maze-ii/#/description'
# Time:  O(m*n)
# Space: O(m*n)
#
# Description:
# There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces
# by rolling up, down, left or right, but it won't stop rolling until hitting a wall.
# When the ball stops, it could choose the next direction.
#
# Given the ball's start position, the destination and the maze, f
# ind the shortest distance for the ball to stop at the destination.
# The distance is defined by the number of empty spaces traveled by the ball
# from the start position (excluded)
# to the destination (included). If the ball cannot stop at the destination, return -1.
#
# The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space.
# You may assume that the borders of the maze are all walls.
# The start and destination coordinates are represented by row and column indexes.
#
# Example 1
#
# Input 1: a maze represented by a 2D array
#
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
#
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (4, 4)
#
# Output: 12
# Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
#              The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.
#
# Example 2
#
# Input 1: a maze represented by a 2D array
#
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
#
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (3, 2)
#
# Output: -1
# Explanation: There is no way for the ball to stop at the destination.
#
# Note:
# There is only one ball and one destination in the maze.
# Both the ball and the destination exist on an empty space, and they will not be
# at the same position initially.
# The given maze does not contain border (like the red rectangle in the example pictures),
# but you could assume the border of the maze are all walls.
# The maze contains at least 2 empty spaces, and both the width and height of
# the maze won't exceed 100.
# Hide Company Tags Google
# Hide Tags Depth-first Search Breadth-first Search
# Hide Similar Problems (M) The Maze (H) The Maze III

import unittest
import heapq
# I tried DFS, BFS but got TLE then I found that we need to use heap instead of list to
# store the current nodes
# (Dijkstra's algorithm).
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        dest = tuple(destination)
        m = len(maze)
        n = len(maze[0])
        res = None
        def go(start, direction):
            # return the stop position and length
            i, j = start
            ii, jj = direction
            l = 0
            while 0<=i+ii<m and 0<=j+jj<n and maze[i+ii][j+jj]!=1:
                i+=ii
                j+=jj
                l+=1
            return l, (i,j)

        # bfs (dijkstra: https://en.wikipedia.org/wiki/Dijkstra's_algorithm)
        visited={}
        q=[]
        heapq.heappush(q, (0, tuple(start)))
        while q:
            length, cur = heapq.heappop(q)
            if cur in visited and visited[cur]<=length:
                continue # if cur is visited and with a shorter length, skip it.
            visited[cur]=length
            if cur == dest:
                return length
            for direction in [(-1, 0), (1, 0), (0,-1), (0,1)]:
                l, np = go(cur, direction)
                heapq.heappush(q, (length+l, np))
        return -1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/the-maze-ii/
#BFS 85%

public class Solution {
    private static final int[][] DIRS ={{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

    public int shortestDistance(int[][] maze, int[] start, int[] destination) {
        //declare a 2-d arr to trace distance
        int[][] distance = new int[maze.length][maze[0].length];
        for (int[] row : distance) {
            Arrays.fill(row, Integer.MAX_VALUE);
        }
        distance[start[0]][start[1]] = 0;

        Queue <int[]> queue = new LinkedList<>();
        queue.offer(start);
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            for (int[] dir : DIRS) {
                int x = cur[0] + dir[0];
                int y = cur[1] + dir[1];
                int count = 0;
                while ( x >= 0 && y >= 0 && x < maze.length && y < maze[0].length && maze[x][y] == 0) {
                    x += dir[0];
                    y += dir[1];
                    count++;
                }
                x -= dir[0];
                y -= dir[1];
                if (distance[x][y] > distance[cur[0]][cur[1]] + count) {
                    distance[x][y] = distance[cur[0]][cur[1]] + count;
                    queue.add(new int[]{x, y});
                }
            }
        }
        return distance[destination[0]][destination[1]] == Integer.MAX_VALUE ? -1 : distance[destination[0]][destination[1]];
    }
}

#DFS
11.59%
public class Solution {
    private static final int[][] DIRS ={{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

    public int shortestDistance(int[][] maze, int[] start, int[] destination) {
        int[][] distance = new int[maze.length][maze[0].length];
        for (int[] row: distance) {
            Arrays.fill(row, Integer.MAX_VALUE);
        }
        distance[start[0]][start[1]] = 0;
        dfs(maze, start, destination, distance);
        return distance[destination[0]][destination[1]] == Integer.MAX_VALUE ? -1 : distance[destination[0]][destination[1]];
    }

    public void dfs(int[][] maze, int[] start, int[] destination, int[][] distance) {
        for (int[] dir : DIRS) {
            int x = start[0] + dir[0];
            int y = start[1] + dir[1];
            int count = 0;

            while (x >= 0 && y >= 0 && x < maze.length && y < maze[0].length && maze[x][y] == 0) {
                x += dir[0];
                y += dir[1];
                count++;
            }

            //remove the additional addition
            x -= dir[0];
            y -= dir[1];
            if (distance[x][y] > distance[start[0]][start[1]] + count) {
                distance[x][y] = distance[start[0]][start[1]] + count;
                dfs(maze, new int[]{x, y}, destination, distance);
            }
        }
    }
}

#3 Using Dijkstra Algorithm [Accepted]
11.82%
public class Solution {
    public int shortestDistance(int[][] maze, int[] start, int[] dest) {
        int[][] distance = new int[maze.length][maze[0].length];
        boolean[][] visited = new boolean[maze.length][maze[0].length];
        for (int[] row: distance)
            Arrays.fill(row, Integer.MAX_VALUE);
        distance[start[0]][start[1]] = 0;
        dijkstra(maze, start, dest, distance, visited);
        return distance[dest[0]][dest[1]] == Integer.MAX_VALUE ? -1 : distance[dest[0]][dest[1]];
    }
    public int[] minDistance(int[][] distance, boolean[][] visited) {
        int[] min={-1,-1};
        int min_val = Integer.MAX_VALUE;
        for (int i = 0; i < distance.length; i++) {
            for (int j = 0; j < distance[0].length; j++) {
                if (!visited[i][j] && distance[i][j] < min_val) {
                    min = new int[] {
                        i,
                        j
                    };
                    min_val = distance[i][j];
                }
            }
        }
        return min;
    }
    public void dijkstra(int[][] maze, int[] start, int[] dest, int[][] distance, boolean[][] visited) {
        int[][] dirs={{0,1},{0,-1},{-1,0},{1,0}};
        while (true) {
            int[] s = minDistance(distance, visited);
            if (s[0] < 0)
                break;
            visited[s[0]][s[1]] = true;
            for (int[] dir: dirs) {
                int x = s[0] + dir[0];
                int y = s[1] + dir[1];
                int count = 0;
                while (x >= 0 && y >= 0 && x < maze.length && y < maze[0].length && maze[x][y] == 0) {
                    x += dir[0];
                    y += dir[1];
                    count++;
                }
                if (distance[s[0]][s[1]] + count < distance[x - dir[0]][y - dir[1]]) {
                    distance[x - dir[0]][y - dir[1]] = distance[s[0]][s[1]] + count;
                }
            }
        }
    }
}
'''