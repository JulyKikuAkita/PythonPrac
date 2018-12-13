__source__ = 'https://leetcode.com/problems/flood-fill/description/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 733. Flood Fill
#
# An image is represented by a 2-D array of integers,
# each integer representing the pixel value of the image (from 0 to 65535).
#
# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill,
# and a pixel value newColor, "flood fill" the image.
#
# To perform a "flood fill", consider the starting pixel,
# plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel,
# plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel),
# and so on. Replace the color of all of the aforementioned pixels with the newColor.
#
# At the end, return the modified image.
#
# Example 1:
# Input:
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation:
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.
# Note:
#
# The length of image and image[0] will be in the range [1, 50].
# The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
# The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
#
#
import unittest

# 52ms 100%
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r + 1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c - 1)
                if c + 1 < C: dfs(r, c + 1)
        dfs(sr, sc)
        return image

# 92ms 11.15%
class Solution2(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        row, col = len(image), len(image[0])
        if row == 0 or col == 0:
            return image
        original_color = image[sr][sc]
        if original_color == newColor:
            return image

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        stack = [(sr, sc)]
        while stack:
            current_r, current_c = stack.pop()
            image[current_r][current_c] = newColor
            for offset_r, offset_c in directions:
                new_r, new_c = current_r + offset_r, current_c + offset_c
                if new_r >= 0 and new_r < row and new_c >= 0 and new_c < col and image[new_r][new_c] == original_color:
                    stack.append((new_r, new_c))
        return image

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/flood-fill/solution/

# DFS
# 10ms 77.49%
class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int originColor = image[sr][sc];
        if (originColor==newColor) return image;
        dfs(image, sr, sc, newColor, originColor);
        return image;
    }

    private void dfs(int[][] image, int sr, int sc, int newC, int old) {
        if (sr<0 || sr>=image.length || sc<0 || sc>=image[0].length || image[sr][sc]!=old) return;
        image[sr][sc]=newC;
        dfs(image, sr-1, sc, newC, old);
        dfs(image, sr+1, sc, newC, old);
        dfs(image, sr, sc-1, newC, old);
        dfs(image, sr, sc+1, newC, old);
    }
}

# 13ms 42.85%
class Solution {
    final int[][] dirs ={{0,1}, {0,-1}, {1,0}, {-1,0}};

    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int originCol = image[sr][sc];
        if (originCol == newColor) return image;
        image[sr][sc] = newColor; //need to color it
        dfs(image, sr, sc, newColor, originCol);
        return image;
    }

    private void dfs(int[][] image, int sr, int sc, int newColor, int old) {
        for (int[] dir : dirs) {
            int x = sr + dir[0];
            int y = sc + dir[1];
            if (x >= 0 && x < image.length && y >= 0 && y < image[0].length && image[x][y] == old) {
                image[x][y] = newColor;
                dfs(image, x, y, newColor, old);
            }
        }
    }
}

# BFS
# 11ms 68.07%
class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        Queue<int[]> queue = new LinkedList();
        int[] first = {sr, sc};
        queue.add(first);
        int oldColor = image[sr][sc];
        boolean[][] visited = new boolean[image.length][image[0].length];
        for (int i = 0; i < visited.length; i++) {
            for (int j = 0; j < visited[i].length; j++) {
                visited[i][j] = false;
            }
        }

        while(!queue.isEmpty()) {
            int row = queue.peek()[0];
            int col = queue.peek()[1];
            queue.remove();
            int val = image[row][col];

            if (!visited[row][col] && val == oldColor) {
                visited[row][col] = true;
                image[row][col] = newColor;
                if (row > 0) queue.add(new int[]{row - 1, col});
                if (row < image.length - 1) queue.add( new int[]{row + 1, col});
                if (col > 0) queue.add(new int[]{row, col -1});
                if (col < image[0].length - 1) queue.add(new int[]{row, col + 1});
            }
        }
        return image;
    }
}
'''