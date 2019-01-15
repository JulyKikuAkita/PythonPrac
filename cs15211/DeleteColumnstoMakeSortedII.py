__source__ = 'https://leetcode.com/problems/delete-columns-to-make-sorted-ii/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 955. Delete Columns to Make Sorted II
#
# We are given an array A of N lowercase letter strings, all of the same length.
#
# Now, we may choose any set of deletion indices, and for each string,
# we delete all the characters in those indices.
#
# For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3},
# then the final array after deletions is ["bef","vyz"].
#
# Suppose we chose a set of deletion indices D such that after deletions,
# the final array has its elements in lexicographic order (A[0] <= A[1] <= A[2] ... <= A[A.length - 1]).
#
# Return the minimum possible value of D.length.
#
#
#
# Example 1:
#
# Input: ["ca","bb","ac"]
# Output: 1
# Explanation:
# After deleting the first column, A = ["a", "b", "c"].
# Now A is in lexicographic order (ie. A[0] <= A[1] <= A[2]).
# We require at least 1 deletion since initially A was not in lexicographic order, so the answer is 1.
# Example 2:
#
# Input: ["xc","yb","za"]
# Output: 0
# Explanation:
# A is already in lexicographic order, so we don't need to delete anything.
# Note that the rows of A are not necessarily in lexicographic order:
# ie. it is NOT necessarily true that (A[0][0] <= A[0][1] <= ...)
# Example 3:
#
# Input: ["zyx","wvu","tsr"]
# Output: 3
# Explanation:
# We have to delete every column.
#
#
# Note:
#
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
#
import unittest

# 72ms 33.33%
class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def is_sorted(A):
            return all(A[i] <= A[i+1] for i in xrange(len(A) - 1))

        ans = 0
        # cur : all rows we have written
        # For example, with A = ["abc","def","ghi"] we might have
        # cur = ["ab", "de", "gh"].
        cur = [""] * len(A)

        for col in zip(*A):
            # cur2 : What we potentially can write, including the
            #        newest column 'col'.
            # Eg. if cur = ["ab","de","gh"] and col = ("c","f","i"),
            # then cur2 = ["abc","def","ghi"].
            cur2 = cur[:]
            for i, letter in enumerate(col):
                cur2[i] = cur2[i] + letter

            if is_sorted(cur2):
                cur = cur2
            else:
                ans += 1
        return ans

# 32ms 100%
class Solution2(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        # cuts[i] is True : we don't need to check col[i] <= col[i+1]
        cuts = [False] * (len(A) - 1)

        ans = 0
        for col in zip(*A):
            if all(cuts[i] or col[i] <= col[i+1] for i in xrange(len(col) - 1)):
                for i in xrange(len(col) - 1):
                    if col[i] < col[i+1]:
                        cuts[i] = True
            else:
                ans += 1
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/delete-columns-to-make-sorted-ii/solution/
Approach 1: Greedy
Complexity Analysis
Time Complexity: O(NW^2), where N is the length of A, and WW is the length of A[i].
Space Complexity: O(NW)

# 15ms 50%
class Solution {
    public int minDeletionSize(String[] A) {
        int N = A.length;
        int W = A[0].length();
        int ans = 0;

        // cur : all rows we have written
        // For example, with A = ["abc","def","ghi"] we might have
        // cur = ["ab", "de", "gh"].
        String[] cur = new String[N];
        for (int j = 0; j < W; ++j) {
            // cur2 : What we potentially can write, including the
            //        newest column col = [A[i][j] for i]
            // Eg. if cur = ["ab","de","gh"] and col = ("c","f","i"),
            // then cur2 = ["abc","def","ghi"].
            String[] cur2 = Arrays.copyOf(cur, N);
            for (int i = 0; i < N; i++) {
                cur2[i] += A[i].charAt(j);
            }
            if (isSorted(cur2)) cur = cur2;
            else ans++;
        }
        return ans;
    }

    private boolean isSorted(String[] A) {
        for (int i = 0; i < A.length - 1; i++) {
            if (A[i].compareTo(A[i + 1]) > 0) return false;
        }
        return true;
    }
}


Approach 2: Greedy with Optimizations
Complexity Analysis
Time Complexity: O(NW), where N is the length of A, and W is the length of A[i].
Space Complexity: O(N) in additional space complexity. (In Python, zip(*A) uses O(NW) space.)

# 8ms 75%
class Solution {
    public int minDeletionSize(String[] A) {
        int N = A.length;
        int W = A[0].length();
        // cuts[j] is true : we don't need to check any new A[i][j] <= A[i][j+1]
        boolean[] cuts = new boolean[N-1];

        int ans = 0;
        search: for (int j = 0; j < W; ++j) {
            // Evaluate whether we can keep this column
            for (int i = 0; i < N-1; ++i)
                if (!cuts[i] && A[i].charAt(j) > A[i+1].charAt(j)) {
                    // Can't keep the column - delete and continue
                    ans++;
                    continue search;
                }

            // Update 'cuts' information
            for (int i = 0; i < N-1; ++i)
                if (A[i].charAt(j) < A[i+1].charAt(j))
                    cuts[i] = true;
        }

        return ans;
    }
}

# 7ms 75%
class Solution {
    public int minDeletionSize(String[] A) {
        int n = A.length, l = A[0].length(), result = 0;
        boolean[] sorted = new boolean[n];
        for (int i = 0; i < l; i++) {
            boolean[] temp = new boolean[n];
            boolean deleted = false;
            for (int j = 0; j < n - 1; j++) {
                if (sorted[j]) continue;
                if (A[j].charAt(i) > A[j + 1].charAt(i)) {
                    deleted = true;
                    result++;
                    break;
                }
                if (A[j].charAt(i) < A[j + 1].charAt(i)) {
                    temp[j] = true;
                }
            }
            if (!deleted) {
                for (int j = 0; j < n - 1; j++) {
                    if (temp[j]) sorted[j] = true;
                }
            }
        }
        return result;
    }
}
'''