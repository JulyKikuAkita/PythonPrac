__source__ = 'https://leetcode.com/problems/walking-robot-simulation/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 874. Walking Robot Simulation
#
# A robot on an infinite grid starts at point (0, 0) and faces north.
# The robot can receive one of three possible types of commands:
#
# -2: turn left 90 degrees
# -1: turn right 90 degrees
# 1 <= x <= 9: move forward x units
# Some of the grid squares are obstacles.
#
# The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])
#
# If the robot would try to move onto them,
# the robot stays on the previous grid square instead (but still continues following the rest of the route.)
#
# Return the square of the maximum Euclidean distance that the robot will be from the origin.
#
# Example 1:
#
# Input: commands = [4,-1,3], obstacles = []
# Output: 25
# Explanation: robot will go to (3, 4)
# Example 2:
#
# Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# Output: 65
# Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)
#
#
# Note:
#
# 0 <= commands.length <= 10000
# 0 <= obstacles.length <= 10000
# -30000 <= obstacle[i][0] <= 30000
# -30000 <= obstacle[i][1] <= 30000
# The answer is guaranteed to be less than 2 ^ 31.
#
import unittest

# 108ms 65.96%
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        obstacleSet = set(map(tuple, obstacles))
        ans = 0

        for cmd in commands:
            if cmd == -2:  #left
                di = (di - 1) % 4
            elif cmd == -1:  #right
                di = (di + 1) % 4
            else:
                for k in xrange(cmd):
                    if (x+dx[di], y+dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x*x + y*y)
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/walking-robot-simulation/solution/
Approach 1: Simulation
Complexity Analysis
Time Complexity: O(N + K), where N, K are the lengths of commands and obstacles respectively.
Space Complexity: O(K), the space used in storing the obstacleSet.

#19ms 98.01%
class Solution {
    public int robotSim(int[] commands, int[][] obstacles) {
        int[] dx = new int[]{0, 1, 0, -1};
        int[] dy = new int[]{1, 0, -1, 0};
        int x = 0, y = 0, di = 0;

        // Encode obstacles (x, y) as (x+30000) * (2^16) + (y+30000)
        Set<Long> obstacleSet = new HashSet();
        for (int[] obstacle: obstacles) {
            long ox = (long) obstacle[0] + 30000;
            long oy = (long) obstacle[1] + 30000;
            obstacleSet.add((ox << 16) + oy);
        }

        int ans = 0;
        for (int cmd: commands) {
            if (cmd == -2)  //left
                di = (di + 3) % 4;
            else if (cmd == -1)  //right
                di = (di + 1) % 4;
            else {
                for (int k = 0; k < cmd; ++k) {
                    int nx = x + dx[di];
                    int ny = y + dy[di];
                    long code = (((long) nx + 30000) << 16) + ((long) ny + 30000);
                    if (!obstacleSet.contains(code)) {
                        x = nx;
                        y = ny;
                        ans = Math.max(ans, x*x + y*y);
                    }
                }
            }
        }

        return ans;
    }
}

#12ms 100%

class Solution {
    static final int[] dx = {0, 1, 0, -1};
    static final int[] dy = {1, 0, -1, 0};

    class Pos {
        int x;
        int y;

        Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int hashCode() {
            return x * 31 + y;
        }

        public boolean equals(Object obj) {
            Pos pos2 = (Pos)obj;
            return x == pos2.x && y == pos2.y;
        }
    }
    public int robotSim(int[] commands, int[][] obstacles) {
        Set<Pos> walls = new HashSet<>(obstacles.length * 2);
        for (int[] obs : obstacles) {
            walls.add(new Pos(obs[0], obs[1]));
        }

        Pos pos = new Pos(0, 0);
        int incx = 0, incy = 0, dir = 0, max = 0;
        for (int command: commands) {
            switch (command) {
                case -2: //turn left
                    dir = (dir + 3) % 4;
                    break;
                case -1: // turn right
                    dir = (dir + 1) % 4;
                    break;
                default: {
                    incx = dx[dir];
                    incy = dy[dir];
                    for (int step = 1; step <= command; ++step) {
                        pos.x += incx;
                        pos.y += incy;

                        if (walls.contains(pos)) {
                            pos.x -= incx;
                            pos.y -= incy;
                            break;
                        }
                    }
                    max = Math.max(max, pos.x * pos.x + pos.y * pos.y);
                    break;
                }
            }
        }
        return max;
    }
}
'''