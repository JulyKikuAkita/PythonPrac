__source__ = 'https://leetcode.com/problems/partition-array-into-disjoint-intervals/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 915. Partition Array into Disjoint Intervals
#
# Given an array A, partition it into two (contiguous) subarrays left and right so that:
#
# Every element in left is less than or equal to every element in right.
# left and right are non-empty.
# left has the smallest possible size.
# Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.
#
# Example 1:
#
# Input: [5,0,3,8,6]
# Output: 3
# Explanation: left = [5,0,3], right = [8,6]
# Example 2:
#
# Input: [1,1,1,0,6,12]
# Output: 4
# Explanation: left = [1,1,1,0], right = [6,12]
#
#
# Note:
#
# 2 <= A.length <= 30000
# 0 <= A[i] <= 10^6
# It is guaranteed there is at least one way to partition A as described.
#
import unittest

# 60ms 58.74%
class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        maxleft = [None] * N
        minright = [None] * N

        m = A[0]
        for i in xrange(N):
            m = max(m, A[i])
            maxleft[i] = m

        m = A[-1]
        for i in xrange(N-1, -1, -1):
            m = min(m, A[i])
            minright[i] = m

        for i in xrange(1, N):
            if maxleft[i-1] <= minright[i]:
                return i

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/partition-array-into-disjoint-intervals/solution/
Approach 1: Next Array
Complexity Analysis
Time Complexity: O(N), where N is the length of A.
Space Complexity: O(N)=.

# 8ms 27.96%
class Solution {
    public int partitionDisjoint(int[] A) {
        int N = A.length;
        int[] maxleft = new int[N];
        int[] minright = new int[N];

        int m = A[0];
        for (int i = 0; i < N; ++i) {
            m = Math.max(m, A[i]);
            maxleft[i] = m;
        }

        m = A[N-1];
        for (int i = N-1; i >= 0; --i) {
            m = Math.min(m, A[i]);
            minright[i] = m;
        }

        for (int i = 1; i < N; ++i)
            if (maxleft[i-1] <= minright[i])
                return i;

        throw null;
    }
}

# 4ms 98.41%
class Solution {
    public int partitionDisjoint(int[] A) {
        int lastMax = A[0];
        int max = lastMax;
        int split = 0;

        for(int i = 0;i < A.length;i++){
            if(A[i] < max){
                split = i;
                max = lastMax ;
            } else if (A[i] > lastMax){
                lastMax = A[i];
            }
        }
        return split + 1;
    }
}
'''