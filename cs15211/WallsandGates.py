__author__ = 'July'
# https://leetcode.com/discuss/60149/straightforward-python-solution-without-recursion
# http://lidang.blogspot.com/2016/02/leetcode-286pythonwalls-and.html
'''
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
#
# Facebook
'''
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


#java
js = '''
public class Solution {
    public static final int[][] DIRECTIONS = new int[][] {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public void wallsAndGates(int[][] rooms) {
        if (rooms.length == 0) {
            return;
        }
        int m = rooms.length;
        int n = rooms[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (rooms[i][j] == 0) {
                    wallsAndGates(rooms, m, n, i, j, DIRECTIONS);
                }
            }
        }
    }

    private void wallsAndGates(int[][] rooms, int m, int n, int row, int col, int[][] directions) {
        Queue<Integer> rowQueue = new LinkedList<>();
        Queue<Integer> colQueue = new LinkedList<>();
        rowQueue.add(row);
        colQueue.add(col);
        int distance = 0;
        while (!rowQueue.isEmpty()) {
            int size = rowQueue.size();
            for (int k = 0; k < size; k++) {
                int i = rowQueue.poll();
                int j = colQueue.poll();
                rooms[i][j] = Math.min(rooms[i][j], distance);
                for (int[] direction : directions) {
                    int newI = i + direction[0];
                    int newJ = j + direction[1];
                    if (newI >= 0 && newI < m && newJ >= 0 && newJ < n && rooms[newI][newJ] >= distance) {
                        rowQueue.add(newI);
                        colQueue.add(newJ);
                    }
                }
            }
            distance++;
        }
    }
}
'''