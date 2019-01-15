__source__ = 'https://leetcode.com/problems/peak-index-in-a-mountain-array/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 852. Peak Index in a Mountain Array
#
# Let's call an array A a mountain if the following properties hold:
#
# A.length >= 3
# There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# Given an array that is definitely a mountain,
# return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].
#
# Example 1:
#
# Input: [0,1,0]
# Output: 1
# Example 2:
#
# Input: [0,2,1,0]
# Output: 1
# Note:
#
# 3 <= A.length <= 10000
# 0 <= A[i] <= 10^6
# A is a mountain, as defined above.
import unittest

# Approach 1: Linear Scan: O(N) time and space
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in xrange(len(A)):
            if A[i] > A[i + 1]:
                return i
# Approach 2: Binary Search
# Time Complexity: O(logN), where N is the length of A.
# Space Complexity: O(1)

class BinarySearchSolution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mid = lo + (hi - lo) / 2
            if A[mid] < A[mid + 1]:
                lo = mid + 1
            else :
                hi = mid
        return lo

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/peak-index-in-a-mountain-array/solution/
# Binary Search
# 1ms 100%
class Solution {
    public int peakIndexInMountainArray(int[] A) {
        int lo = 0, hi = A.length - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (A[mid] < A[mid + 1]) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}

# 1ms 100%
class Solution {
    public int peakIndexInMountainArray(int[] A) {
        return searchPeak(A,0,A.length - 1);
    }

    public int searchPeak(int[]A , int low, int high){
        if(low == high){
            return low;
        }
        int mid = (low + high)/2;
        if(A[mid] > A[mid + 1]){
            return searchPeak(A,low,mid);
        }
        return searchPeak(A,mid + 1, high);
    }
}

# 3ms 25.39%
class Solution {
    public int peakIndexInMountainArray(int[] A) {
        int i = 0;
        while (A[i] < A[i + 1]) i++;
        return i;
    }
}
'''