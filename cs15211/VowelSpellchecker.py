__source__ = 'https://leetcode.com/problems/vowel-spellchecker/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 966. Vowel Spellchecker
#
# Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.
#
# For a given query word, the spell checker handles two categories of spelling mistakes:
#
#     Capitalization: If the query matches a word in the wordlist (case-insensitive),
# then the query word is returned with the same case as the case in the wordlist.
#         Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
#         Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
#         Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
#     Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word
# with any vowel individually, it matches a word in the wordlist (case-insensitive),
# then the query word is returned with the same case as the match in the wordlist.
#         Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
#         Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
#         Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
#
# In addition, the spell checker operates under the following precedence rules:
#
#     When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
#     When the query matches a word up to capitlization, you should return the first such match in the wordlist.
#     When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
#     If the query has no matches in the wordlist, you should return the empty string.
#
# Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].
#
# Example 1:
#
# Input: wordlist = ["KiTe","kite","hare","Hare"],
# queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
# Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
#
# Note:
#
#     1 <= wordlist.length <= 5000
#     1 <= queries.length <= 5000
#     1 <= wordlist[i].length <= 7
#     1 <= queries[i].length <= 7
#     All strings in wordlist and queries consist only of english letters.
#
import unittest
# 296ms 52.32%
class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        def devowel(word):
            return "".join('*' if c in 'aeiou' else c
                           for c in word)

        words_perfect = set(wordlist)
        words_cap = {}
        words_vow = {}

        for word in wordlist:
            wordlow = word.lower()
            words_cap.setdefault(wordlow, word)
            words_vow.setdefault(devowel(wordlow), word)

        def solve(query):
            if query in words_perfect:
                return query

            queryL = query.lower()
            if queryL in words_cap:
                return words_cap[queryL]

            queryLV = devowel(queryL)
            if queryLV in words_vow:
                return words_vow[queryLV]
            return ""

        return map(solve, queries)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/vowel-spellchecker/solution/
#
Approach 1: HashMap
Complexity Analysis
Time Complexity: O(C), where C is the total content of wordlist and queries.
Space Complexity: O(C)
# 47ms 78.76%
class Solution {
    Set<String> words_perfect;
    Map<String, String> words_cap;
    Map<String, String> words_vow;

    public String[] spellchecker(String[] wordlist, String[] queries) {
        words_perfect = new HashSet();
        words_cap = new HashMap();
        words_vow = new HashMap();

        for (String word: wordlist) {
            words_perfect.add(word);

            String wordlow = word.toLowerCase();
            words_cap.putIfAbsent(wordlow, word);

            String wordlowDV = devowel(wordlow);
            words_vow.putIfAbsent(wordlowDV, word);
        }

        String[] ans = new String[queries.length];
        int t = 0;
        for (String query: queries)
            ans[t++] = solve(query);
        return ans;
    }

    public String solve(String query) {
        if (words_perfect.contains(query))
            return query;

        String queryL = query.toLowerCase();
        if (words_cap.containsKey(queryL))
            return words_cap.get(queryL);

        String queryLV = devowel(queryL);
        if (words_vow.containsKey(queryLV))
            return words_vow.get(queryLV);

        return "";
    }

    public String devowel(String word) {
        StringBuilder ans = new StringBuilder();
        for (char c: word.toCharArray())
            ans.append(isVowel(c) ? '*' : c);
        return ans.toString();
    }

    public boolean isVowel(char c) {
        return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
    }
}

# 37ms 93.98%
class Solution {
    public String[] spellchecker(String[] wordlist, String[] queries) {
        String[] result = new String[queries.length];
        HashMap<String,String> hashMap = new HashMap<>();
        HashSet<String> wordSet = new HashSet<>();
        for (String s : wordlist){
            wordSet.add(s);
            hashMap.putIfAbsent(s.toLowerCase(), s);
            hashMap.putIfAbsent(wordPattern(s), s);
        }
        
        for (int i = 0; i < queries.length; i++){
            if (wordSet.contains(queries[i])) {
                result[i] = queries[i];
                continue;
            }
            if (hashMap.containsKey(queries[i].toLowerCase())){
                result[i] = hashMap.get(queries[i].toLowerCase());
                continue;
            }
            String pattern = wordPattern(queries[i]);
            if (hashMap.containsKey(pattern)){
                result[i] = hashMap.get(pattern);
                continue;
            }
            else
                result[i] = "";
        }
        return result;
    }
    
    public String wordPattern(String s){
        char[] chars = s.toLowerCase().toCharArray();
        for(int i = 0; i < chars.length; i++){
            if (chars[i] == 'a' || chars[i] == 'e' || chars[i] == 'i' || chars[i] == 'o' || chars[i] == 'u') {
                chars[i] = '*';
            }
        }
        return new String(chars);
    }
}
'''
