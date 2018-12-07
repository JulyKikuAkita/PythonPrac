# coding=utf-8
__source__ = 'https://leetcode.com/problems/fair-candy-swap/'
# Time:  O(A +B)
# Space: O(Min(A, B))
#
# Description: Leetcode # 888. Fair Candy Swap
#
# Alice and Bob have candy bars of different sizes:
# A[i] is the size of the i-th bar of candy that Alice has,
# and B[j] is the size of the j-th bar of candy that Bob has.
#
# Since they are friends, they would like to exchange one candy bar each so that after the exchange,
# they both have the same total amount of candy.
# (The total amount of candy a person has is the sum of the sizes of candy bars they have.)
#
# Return an integer array ans where ans[0] is the size of the candy bar that Alice must exchange,
# and ans[1] is the size of the candy bar that Bob must exchange.
#
# If there are multiple answers, you may return any one of them.  It is guaranteed an answer exists.
#
# Example 1:
#
# Input: A = [1,1], B = [2,2]
# Output: [1,2]
# Example 2:
#
# Input: A = [1,2], B = [2,3]
# Output: [1,2]
# Example 3:
#
# Input: A = [2], B = [1,3]
# Output: [2,3]
# Example 4:
#
# Input: A = [1,2,5], B = [2,4]
# Output: [5,4]
#
#
# Note:
#
# 1 <= A.length <= 10000
# 1 <= B.length <= 10000
# 1 <= A[i] <= 100000
# 1 <= B[i] <= 100000
# It is guaranteed that Alice and Bob have different total amounts of candy.
# It is guaranteed there exists an answer.
#
import unittest

# 48ms 97.59%
class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        Sa, Sb = sum(A), sum(B)
        setB = set(B)
        for x in A:
            if x + (Sb - Sa) / 2 in setB:
                return [x, x + (Sb - Sa) / 2]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/fair-candy-swap/solution/
Approach 1: Solve the Equation
Complexity Analysis
Time Complexity: O(A.length+B.length).
Space Complexity: O(B.length), the space used by setB. (
We can improve this to min(A.length,B.length) by using an if statement.)

# 19ms 90.79%
class Solution {
    public int[] fairCandySwap(int[] A, int[] B) {
        int sa = 0, sb = 0;  // sum of A, B respectively
        for (int x: A) sa += x;
        for (int x: B) sb += x;
        int delta = (sb - sa) / 2;
        // If Alice gives x, she expects to receive x + delta

        Set<Integer> setB = new HashSet();
        for (int x: B) setB.add(x);

        for (int x: A)
            if (setB.contains(x + delta))
                return new int[]{x, x + delta};

        throw null;
    }
}

# 10ms 99.21%
class Solution {
    public int[] fairCandySwap(int[] A, int[] B) {
        int s = 0;
        BitSet set = new BitSet();
        for(int i = 0;i< A.length;i++) {
            s = s + A[i];
            set.set(A[i]);
        }
        for(int i = 0;i< B.length;i++) {
            s = s - B[i];
        }
        int a;
        for(int i = 0;i < B.length;i++) {
            if((a = B[i] + s / 2) > 0 && set.get(a)){
                return new int[]{a, B[i]};
            }
        }
        return null;
    }
}

# 7ms 99.84%
class Solution {
    public int[] fairCandySwap(int[] A, int[] B) {

        int[] result = new int[2];
        int sumA = 0, sumB = 0;
        for (int i = 0; i < A.length; i++) {
            sumA += A[i];
        }
        for (int i = 0; i < B.length; i++) {
            sumB += B[i];
        }
        // 记录数组 B 存在的数
        boolean[] exist = new boolean[200000];
        for (int i = 0; i < B.length; i++) {
            exist[B[i]] = true;
        }

        for (int i = 0; i < A.length; i++) {
            int x = sumB - sumA + 2*A[i];
            if (x>=0 && x%2==0 && exist[x/2]){
                result[0] = A[i];
                result[1] = x/2;
                break;
            }
        }
        return result;
    }
}
'''