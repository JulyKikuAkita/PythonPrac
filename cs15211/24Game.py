__source__ = 'https://leetcode.com/problems/24-game/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode #
#
# You have 4 cards each containing a number from 1 to 9.
# You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.
#
# Example 1:
# Input: [4, 1, 8, 7]
# Output: True
# Explanation: (8-4) * (7-1) = 24
# Example 2:
# Input: [1, 2, 1, 2]
# Output: False
# Note:
# The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
# Every operation done is between two numbers. In particular, we cannot use - as a unary operator.
#
# For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
# You cannot concatenate numbers together.
# For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
#
# Companies
# Google
# Related Topics
# Depth-first Search
#
#1413ms
import unittest
import itertools
from operator import truediv, mul, add, sub
from fractions import Fraction
class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def apply(A, B):
            ans = set()
            for x, y, op in itertools.product(A, B, (truediv, mul, add, sub)):
                if op is not truediv or y: ans.add(op(x, y))
                if op is not truediv or x: ans.add(op(y, x))
            return ans

        A = [{x} for x in map(Fraction, nums)]
        for i, j in itertools.combinations(range(4), 2):
            r1 = apply(A[i], A[j])
            k, l = {0, 1, 2, 3} - {i, j}
            if 24 in apply(apply(r1, A[k]), A[l]): return True
            if 24 in apply(apply(r1, A[l]), A[k]): return True
            if 24 in apply(r1, apply(A[k], A[l])): return True

        return False

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/24-game/

Given: (a, b, c, d) - (A tuple of 4)
Generate:

((a+b),c,d) ((a-b),c,d) ((b-a),c,d) ((a*b),c,d) ((a/b),c,d) ((b/a),c,d)
((a+c),b,d) ................................................................. ((c/a),b,d)
((a+d),b,c) ................................................................. ((d/a),b,c)
(a,(b+c),d) ................................................................. (a,(c/b),d)
(a,(b+d),d) ................................................................. (a,(d/b),d)
(a,b,(c+d)) ................................................................. (a,b,(d/c))
There are 36 (6*6) such tuples. Of these, + & - are not order dependent. That is 2+3 = 3+2.
But / & - are order dependent. i.e. 2/3 != 3/2. These look like (e,f,g) i.e. a tuple of 3 now.

Carrying out similar reductions gives 18 (6*3) tuples for each of the above-generated tuples.
These now look like (h, i) i.e. a tuple of 2 now.

Similiar, the final reduction now yields 6 answers (a+b, a-b, a*b, a/b, b-a, b/a)
for each of the above-generated tuple.

Thus in total 36x18x6 final values can be generated using the 4 operators and 4 initial values.

Algo: Generate all such answers using dfs method and stop when it's 24.

Catches:

Use double instead of int
Be careful about the classical divide by zero error

#23ms
class Solution {
    public boolean judgePoint24(int[] nums) {
        ArrayList A = new ArrayList<Double>();
        for (int v: nums) A.add((double) v);
        return solve(A);
    }
    private boolean solve(ArrayList<Double> nums) {
        if (nums.size() == 0) return false;
        if (nums.size() == 1) return Math.abs(nums.get(0) - 24) < 1e-6;

        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < nums.size(); j++) {
                if (i != j) {
                    ArrayList<Double> nums2 = new ArrayList<Double>();
                    for (int k = 0; k < nums.size(); k++) if (k != i && k != j) {
                        nums2.add(nums.get(k));
                    }
                    for (int k = 0; k < 4; k++) {
                        if (k < 2 && j > i) continue;
                        if (k == 0) nums2.add(nums.get(i) + nums.get(j));
                        if (k == 1) nums2.add(nums.get(i) * nums.get(j));
                        if (k == 2) nums2.add(nums.get(i) - nums.get(j));
                        if (k == 3) {
                            if (nums.get(j) != 0) {
                                nums2.add(nums.get(i) / nums.get(j));
                            } else {
                                continue;
                            }
                        }
                        if (solve(nums2)) return true;
                        nums2.remove(nums2.size() - 1);
                    }
                }
            }
        }
        return false;
    }
}

'''