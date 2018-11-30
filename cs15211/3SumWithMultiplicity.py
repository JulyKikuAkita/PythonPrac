__source__ = 'https://leetcode.com/problems/3sum-with-multiplicity/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 923. 3Sum With Multiplicity
#
# Given an integer array A, and an integer target,
# return the number of tuples i, j, k
# such that i < j < k and A[i] + A[j] + A[k] == target.
#
# As the answer can be very large, return it modulo 10^9 + 7.
#
# Example 1:
#
# Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
# Output: 20
# Explanation:
# Enumerating by the values (A[i], A[j], A[k]):
# (1, 2, 5) occurs 8 times;
# (1, 3, 4) occurs 8 times;
# (2, 2, 4) occurs 2 times;
# (2, 3, 3) occurs 2 times.
# Example 2:
#
# Input: A = [1,1,2,2,2,2], target = 5
# Output: 12
# Explanation:
# A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
# We choose one 1 from [1,1] in 2 ways,
# and two 2s from [2,2,2,2] in 6 ways.
#
#
# Note:
#
# 3 <= A.length <= 3000
# 0 <= A[i] <= 100
# 0 <= target <= 300
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
#Thought: https://leetcode.com/problems/3sum-with-multiplicity/solution/
Approach 1: Three Pointer
Complexity Analysis
Time Complexity: O(N^2), where N is the length of A.
Space Complexity: O(1)

#67ms 46.95%
class Solution {
    public int threeSumMulti(int[] A, int target) {
        int MOD = 1_000_000_007;
        long ans = 0;
        Arrays.sort(A);

        for (int i = 0; i < A.length; ++i) {
            // We'll try to find the number of i < j < k
            // with A[j] + A[k] == T, where T = target - A[i].

            // The below is a "two sum with multiplicity".
            int T = target - A[i];
            int j = i+1, k = A.length - 1;

            while (j < k) {
                 if (A[j] + A[k] < T)
                    j++;
                else if (A[j] + A[k] > T)
                    k--;
                else if (A[j] != A[k]) {// We have A[j] + A[k] == T.
                    // Let's count "left": the number of A[j] == A[j+1] == A[j+2] == ...
                    // And similarly for "right".
                    int left = 1, right = 1;
                    while (j + 1 < k && A[j] == A[j + 1]) {
                        left++;
                        j++;
                    }
                    while (k - 1 > j && A[k] == A[k - 1]) {
                        right++;
                        k--;
                    }

                    ans += left * right;
                    ans %= MOD;
                    j++;
                    k--;
                } else {
                    // M = k - j + 1
                    // We contributed M * (M-1) / 2 pairs.
                    ans += (k - j + 1) * (k - j) / 2;
                    ans %= MOD;
                    break;
                }
            }
        }
        return (int) ans;
    }
}

Approach 2: Counting with Cases
Complexity Analysis
Time Complexity: O(N + W^2), where N is the length of A, and W is the maximum possible value of A[i].
(Note that this solution can be adapted to be O(N^2) even in the case that WW is very large.)
Space Complexity: O(W)

#6ms 97.27%
class Solution {
    public int threeSumMulti(int[] A, int target) {
        int MOD = 1_000_000_007;
        long[] count = new long[101];
        for (int x: A)
            count[x]++;

        long ans = 0;

        // All different
        for (int x = 0; x <= 100; ++x) {
            for (int y = x+1; y <= 100; ++y) {
                int z = target - x - y;
                if (y < z && z <= 100) {
                    ans += count[x] * count[y] * count[z];
                    ans %= MOD;
                }
            }
        }

        // x == y != z
        for (int x = 0; x <= 100; ++x) {
            int z = target - 2*x;
            if ( x < z && z <= 100) {
                ans += count[x] * (count[x] - 1) / 2 * count[z];
                ans %= MOD;
            }
        }

         // x != y == z
        for (int x = 0; x <= 100; ++x) {
            if (target % 2 == x % 2) {
                int y = (target - x) / 2;
                if (x < y && y <= 100) {
                    ans += count[x] * count[y] * (count[y] - 1) / 2;
                    ans %= MOD;
                }
            }
        }

        // x == y == z
        if (target % 3 == 0) {
            int x = target / 3;
            if (0 <= x && x <= 100) {
                ans += count[x] * (count[x] - 1) * (count[x] - 2) / 6;
                ans %= MOD;
            }
        }
        return (int) ans;
    }
}

Approach 3: Adapt from Three Sum
Complexity Analysis
Time Complexity: O(N^2), where N is the length of A.
Space Complexity: O(N)

#5ms 99.94%
class Solution {
    public int threeSumMulti(int[] A, int target) {
        int MOD = 1_000_000_007;
        long[] count = new long[101];
        int uniq = 0;
        for (int x : A) {
            count[x]++;
            if (count[x] == 1) uniq++;
        }

        int[] keys = new int[uniq];
        int t = 0;
        for (int i = 0; i <= 100; i++) {
            if (count[i] > 0) keys[t++] = i;
        }

        long ans = 0;
        for (int i = 0; i < keys.length; i++) {
            int x = keys[i];
            int T = target - x;
            int j = i, k = keys.length - 1;
            while (j <= k) {
                int y = keys[j], z = keys[k];
                if (y + z < T) {
                    j++;
                } else if (y + z > T) {
                    k--;
                } else { // # x+y+z == T, now calc the size of the contribution
                    if (i < j && j < k) {
                        ans += count[x] * count[y] * count[z];
                    } else if (i == j && j < k) {
                        ans += count[x] * (count[x] - 1) / 2 * count[z];
                    } else if (i < j && j == k) {
                        ans += count[x] * count[y] * (count[y] - 1) / 2;
                    } else { // i == j == k // C 3 over 2
                        ans += count[x] * ( count[x] - 1) * (count[x] - 2) / (2 * 3);
                    }
                    ans %= MOD;
                    j++;
                    k--;
                }
            }
        }
        return (int)ans;
    }
}

'''