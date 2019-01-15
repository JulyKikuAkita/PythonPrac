__source__ = 'https://leetcode.com/problems/island-perimeter/'
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 463. Island Perimeter
# Though: what if theres' a lake?
# Lake:    [[0,1,0,0],[1,0,1,0],[0,1,0,0],[1,1,0,0]]
# No Lake: [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# -> both works
# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
# and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes"
# (water inside that isn't connected to the water around the island). One cell is a square with side length 1.
# The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
#
# Example:
#
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
#
# Answer: 16
# Explanation: The perimeter is the 16 yellow stripes in the image below:
#
# Companies
# Google
# Related Topics
# Hash Table
#
import unittest
import operator
class Solution(object):
    # Since there are no lakes, every pair of neighbour cells with different values is part of the perimeter
    # (more precisely, the edge between them is).
    # So just count the differing pairs, both horizontally and vertically
    # (for the latter I simply transpose the grid).
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return sum(sum(map(operator.ne, [0] + row, row + [0]))
               for row in grid + map(list, zip(*grid)))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().containsDuplicate([12344555,12344555])

if __name__ == '__main__':
    unittest.main()

Java = '''
Thought:

# Brute force, but do we need to do flood fill?
# 114ms 62.73%
class Solution {
    public int islandPerimeter(int[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) return 0;
        int row = grid.length;
        int col = grid[0].length;
        int sum = 0;

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == 1) {
                    int k = 0;
                    if (i > 0 && grid[i - 1][j] == 1) k++;
                    if (j > 0 && grid[i][j - 1] == 1) k++;
                    if (i + 1 < row && grid[i + 1][j] == 1) k++;
                    if (j + 1 < col && grid[i][j + 1] == 1) k++;
                    sum += (4 - k);
                }
            }
        }
        return sum;
    }
}

# Improve, do not re-visit
add 4 for each land and remove 2 for each neighbor
Thought: loop over the matrix and count the number of islands;
if the current dot is an island, count if it has any right neighbour or down neighbour;
the result is islands * 4 - neighbours * 2

# 78ms 45.56%
class Solution {
    public int islandPerimeter(int[][] grid) {
        int islands = 0, neighbors = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == 1) {
                    islands++;
                    if ( i < grid.length - 1 && grid[i+1][j] == 1) neighbors++;
                    if (j < grid[i].length - 1 && grid[i][j + 1] == 1) neighbors++;
                }
            }
        }
        return islands * 4 - neighbors * 2;
    }
}

# 53ms 98.72%
class Solution {
    public int islandPerimeter(int[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) return 0;
        int res = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    res += 4;
                    if (i > 0 && grid[i - 1][j] == 1) res -= 2;
                    if (j > 0 && grid[i][j-1] == 1) res -= 2;
                }
            }
        }
        return res;
    }
}

# DFS:
# 132ms 18.36%
class Solution {
    public int islandPerimeter(int[][] grid) {
        if (grid == null) return 0;
        for (int i = 0 ; i < grid.length ; i++){
            for (int j = 0 ; j < grid[0].length ; j++){
                if (grid[i][j] == 1) {
                    return getPerimeter(grid,i,j); // if not lake,
                    // count += getPerimeter(grid,i,j); // and return count at the end if with lake
                }
            }
        }
        return 0;
    }
    
    public int getPerimeter(int[][] grid, int i, int j){
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || grid[i][j] == 0) {return 1;}
        
        if (grid[i][j] == -1) return 0;
        
        int count = 0;
        grid[i][j] = -1;
        
        count += getPerimeter(grid, i-1, j);
        count += getPerimeter(grid, i, j-1);
        count += getPerimeter(grid, i, j+1);
        count += getPerimeter(grid, i+1, j);
        
        return count;
    }
}

# 124ms 32.91%
class Solution {
    // the idea is traverse the whole grid, automatically +=4 every time we see a 1, 
    // check this point's surroundings, if the surrounding is not of of boundary and it
    // is a 1, means, also a land, then -= 1 
    private static final int[][] dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    public int islandPerimeter(int[][] grid) {
        int res = 0;
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] == 1){
                    res += 4;
                    for(int[] dir : dirs){
                        int x = dir[0] + i;
                        int y = dir[1] + j;
                        if(x < 0 || y < 0 || x >= grid.length || y >= grid[0].length || grid[x][y] == 0) continue;
                        res -= 1;
                        
                    }
                }
            }
        }
        return res;
    }
}

'''
