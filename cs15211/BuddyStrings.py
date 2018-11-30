import itertools

__source__ = 'https://leetcode.com/problems/buddy-strings/'
# Time:  O(N) where NN is the length of A and B
# Space: O(1)
#
# Description: Leetcode # 859. Buddy Strings
#
# Given two strings A and B of lowercase letters,
# return true if and only if we can swap two letters in A so that the result equals B.
#
# Example 1:
#
# Input: A = "ab", B = "ba"
# Output: true
# Example 2:
#
# Input: A = "ab", B = "ab"
# Output: false
# Example 3:
#
# Input: A = "aa", B = "aa"
# Output: true
# Example 4:
#
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
# Example 5:
#
# Input: A = "", B = "aa"
# Output: false
#
#
# Note:
#
# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A and B consist only of lowercase letters.
#
import unittest

#88.96% 24ms
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):return False
        if A == B: # True when A can swap 2 identical chars
            seen = set()
            for a in A:
                if a in seen:
                    return True
                seen.add(a)
            return False
        else:
            pairs = []
            for a, b in itertools.izip(A, B):
                if a != b:
                    pairs.append((a, b))
                if len(pairs) >= 3:
                    return False
            return len(pairs) == 2 and pairs[0] == pairs[1][::-1]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/buddy-strings/solution/
#
# If swapping A[i] and A[j] would demonstrate that A and B are buddy strings,
# then A[i] == B[j] and A[j] == B[i]. That means among the four free variables A[i], A[j],
# B[i], B[j], there are only two cases: either A[i] == A[j] or not.
#

# 2ms 99.73$
class Solution {
    public boolean buddyStrings(String A, String B) {
        if (A.length() != B.length()) return false;
        if (A.equals(B)) {
            int[] count = new int[26];
            for (char c : A.toCharArray()) {
                count[c-'a']++;
            }

            for (int cnt : count) {
                if (cnt > 1) return true;
            }
            return false;
        } else {
            int first = -1, second = -1;
            for (int i = 0; i < A.length(); i++) {
                if (A.charAt(i) != B.charAt(i)) {
                    if (first == -1) first = i;
                    else if (second == -1) second = i;
                    else return false;
                }
            }
            return (second != -1 && A.charAt(first) == B.charAt(second) && A.charAt(second) == B.charAt(first));
        }

    }
}
'''