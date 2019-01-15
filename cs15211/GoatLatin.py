__source__ = 'https://leetcode.com/problems/goat-latin/'
# Time:  O(N^2)
# Space: O(N^2)
#
# Description: Leetcode # 824. Goat Latin
#
# A sentence S is given, composed of words separated by spaces.
# Each word consists of lowercase and uppercase letters only.
#
# We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)
#
# The rules of Goat Latin are as follows:
#
#     If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
#     For example, the word 'apple' becomes 'applema'.
#
#     If a word begins with a consonant (i.e. not a vowel),
# remove the first letter and append it to the end, then add "ma".
#     For example, the word "goat" becomes "oatgma".
#
#     Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
#     For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
#
# Return the final sentence representing the conversion from S to Goat Latin.
#
# Example 1:
#
# Input: "I speak Goat Latin"
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
#
# Example 2:
#
# Input: "The quick brown fox jumped over the lazy dog"
# Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa
# overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
#
# Notes:
#
#     S contains only uppercase, lowercase and spaces. Exactly one space between each word.
#     1 <= S.length <= 150.
#

import unittest

# 20ms 100%
class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        def convert(word):
            if word[0] not in 'aeiouAEIOU':
                word = word[1:] + word[:1]
            return word + 'ma'

        return " ".join(convert(word) + 'a' * i
                        for i, word in enumerate(S.split(), 1))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/goat-latin/solution/
Approach #1: String [Accepted]
Complexity Analysis
Time Complexity: O(N^2), where N is the length of S.
This represents the complexity of rotating the word and adding extra "a" characters.
Space Complexity: O(N^2), the space added to the answer by adding extra "a" characters.

# 10ms 30.85%
class Solution {
    public String toGoatLatin(String S) {
        String[] words = S.split(" ");
        StringBuilder sb = new StringBuilder();
        Set<Character> vowels = new HashSet<Character>();
        for (char c : "aeiou".toCharArray()) {
            vowels.add(c);
        }

        for (int i = 0; i < words.length; i++) {
            if (vowels.contains(words[i].toLowerCase().toCharArray()[0])) { //if start with vowel
                sb.append(words[i]);
            } else { //if start with constant
                sb.append(words[i].substring(1));
                sb.append(words[i].substring(0,1));
            }
            sb.append("ma");

            for (int j = i; j >= 0 ;j--) {
                sb.append('a');
            }
            if (i < words.length - 1) sb.append(" ");
        }
        return sb.toString();
    }
}

# 5ms 98.82%
class Solution {
    public String toGoatLatin(String S) {
        Set<Character> vowel = new HashSet();
        for (char c: new char[]{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}) vowel.add(c);
        int t = 1;
        StringBuilder ans = new StringBuilder();
        for (String word: S.split(" ")) {
            char first = word.charAt(0);
            if (vowel.contains(first)) ans.append(word);
            else {
                ans.append(word.substring(1));
                ans.append(word.substring(0, 1));
            }
            ans.append("ma");
            for (int i = 0; i < t; i++) ans.append("a");
            t++;
            ans.append(" ");
        }
        ans.deleteCharAt(ans.length() - 1);
        return ans.toString();
    }
}
'''