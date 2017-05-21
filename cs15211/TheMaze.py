__source__ = 'https://leetcode.com/problems/the-maze/#/description'
# Time:  O(m*n)
# Space: O(m*n)
#
# Description:
# There is a ball in a maze with empty spaces and walls.
# The ball can go through empty spaces by rolling up, down, left or right,
# but it won't stop rolling until hitting a wall. When the ball stops,
# it could choose the next direction.
#
# Given the ball's start position, the destination and the maze,
# determine whether the ball could stop at the destination.
#
# The maze is represented by a binary 2D array.
# 1 means the wall and 0 means the empty space.
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
# Output: true
# Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
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
# Output: false
# Explanation: There is no way for the ball to stop at the destination.
#
# Note:
# There is only one ball and one destination in the maze.
# Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
# The given maze does not contain border (like the red rectangle in the example pictures),
# but you could assume the border of the maze are all walls.
# The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
# Hide Company Tags Google
# Hide Tags Depth-first Search Breadth-first Search
# Hide Similar Problems (H) The Maze III (M) The Maze II

import unittest
class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        Q = [start]
        n = len(maze)
        m = len(maze[0])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while Q:
            # Use Q.pop() as DFS or Q.popleft() with deque from collections library for better performance.
            i, j = Q.pop(0)
            maze[i][j] = 2
            if i == destination[0] and j == destination[1]:
                return True
            for x, y in dirs:
                row = i + x
                col = j + y
                while 0 <= row < n and 0 <= col < m and maze[row][col] != 1:
                    row += x
                    col += y
                row -= x
                col -= y
                if maze[row][col] == 0:
                    Q.append([row, col])

        return False

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/the-maze/
Search in the four possible directions when coming to a stopping point (i.e. a new starting point).
Keep track of places that you already started at in case you roll back to that point.
# BFS: 20.21%
public class Solution {
    private static final int[][] DIRS ={{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

    public boolean hasPath(int[][] maze, int[] start, int[] destination) {
        boolean[][] visited = new boolean[maze.length][maze[0].length];
        Queue <int[]> queue = new LinkedList <>();
        queue.add(start);
        visited[start[0]][start[1]] = true;
        while ( !queue.isEmpty() ) {
            int[] cur = queue.poll();
            if (Arrays.equals(cur, destination)) { //if (s[0] == destination[0] && s[1] == destination[1])
                return true;
            }

            for (int[] dir :DIRS) {
                int x = cur[0] + dir[0];
                int y = cur[1] + dir[1];

                while (x >= 0 && x < maze.length && y >= 0 && y < maze[0].length && maze[x][y] == 0) {
                    x += dir[0];
                    y += dir[1];
                } //optimize
                x -= dir[0];
                y -= dir[1];
                if (!visited[x][y]) {
                    queue.add(new int[] {x, y});
                    visited[x][y] = true;
                }
            }
        }
        return false;
    }
}

# DFS: 89%
public class Solution {
    private static final int[] DIR = { 0, 1, 0, -1, 0 };

    public boolean hasPath(int[][] maze, int[] start, int[] destination) {
        boolean[][] visited = new boolean[maze.length][maze[0].length];
        return dfs(maze, visited, start, destination);
    }

    private boolean dfs(int[][] maze, boolean[][] visited, int[] start, int[] destination) {
        if (visited[start[0]][start[1]]) return false;
        if (Arrays.equals(start, destination)) return true;

        visited[start[0]][start[1]] = true;
        for (int i = 0 ; i < DIR.length - 1; i++) {
            int[] newStart = roll(maze, start[0], start[1], DIR[i], DIR[i + 1]);
            if (dfs(maze, visited, newStart, destination)) return true;
        }
        return false;
    }

    private boolean canRoll(int[][] maze, int row, int col) {
        if (row >= maze.length || row < 0 || col >= maze[0].length || col < 0) return false;
        return maze[row][col] != 1; //1 is wall
    }

    private int[] roll(int[][] maze, int row, int col, int rowInc, int colInc) {
        while (canRoll(maze, row + rowInc, col + colInc)) {
            row += rowInc;
            col += colInc;
        }
        return new int[]{row, col};
    }
}
'''