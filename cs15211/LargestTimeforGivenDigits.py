__source__ = 'https://leetcode.com/problems/largest-time-for-given-digits/'
# Time:  O(1)
# Space: O(1)
#
# Description: Leetcode # 949. Largest Time for Given Digits
# Given an array of 4 digits, return the largest 24 hour time that can be made.
#
# The smallest 24 hour time is 00:00, and the largest is 23:59.
# Starting from 00:00, a time is larger if more time has elapsed since midnight.
#
# Return the answer as a string of length 5.
# If no valid time can be made, return an empty string.
#
# Example 1:
#
# Input: [1,2,3,4]
# Output: "23:41"
#
# Example 2:
#
# Input: [5,5,5,5]
# Output: ""
#
# Note:
#
#     A.length == 4
#     0 <= A[i] <= 9
#
import itertools
import unittest
# 24ms 89.17%
class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        ans = -1
        for h1, h2, m1, m2 in itertools.permutations(A):
            hours = 10 * h1 + h2
            mins = 10 * m1 + m2
            time = 60 * hours + mins
            if 0 <= hours < 24 and 0 <= mins < 60 and time > ans:
                ans = time

        return "{:02}:{:02}".format(*divmod(ans, 60)) if ans >= 0 else ""

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/largest-time-for-given-digits/solution/
#
Approach 1: Brute Force
Complexity Analysis
Time Complexity: O(1)
Space Complexity: O(1)

# 14ms 43.20%
class Solution {
    public String largestTimeFromDigits(int[] A) {
        int ans = -1;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (j != i) {
                    for (int k = 0; k < 4; k++) {
                        if (k != i && k != j) {
                            int l = 6 - i - j - k;
                            
                            // For each permutation of A[i], read out the time and
                            // record the largest legal time.
                            int hours = 10 * A[i] + A[j];
                            int mins = 10 * A[k] + A[l];
                            if (hours < 24 && mins < 60) ans = Math.max(ans, hours * 60 + mins);
                        }
                    }
                }
            }
        }
        return ans >= 0 ? String.format("%02d:%02d", ans / 60, ans % 60) : "";
    }
}

# 5ms 100%
class Solution {
    public String largestTimeFromDigits(int[] A) {
        int[] count = new int[10];
        for (int i : A) count[i]++;
        char[] builder = new char[5];
        if (dfs(count, 0, 0, builder)) return new String(builder);
        return "";
    }
    
    private boolean dfs(int[] digits, int ith, int pre, char[] builder) {
        if (ith >= builder.length) return true;
        int max = 0;
        if (ith == 0) {
            max = 2;
        } else if (ith == 1) {
            max = pre == 2 ? 3: 9;
        } else if (ith == 2) {
            builder[ith] = ':';
            return dfs(digits, ith + 1, 10, builder);
        } else if (ith == 3) {
            max = 5;
        } else {
            max = 9;
        }
        
        for (int i = max; i >= 0; i--) {
            if (digits[i] > 0) {
                digits[i]--;
                builder[ith] = (char) ('0' + i);
                if (dfs(digits, ith + 1, i, builder)) return true;
                digits[i]++;
            }
        }
        return false;
    }
}
'''
