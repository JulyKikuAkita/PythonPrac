__source__ = 'https://leetcode.com/problems/maximal-rectangle/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/maximal-rectangle.py
# Time:  O(n^2)
# Space: O(n)
# DP
#
# Description: Leetcode # 85. Maximal Rectangle
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
#
# For example, given the following matrix:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Return 6.
#
# Companies
# Facebook
# Related Topics
# Array Hash Table Stack Dynamic Programming
# Similar Questions
# Largest Rectangle in Histogram Maximal Square
#
import unittest


class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        result = 0
        m = len(matrix)
        n = len(matrix[0])
        L = [0 for _ in xrange(n)]
        H = [0 for _ in xrange(n)]
        R = [0 for _ in xrange(n)]

        for i in xrange(m):
            left = 0
            for j in xrange(n):
                if matrix[i][j] == '1':
                    L[j] = max(L[j], left)
                    H[j] += 1
                else:
                    L[j] = 0
                    H[j] = 0
                    R[j] = n
                    left = j + 1

            right = n
            for j in reversed(xrange(n)):
                if matrix[i][j] == '1':
                    R[j] = min(R[j], right)
                    result = max(result, H[j] * (R[j] - L[j]))
                else:
                    right = j
                    #print i, j, L, left, result, right

        print L
        print H
        print R
        return result


# http://www.cnblogs.com/zuoyuan/p/3784252.html
# http://jelices.blogspot.com/2014/05/leetcode-python-maximal-rectangle.html  diff solution create a temp matrix
class SolutionOther:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if matrix == []: return 0
        a = [0 for i in range(len(matrix[0]))]
        maxArea = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                a[j] = a[j] + 1 if matrix[i][j] == '1' else 0

            maxArea = max(maxArea, self.largestRectangleArea(a))

        return maxArea

    def largestRectangleArea(self, height):
        stack = []
        i = 0
        area = 0

        while i < len(height):
            if stack == [] or height[i] > height[stack[len(stack) - 1]]:
                stack.append(i)
            else:
                curr = stack.pop()
                width = i if stack == [] else i - stack[len(stack) - 1] - 1
                area = max(area, width * height[curr])
                i -= 1
            i += 1

        while stack != []:
            curr = stack.pop()
            width = i if stack == [] else len(height) - stack[len(stack) - 1] - 1
            area = max(area, width * height[curr])
        return area


#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        test = SolutionOther()
        matrix1 = ["1010", "1011", "1011", "1111"]
        matrix2 = ["1111", "1111", "1111", "1111"]
        print test.maximalRectangle(matrix2)

        matrix = ["11101",
                  "11010",
                  "01110",
                  "11110",
                  "11111",
                  "00000"]
        print Solution().maximalRectangle(matrix)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/contains-duplicate/solution/

A O(n^2) solution based on Largest Rectangle in Histogram
This question is similar as [Largest Rectangle in Histogram]:

You can maintain a row length of Integer array H recorded its height of '1's,
and scan and update row by row to find out the largest rectangle of each row.

For each row, if matrix[row][i] == '1'. H[i] +=1, or reset the H[i] to zero.
and according the algorithm of [Largest Rectangle in Histogram], to update the maximum area.

58% - 74%(if break when minHeight == 0)
# 69.04% 12ms
public class Solution {
    public int maximalRectangle(char[][] matrix) {
        int m = matrix.length;
        int n = m == 0 ? 0 : matrix[0].length;
        if (m == 0 || n == 0) {
            return 0;
        }
        int[] height = new int[n];
        int result = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == '1') {
                    height[j]++;
                } else {
                    height[j] = 0;
                }
            }
            for (int j = 0; j < n; j++) {
                if (j < n - 1 && height[j] <= height[j + 1]) {
                    continue;
                }
                int minHeight = height[j];
                for (int k = j; k >= 0; k--) {
                    minHeight = Math.min(minHeight, height[k]);
                    if (minHeight == 0) break; // become 74 %
                    result = Math.max(result, (j - k + 1) * minHeight);
                }
            }
        }
        return result;
    }
}

# 22.09% 35ms
public class Solution {
    public int maximalRectangle(char[][] matrix) {
        int m = matrix.length;
        int n = m == 0 ? 0 : matrix[0].length;
        if (m == 0 || n == 0) {
            return 0;
        }
        int result = 0;
        Stack<Integer> stack = new Stack<>();
        int[] height = new int[n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == '1') {
                    height[j]++;
                } else {
                    height[j] = 0;
                }
                while (!stack.isEmpty() && height[stack.peek()] > height[j]) {
                    int top = stack.pop();
                    result = Math.max(result, height[top] * (stack.isEmpty() ? j : j - stack.peek() - 1));
                }
                stack.push(j);
            }
            while (!stack.isEmpty()) {
                int top = stack.pop();
                result = Math.max(result, height[top] * (stack.isEmpty() ? n : n - stack.peek() - 1));
            }
        }
        return result;
    }
}

#dp
Thought:
The DP solution proceeds row by row, starting from the first row. Let the maximal rectangle area
at row i and column j be computed by [right(i,j) - left(i,j)]*height(i,j).

All the 3 variables left, right, and height can be determined by the information from previous row,
and also information from the current row. So it can be regarded as a DP solution.
The transition equations are:

