__source__ = 'https://leetcode.com/problems/subarray-sums-divisible-by-k/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 974. Subarray Sums Divisible by K
#
# Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.
#
# Example 1:
#
# Input: A = [4,5,0,-2,-3,1], K = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by K = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
#
#
# Note:
#
# 1 <= A.length <= 30000
# -10000 <= A[i] <= 10000
# 2 <= K <= 10000
#
import unittest
import collections

# 100ms 86.53%
class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        P = [0]
        for x in A:
            P.append((P[-1] + x) % K)

        count = collections.Counter(P)
        return sum(v*(v-1)/2 for v in count.values())

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/subarray-sums-divisible-by-k/solution/
# https://leetcode.com/problems/subarray-sums-divisible-by-k/discuss/217962/Java-Clean-O(n)-Number-Theory-%2B-Prefix-Sums
# Approach 1: Prefix Sums and Counting
# Complexity Analysis
# Time Complexity: O(N), where N is the length of A.
# Space Complexity: O(N). (However, the solution can be modified to use O(K) space by storing only count.) 
# 5ms 100%
class Solution {
    public int subarraysDivByK(int[] A, int K) {
        //There K mod groups 0...K-1
        //For each prefix sum that does not have remainder 0 it needs to be paired with 1 with the same remainder
        //this is so the remainders cancel out.
        int N = A.length;
        int[] modGroups = new int[K];
        int sum = 0;
        for (int i = 0; i < N; i++){
            sum += A[i];
            int group = sum % K;
            
            if (group < 0) group += K; //Java has negative modulus so correct it
            modGroups[group]++;
        }
        
        int total = 0;
        for (int x : modGroups){
             if (x > 1) total += (x*(x-1)) / 2;
        }
        //Dont forget all numbers that divide K
        return total + modGroups[0];
    }
}

So why use a Map instead of just an array int[K]?
A. Because it's a waste of space if K is huge and N is relatively small or the partial sums mod K are relatively few. 
This way there are at most K or N, whichever is lower, entries in the Map.
Also counting pairs => N choose 2 = > n*(n-1) / 2.
# Count the Remainder
# 35ms 56.65%
class Solution {
    public int subarraysDivByK(int[] A, int K) {
        Map<Integer, Integer> count = new HashMap<>();
        count.put(0, 1);
        int prefix = 0, res = 0;
        for (int a : A) {
            prefix = (prefix + a % K + K) % K;
            res += count.getOrDefault(prefix, 0);
            count.put(prefix, count.getOrDefault(prefix, 0) + 1);
        }
        return res;
    }
}

# Same with Array
# 7ms 100%
class Solution {
    public int subarraysDivByK(int[] A, int K) {
        int[] count = new int[K];
        count[0] = 1;
        int prefix = 0, res = 0;
        for (int a : A) {
            prefix = (prefix + a % K + K) % K;
            res += count[prefix]++;
        }
        return res;
    }
}

# Brute Force
# Time Complexity: O(N^2)
# 7530ms 9.88%
class Solution {
    public int subarraysDivByK(int[] A, int K) {
        int[] sum = new int[A.length];
        sum[0] = A[0];
        for (int i = 1; i < A.length; i++) {
            sum[i] = A[i] + sum[i - 1];
        }
        int ans = 0;

        for (int i = 0; i < A.length; i++) if (sum[i] % K == 0) ans++;
        for (int i = 1; i < A.length; i++) {
            for (int j = 0; j < i; j++) {
                if ((sum[i] - sum[j]) % K == 0) ans++;
            }
        }
        return ans;
    }
}
'''
