__source__ = 'https://leetcode.com/problems/groups-of-special-equivalent-strings/description/'
# Time:  O(sum of str length of all input string)
# Space: O(N)
#
# Description: Leetcode # 893. Groups of Special-Equivalent Strings
#
# You are given an array A of strings.
#
# Two strings S and T are special-equivalent if after any number of moves, S == T.
#
# A move consists of choosing two indices i and j with i % 2 == j % 2, and swapping S[i] with S[j].
#
# Now, a group of special-equivalent strings from A is a non-empty subset S of A
# such that any string not in S is not special-equivalent with any string in S.
#
# Return the number of groups of special-equivalent strings from A.
#
#
#
# Example 1:
#
# Input: ["a","b","c","a","c","c"]
# Output: 3
# Explanation: 3 groups ["a","a"], ["b"], ["c","c","c"]
# Example 2:
#
# Input: ["aa","bb","ab","ba"]
# Output: 4
# Explanation: 4 groups ["aa"], ["bb"], ["ab"], ["ba"]
# Example 3:
#
# Input: ["abc","acb","bac","bca","cab","cba"]
# Output: 3
# Explanation: 3 groups ["abc","cba"], ["acb","bca"], ["bac","cab"]
# Example 4:
#
# Input: ["abcd","cdab","adcb","cbad"]
# Output: 1
# Explanation: 1 group ["abcd","cdab","adcb","cbad"]
#
#
# Note:
#
# 1 <= A.length <= 1000
# 1 <= A[i].length <= 20
# All A[i] have the same length.
# All A[i] consist of only lowercase letters.
#
# Note, to understand the q, the wording of the question is unnecessarily complex,
# so here's an alternate, hopefully simpler explanation.
# A "group" consists of a subset of the original A that has the same letters at all even positions
# (in any order) and the same letter in all odd positions (in any order).
# Hence, the original set A can unambiguously be separated into N non-overlapping groups.
# The goal is to find N.
#
import unittest

#32 ms 88.32%
class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        s = set()
        for w in A:
            even = ''.join(sorted(w[0::2]))
            odd = ''.join(sorted(w[1::2]))
            s.add(odd + even)
        return len(s)

#36ms 67.99%
class Solution2(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def count(A):
            ans = [0] * 52
            for i, letter in enumerate(A):
                ans[ord(letter) - ord('a') + 26 * (i % 2)] += 1
            return tuple(ans)
        return len({count(word) for word in A})

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/groups-of-special-equivalent-strings/solution/
# Thus, the function \mathcal{C}(S) =C(S)= (the count of the even indexed letters in S,
# followed by the count of the odd indexed letters in S)
# successfully characterizes the equivalence relation.
#
# Time Complexity: O(\sum\limits_{i} (A_i){.length})
# Space Complexity: O(N), where NN is the length of A.
#
#67.92% 19ms
class Solution {
    public int numSpecialEquivGroups(String[] A) {
        Set<String> seen = new HashSet();
        for (String str : A) {
            int[] count = new int[52];
            for (int i = 0; i < str.length(); i++) {
                count[str.charAt(i) - 'a' + 26 * (i % 2)]++;
            }
            seen.add(Arrays.toString(count));
        }
        return seen.size();
    }
}

#97.65% 7ms
class Solution {
    public int numSpecialEquivGroups(String[] A) {
        Set set = new HashSet<>();
        for (String s : A) {
            StringBuilder odd = new StringBuilder();
            StringBuilder even = new StringBuilder();
            for (int i = 0, len = s.length(); i < len; i++) {
                if (i % 2 == 0) {
                    even.append(s.charAt(i));
                } else {
                    odd.append(s.charAt(i));
                }
            }
            char[] oddArray = odd.toString().toCharArray();
            char[] evenArray = even.toString().toCharArray();
            Arrays.sort(oddArray);
            Arrays.sort(evenArray);
            set.add("" + new String(oddArray) + new String(evenArray));
        }
        return set.size();
    }
}
'''