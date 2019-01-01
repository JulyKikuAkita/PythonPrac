__source__ = 'https://leetcode.com/problems/smallest-rotation-with-highest-score/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 798. Smallest Rotation with Highest Score
#
# Given an array A,
# we may rotate it by a non-negative integer K so that the array becomes
# A[K], A[K+1], A{K+2], ... A[A.length - 1], A[0], A[1], ..., A[K-1].
# Afterward, any entries that are less than or equal to their index are worth 1 point.
#
# For example, if we have [2, 4, 1, 3, 0], and we rotate by K = 2, it becomes [1, 3, 0, 2, 4].
# This is worth 3 points because
# 1 > 0 [no points], 3 > 1 [no points], 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point].
#
# Over all possible rotations, return the rotation index K that corresponds to the highest score we could receive.
# If there are multiple answers, return the smallest such index K.
#
# Example 1:
# Input: [2, 3, 1, 4, 0]
# Output: 3
# Explanation:
# Scores for each K are listed below:
# K = 0,  A = [2,3,1,4,0],    score 2
# K = 1,  A = [3,1,4,0,2],    score 3
# K = 2,  A = [1,4,0,2,3],    score 3
# K = 3,  A = [4,0,2,3,1],    score 4
# K = 4,  A = [0,2,3,1,4],    score 3
#
# So we should choose K = 3, which has the highest score.
#
# Example 2:
# Input: [1, 3, 0, 2, 4]
# Output: 0
# Explanation:  A will always have 3 points no matter how it shifts.
# So we will choose the smallest K, which is 0.
#
# Note:
#
#     A will have length at most 20000.
#     A[i] will be in the range [0, A.length].
#
import unittest
# 60ms 71.05%
class Solution(object):
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        bad = [0] * N
        for i, x in enumerate(A):
            left, right = (i - x + 1) % N, (i + 1) % N
            bad[left] -= 1
            bad[right] += 1
            if left > right:
                bad[0] -= 1

        best = -N
        ans = cur = 0
        for i, score in enumerate(bad):
            cur += score
            if cur > best:
                best = cur
                ans = i
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/smallest-rotation-with-highest-score/solution/
#
Approach #1: Interval Stabbing [Accepted]
Complexity Analysis
Time Complexity: O(N), where N is the length of A.
Space Complexity: O(N)

# 7ms 35.23%
class Solution {
    public int bestRotation(int[] A) {
        int N = A.length;
        int[] bad = new int[N];
        for (int i = 0; i < N; i++) {
            int left = (i - A[i] + 1 + N) % N;
            int right = (i + 1) % N;
            bad[left]--;
            bad[right]++;
            if (left > right) bad[0]--;
        }
        
        int best = -N;
        int ans = 0, cur = 0;
        for (int i  = 0; i < N; i++) {
            cur += bad[i];
            if (cur > best) {
                best = cur;
                ans = i;
            }
        }
        return ans;
    }
}

# 4ms 97.73%
class Solution {
    public int bestRotation(int[] A) {
        int n = A.length;
        int[] change = new int[n];
        for ( int i = 0; i < n; i++ ) {
            change[ (i - A[i] + 1 + n) % n ]-= 1;
        }
        int res = 0;
        for ( int i = 1; i < n; i++ ) {
            change[i] += change[i - 1] + 1;
            res = change[i] > change[res] ? i : res;
        }
        return res;
    }
}
'''
