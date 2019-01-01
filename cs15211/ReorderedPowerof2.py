__source__ = 'https://leetcode.com/problems/reordered-power-of-2/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 869. Reordered Power of 2
#
# Starting with a positive integer N, we reorder the digits in any order (including the original order)
# such that the leading digit is not zero.
#
# Return true if and only if we can do this in a way such that the resulting number is a power of 2.
#
# Example 1:
#
# Input: 1
# Output: true
#
# Example 2:
#
# Input: 10
# Output: false
#
# Example 3:
#
# Input: 16
# Output: true
#
# Example 4:
#
# Input: 24
# Output: false
#
# Example 5:
#
# Input: 46
# Output: true
#
# Note:
#     1 <= N <= 10^9
#
import unittest
import collections
import itertools
# TLE
class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool

        Let's work through an example like N = 128.
        In the last line, 'for cand in itertools.permutations(str(N))' will
        iterate through the six possibilities cand = ('1', '2', '8'),
        cand = ('1', '8', '2'), cand = ('2', '1', '8'), and so on.

        The check cand[0] != '0' is a check that the candidate permutation
        does not have a leading zero.

        The check bin(int("".join(cand))).count('1') == 1 is a check that cand
        represents a power of 2: namely, that the number of ones in its binary
        representation is 1.
        """
        return any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1
                   for cand in itertools.permutations(str(N)))
# 52ms 17.65%
class Solution2(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        count = collections.Counter(str(N))
        return any(count == collections.Counter(str(1 << b))
                   for b in xrange(31))
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/reordered-power-of-2/solution/
#
Approach 1: Permutations
Complexity Analysis
Time Complexity: O((LogN)! * LogN) Note that LogN is the number of digits in the binary representation of N. 
For each of (LogN)! permutations of the digits of N, 
we need to check that it is a power of 2 in O(LogN) time.
Space Complexity: O(LogN), the space used by A (or cand in Python).

# 128ms 19.81%
class Solution {
    public boolean reorderedPowerOf2(int N) {
        // Build eg. N = 128 -> A = [1, 2, 8]
        String S = Integer.toString(N);
        int[] A = new int[S.length()];
        for (int i = 0; i < S.length(); ++i)
            A[i] = S.charAt(i) - '0';
        return permutations(A, 0);
    }
    
    /**
     * Returns true if some permutation of (A[start], A[start+1], ...)
     * can result in A representing a power of 2.
     */
    private boolean permutations(int[] A, int start) {
        if (start == A.length) return isPowerOfTwo(A);
        
        // Choose some index i from [start, A.length - 1]
        // to be placed into position A[start].
        for (int i = start; i < A.length; ++i) {
            // Place A[start] with value A[i].
            swap(A, start, i);
            
            // For each such placement of A[start], if a permutation
            // of (A[start+1], A[start+2], ...) can result in A
            // representing a power of 2, return true.
            if (permutations(A, start + 1)) return true;
            
             // Restore the array to the state it was in before
            // A[start] was placed with value A[i].
            swap(A, start, i);    
        }
        return false;
            
    }
    
    private boolean isPowerOfTwo(int[] A) {
        if (A[0] == 0) return false;  // no leading zero
        
        // Build eg. A = [1, 2, 8] -> N = 128
        int N = 0;
        for (int x: A) N = 10 * N + x;
        
        // Remove the largest power of 2
        while (N > 0 && ((N & 1) == 0)) N >>= 1;
        
        // Check that there are no other factors besides 2
        return N == 1;
    }

    private void swap(int[] A, int i, int j) {
        int t = A[i];
        A[i] = A[j];
        A[j] = t;
    }
}

Approach 2: Counting
Complexity Analysis
Time Complexity: O(Log^2 N). There are LogN different candidate powers of 2, 
and each comparison has O(LogN) time complexity.
Space Complexity: O(LogN). 

# 8ms 56.52%
class Solution {
    public boolean reorderedPowerOf2(int N) {
        int[] A = count(N);
        for (int i = 0; i < 31; ++i){
            if (Arrays.equals(A, count(1 << i))) return true;                
        }
        return false;
    }
    
    // Returns the count of digits of N
    // Eg. N = 112223334, returns [0,2,3,3,1,0,0,0,0,0]
    private int[] count(int N) {
        int[] ans = new int[10];
        while (N > 0) {
            ans[N % 10]++;
            N /= 10;
        }
        return ans;
    }
}

# 7ms 66.18%
class Solution {
    public boolean reorderedPowerOf2(int N) {
        for(int i = 0; i<32; i++){
            if(same(N, 1<<i))
                return true;
        }
        
        return false;
    }
    
    public boolean same(int num1, int num2){
        String str1 = String.valueOf(num1);
        String str2 = String.valueOf(num2);
        char[] c1 = str1.toCharArray();
        char[] c2 = str2.toCharArray();
        Arrays.sort(c1);
        Arrays.sort(c2);
        return String.valueOf(c1).equals(String.valueOf(c2));
    }
}
'''
