__source__ = 'https://leetcode.com/problems/repeated-string-match/'
# Time:  O(n * (m + n) where M, NM,N are the lengths of strings A, B. We create two strings A * q, A * (q+1)
# which have length at most O(M+N). When checking whether B is a substring of A,
# this check takes naively the product of their lengths.
# Space: O(m + n)
#
# Description: Leetcode # 686. Repeated String Match
#
# Given two strings A and B,
# find the minimum number of times A has to be repeated such that B is a substring of it.
# If no such solution, return -1.
#
# For example, with A = "abcd" and B = "cdabcdab".
#
# Return 3, because by repeating A three times ("abcdabcdabcd"), B is a substring of it.
# and B is not a substring of A repeated two times ("abcdabcd").
#
# Note:
# The length of A and B will be between 1 and 10000.
#
import unittest

# 112ms 75.69%
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        q = (len(B) - 1) // len(A) + 1
        for i in range(2):
            if B in A * (q+i): return q+i
        return -1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/repeated-string-match/solution/
#
# 209ms 29.32%
class Solution {
    public int repeatedStringMatch(String A, String B) {
        int sum = 1;
        StringBuilder sb = new StringBuilder(A);
        for (; sb.length() < B.length(); sum++) sb.append(A);
        if (sb.indexOf(B) >= 0) return sum;
        if (sb.append(A).indexOf(B) >= 0) return sum+1;
        return -1;
    }
}
'''
