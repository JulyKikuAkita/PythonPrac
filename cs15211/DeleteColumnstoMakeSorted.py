__source__ = 'https://leetcode.com/problems/delete-columns-to-make-sorted/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 944. Delete Columns to Make Sorted
#
# We are given an array A of N lowercase letter strings, all of the same length.
#
# Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.
# The remaining rows of strings form columns when read north to south.
#
# For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3},
# then the final array after deletions is ["bef","vyz"],
# and the remaining columns of A are ["b","v"], ["e","y"], and ["f","z"].
# (Formally, the c-th column is [A[0][c], A[1][c], ..., A[A.length-1][c]].)
#
# Suppose we chose a set of deletion indices D such that after deletions,
# each remaining column in A is in non-decreasing sorted order.
#
# Return the minimum possible value of D.length.
#
#
#
# Example 1:
#
# Input: ["cba","daf","ghi"]
# Output: 1
# Explanation:
# After choosing D = {1}, each column ["c","d","g"] and ["a","f","i"] are in non-decreasing sorted order.
# If we chose D = {}, then a column ["b","a","h"] would not be in non-decreasing sorted order.
# Example 2:
#
# Input: ["a","b"]
# Output: 0
# Explanation: D = {}
# Example 3:
#
# Input: ["zyx","wvu","tsr"]
# Output: 3
# Explanation: D = {0, 1, 2}
#
#
# Note:
#
# 1 <= A.length <= 100
# 1 <= A[i].length <= 1000
# Accepted
#
import unittest

#80ms 99.68%
class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        return sum(list(col) != sorted(col) for col in zip(*A))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/delete-columns-to-make-sorted/solution/

Approach 1: Greedy
Complexity Analysis
Time Complexity: O(A), where A is the total content of A.
Space Complexity: O(1)

# 16ms 87.23%
class Solution {
    public int minDeletionSize(String[] A) {
        int ans = 0;
        for (int c = 0; c < A[0].length(); ++c) {
           for (int r = 0; r < A.length - 1; r++) {
               if (A[r].charAt(c) > A[r + 1].charAt(c)) {
                   ans++;
                   break;
               }
           }
        }
        return ans;
    }
}

# 6ms 99.64%
class Solution {
    public int minDeletionSize(String[] A) {
        int res = 0;
        if (A.length <= 1) return res;
        for (int i = 0; i < A[0].length(); i++) {
            if (!isValid(A, i)) res++;
        }

        return res;
    }

    public boolean isValid(String[] strs, int k) {
        for (int i = 1; i < strs.length; i++) {
            if (strs[i].charAt(k) < strs[i - 1].charAt(k)) return false;
        }
        return true;
    }
}

'''