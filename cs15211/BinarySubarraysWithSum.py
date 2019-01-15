import collections

__source__ = 'https://leetcode.com/problems/binary-subarrays-with-sum/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 930. Binary Subarrays With Sum
#
# In an array A of 0s and 1s, how many non-empty subarrays have sum S?
#
# Example 1:
#
# Input: A = [1,0,1,0,1], S = 2
# Output: 4
# Explanation:
# The 4 subarrays are bolded below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
#
#
# Note:
#
# A.length <= 30000
# 0 <= S <= A.length
# A[i] is either 0 or 1.
#
import unittest

#44ms 97.72%
class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        indexes = [-1] + [ix for ix, v in enumerate(A) if v] + [len(A)]
        ans = 0

        if S == 0:
            for i in xrange(len(indexes) - 1):
                # w: number of zeros between two consecutive ones
                w = indexes[i+1] - indexes[i] - 1
                ans += w * (w+1) / 2
            return ans

        for i in xrange(1, len(indexes) - S):
            j = i + S - 1
            left = indexes[i] - indexes[i-1]
            right = indexes[j+1] - indexes[j]
            ans += left * right
        return ans

#172ms 11.98%
class Solution2(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        P = [0]
        for x in A: P.append(P[-1] + x)
        count = collections.Counter()

        ans = 0
        for x in P:
            ans += count[x]
            count[x + S] += 1
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/binary-subarrays-with-sum/solution/
Approach 1: Index of Ones
Complexity Analysis
Time Complexity: O(N), where N is the length of A.
Space Complexity: O(N).

#4ms 100%
class Solution {
    public int numSubarraysWithSum(int[] A, int S) {
        int su = 0;
        for (int x: A) su += x;

        // indexes[i] = location of i-th one (1 indexed)
        int[] indexes = new int[su + 2];
        int t = 0;
        indexes[t++] = -1;
        for (int i = 0; i < A.length; i++) {
            if (A[i] == 1) indexes[t++] = i;
        }
        indexes[t] = A.length;

        int ans = 0;
        if (S == 0) {
            for (int i = 0; i < indexes.length - 1; ++i) {
                // w: number of zeros between consecutive ones
                int w = indexes[i + 1] - indexes[i] - 1;
                ans += w * (w + 1) / 2;
            }
            return ans;
        }

        for (int i = 1; i < indexes.length - S; i++) {
            int j = i + S - 1;
            int left = indexes[i] - indexes[i - 1];
            int right = indexes[j + 1] - indexes[j];
            ans += left * right;
        }
        return ans;
    }
}

Approach 2: Prefix Sums
Complexity Analysis
Time Complexity: O(N), where N is the length of A.
Space Complexity: O(N)

# 24ms 64.99%
class Solution {
    public int numSubarraysWithSum(int[] A, int S) {
        int N = A.length;
        int[] P = new int[N + 1];
        for (int i = 0; i < N; i++) {
            P[i + 1] = P[i] + A[i];
        }

        Map<Integer, Integer> count = new HashMap();
        int ans = 0;
        for (int x : P) {
            ans += count.getOrDefault(x, 0);
            count.put(x + S, count.getOrDefault(x + S, 0) + 1);
        }
        return ans;
    }
}

Approach 3: Three Pointer
For each j (in increasing order), let's maintain 4 variables:

sum_lo : the sum of subarray [i_lo, j]
sum_hi : the sum of subarray [i_hi, j]
i_lo : the smallest i so that sum_lo <= S
i_hi : the largest i so that sum_hi <= S
Then, (provided that sum_lo == S), the number of subarrays ending in j is i_hi - i_lo + 1.

As an example, with A = [1,0,0,1,0,1] and S = 2, when j = 5, we want i_lo = 1 and i_hi = 3.

Complexity Analysis
Time Complexity: O(N), where N is the length of A.
Space Complexity: O(1)

# 6ms 93.50%
class Solution {
    public int numSubarraysWithSum(int[] A, int S) {
        int iLo = 0, iHi = 0;
        int sumLo = 0, sumHi = 0;
        int ans = 0;

        for (int j = 0; j < A.length; ++j) {
            // While sumLo is too big, iLo++
            sumLo += A[j];
            while (iLo < j && sumLo > S) {
                sumLo -= A[iLo++];
            }

            // While sumHi is too big, or equal and we can move, iHi++
            sumHi += A[j];
            while (iHi < j && (sumHi > S || sumHi == S && A[iHi] == 0)) sumHi -= A[iHi++];
            if (sumLo == S) ans += iHi - iLo + 1;
        }
        return ans;
    }
}

# 5ms 98.15%
class Solution {
    public int numSubarraysWithSum(int[] A, int S) {
        int l = A.length;
        int[] map = new int[l + 1];
        int sum = 0, ans = 0;
        for (int i = 0; i < A.length; i++) {
            sum += A[i];
            int diff = sum - S;
            if (diff >= 0) ans += map[diff];
            if (sum == S) ans++;
            map[sum]++;
        }
        return ans;
    }
}

#4ms 100%
class Solution {
    public int numSubarraysWithSum(int[] A, int S) {
        int previousSum = 0, result = 0;
        int[] counts = new int[A.length + 1];
        counts[0] = 1;

        for (int value : A) {
            previousSum += value;
            if (previousSum >= S) {
                result += counts[previousSum - S];
            }
            counts[previousSum]++;
        }

        return result;
    }
}
'''