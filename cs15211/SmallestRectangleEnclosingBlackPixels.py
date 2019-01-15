__source__ = 'https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/'
# Time:  O(m long n + n log m) m and nn are the height and width of the image
# Space: O(1)
#
# Description: Leetcode # 302. Smallest Rectangle Enclosing Black Pixels
#
# An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel.
# The black pixels are connected, i.e., there is only one black region.
# Pixels are connected horizontally and vertically.
# Given the location (x, y) of one of the black pixels,
# return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.
#
# For example, given the following image:
#
# [
#   "0010",
#   "0110",
#   "0100"
# ]
#
# and x = 0, y = 2,
# Return 6.
#
# Companies
# Google
# Related Topics
# Binary Search
#
import itertools
import unittest
# Time:  O(nlogn)
# Space: O(1)
class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        def binarySearch(left, right, find, image, has_one):
            while left <= right:  # O(logn) times
                mid = left + (right - left) / 2
                if find(image, has_one, mid):  # Time: O(n)
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        searchColumns = lambda image, has_one, mid: any([int(row[mid]) for row in image]) == has_one
        left = binarySearch(0, y - 1, searchColumns, image, True)
        right = binarySearch(y + 1, len(image[0]) - 1, searchColumns, image, False)

        searchRows = lambda image, has_one, mid: any(itertools.imap(int, image[mid])) == has_one
        top = binarySearch(0, x - 1, searchRows, image, True)
        bottom = binarySearch(x + 1, len(image) - 1, searchRows, image, False)

        return (right - left) * (bottom - top)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/solution/
# Approach #3 (Binary Search) [Accepted]
#
# 8ms 56.06%
class Solution {
    public int minArea(char[][] image, int x, int y) {
        int m = image.length, n = image[0].length;
        int left = searchColumns(image, 0, y, 0, m, true);
        int right = searchColumns(image, y + 1, n, 0, m, false);
        int top = searchRows(image, 0, x, left, right, true);
        int bottom = searchRows(image, x + 1, m, left, right, false);
        return (right - left) * (bottom - top);
    }
    private int searchColumns(char[][] image, int i, int j, int top, int bottom, boolean whiteToBlack) {
        while (i != j) {
            int k = top, mid = (i + j) / 2;
            while (k < bottom && image[k][mid] == '0') ++k;
            if (k < bottom == whiteToBlack) // k < bottom means the column mid has black pixel
                j = mid; //search the boundary in the smaller half
            else
                i = mid + 1; //search the boundary in the greater half
        }
        return i;
    }
    private int searchRows(char[][] image, int i, int j, int left, int right, boolean whiteToBlack) {
        while (i != j) {
            int k = left, mid = (i + j) / 2;
            while (k < right && image[mid][k] == '0') ++k;
            if (k < right == whiteToBlack) // k < right means the row mid has black pixel
                j = mid;
            else
                i = mid + 1;
        }
        return i;
    }
}

# 5ms 99.24%
class Solution {
    public int minArea(char[][] image, int x, int y) {
        int m = image.length;
        int n = m == 0 ? 0 : image[0].length;
        if (m == 0 || n == 0) {
            return 0;
        }
        int left = getIndex(image, 0, y, 0, m - 1, false, true);
        int right = getIndex(image, y, n - 1, 0, m - 1, false, false);
        int top = getIndex(image, 0, x, left, right, true, true);
        int bottom = getIndex(image, x, m - 1, left, right, true, false);
        return (right - left + 1) * (bottom - top + 1);
    }

    private int getIndex(char[][] image, int start, int end, int min, int max, boolean isRow, boolean isLow) {
        int result = isLow ? Integer.MAX_VALUE : 0;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (hasBlack(image, mid, isRow, min, max)) {
                if (isLow) {
                    result = Math.min(result, mid);
                    end = mid - 1;
                } else {
                    result = Math.max(result, mid);
                    start = mid + 1;
                }
            } else {
                if (isLow) {
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            }
        }
        return result;
    }

    private boolean hasBlack(char[][] image, int index, boolean isRow, int min, int max) {
        return isRow ? hasBlackRow(image, index, min, max) : hasBlackCol(image, index, min, max);
    }

    private boolean hasBlackRow(char[][] image, int index, int min, int max) {
        for (int j = min; j <= max; j++) {
            if (image[index][j] == '1') {
                return true;
            }
        }
        return false;
    }

    private boolean hasBlackCol(char[][] image, int index, int min, int max) {
        for (int i = min; i <= max; i++) {
            if (image[i][index] == '1') {
                return true;
            }
        }
        return false;
    }
}
'''
