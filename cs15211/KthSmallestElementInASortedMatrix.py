__source__ = 'https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/kth-smallest-element-in-a-sorted-matrix.py
# Time:  O(k * log(min(n, m, k))), with n x m matrix
# Space: O(min(n, m, k))
#
# Description: Leetcode # 378. Kth Smallest Element in a Sorted Matrix
#
# Given a n x n matrix where each of the rows and
# columns are sorted in ascending order,
# find the kth smallest element in the matrix.
#
# Note that it is the kth smallest element in the sorted order,
# not the kth distinct element.
#
# Example:
#
# matrix = [
#   [ 1,  5,  9],
#   [10, 11, 13],
#   [12, 13, 15]
# ],
# k = 8,
#
# return 13.
# Note:
# You may assume k is always valid, 1 <= k <= n^2.
#
# Companies
# Google Twitter
# Related Topics
# Binary Search Heap
# Similar Questions
# Find K Pairs with Smallest Sums Kth Smallest Number in Multiplication Table
#

import unittest
from heapq import heappush, heappop
# 136ms 27.62%
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        kth_smallest = 0
        min_heap = []

        def push(i, j):
            if len(matrix) > len(matrix[0]):
                if i < len(matrix[0]) and j < len(matrix):
                    heappush(min_heap, [matrix[j][i], i, j])
            else:
                if i < len(matrix) and j < len(matrix[0]):
                    heappush(min_heap, [matrix[i][j], i, j])

        push(0, 0)
        while min_heap and k > 0:
            kth_smallest, i, j = heappop(min_heap)
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
            k -= 1

        return kth_smallest

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
#
# https://discuss.leetcode.com/topic/52948/share-my-thoughts-and-clean-java-code
Solution 1 : Heap
Here is the step of my solution:

Build a minHeap of elements from the first row.
Do the following operations k-1 times :
Every time when you poll out the root(Top Element in Heap),
you need to know the row number and column number of that element(so we can create a tuple class here),
replace that root with the next element from the same column.
After you finish this problem, thinks more :

For this question, you can also build a min Heap from the first column, and do the similar operations as above.
(Replace the root with the next element from the same row)
What is more, this problem is exact the same with Leetcode373 Find K Pairs with Smallest Sums,
I use the same code which beats 96.42%, after you solve this problem, you can check with this link:
https://discuss.leetcode.com/topic/52953/share-my-solution-which-beat-96-42

# 24ms 41.99%
class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        PriorityQueue<Tuple> pq = new PriorityQueue<Tuple>();
        for (int j = 0; j <= n - 1; j++) {
            pq.offer(new Tuple(0, j, matrix[0][j]));
        }

        for (int i = 0; i < k - 1; i++) {
            Tuple t = pq.poll();
            if (t.x == n - 1) continue;
            pq.offer(new Tuple(t.x+1, t.y, matrix[t.x+1][t.y]));
        }
        return pq.poll().val;
    }

    class Tuple implements Comparable<Tuple> {
        int x, y, val;
        public Tuple(int x, int y, int val) {
            this.x = x;
            this.y = y;
            this.val = val;
        }

        @Override
        public int compareTo(Tuple that) {
            return this.val - that.val; //minHeap
        }
    }
}



Solution 2 : Binary Search
We are done here, but let's think about this problem in another way:
The key point for any binary search is to figure out the "Search Space".
For me, I think there are two kind of "Search Space" --
index and range(the range from the smallest number to the biggest number).
Most usually, when the array is sorted in one direction,
we can use index as "search space",
when the array is unsorted and we are going to find a specific number, we can use "range".

Let me give you two examples of these two "search space"

index -- A bunch of examples -- https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
( the array is sorted)
range -- https://leetcode.com/problems/find-the-duplicate-number/ (Unsorted Array)
The reason why we did not use index as "search space"
for this problem is the matrix is sorted in two directions,
 we can not find a linear way to map the number and its index.

# 1ms 85.42%
class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int lo = matrix[0][0], hi = matrix[matrix.length - 1][matrix[0].length - 1] + 1;//[lo, hi)
        while(lo < hi) {
            int mid = lo + (hi - lo) / 2;
            int count = 0,  j = matrix[0].length - 1;
            for(int i = 0; i < matrix.length; i++) {
                while(j >= 0 && matrix[i][j] > mid) j--;
                count += (j + 1);
            }
            if(count < k) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}

# 0ms 100%
class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int m = matrix.length;
        int n = matrix[0].length;

        int lower = matrix[0][0];
        int upper = matrix[m-1][n-1];

        while (lower < upper) {
            int mid = lower + (upper - lower) / 2;
            int count = count(matrix, mid);
            if (count < k) {
                lower = mid + 1;
            } else {
                upper = mid;
            }
        }
        return upper;
    }

    public int count(int[][] matrix, int target) {
        int count = 0;
        int j = matrix[0].length - 1;
        for (int i = 0; i < matrix.length; i++) {
            while(j >= 0 && matrix[i][j] > target) j--;
            count += (j + 1);
        }
        return count;
    }
}
'''