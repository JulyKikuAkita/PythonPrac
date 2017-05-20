__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/maximal-rectangle.py
# Time:  O(n^2)
# Space: O(n)
# DP
#
# Given a 2D binary matrix filled with 0's and 1's,
# find the largest rectangle containing all ones and return its area.
# Facebook
# Array Hash Table Stack Dynamic Programming

class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        result = 0
        m = len(matrix)
        n = len(matrix[0])
        L = [ 0 for _ in xrange(n)]
        H = [ 0 for _ in xrange(n)]
        R = [ 0 for _ in xrange(n)]

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
        a = [ 0 for i in range(len(matrix[0]))]
        maxArea = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                a[j] = a[j]+1 if matrix[i][j] == '1' else 0

            maxArea = max(maxArea, self.largestRectangleArea(a))

        return maxArea

    def largestRectangleArea(self, height):
        stack = []
        i = 0
        area = 0

        while i < len(height):
            if stack == [] or height[i] > height[stack[len(stack)-1]]:
                stack.append(i)
            else:
                curr = stack.pop()
                width = i if stack ==[] else i - stack[len(stack)-1] - 1
                area = max(area, width*height[curr])
                i -= 1
            i += 1

        while stack != []:
            curr = stack.pop()
            width = i if stack ==[] else len(height) - stack[len(stack) - 1] -1
            area = max(area, width*height[curr])
        return area

#test
test = SolutionOther()
matrix1 = ["1010","1011","1011","1111"]
matrix2 = ["1111","1111","1111","1111"]
print test.maximalRectangle(matrix2)

if __name__ == "__main__":
    matrix = ["11101",
              "11010",
              "01110",
              "11110",
              "11111",
              "00000"]
    print Solution().maximalRectangle(matrix)

#java
js = '''
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
                    result = Math.max(result, (j - k + 1) * minHeight);
                }
            }
        }
        return result;
    }
}

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

public class Solution {
    public int maximalRectangle(char[][] matrix) {
        int m = matrix.length;
        int n = m == 0 ? 0 : matrix[0].length;

        int[][] dp = new int[m][n + 1];

        for (int i = 0 ; i < m ; i++) {
            for ( int j = 0; j < n; j++) {
                if (matrix[i][j] == '0') {
                    dp[i][j] = 0;
                }else if(i == 0) {
                    dp[i][j] = 1;
                }else{
                    dp[i][j] = dp[i-1][j] + 1;
                }
            }
            dp[i][n] = 0;
        }

        int maxArea = 0;
        for (int i = 0; i < m ;i++) {
            maxArea = Math.max(maxArea, dfs(dp[i]));
        }
        return maxArea;
    }

    private int dfs(int[] input) {
        int maxArea = 0;
        Stack<Integer> stack = new Stack<Integer>();

        for (int i = 0; i < input.length ; i++) {
            if (stack.isEmpty() || input[stack.peek()] <= input[i]) {
                stack.push(i);
            }else{
                int h = input[stack.pop()];
                int curArea = h * (stack.isEmpty() ? i : i - stack.peek() - 1);
                maxArea = Math.max( maxArea, curArea);
                i--;
            }
        }
        return maxArea;
    }
}
'''