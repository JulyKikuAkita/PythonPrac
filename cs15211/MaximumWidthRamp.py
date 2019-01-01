__source__ = 'https://leetcode.com/problems/maximum-width-ramp/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 962. Maximum Width Ramp
#
# Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].
# The width of such a ramp is j - i.
#
# Find the maximum width of a ramp in A.  If one doesn't exist, return 0.
#
# Example 1:
#
# Input: [6,0,8,2,1,5]
# Output: 4
# Explanation:
# The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.
#
# Example 2:
#
# Input: [9,8,1,0,1,9,4,0,4,1]
# Output: 7
# Explanation:
# The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.
#
# Note:
#
#     2 <= A.length <= 50000
#     0 <= A[i] <= 50000
#
import unittest
# 260ms 40.40%
class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = 0
        m = float('inf')
        for i in sorted(range(len(A)), key = A.__getitem__):
            ans = max(ans, i - m)
            m = min(m, i)
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/maximum-width-ramp/solution/
#
Approach 1: Sort
Complexity Analysis
Time Complexity: O(NLogN), where N is the length of A.
Space Complexity: O(N), depending on the implementation of the sorting function.

# 160ms 40.70%
class Solution {
    public int maxWidthRamp(int[] A) {
        int N = A.length;
        Integer[] B = new Integer[N];
        for (int i = 0; i < N; ++i) B[i] = i;
        Arrays.sort(B, (i, j) -> ((Integer) A[i]).compareTo(A[j]));

        int ans = 0;
        int m = N;
        for (int i: B) {
            ans = Math.max(ans, i - m);
            m = Math.min(m, i);
        }
        return ans;
    }
}

Approach 2: Binary Search Candidates
Complexity Analysis
Time Complexity: O(NlogN), where N is the length of A.
Space Complexity: O(N)

# 38ms 73.26%
import java.awt.Point;
class Solution {
    public int maxWidthRamp(int[] A) {
        int N = A.length;

        int ans = 0;
        List<Point> candidates = new ArrayList();
        candidates.add(new Point(A[N-1], N-1));

        // candidates: i's decreasing, by increasing value of A[i]
        for (int i = N-2; i >= 0; --i) {
            // Find largest j in candidates with A[j] >= A[i]
            int lo = 0, hi = candidates.size();
            while (lo < hi) {
                int mi = lo + (hi - lo) / 2;
                if (candidates.get(mi).x < A[i])
                    lo = mi + 1;
                else
                    hi = mi;
            }

            if (lo < candidates.size()) {
                int j = candidates.get(lo).y;
                ans = Math.max(ans, j - i);
            } else {
                candidates.add(new Point(A[i], i));
            }
        }
        return ans;
    }
}

# 12ms 94.64%
class Solution {
    public int maxWidthRamp(int[] A) {
        int[] s = new int[A.length];
        int ptr = 0;
        int res = 0, n = A.length;
        for (int i = 0; i < n; ++i){
            if (ptr == 0 || A[s[ptr-1]] > A[i]) s[ptr++] = i;
        }
        for (int i = n - 1; i > res; --i) {
            while (ptr != 0 && A[s[ptr-1]] <= A[i]) {
                res = Math.max(res, i - s[--ptr]);
            }
        }
        return res;
    }
}
'''