left(i,j) = max(left(i-1,j), cur_left), cur_left can be determined from the current row
right(i,j) = min(right(i-1,j), cur_right), cur_right can be determined from the current row
height(i,j) = height(i-1,j) + 1, if matrix[i][j]=='1';
height(i,j) = 0, if matrix[i][j]=='0'

If you think this algorithm is not easy to understand, you can try this example:

0 0 0 1 0 0 0
0 0 1 1 1 0 0
0 1 1 1 1 1 0
The vector "left" and "right" from row 0 to row 2 are as follows

row 0:

l: 0 0 0 3 0 0 0
r: 7 7 7 4 7 7 7
row 1:

l: 0 0 2 3 2 0 0
r: 7 7 5 4 5 7 7
row 2:

l: 0 1 2 3 2 1 0
r: 7 6 5 4 5 6 7
The vector "left" is computing the left boundary.
Take (i,j)=(1,3) for example. On current row 1,
the left boundary is at j=2. However, because matrix[1][3] is 1,
you need to consider the left boundary on previous row as well, which is 3. So the real left boundary at (1,3) is 3.

I hope this additional explanation makes things clearer.

69.04% 12ms
public class Solution {
    public int maximalRectangle(char[][] matrix) {
        int m = matrix.length;
        int n = m == 0 ? 0 : matrix[0].length;
        if (m == 0 || n == 0) {
            return 0;
        }
        int[] height = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];
        for (int j = 0; j < n; j++) right[j] = n;
        int result = 0;
        for (int i = 0; i < m; i++) {
            int cur_left = 0, cur_right = n;

             // compute height (can do this from either side)
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == '1') height[j]++;
                else height[j] = 0;
            }

            // compute right (from right to left)
            for (int j = n-1; j>=0; j--) {
                if (matrix[i][j] == '1') right[j] = Math.min(right[j], cur_right);
                else {
                    right[j] = n;
                    cur_right = j;
                }
            }

            // compute left (from left to right)
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == '1') {
                    left[j] = Math.max(left[j], cur_left);
                } else {
                    left[j] = 0;
                    cur_left = j + 1;
                }
            }

            // compute the area of rectangle (can do this from either side)
            for (int j = 0; j < n; j++) {
                result = Math.max(result, (right[j] - left[j]) * height[j]);
            }
        }
        return result;
    }
}

# 99.69% 6ms
public class Solution {
    public int maximalRectangle(char[][] matrix) {
		/**
		 * idea: using [LC84 Largest Rectangle in Histogram]. For each row
		 * of the matrix, construct the histogram based on the current row
		 * and the previous histogram (up to the previous row), then compute
		 * the largest rectangle area using LC84.
		 */
		int m = matrix.length, n;
		if (m == 0 || (n = matrix[0].length) == 0)
			return 0;

		int i, j, res = 0;
		int[] heights = new int[n];
		for (i = 0; i < m; i++) {
			for (j = 0; j < n; j++) {
				if (matrix[i][j] == '0')
					heights[j] = 0;
				else
					heights[j] += 1;
			}
			res = Math.max(res, largestRectangleArea(heights));
		}

		return res;
	}

	public int largestRectangleArea(int[] heights) {
		/**
		 * idea: scan and store if a[i-1]<=a[i] (increasing), then as long
		 * as a[i]<a[i-1], then we can compute the largest rectangle area
		 * with base a[j], for j<=i-1, and a[j]>a[i], which is a[j]*(i-j).
		 * And meanwhile, all these bars (a[j]'s) are already done, and thus
		 * are throwable (using pop() with a stack).
		 *
		 * We can use an array nLeftGeq[] of size n to simulate a stack.
		 * nLeftGeq[i] = the number of elements to the left of [i] having
		 * value greater than or equal to a[i] (including a[i] itself). It
		 * is also the index difference between [i] and the next index on
		 * the top of the stack.
		 */
		int n = heights.length;
		if (n == 0)
			return 0;

		int[] nLeftGeq = new int[n]; // the number of elements to the left
										// of [i] with value >= heights[i]
		nLeftGeq[0] = 1;

		// preIdx=the index of stack.peek(), res=max area so far
		int preIdx = 0, res = 0;

		for (int i = 1; i < n; i++) {
			nLeftGeq[i] = 1;

			// notice that preIdx = i - 1 = peek()
			while (preIdx >= 0 && heights[i] < heights[preIdx]) {
				res = Math.max(res, heights[preIdx] * (nLeftGeq[preIdx] + i - preIdx - 1));
				nLeftGeq[i] += nLeftGeq[preIdx]; // pop()

				preIdx = preIdx - nLeftGeq[preIdx]; // peek() current top
			}

			if (preIdx >= 0 && heights[i] == heights[preIdx])
				nLeftGeq[i] += nLeftGeq[preIdx]; // pop()
			// otherwise nothing to do

			preIdx = i;
		}

		// compute the rest largest rectangle areas with (indices of) bases
		// on stack
		while (preIdx >= 0 && 0 < heights[preIdx]) {
			res = Math.max(res, heights[preIdx] * (nLeftGeq[preIdx] + n - preIdx - 1));
			preIdx = preIdx - nLeftGeq[preIdx]; // peek() current top
		}

		return res;
	}
}
'''