__source__ = 'https://leetcode.com/problems/bitwise-ors-of-subarrays/'
# Time:  O(NlogW)
# Space: O(NlogW)
#
# Description: Leetcode # 898. Bitwise ORs of Subarrays
#
# We have an array A of non-negative integers.
#
# For every (contiguous) subarray B = [A[i], A[i+1], ..., A[j]] (with i <= j),
# we take the bitwise OR of all the elements in B, obtaining a result A[i] | A[i+1] | ... | A[j].
#
# Return the number of possible results.
# (Results that occur more than once are only counted once in the final answer.)#
#
# Example 1:
#
# Input: [0]
# Output: 1
# Explanation:
# There is only one possible result: 0.
# Example 2:
#
# Input: [1,1,2]
# Output: 3
# Explanation:
# The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
# These yield the results 1, 1, 2, 1, 3, 3.
# There are 3 unique values, so the answer is 3.
# Example 3:
#
# Input: [1,2,4]
# Output: 6
# Explanation:
# The possible results are 1, 2, 3, 4, 6, and 7.
#
# Note:
#
# 1 <= A.length <= 50000
# 0 <= A[i] <= 10^9
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
# Thought: https://leetcode.com/problems/bitwise-ors-of-subarrays/solution/
Approach 1: Frontier Set
Note: 1,
result(i, j) = A[i] | A[i+1] | ... | A[j] then
result(i, j+1) = result(i, j) | A[j+1]
Note: 2,
the number of unique values in this set cur is at most 32,
since the list result(k, k), result(k-1, k), result(k-2, k), ... is monotone increasing,
and any subsequent values that are different must have more 1s in it's binary representation (to a maximum of 32 ones).
Complexity Analysis
Time Complexity: O(NlogW), where N is the length of A, and WW is the maximum size of elements in A.
Space Complexity: O(NlogW), the size of the answer.

#509ms 20%
class Solution {
    public int subarrayBitwiseORs(int[] A) {
        Set<Integer> ans = new HashSet();
        Set<Integer> cur = new HashSet();
        cur.add(0);
        for (int x : A) {
            Set<Integer> cur2 = new HashSet();
            for (int y : cur) cur2.add(x | y);
            cur2.add(x);
            cur = cur2;
            ans.addAll(cur);
        }
        return ans.size();
    }
}

#193ms 99.76%
class Solution {
    public int subarrayBitwiseORs(int[] A) {
        Set<Integer> set = new HashSet<>();
        int ors = 0, res = 0, cum = 0;
        for (int i = 0; i < A.length; i++) {
            int cand = 0;
            for (int j = i; j >= 0; j--) {
                cand |= A[j];
                set.add(cand);
                if ((cand & (cand + 1)) == 0 && cand >= cum) break;
            }
            cum |= A[i];
        }
        return set.size();
    }
}

#203ms 99.52%
class Solution {
    public int subarrayBitwiseORs(int[] A) {
        if (A == null || A.length == 0) return 0;
        int n = A.length;

        // initialize
        Set<Integer> seen = new HashSet<>();
        for (int i = 0; i < A.length; i++) seen.add(A[i]);

        // join pairs [i] and [i+1]
        int end = A.length - 1;
        while (end >= 1) {
            for (int i = 0; i < end; i++) A[i] |= A[i + 1];

            // filter out consecutive duplicates in array and add [i] to the set
            int i = 0;
            seen.add(A[i]);
            int j = 1;
            while (j < end) {
                if (A[i] != A[j]) {
                    A[++i] = A[j];
                    seen.add(A[i]);
                }
                j++;
            }
            end = i;
        }
        return seen.size();
    }
}
'''