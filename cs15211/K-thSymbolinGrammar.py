__source__ = 'https://leetcode.com/problems/k-th-symbol-in-grammar/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 779. K-th Symbol in Grammar
#
# On the first row, we write a 0. Now in every subsequent row,
# we look at the previous row and replace each occurrence of 0 with 01,
# and each occurrence of 1 with 10.
#
# Given row N and index K, return the K-th indexed symbol in row N.
# (The values of K are 1-indexed.) (1 indexed).
#
# Examples:
# Input: N = 1, K = 1
# Output: 0
#
# Input: N = 2, K = 1
# Output: 0
#
# Input: N = 2, K = 2
# Output: 1
#
# Input: N = 4, K = 5
# Output: 1
#
# Explanation:
# row 1: 0
# row 2: 01
# row 3: 0110
# row 4: 01101001
# Note:
#
# N will be an integer in the range [1, 30].
# K will be an integer in the range [1, 2^(N-1)].
#
import unittest
# 20ms 97.70%
class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1: return 0
        return (1 - K%2) ^ self.kthGrammar(N-1, (K+1)/2)

# 20ms 97.70%
class Solution2(object):
    def kthGrammar(self, N, K):
        return bin(K - 1).count('1') % 2

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/k-th-symbol-in-grammar/solution/
Approach #1: Brute Force [Time Limit Exceeded]
Complexity Analysis
Time Complexity: O(2^N). We parse rows with lengths 2^0 + 2^1 +...+ 2^(N -1)
Space Complexity: O(2^N), the length of the lastrow.

# Memory Limit Exceeded
class Solution {
    public int kthGrammar(int N, int K) {
        int[] lastrow = new int[1 << N];
        for (int i = 1; i < N; ++i) {
            for (int j = (1 << (i-1)) - 1; j >= 0; --j) {
                lastrow[2*j] = lastrow[j];
                lastrow[2*j+1] = 1 - lastrow[j];
            }
        }
        return lastrow[K-1];
    }
}

Approach #2: Recursion (Parent Variant) [Accepted]
Complexity Analysis
Time Complexity: O(N). It takes N-1 steps to find the answer.
Space Complexity: O(1)
In general, the Kth digit's parent is going to be (K+1) / 2.
If the parent is 0, then the digit will be the same as 1 - (K%2).
If the parent is 1, the digit will be the opposite, ie. K%2.

# 2ms 100%
class Solution {
    public int kthGrammar(int N, int K) {
        if (N == 1) return 0;
        return (~K & 1) ^ kthGrammar(N - 1, (K + 1) /2 );
    }
}


Approach #3: Recursion (Flip Variant) [Accepted]
Complexity Analysis
Time Complexity: O(N). It takes N-1 steps to find the answer.
Space Complexity: O(1)
If K is in the second half, then we could put K -= (1 << N-2)
so that it is in the first half, and flip the final answer.

# 2ms 100%
class Solution {
    public int kthGrammar(int N, int K) {
        if (N == 1) return 0;
        if (K <= 1 << N-2)
            return kthGrammar(N-1, K);
        return kthGrammar(N-1, K - (1 << N-2)) ^ 1;
    }
}

Approach #4: Binary Count [Accepted]
Complexity Analysis
Time Complexity: O(logN), the number of binary bits in N.
If logN is taken to be bounded, this can be considered to be O(1)
Space Complexity: O(1). (In Python, bin(X) creates a string of length O(logX), which could be avoided.)
This means when applying the algorithm in Approach #3 virtually,
the number of times we will flip the final answer is just the number of 1s in the binary representation of K-1.

# 3ms 50.72%
class Solution {
    public int kthGrammar(int N, int K) {
        return Integer.bitCount(K - 1) % 2;
    }
}

# 2ms 100%
class Solution {
    public int kthGrammar(int n, int k) {
        if(n == 1) return 0;
        int source = kthGrammar(n - 1, (k + 1) / 2);
        if (source == 0) {
            return k % 2 == 0 ? 1 : 0;
        } else {
            return k % 2 == 0 ? 0 : 1;
        }
    }
}
'''