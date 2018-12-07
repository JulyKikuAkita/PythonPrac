__source__ = ' https://leetcode.com/problems/custom-sort-string/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 791. Custom Sort String
#
# S and T are strings composed of lowercase letters. In S, no letter occurs more than once.
#
# S was sorted in some custom order previously.
# We want to permute the characters of T so that they match the order that S was sorted.
# More specifically, if x occurs before y in S,
# then x should occur before y in the returned string.
#
# Return any permutation of T (as a string) that satisfies this property.
#
# Example :
# Input:
# S = "cba"
# T = "abcd"
# Output: "cbad"
# Explanation:
# "a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
# Since "d" does not appear in S, it can be at any position in T.
# "dcba", "cdba", "cbda" are also valid outputs.
#
#
# Note:
#
# S has length at most 26, and no character is repeated in S.
# T has length at most 200.
# S and T consist of lowercase letters only.
#
#
import unittest
import collections

class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        count = collections.Counter(T)
        ans = []

        for c in S:
            ans.append(c * count[c])
            count[c] = 0
        for c in count:
            ans.append(c * count[c])
        return "".join(ans)

class Solution2(object):
    def customSortString(self, S, T):
        off_list=[]
        on_list=[]
        for i in range(0,len(S)):
            counted=T.count(S[i])
            if S[i] in T:
                on_list.append(counted*S[i])
        for i in range (0,len(T)):
            if T[i] not in S:
                off_list.append(T[i])
        return ("".join(on_list+off_list))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/custom-sort-string/solution/
# Approach #1: Count and Write [Accepted]
#
# Time Complexity: O(S.length+T.length), the time it takes to iterate through S and T
# Space Complexity: O(T.length). We count at most 26 different lowercase letters,
# but the final answer has the same length as T.
#
# 2ms 100%
class Solution {
    public String customSortString(String S, String T) {
        int[] count = new int[26];
        for(char c: T.toCharArray()){
            count[c-'a']++;
        }
        StringBuilder sb= new StringBuilder();

        for(char c: S.toCharArray()){
            while(count[c-'a']-- >0) sb.append(c);

        }
        for(int i=0;i<26;i++){
            while(count[i]-- >0) sb.append((char)(i+'a'));
        }
        return sb.toString();
    }
}

'''