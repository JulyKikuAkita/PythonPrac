__source__ = 'https://leetcode.com/problems/array-of-doubled-pairs/'
# Time:  O(NLogN)
# Space: O(N)
#
# Description: Leetcode # 954. Array of Doubled Pairs
#
# Given an array of integers A with even length,
# return true if and only if it is possible to reorder it
# such that A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.
#
# Example 1:
#
# Input: [3,1,3,6]
# Output: false
#
# Example 2:
#
# Input: [2,1,2,6]
# Output: false
#
# Example 3:
#
# Input: [4,-2,2,-4]
# Output: true
# Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
#
# Example 4:
#
# Input: [1,2,4,16,8,4]
# Output: false
#
# Note:
#
#     0 <= A.length <= 30000
#     A.length is even
#     -100000 <= A[i] <= 100000
#
import unittest
import collections
# 720ms 9.96%
class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        count = collections.Counter(A)
        for x in sorted(A, key = abs):
            if count[x] == 0: continue
            if count[2*x] == 0: return False
            count[x] -= 1
            count[2*x] -= 1
        return True

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/array-of-doubled-pairs/solution/
#
Approach 1: Greedy
Complexity Analysis
Time Complexity: O(NLogN), where N is the length of A.
Space Complexity: O(N)

# 311ms 5.12%
class Solution {
    public boolean canReorderDoubled(int[] A) {
        // count[x] = the number of occurrences of x in A
        Map<Integer, Integer> count = new HashMap();
        for (int x: A) count.put(x, count.getOrDefault(x, 0) + 1);
        
        // B = A as Integer[], sorted by absolute value
        Integer[] B = new Integer[A.length];
        for (int i = 0; i < A.length; ++i) B[i] = A[i];
        Arrays.sort(B, Comparator.comparingInt(Math::abs));
        
        for (int x: B) {
            // If this can't be consumed, skip
            if (count.get(x) == 0) continue;
            // If this doesn't have a doubled partner, the answer is false
            if (count.getOrDefault(2*x, 0) <= 0) return false;

            // Write x, 2*x
            count.put(x, count.get(x) - 1);
            count.put(2*x, count.get(2*x) - 1);
        }

        // If we have written everything, the answer is true
        return true;
    }
}

# 22ms 95.50%
class Solution {
    public boolean canReorderDoubled(int[] A) {
        if (A == null || A.length == 0) return true;
        int len = A.length;
        //if(len % 2 != 0) return false;
        int flag = 1;
        for (int i = 0; i < A.length; i++) {
            flag *= A[i];
            A[i] = Math.abs(A[i]);
        }
        int[] freq = new int[100000];
        for (int i = 0; i < A.length; i++) freq[A[i]]++;
        for (int i = 0; i < 100000; ){
            if (freq[i] == 0) {
                i++;
                continue;
            }
            while (freq[i] > 0) {
                if (freq[i * 2] == 0) return false;
                freq[i * 2]--;
                freq[i]--;
            }
            i++;
        }
        return true;
    }
}

# 21ms 96.08%
class Solution {
    public boolean canReorderDoubled(int[] A) {
        //TreeMap : ordered tree (natural) based on red-black tree
        Map<Integer, Integer> count = new TreeMap<>();
        for (int a : A) count.put(a, count.getOrDefault(a, 0) + 1);
        for (int x : count.keySet()) {
            if (count.get(x) == 0) continue;
            int want = x < 0 ? x / 2 : x * 2;
            // order for positive: 1 2 4 8
            // order for negative: -8 -4 -2 -1
            // 5 can search for 5 * 2 = 10
            // -5 can not search for -5/2=-2
            if (x < 0 && x % 2 != 0 || count.get(x) > count.getOrDefault(want, 0)) return false;
            count.put(want, count.get(want) - count.get(x));
        }
        return false;
    }
}
'''
