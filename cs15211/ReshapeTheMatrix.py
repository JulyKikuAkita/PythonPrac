__author__ = 'July'
#In MATLAB, there is a very useful function called 'reshape',
# which can reshape a matrix into a new one with different size but keep its original data.
#
# You're given a matrix represented by a two-dimensional array,
# and two positive integers r and c representing the row number
# and column number of the wanted reshaped matrix, respectively.
#
# The reshaped matrix need to be filled with all the elements of
# the original matrix in the same row-traversing order as they were.
#
# If the 'reshape' operation with given parameters is possible and legal,
# output the new reshaped matrix; Otherwise, output the original matrix.
#
# Example 1:
# Input:
# nums =
# [[1,2],
#  [3,4]]
# r = 1, c = 4
# Output:
# [[1,2,3,4]]
# Explanation:
# The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
# Example 2:
# Input:
# nums =
# [[1,2],
#  [3,4]]
# r = 2, c = 4
# Output:
# [[1,2],
#  [3,4]]
# Explanation:
# There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
# Note:
# The height and width of the given matrix is in range [1, 100].
# The given r and c are all positive.
# Hide Company Tags Mathworks
# Hide Tags Array
#

#Solution 1 - NumPy
#
# When I read "MATLAB", I immediately thought "NumPy". Thanks to @fallcreek for tolist,
# makes converting the result to the correct type easier than what I had originally.

import numpy as np

class Solution(object):
    def matrixReshape1(self, nums, r, c):
        try:
            return np.reshape(nums, (r, c)).tolist()
        except:
            return nums
# Solution 2 - Oneliner
    def matrixReshape2(self, nums, r, c):
        return nums if len(sum(nums, [])) != r * c else map(list, zip(*([iter(sum(nums, []))]*c)))

# A more readable version of that:
    def matrixReshape3(self, nums, r, c):
        flat = sum(nums, [])
        if len(flat) != r * c:
            return nums
        tuples = zip(*([iter(flat)] * c))
        return map(list, tuples)

# Solution 3 - itertools
    def matrixReshape4(self, nums, r, c):
        if r * c != len(nums) * len(nums[0]):
            return nums
        it = itertools.chain(*nums)
        return [list(itertools.islice(it, c)) for _ in xrange(r)]

java = '''
We can use matrix[index / width][index % width] for both the input and the output matrix.
public class Solution {
    public int[][] matrixReshape(int[][] nums, int r, int c) {
        int m = nums.length, n = nums[0].length;
        if ( m * n != r * c) return nums;
        int[][] res = new int[r][c];
        for (int i = 0; i < r * c ; i++) {
            res[ i / c][ i % c] = nums[i / n][i % n];
        }
        return res;
    }
}


'''