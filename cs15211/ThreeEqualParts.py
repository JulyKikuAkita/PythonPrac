__source__ = 'https://leetcode.com/problems/three-equal-parts/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 927. Three Equal Parts
#
# Given an array A of 0s and 1s, divide the array into 3 non-empty parts
# such that all of these parts represent the same binary value.
#
# If it is possible, return any [i, j] with i+1 < j, such that:
#
# A[0], A[1], ..., A[i] is the first part;
# A[i+1], A[i+2], ..., A[j-1] is the second part, and
# A[j], A[j+1], ..., A[A.length - 1] is the third part.
# All three parts have equal binary value.
# If it is not possible, return [-1, -1].
#
# Note that the entire part is used when considering what binary value it represents.
# For example, [1,1,0] represents 6 in decimal, not 3.
# Also, leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.
#
# Example 1:
#
# Input: [1,0,1,0,1]
# Output: [0,3]
# Example 2:
#
# Input: [1,1,0,1,1]
# Output: [-1,-1]
#
#
# Note:
#
# 3 <= A.length <= 30000
# A[i] == 0 or A[i] == 1
#
import unittest

# 76ms 77.81%
class Solution(object):
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        IMP = [-1, -1]

        S = sum(A)
        if S % 3: return IMP
        T = S / 3
        if T == 0:
            return [0, len(A) - 1]

        breaks = []
        su = 0
        for i, x in enumerate(A):
            if x:
                su += x
                if su in {1, T+1, 2*T+1}:
                    breaks.append(i)
                if su in {T, 2*T, 3*T}:
                    breaks.append(i)

        i1, j1, i2, j2, i3, j3 = breaks

        # The array is in the form W [i1, j1] X [i2, j2] Y [i3, j3] Z
        # where [i1, j1] is a block of 1s, etc.
        if not(A[i1:j1+1] == A[i2:j2+1] == A[i3:j3+1]):
            return [-1,-1]

        # x, y, z: the number of zeros after part 1, 2, 3
        x = i2 - j1 - 1
        y = i3 - j2 - 1
        z = len(A) - j3 - 1

        if x < z or y < z: return IMP
        j1 += z
        j2 += z
        return [j1, j2+1]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/three-equal-parts/solution/
Approach 1: Equal Ones
Complexity Analysis
Time Complexity: O(N), where N is the length of S.
Space Complexity: O(N).

# 12ms 69.58%
class Solution {
    public int[] threeEqualParts(int[] A) {
        int[] IMP = new int[]{-1, -1};
        int N = A.length;

        int sum = 0;
        for (int x : A) sum += x;
        if (sum % 3 != 0) return IMP;
        int T = sum / 3;
        if (T == 0) return new int[]{0, N - 1};

        int i1 = -1, j1 = -1, i2 = -1, j2 = -1, i3 = -1, j3 = -1;
        int su = 0;

        for (int i = 0; i < N; i++) {
            if (A[i] == 1) {
                su += 1;
                if (su == 1) i1 = i;
                if (su == T) j1 = i;
                if (su == T+1) i2 = i;
                if (su == 2*T) j2 = i;
                if (su == 2*T + 1) i3 = i;
                if (su == 3*T) j3 = i;
            }
        }

        // The array is in the form W [i1, j1] X [i2, j2] Y [i3, j3] Z
        // where [i1, j1] is a block of 1s, etc.
        int[] part1 = Arrays.copyOfRange(A, i1, j1+1);
        int[] part2 = Arrays.copyOfRange(A, i2, j2+1);
        int[] part3 = Arrays.copyOfRange(A, i3, j3+1);

        if (!Arrays.equals(part1, part2)) return IMP;
        if (!Arrays.equals(part1, part3)) return IMP;

        // x, y, z: the number of zeros after part 1, 2, 3
        int x = i2 - j1 - 1;
        int y = i3 - j2 - 1;
        int z = A.length - j3 - 1;

        if (x < z || y < z) return IMP;
        return new int[]{j1 + z, j2 + z + 1};
    }
}

# 6ms 100%
class Solution {
    public int[] threeEqualParts(int[] A) {
        int[] sum = new int[A.length];
        int s = 0;
        for (int i = 0; i < A.length; i++) {
            s += A[i];
            sum[i] = s;
        }

        if (s == 0) return new int[]{0, A.length - 1};
        if (s % 3 != 0) return new int[]{-1, -1};
        s /= 3;
        int i = bs(sum, s), j = bs(sum, s + s), k = bs(sum, s * 3);
        int zero = A.length - 1 - k;
        if(sum[i] != sum[i + zero] || sum[j] != sum[j + zero])
            return new int[]{-1, -1};
        i += zero;
        j += zero;
        k += zero;
        int ii = i, jj = j, kk = k;
        while(jj > i && kk > j && ii >= 0) {
            if(A[ii] == A[jj] && A[jj] == A[kk]) {
                ii--;
                jj--;
                kk--;
            } else {
                return new int[]{-1, -1};
            }
        }
        return new int[]{i, j+1};
    }

    private int bs(int[] a, int t) {
        int lo = 0, hi = a.length-1;
        while(lo <= hi) {
            int m = (lo + hi) >>> 1;
            if(a[m] >= t)
                hi = m - 1;
            else
                lo = m + 1;
        }
        return lo;
    }
}
'''