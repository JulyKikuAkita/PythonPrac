__source__ = 'https://leetcode.com/problems/n-repeated-element-in-size-2n-array/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 961. N-Repeated Element in Size 2N Array
#
# In a array A of size 2N, there are N+1 unique elements,
# and exactly one of these elements is repeated N times.
#
# Return the element repeated N times.
#
# Example 1:
#
# Input: [1,2,3,3]
# Output: 3
#
# Example 2:
#
# Input: [2,1,2,5,3,2]
# Output: 2
#
# Example 3:
#
# Input: [5,1,5,2,5,3,5,4]
# Output: 5
#
# Note:
#     4 <= A.length <= 10000
#     0 <= A[i] < 10000
#     A.length is even
#
import unittest
# 44ms 79.92%
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for k in xrange(1, 4):
            for i in xrange(len(A) - k):
                if A[i] == A[i+k]:
                    return A[i]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/solution/
#
Approach 1: Count
Complexity Analysis
Time Complexity: O(N), where N is the length of A.
Space Complexity: O(N)
# 55ms 9.20%
class Solution {
    public int repeatedNTimes(int[] A) {
        Map<Integer, Integer> count = new HashMap();
        for (int x: A) {
            count.put(x, count.getOrDefault(x, 0) + 1);
        }

        for (int k: count.keySet())
            if (count.get(k) > 1)
                return k;

        throw null;
    }
}


Approach 2: Compare
Complexity Analysis
Time Complexity: O(N), where N is the length of A.
Space Complexity: O(1)
# 7ms 77.46%
class Solution {
    public int repeatedNTimes(int[] A) {
        for (int k = 1; k <= 3; ++k)
            for (int i = 0; i < A.length - k; ++i)
                if (A[i] == A[i+k])
                    return A[i];

        throw null;
    }
}

# 8ms 66.46%
class Solution {
    public int repeatedNTimes(int[] A) {
        Set<Integer> set = new HashSet<>();
        for (int x : A) {
            if (set.contains(x)) return x;
            set.add(x);
        }
        throw null;
    }
}
'''
