__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/max-sum-of-sub-matrix-no-larger-than-k.py
# Time:  O(min(m, n)^2 * max(m, n) * log(max(m, n)))
# Space: O(max(m, n))

# Given a non-empty 2D matrix matrix and an integer k,
# find the max sum of a rectangle in the matrix such that its sum is no larger than k.
#
# Example:
# Given matrix = [
#   [1,  0, 1],
#   [0, -2, 3]
# ]
# k = 2
# The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]]
# is 2 and 2 is the max number no larger than k (k = 2).
#
# Note:
# The rectangle inside the matrix must have an area > 0.
# What if the number of rows is much larger than the number of columns?

# Time:  O(min(m, n)^2 * max(m, n)^2)
# Space: O(max(m, n))

# Given a non-empty 2D matrix matrix and an integer k,
# find the max sum of a rectangle in the matrix such that its sum is no larger than k.
#
# Example:
# Given matrix = [
#   [1,  0, 1],
#   [0, -2, 3]
# ]
# k = 2
# The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]]
# is 2 and 2 is the max number no larger than k (k = 2).
#
# Note:
# The rectangle inside the matrix must have an area > 0.
# What if the number of rows is much larger than the number of columns?
#  Google
# Hide Tags Binary Search Dynamic Programming Queue


# Time:  O(min(m, n)^2 * max(m, n)^2)
# Space: O(max(m, n))
from bisect import bisect_left, insort

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return 0

        m = min(len(matrix), len(matrix[0]))
        n = max(len(matrix), len(matrix[0]))
        result = float("-inf")

        for i in xrange(m):
            sums = [0] * n
            for j in xrange(i, m):
                for l in xrange(n):
                    sums[l] += matrix[j][l] if m == len(matrix) else matrix[l][j]

                # Find the max subarray no more than K.
                accu_sum_set, accu_sum = [0], 0
                for sum in sums:
                    accu_sum += sum
                    it = bisect_left(accu_sum_set, accu_sum - k)  # Time: O(logn)
                    if it != len(accu_sum_set):
                        result = max(result, accu_sum - accu_sum_set[it])
                    insort(accu_sum_set, accu_sum)  # Time: O(n)

        return result


# Time:  O(min(m, n)^2 * max(m, n) * log(max(m, n))) ~ O(min(m, n)^2 * max(m, n)^2)
# Space: O(max(m, n))
class Solution_TLE(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        class BST(object):  # not avl, rbtree
            def __init__(self, val):
                self.val = val
                self.left = None
                self.right = None

            def insert(self, val):  # Time: O(h) = O(logn) ~ O(n)
                curr = self
                while curr:
                    if curr.val >= val:
                        if curr.left:
                            curr = curr.left
                        else:
                            curr.left = BST(val)
                            return
                    else:
                        if curr.right:
                            curr = curr.right
                        else:
                            curr.right = BST(val)
                            return

            def lower_bound(self, val):  # Time: O(h) = O(logn) ~ O(n)
                result, curr = None, self
                while curr:
                    if curr.val >= val:
                        result, curr = curr, curr.left
                    else:
                        curr = curr.right
                return result


        if not matrix:
            return 0

        m = min(len(matrix), len(matrix[0]))
        n = max(len(matrix), len(matrix[0]))
        result = float("-inf")

        for i in xrange(m):
            sums = [0] * n
            for j in xrange(i, m):
                for l in xrange(n):
                    sums[l] += matrix[j][l] if m == len(matrix) else matrix[l][j]

                # Find the max subarray no more than K.
                accu_sum_set = BST(0)
                accu_sum = 0
                for sum in sums:
                    accu_sum += sum
                    node = accu_sum_set.lower_bound(accu_sum - k);
                    if node:
                        result = max(result, accu_sum - node.val)
                    accu_sum_set.insert(accu_sum)

        return result

#java
js = '''
public class Solution {
    public int maxSumSubmatrix(int[][] matrix, int k) {
        int m = matrix.length;
        int n = m == 0 ? 0 : matrix[0].length;
        int result = Integer.MIN_VALUE;
        int[][] sums = getSums(matrix, m, n);
        int rows = Math.min(m, n);
        int cols = Math.max(m, n);

        for (int i = 0; i < rows; i++) {
            for (int j = i + 1; j <= rows; j++) {
                SortedSet<Integer> set = new TreeSet<>();
                set.add(0);
                for (int l = 1; l <= cols; l++) {
                    int cur = m <= n ? sums[j][l] - sums[i][l] : sums[l][j] - sums[l][i];
                    SortedSet<Integer> tailSet = set.tailSet(cur - k);
                    if (!tailSet.isEmpty()) {
                        result = Math.max(result, cur - tailSet.first());
                    }
                    set.add(cur);
                }
            }
        }
        return result;
    }

    private int[][] getSums(int[][] matrix, int m, int n) {
        int[][] sums = new int[m + 1][n + 1];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                sums[i + 1][j + 1] = sums[i + 1][j] + sums[i][j + 1] - sums[i][j] + matrix[i][j];
            }
        }
        return sums;
    }
}
'''