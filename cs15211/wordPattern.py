__source__ = 'https://leetcode.com/problems/word-pattern/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/word-pattern.py
# Time:  O(n)
# Space: O(c), c is unique count of pattern
#
# Description: Leetcode # 290. Word Pattern
#
# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection
# between a letter in pattern and a non-empty word in str.
#
# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
#
# Notes:
# You may assume pattern contains only lowercase letters,
# and str contains lowercase letters separated by a single space.
#
#
# Companies
# Dropbox Uber Tesla
# Related Topics
# Hash Table
# Similar Questions
# Isomorphic Strings Word Pattern II
#
from itertools import izip  # Generator version of zip.
import unittest
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if len(pattern) != self.wordCounts(str):
            return False

        w2p, p2w = {}, {}

        for p, w in izip(pattern, self.wordGenerator(str)):
            if w not in w2p and p not in p2w:
                # Build mapping. Space: O(c)
                w2p[w] = p
                p2w[p] = w
            elif w not in w2p or w2p[w] != p:
                # Contradict mapping.
                return False
        return True

    def wordCounts(self, str):
        cnt = 1 if str else 0
        for c in str:
            if c == ' ':
                cnt += 1
        return cnt

     # Generate a word at a time without saving all the words.
    def wordGenerator(self, str):
        w = ""
        for c in str:
            if c == ' ':
                yield w
                w = ""
            else:
                w += c
        yield w

# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split() #Space O(n)
        if len(pattern) != len(words):
            return False

        w2p, p2w = {}, {}
        for p, w in izip(pattern, words):
            if w not in w2p and p not in p2w:
                # Build mapping. Space: O(c)
                w2p[w] = p
                p2w[p] = w
            elif w not in w2p or w2p[w] != p:
                 # Contradict mapping.
                return False
        return True

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
#
# 1ms 99.02%
class Solution {
    public boolean wordPattern(String pattern, String str) {
        String[] strs = str.split(" ");
        if (pattern.length() != strs.length) {
            return false;
        }
        String[] mapping = new String[26];
        Set<String> set = new HashSet<>();
        for (int i = 0; i < pattern.length(); i++) {
            int index = pattern.charAt(i) - 'a';
            if (mapping[index] == null) {
                if (set.contains(strs[i])) {
                    return false;
                }
                mapping[index] = strs[i];
                set.add(strs[i]);
            } else {
                if (!mapping[index].equals(strs[i])) {
                    return false;
                }
            }
        }
        return true;
    }
}

# 1ms 99.02%
class Solution {
    public boolean wordPattern(String pattern, String str) {
        String[] arr= str.split(" ");
        HashMap<Character, String> map = new HashMap<Character, String>();
        if(arr.length!= pattern.length())
            return false;
        for(int i=0; i<arr.length; i++){
            char c = pattern.charAt(i);
            if(map.containsKey(c)){
                if(!map.get(c).equals(arr[i]))
                    return false;
            }else{
                if(map.containsValue(arr[i]))
                    return false;
                map.put(c, arr[i]);
            }
        }
        return true;
    }
}

# 1ms 99.02%
class Solution {
    //pattern = "abba", str = "dog dog dog dog"
    public boolean wordPattern(String pattern, String str) {
        String[] arr = str.split(" ");
        if (pattern.length() != arr.length) return false;
        Map<Character, String> map = new HashMap<Character, String>();
        for (int i = 0; i< arr.length; i++) {
            char key = pattern.charAt(i);
            if (map.containsKey(key)) {
                if (!map.get(key).equals(arr[i])) return false;
            }else {
                if (map.containsValue(arr[i])) return false;
                map.put(key, arr[i]);
            }
        }
        return true;
    }
}
'''