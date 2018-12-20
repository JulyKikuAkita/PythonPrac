__source__ = 'https://leetcode.com/problems/lonely-pixel-i/'
# Time:  O(mn)
# Space: O(m + n)
#
# Description: Leetcode # 531. Lonely Pixel I
#
# Given a picture consisting of black and white pixels, find the number of black lonely pixels.
#
# The picture is represented by a 2D char array consisting of 'B' and 'W',
# which means black and white pixels respectively.
#
# A black lonely pixel is character 'B' that located at a specific position
# where the same row and same column don't have any other black pixels.
#
# Example:
# Input:
# [['W', 'W', 'B'],
#  ['W', 'B', 'W'],
#  ['B', 'W', 'W']]
#
# Output: 3
# Explanation: All the three 'B's are black lonely pixels.
#
# Note:
# The range of width and height of the input 2D array is [1,500].
# Hide Company Tags Google
# Hide Tags Array Depth-first Search
#
import unittest
# 116ms 99.03%
class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        return sum(col.count('B') == 1 == picture[col.index('B')].count('B') for col in zip(*picture))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
/**
 * suppose matrix is m*n, there is at most min(m, n) lonely pixels,
 because there could be no more than 1 in each row, or column;
 * therefore, if we record num of black pixel on each row and column,
 we can easily tell whether each pixel is lonely or NO.
 *     _0_1_2_
 *  0 | 0 0 1   rows[0] = 1
 *  1 | 0 1 0   rows[1] = 1
 *  2 | 1 0 0   rows[2] = 1
 *
 * cols[0][1][2]
 *     1  1  1
 */
# 7ms 47.71%
class Solution {
    public int findLonelyPixel(char[][] picture) {
        if (picture == null || picture.length == 0 || picture[0].length == 0) return 0;
        int m = picture.length;
        int n = picture[0].length;
        int[] rows = new int[m];
        int[] cols = new int[n];

        for ( int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                cols[j] += picture[i][j] == 'B' ? 1 : 0;
                rows[i] += picture[i][j] == 'B' ? 1 : 0;
            }
        }

        int res = 0;
        for ( int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (picture[i][j] == 'B' && cols[j] == 1 && rows[i] == 1) res++;
            }
        }
        return res;
    }
}

'''
