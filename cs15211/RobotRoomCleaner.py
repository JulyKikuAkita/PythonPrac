__source__ = 'https://leetcode.com/problems/robot-room-cleaner/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 489. Robot Room Cleaner
#
# Given a robot cleaner in a room modeled as a grid.
#
# Each cell in the grid can be empty or blocked.
#
# The robot cleaner with 4 given APIs can move forward, turn left or turn right.
# Each turn it made is 90 degrees.
#
# When it tries to move into a blocked cell,
# its bumper sensor detects the obstacle and it stays on the current cell.
#
# Design an algorithm to clean the entire room using only the 4 given APIs shown below.
#
# interface Robot {
#   // returns true if next cell is open and robot moves into the cell.
#   // returns false if next cell is obstacle and robot stays on the current cell.
#   boolean move();
#
#   // Robot will stay on the same cell after calling turnLeft/turnRight.
#   // Each turn will be 90 degrees.
#   void turnLeft();
#   void turnRight();
#
#   // Clean the current cell.
#   void clean();
# }
# Example:
#
# Input:
# room = [
#   [1,1,1,1,1,0,1,1],
#   [1,1,1,1,1,0,1,1],
#   [1,0,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0,0],
#   [1,1,1,1,1,1,1,1]
# ],
# row = 1,
# col = 3
#
# Explanation:
# All grids in the room are marked by either 0 or 1.
# 0 means the cell is blocked, while 1 means the cell is accessible.
# The robot initially starts at the position of row=1, col=3.
# From the top left corner, its position is one row below and three columns right.
# Notes:
#
# The input is only given to initialize the room and the robot's position internally.
# You must solve this problem "blindfolded". In other words,
# you must control the robot using only the mentioned 4 APIs,
# without knowing the room layout and the initial robot's position.
# The robot's initial position will always be in an accessible cell.
# The initial direction of the robot will be facing up.
# All accessible cells are connected,
# which means the all cells marked as 1 will be accessible by the robot.
# Assume all four edges of the grid are all surrounded by wall.
#
import unittest

# https://leetcode.com/problems/robot-room-cleaner/discuss/150132/Very-clear-Python-DFS-code-beat-99-+

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

# 52ms 98.74%
class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.dfs(robot, 0, 0, 0, 1, set())

    def dfs(self, robot, x, y, direction_x, direction_y, visited):
        robot.clean()
        visited.add((x,y))
        for k in xrange(4):
            neighbor_x = x + direction_x
            neighbor_y = y + direction_y
            if (neighbor_x, neighbor_y) not in visited and robot.move():
                self.dfs(robot, neighbor_x, neighbor_y, direction_x, direction_y, visited)
                robot.turnLeft() # turn 90degree
                robot.turnLeft() # turn 90degree to face the opposite direction
                robot.move()
                robot.turnLeft()
                robot.turnLeft()
            robot.turnLeft()
            direction_x, direction_y = -direction_y, direction_x

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
#
# https://leetcode.com/problems/robot-room-cleaner/discuss/151942/Java-DFS-Solution-with-Detailed-Explanation-and-6ms-(99)-Solution
# DFS + backtracking + visited
#
# We want to do a DFS with backtracking.
# The following details are different in this problem than a common dfs problem:
# 1.A way to encode already visited positions (The easy solution is just use relative positions from the starting point)
# 2.A way to backtrack (The concept is the same, we want to reset the position to what it originally was.
# In this case the direction is also added in,
# so we want to reset the direction it's facing to the direction it originally was facing with the original position).
#
# I assume the robot is starting facing upwards,
# but any direction works as long as the order of the directions match the direction with the turning.
#
# The algorithm starts off at 0,0 which is our starting point (the boards starting point doesn't matter,
# and it doesn't matter that there are negative positions), as long as all the values are consistent.
# We add this position to our visited list and clean it. For each of the 4 directions,
# we calculate its next row and next column (remember that we are currently facing in the last direction moved,
# in this code's case the variable curDirection) if we went in that direction.
# If the next position is unvisited we try moving there.
# If we are able to move we call it recursively down the next branch.
#
# After we return from the recursive call we need to backtrack:
#
#                 robot.turnLeft();
#                 robot.turnLeft();
#                 robot.move();
#                 robot.turnRight();
#                 robot.turnRight();
#
# or we can use 2 robot.turnLeft()s like I did.
# We reset the state by turning 180 degrees, moving, and then changing the direction back to what it originally was
# by turning another 180 degrees.
# Then we try the next direction (turning it to the right).
# After all 4 directions are tried it is automatically turned to the original direction
# after the loop since we turned right 4 times.
#
/**
 * // This is the robot's control interface.
 * // You should not implement it, or speculate about its implementation
 * interface Robot {
 *     // Returns true if the cell in front is open and robot moves into the cell.
 *     // Returns false if the cell in front is blocked and robot stays in the current cell.
 *     public boolean move();
 *
 *     // Robot will stay in the same cell after calling turnLeft/turnRight.
 *     // Each turn will be 90 degrees.
 *     public void turnLeft();
 *     public void turnRight();
 *
 *     // Clean the current cell.
 *     public void clean();
 * }
 */
 
# 16ms 11.04%
class Solution {
    final int[][] dirs = new int[][]{{-1,0},{0,1},{1,0},{0,-1}};

    public void cleanRoom(Robot robot) {
        Set<String> offset = new HashSet<>();
        find(robot, offset, 0, 0, 0, new StringBuilder());
    }

    private void find(Robot robot, Set<String> visited, int curDir, int row, int col, StringBuilder sb) {
        sb.append(row);
        sb.append(">");
        sb.append(col);
        visited.add(sb.toString());
        robot.clean();
        for (int i = 0; i < 4; i++) {
            int dir = (curDir + i ) % 4;
            int[] next = dirs[dir];
            int nextRow = row + next[0];
            int nextCol = col + next[1];
            sb.setLength(0); //shall we allocate a new StringBuilder instead of clear buffer? sb.setLength(0)?
            sb.append(nextRow);
            sb.append(">");
            sb.append(nextCol);
            if (!visited.contains(sb.toString()) && robot.move()) {
                find(robot, visited, dir, nextRow, nextCol, new StringBuilder()); //need to new SB for every recursion call
                robot.turnLeft();
                robot.turnLeft();
                robot.move();
                robot.turnLeft();
                robot.turnLeft();
            }
            robot.turnRight(); //cannot turnLEft
        }
    }
}

#100% 3ms
class Solution {
    class Pair{
        int x;
        int y;
        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    public void cleanRoom(Robot robot) {
        boolean[][] visited = new boolean[robot.room.length][robot.room[0].length];
        int[][] dirs = new int[][]{{-1,0},{0,1},{1,0},{0,-1}};
        helper(new Pair(robot.row, robot.col), 0, dirs, robot, visited);
    }

    public void helper(Pair pair, int dir, int[][] dirs, Robot robot, boolean[][] visited) {
        if (visited[pair.x][pair.y]) return;
        visited[pair.x][pair.y] = true;
        robot.clean();
        for (int i = 0; i < 4; i++) {
            if (robot.move()) {
                Pair nextDir = new Pair(pair.x + dirs[dir][0], pair.y + dirs[dir][1]);
                helper(nextDir, dir, dirs, robot, visited);
                robot.turnRight();
                robot.turnRight();
                robot.move();
                robot.turnRight();
                robot.turnRight();
            }
            robot.turnRight(); //cannot turn left
            dir = (dir + 1 ) % 4;
        }
    }
}
'''
