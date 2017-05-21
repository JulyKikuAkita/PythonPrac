__source__ = 'https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/#/description'
# Time:  O(nlogn + n*x), Sorting takes O(nlogn) and isSubsequence takes O(x)
# Space: O(logn) Sorting takes O(logn) space in average case.
#
# Description:
# Given a string and a string dictionary, find the longest string in the dictionary
# that can be formed by deleting some characters of the given string.
# If there are more than one possible results, return the longest word with the smallest lexicographical order.
# If there is no possible result, return the empty string.
#
# Example 1:
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
#
# Output:
# "apple"
# Example 2:
# Input:
# s = "abpcplea", d = ["a","b","c"]
#
# Output:
# "a"
#
# Note:
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.
# Hide Company Tags Google
# Hide Tags Two Pointers Sort

import unittest
# Let's check whether each word is a subsequence of S individually by "best" order
# (largest size, then lexicographically smallest.) Then if we find a match,
# we know the word being considered must be the best possible answer,
# since better answers were already considered beforehand.
#
# Let's figure out how to check if a needle (word) is a subsequence of a haystack (S).
# This is a classic problem with the following solution: walk through S,
# keeping track of the position (i) of the needle that indicates that word[i:]
# still remains to be matched to S at this point in time. Whenever word[i] matches the current character in S,
# we only have to match word[i+1:], so we increment i. At the end of this process, i == len(word)
# if and only if we've matched every character in word to some character in S in order of our walk.

class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort(key = lambda x: (-len(x), x))
        for word in d:
            i = 0
            for c in s:
                if i < len(word) and word[i] == c:
                    i += 1
            if i == len(word):
                return word
        return ""

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/longest-word-in-dictionary-through-deletion/
1.
An alternate, more efficient solution which avoids sorting the dictionary:

#80.93$
public class Solution {
    public String findLongestWord(String s, List<String> d) {
        String res = "";
        for (String key : d) {
            int i = 0;
            for ( char c : s.toCharArray()) {
                if ( i < key.length() && c == key.charAt(i)) i++;
            }
            if (i == key.length() && key.length() >= res.length()) {
                if (key.length() > res.length() || key.compareTo(res) < 0) { //asec
                    res = key;
                }
            }
        }
        return res;
    }
}

2. 15.12%
Idea is sort the dictionary d first by length DESC then lexicographical ASC
and test if p is SubSequence of s. The first match is the answer.

public class Solution {
    public String findLongestWord(String s, List<String> d) {
        if (s.length() == 0 || d.size() == 0) return "";

        //sort dict:
        Collections.sort(d, (a, b) -> {
            return s2.length() != s1.length() ?
                s2.length() - s1.length() :  //desc
                s1.compareTo(s2); //asec
        });

        for (String key : d) {
            if (s.length() < key.length()) continue;
            if (isSubSeq(key, s)) return key;
        }
        return "";
    }

    public boolean isSubSeq(String needle, String Hay) {
        int i = 0;
        for (char c : Hay.toCharArray()) {
            if (i < needle.length() && c == needle.charAt(i)) {
                i++;
            }
        }
        return i == needle.length();
    }
}
'''