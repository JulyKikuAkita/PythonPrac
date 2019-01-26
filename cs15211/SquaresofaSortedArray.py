__source__ = 'https://leetcode.com/problems/squares-of-a-sorted-array/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 977. Squares of a Sorted Array
#
# Given an array of integers A sorted in non-decreasing order,
# return an array of the squares of each number, also in sorted non-decreasing order.
#
# Example 1:
#
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Example 2:
#
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
#
# Note:
#
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A is sorted in non-decreasing order.
#
import unittest

# 192ms 100%
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted(x*x for x in A)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/squares-of-a-sorted-array/solution/
Approach 1: Sort
Complexity Analysis
Time Complexity: O(N logN), where N is the length of A.
Space Complexity: O(N). 

# 9ms 100% 
class Solution {
    public int[] sortedSquares(int[] A) {
        int N = A.length;
        int[] ans = new int[N];
        for (int i = 0; i < N; ++i)
            ans[i] = A[i] * A[i];

        Arrays.sort(ans);
        return ans;
    }
}

# Approach 2: Two Pointer
# Complexity Analysis
# Time Complexity: O(N), where N is the length of A.
# Space Complexity: O(N) 
# 8ms 100%
class Solution {
    public int[] sortedSquares(int[] A) {
        int N = A.length;
        int j = 0;
        while (j < N && A[j] < 0)
            j++;
        int i = j-1;

        int[] ans = new int[N];
        int t = 0;

        while (i >= 0 && j < N) {
            if (A[i] * A[i] < A[j] * A[j]) {
                ans[t++] = A[i] * A[i];
                i--;
            } else {
                ans[t++] = A[j] * A[j];
                j++;
            }
        }

        while (i >= 0) {
            ans[t++] = A[i] * A[i];
            i--;
        }
        while (j < N) {
            ans[t++] = A[j] * A[j];
            j++;
        }

        return ans;
    }
}

# 2 pointers
# 8ms 100%
class Solution {
    public int[] sortedSquares(int[] A) {
        int i = 0, j = A.length - 1;
        int[] res = new int[A.length];
        int index = A.length - 1;
        while (i <= j ) {
            if (A[i] * A[i] > A[j] * A[j]) {
                res[index--] = A[i] * A[i];
                i++;
            } else if (A[i] * A[i] < A[j] * A[j]) {
                res[index--] = A[j] * A[j];
                j--;
            } else {
                if (i != j) {
                    res[index--] = A[i] * A[i];
                    res[index--] = A[j] * A[j];
                    i++;
                    j--;
                } else {
                    res[index--] = A[i] * A[j];
                    i++;
                    j--;
                }
            }
        }
        return res;
    }
}
'''
