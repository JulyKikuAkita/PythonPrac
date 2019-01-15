# coding=utf-8
__source__ = 'https://leetcode.com/problems/maximum-length-of-repeated-subarray/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 718. Maximum Length of Repeated Subarray
#
# Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.
#
# Example 1:
#
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation:
# The repeated subarray with maximum length is [3, 2, 1].
#
# Note:
#     1 <= len(A), len(B) <= 1000
#     0 <= A[i], B[i] < 100
#
import unittest

# 1580ms 94.15%
class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i+1][j+1]+1
        return max(max(row) for row in memo)

# Binary Search
# 88ms 100%
class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        def check(length):
            seen = {A[i:i+length]
                    for i in xrange(len(A) - length + 1)}
            return any(B[j:j+length] in seen
                       for j in xrange(len(B) - length + 1))

        A = ''.join(map(chr, A))
        B = ''.join(map(chr, B))
        lo, hi = 0, min(len(A), len(B)) + 1
        while lo < hi:
            mi = (lo + hi) / 2
            if check(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo - 1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/maximum-length-of-repeated-subarray/solution/
#
Approach #1: Brute Force with Initial Character Map [Time Limit Exceeded]
Complexity Analysis
Time Complexity: O(M * N * min(M,N)), where M,N are the lengths of A, B. 
The worst case is when all the elements are equal.
Space Complexity: O(N), the space used by Bstarts. 
(Of course, we could amend our algorithm to make this O(min⁡(M,N))
# TLE
class Solution {
    public int findLength(int[] A, int[] B) {
        int ans = 0;
        Map<Integer, ArrayList<Integer>> Bstarts = new HashMap();
        for (int j = 0; j < B.length; j++) {
            Bstarts.computeIfAbsent(B[j], x -> new ArrayList()).add(j);
        }

        for (int i = 0; i < A.length; i++) if (Bstarts.containsKey(A[i])) {
            for (int j: Bstarts.get(A[i])) {
                int k = 0;
                while (i+k < A.length && j+k < B.length && A[i+k] == B[j+k]) {
                    k++;
                }
                ans = Math.max(ans, k);
            }
        }
        return ans;
    }
}

Approach #2: Binary Search with Naive Check [Time Limit Exceeded]
Complexity Analysis
Time Complexity: O((M+N) * min⁡(M,N) * log⁡(min⁡(M,N))), where M,N are the lengths of A, B. 
The log factor comes from the binary search. 
The complexity of our naive check of a given length is O((M+N) * length), 
as we will create the seen strings with complexity O(M * length), 
then search for them with complexity O(N * length), 
and our total complexity when performing our check is the addition of these two.
Space Complexity: O(M^2), the space used by seen

# TLE ~ 1113ms 1.39%
class Solution {
    public boolean check(int length, int[] A, int[] B) {
        Set<String> seen = new HashSet();
        for (int i = 0; i + length <= A.length; ++i) {
            seen.add(Arrays.toString(Arrays.copyOfRange(A, i, i+length)));
        }
        for (int j = 0; j + length <= B.length; ++j) {
            if (seen.contains(Arrays.toString(Arrays.copyOfRange(B, j, j+length)))) {
                return true;
            }
        }
        return false;
    }

    public int findLength(int[] A, int[] B) {
        int lo = 0, hi = Math.min(A.length, B.length) + 1;
        while (lo < hi) {
            int mi = (lo + hi) / 2;
            if (check(mi, A, B)) lo = mi + 1;
            else hi = mi;
        }
        return lo - 1;
    }
}

Approach #3: Dynamic Programming [Accepted]
Complexity Analysis
Time Complexity: O(M * N), where M,N are the lengths of A, B.
Space Complexity: O(M * N), the space used by dp.
# dp[i][j] = dp[i+1][j+1] + 1. Also, the answer is max(dp[i][j]) over all i, j.
# 47ms 73.24%
class Solution {
    public int findLength(int[] A, int[] B) {
        int ans = 0;
        int[][] memo = new int[A.length + 1][B.length + 1];
        for (int i = A.length - 1; i >= 0; --i) {
            for (int j = B.length - 1; j >= 0; --j) {
                if (A[i] == B[j]) {
                    memo[i][j] = memo[i+1][j+1] + 1;
                    if (ans < memo[i][j]) ans = memo[i][j];
                }
            }
        }
        return ans;
    }
}

Approach #4: Binary Search with Rolling Hash [Accepted] Rabin-Karp algorithm
Complexity Analysis
Time Complexity: O((M+N)*log(min(M,N))), where M,N are the lengths of A, B. 
The log factor is contributed by the binary search, while creating the rolling hashes is O(M+N). 
The checks for duplicate hashes are O(1). 
If we perform a naive check to make sure our answer is correct, 
it adds a factor of OO(min(M,N)) to our cost of check, which keeps the complexity the same.
Space Complexity: O(M), the space used to store hashes and the subarrays in our final naive check.
# Rabin-Karp algorithm
# 101ms 8.23%
import java.math.BigInteger;
class Solution {
    int P = 113;
    int MOD = 1_000_000_007;
    int Pinv = BigInteger.valueOf(P).modInverse(BigInteger.valueOf(MOD)).intValue();

    private int[] rolling(int[] source, int length) {
        int[] ans = new int[source.length - length + 1];
        long h = 0, power = 1;
        if (length == 0) return ans;
        for (int i = 0; i < source.length; ++i) {
            h = (h + source[i] * power) % MOD;
            if (i < length - 1) {
                power = (power * P) % MOD;
            } else {
                ans[i - (length - 1)] = (int) h;
                h = (h - source[i - (length - 1)]) * Pinv % MOD;
                if (h < 0) h += MOD;
            }
        }
        return ans;
    }

    private boolean check(int guess, int[] A, int[] B) {
        Map<Integer, List<Integer>> hashes = new HashMap();
        int k = 0;
        for (int x: rolling(A, guess)) {
            hashes.computeIfAbsent(x, z -> new ArrayList()).add(k++);
        }
        int j = 0;
        for (int x: rolling(B, guess)) {
            for (int i: hashes.getOrDefault(x, new ArrayList<Integer>()))
                if (Arrays.equals(Arrays.copyOfRange(A, i, i+guess),
                                  Arrays.copyOfRange(B, j, j+guess))) {
                    return true;
                }
            j++;
        }
        return false;
    }

    public int findLength(int[] A, int[] B) {
        int lo = 0, hi = Math.min(A.length, B.length) + 1;
        while (lo < hi) {
            int mi = (lo + hi) / 2;
            if (check(mi, A, B)) lo = mi + 1;
            else hi = mi;
        }
        return lo - 1;
    }
}
'''
