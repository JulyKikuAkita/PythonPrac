__source__ = 'https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/max-sum-of-sub-matrix-no-larger-than-k.py
# Time:  O(min(m, n)^2 * max(m, n) * log(max(m, n)))
# Space: O(max(m, n))
#
# Description: Leetcode # 363. Max Sum of Rectangle No Larger Than K

#
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
#
# Companies
# Google
# Related Topics
# Binary Search Dynamic Programming Queue
#

# Time:  O(min(m, n)^2 * max(m, n)^2)
# Space: O(max(m, n))
from bisect import bisect_left, insort
import unittest
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

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().containsDuplicate([12344555,12344555])

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
The naive solution is brute-force, which is O((mn)^2). In order to be more efficient,
I tried something similar to Kadane's algorithm. The only difference is that here we have upper bound restriction K.
Here's the easily understanding video link for the problem "find the max sum rectangle in 2D array":
https://www.youtube.com/watch?v=yCQN096CwWM
Maximum Sum Rectangular Submatrix in Matrix dynamic programming/2D kadane (Trust me, it's really easy and straightforward).

#39.81% 251ms
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

#56.38% 163ms
public class Solution {
    /* first  consider the situation matrix is 1D
    we can save every sum of 0~i(0<=i<len) and binary search previous sum to find
    possible result for every index, time complexity is O(NlogN).
    so in 2D matrix, we can sum up all values from row i to row j and create a 1D array
    to use 1D array solution.
    If col number is less than row number, we can sum up all values from col i to col j
    then use 1D array solution.
    */
    public int maxSumSubmatrix(int[][] matrix, int target) {
        int row = matrix.length;
        if(row==0)return 0;
        int col = matrix[0].length;
        int m = Math.min(row,col);
        int n = Math.max(row,col);
        //indicating sum up in every row or every column
        boolean colIsBig = col>row;
        int res = Integer.MIN_VALUE;
        for(int i = 0;i<m;i++){
            int[] array = new int[n];
            // sum from row j to row i
            for(int j = i;j>=0;j--){
                int val = 0;
                TreeSet<Integer> set = new TreeSet<Integer>();
                set.add(0);
                //traverse every column/row and sum up
                for(int k = 0;k<n;k++){
                    array[k]=array[k]+(colIsBig?matrix[j][k]:matrix[k][j]);
                    val = val + array[k];
                    //use  TreeMap to binary search previous sum to get possible result
                    Integer subres = set.ceiling(val-target);
                    if(null!=subres){
                        res=Math.max(res,val-subres);
                    }
                    set.add(val);
                }
            }
        }
        return res;
    }
}

#96.59% 104ms
public class Solution {
    public int maxSumSubmatrix(int[][] matrix, int k) {
        int m = matrix.length, n = matrix[0].length, ans = Integer.MIN_VALUE;
        long[] sum = new long[m+1]; // stores sum of rect[0..p][i..j]
        for (int i = 0; i < n; ++i) {
            long[] sumInRow = new long[m];
            for (int j = i; j < n; ++j) { // for each rect[*][i..j]
                for (int p = 0; p < m; ++p) {
                    sumInRow[p] += matrix[p][j];
                    sum[p+1] = sum[p] + sumInRow[p];
                }
                ans = Math.max(ans, mergeSort(sum, 0, m+1, k));
                if (ans == k) return k;
            }
        }
        return ans;
    }
    int mergeSort(long[] sum, int start, int end, int k) {
        if (end == start+1) return Integer.MIN_VALUE; // need at least 2 to proceed
        int mid = start + (end - start)/2, cnt = 0;
        int ans = mergeSort(sum, start, mid, k);
        if (ans == k) return k;
        ans = Math.max(ans, mergeSort(sum, mid, end, k));
        if (ans == k) return k;
        long[] cache = new long[end-start];
        for (int i = start, j = mid, p = mid; i < mid; ++i) {
            while (j < end && sum[j] - sum[i] <= k) ++j;
            if (j-1 >= mid) {
                ans = Math.max(ans, (int)(sum[j-1] - sum[i]));
                if (ans == k) return k;
            }
            while (p < end && sum[p] < sum[i]) cache[cnt++] = sum[p++];
            cache[cnt++] = sum[i];
        }
        System.arraycopy(cache, 0, sum, start, cnt);
        return ans;
    }
}

#100% 31ms
class Solution {
    public int maxSumSubmatrix(int[][] matrix, int k) {
        if(matrix.length == 0) return 0;
        int m = matrix.length;
        int n = matrix[0].length;
        int result = Integer.MIN_VALUE;
        for(int left = 0; left < n; left ++){
             int[] sums = new int[m];
            for(int right = left; right < n; right ++){
                int sum = 0, maxSum = Integer.MIN_VALUE;
                for(int i = 0; i < m; i++){
                    sums[i] += matrix[i][right];
                    sum = Math.max(sum + sums[i], sums[i]);
                    maxSum = Math.max(maxSum, sum);
                }
                if(maxSum <= k){
                    result = Math.max(result, maxSum);
                    continue;
                }
                TreeSet<Integer> set = new TreeSet<>();
                set.add(0); //this is for one dimensional first element equals to K: [3, 2] k = 3;
                int curSum = 0;
                for(int s: sums) {
                    curSum += s;
                    Integer c = set.ceiling(curSum - k);
                    if(c != null) result = Math.max(result, curSum - c);
                    set.add(curSum);
                }


            }
        }
        return result;

    }
}
'''