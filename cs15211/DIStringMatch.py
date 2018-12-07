__source__ = 'https://leetcode.com/problems/di-string-match/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 942. DI String Match
#
# Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
#
# Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
#
# If S[i] == "I", then A[i] < A[i+1]
# If S[i] == "D", then A[i] > A[i+1]
#
#
# Example 1:
#
# Input: "IDID"
# Output: [0,4,1,3,2]
# Example 2:
#
# Input: "III"
# Output: [0,1,2,3]
# Example 3:
#
# Input: "DDI"
# Output: [3,2,0,1]
#
#
# Note:
#
# 1 <= S.length <= 10000
# S only contains characters "I" or "D".
#
import unittest

# 156ms 20.33%
class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lo, hi = 0, len(S)
        ans = []
        for x in S:
            if x == 'I':
                ans.append(lo)
                lo += 1
            else:
                ans.append(hi)
                hi -= 1

        return ans + [lo]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/di-string-match/solution/
Approach 1: Ad-Hoc
Complexity Analysis
Time Complexity: O(N), where N is the length of S.
Space Complexity: O(N)

# 5ms 99.59%
class Solution {
    public int[] diStringMatch(String S) {
        int N = S.length();
        int lo = 0, hi = N;
        int[] ans = new int[N + 1];
        for (int i = 0; i < N; ++i) {
            if (S.charAt(i) == 'I') ans[i] = lo++;
            else ans[i] = hi--;
        }
        ans[N] = lo;
        return ans;
    }
}

# 5ms 99.59%
class Solution {
    public int[] diStringMatch(String S) {
        int n = S.length();
        int[] res = new int[n + 1];
        int left = 0;
        int right = n;
        for (int i = 0; i < n; i++) {
            res[i] = S.charAt(i) == 'I' ? left++ : right--;
        }
        res[n] = left; //res[n] = right;    also works
        return res;
    }
}
'''