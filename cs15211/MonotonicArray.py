__source__ = 'https://leetcode.com/problems/monotonic-array/description/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 896. Monotonic Array
# An array is monotonic if it is either monotone increasing or monotone decreasing.
#
# An array A is monotone increasing if for all i <= j, A[i] <= A[j].
# An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
#
# Return true if and only if the given array A is monotonic.
#
#
#
# Example 1:
#
# Input: [1,2,2,3]
# Output: true
# Example 2:
#
# Input: [6,5,4,4]
# Output: true
# Example 3:
#
# Input: [1,3,2]
# Output: false
# Example 4:
#
# Input: [1,2,4,5]
# Output: true
# Example 5:
#
# Input: [1,1,1]
# Output: true
#
#
# Note:
#
# 1 <= A.length <= 50000
# -100000 <= A[i] <= 100000
#
import unittest


class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/monotonic-array/solution/
# one pass 13ms 100%
#
class Solution {
    public boolean isMonotonic(int[] A) {
        boolean increasing = true;
        boolean decreasing = true;
        for (int i = 0; i < A.length - 1; i++) {
            if (A[i] > A[i+1]) increasing = false;
            if (A[i] < A[i+1]) decreasing = false;
        }
        return increasing || decreasing;
    }
}

#two pass
class Solution {
    public boolean isMonotonic(int[] A) {
        boolean isMonotonic = true;
        // increasing
        for(int i = 1; i < A.length; i++) {
            if (A[i - 1] > A[i]) {
                isMonotonic = false;
                break;
            }
        }
        if (isMonotonic) {
            return true;
        }

        // decreasing
        for(int i = 1; i < A.length; i++) {
            if (A[i - 1] < A[i]) {
                isMonotonic = false;
                break;
            }
            if (i == A.length - 1) {
                isMonotonic = true;
            }
        }

        return isMonotonic;
    }
}
'''