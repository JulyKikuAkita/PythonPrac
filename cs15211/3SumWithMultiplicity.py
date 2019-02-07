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

# 81ms 40%
class Solution {
    public int threeSumMulti(int[] A, int target) {
        Arrays.sort(A);
        long res = 0;
        int MOD = 1_000_000_007;
        for (int i = 0; i < A.length - 2; i++) {
            int j = i + 1, k = A.length - 1;
            // The below is a "two sum with multiplicity".
            while (j < k) {
                if (A[i] + A[j] + A[k] < target) j++;
                else if (A[i] + A[j] + A[k] > target) k--;
                else { // A[i] + A[j] + A[k] == target
                    if (A[j] == A[k]) {
                        // M = k - j + 1
                        // We contributed M * (M-1) / 2 pairs.
                        res += (k - j) * (k - j + 1) / 2;
                        res %= MOD;
                        break;
                    } else {
                        // Let's count "left": the number of A[j] == A[j+1] == A[j+2] == ...
                        // And similarly for "right".
                        int left = 1, right = 1;
                        while (j + 1 < k && A[j] == A[j + 1]) {
                            j++;
                            left++;
                        }
                        while (k - 1 > j && A[k] == A[k - 1]) {
                            k--;
                            right++;
                        }
                        res += (left * right);
                        res %= MOD;
                        j++;
                        k--;
                    }
                }
            }
        }
        return (int) res;
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

# 5ms 99.94%
class Solution {
    public int threeSumMulti(int[] A, int target) {
        long res = 0;
        int MOD = (int) (1e9 + 7);; 
        
        // Initializing as long saves us the trouble of
        // managing count[x] * count[y] * count[z] overflowing later.
        long[] count = new long[101];
        int uniq = 0;
        for (int a : A) {
            count[a]++;
            if (count[a] == 1) uniq++;
        }
        
        int[] keys = new int[uniq];
        int t = 0;
        for (int i = 0; i <= 100; i++) {
            if (count[i] > 0) keys[t++] = i;
        }
        
        // Now, let's do a 3sum on "keys", for i <= j <= k.
        // We will use count to add the correct contribution to ans.
        for (int i = 0; i < uniq; i++) {
            int j = i, k = uniq - 1;    
            while (j <= k) {
                if (keys[i] + keys[j] + keys[k] < target) j++;
                else if (keys[i] + keys[j] + keys[k] > target) k--;
                else {
                    if (i < j && j < k) {
                        res += count[keys[i]] * count[keys[j]] * count[keys[k]];
                    } else if (i == j && j < k){
                        res += (count[keys[i]] - 1) * count[keys[i]] / 2 * count[keys[k]];
                    } else if (i < j && j == k){
                        res += (count[keys[j]] - 1) * count[keys[j]] / 2 * count[keys[i]];
                    } else { //i ==j == k
                        res += (count[keys[i]] - 1) * (count[keys[i]] - 2) * count[keys[i]] / 6;
                    }
                    res %= MOD;
                    j++;
                    k--;
                }
            }
        }
        return (int) res;
    }
}

# Simplified version
# 5ms 98.67%
class Solution {
    public int threeSumMulti(int[] A, int target) {
        long res = 0;
        long[] count = new long[101];
        for (int a : A) count[a]++;
        
        for (int i = 0; i <= 100; i++) {
            for (int j = i; j <= 100; j++) {
                int k = target - i - j;
                if (k < 0 || k > 100) continue;
                if ( i == j && j != k) {
                    res += count[i] * (count[i] - 1) / 2 * count[k];
                } else if (i == j && j == k) {
                    res += count[i] * (count[i] - 1) * (count[i] - 2) / 6;
                } else if (j < k) {
                    res += count[i] * count[j] * count[k];
                }
            }
        }
        return (int) (res % (1e9 + 7));
    }
}

# Map + 2 sum
# 1003ms 7.33%
class Solution {
    public int threeSumMulti(int[] A, int target) {
        int mod = (int) (1e9 + 7);
        int res = 0;
        
        for (int i = 0; i < A.length - 2; i++) {
            Map<Integer, Integer> map = new HashMap();
            for (int j = i + 1; j < A.length; j++) {
                if (map.containsKey(target - A[j])) res = (res + map.get(target - A[j])) % mod;
                int val = A[i] + A[j];
                map.put(val, map.getOrDefault(val, 0) + 1);
            }
        }
        return (int) res;
    }
}

# https://leetcode.com/problems/3sum-with-multiplicity/discuss/181131/C%2B%2BJavaPython-O(1012)

'''
