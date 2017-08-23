__source__ = 'https://leetcode.com/problems/word-pattern-ii/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/word-pattern-ii.py
# Time:  O(n * C(n - 1, c - 1)), n is length of str, c is unique count of pattern,
#                                there are H(n - c, c - 1) = C(n - 1, c - 1) possible splits of string,
#                                and each one costs O(n) to check if it matches the word pattern.
# Space: O(n + c)
#
# Description: 291. Word Pattern II
#
# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection
# between a letter in pattern and a non-empty substring in str.
#
# Examples:
# pattern = "abab", str = "redblueredblue" should return true.
# pattern = "aaaa", str = "asdasdasdasd" should return true.
# pattern = "aabb", str = "xyzabcxzyabc" should return false.
# Notes:
# You may assume both pattern and str contains only lowercase letters.
#
# Companies
# Dropbox Uber
# Related Topics
# Backtracking
# Similar Questions
# Word Pattern
#
import unittest
# 362 ms
class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        w2p, p2w = {}, {}
        return self.match(pattern, str, 0, 0, w2p, p2w)


    def match(self, pattern, str, i, j, w2p, p2w):
        is_match = False
        if i == len(pattern) and j == len(str):
            is_match = True
        elif i < len(pattern) and j < len(str):
            p = pattern[i]
            if p in p2w:
                w = p2w[p]
                if w == str[j:j+len(w)]:  # Match pattern.
                    is_match = self.match(pattern, str, i + 1, j + len(w), w2p, p2w)
                # Else return false.
            else:
                for k in xrange(j, len(str)):  # Try any possible word
                    w = str[j:k+1]
                    if w not in w2p:
                        # Build mapping. Space: O(n + c)
                        w2p[w], p2w[p] = p, w;
                        is_match = self.match(pattern, str, i + 1, k + 1, w2p, p2w)
                        w2p.pop(w), p2w.pop(p);
                    if is_match:
                        break
        return is_match

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
We can solve this problem using backtracking, we just have to keep trying to use a character in the pattern to
match different length of substrings in the input string, keep trying till we go through the input string and the pattern.

For example, input string is "redblueredblue", and the pattern is "abab", first let's use 'a' to match "r",
'b' to match "e", then we find that 'a' does not match "d", so we do backtracking, use 'b' to match "ed",
so on and so forth ...

When we do the recursion, if the pattern character exists in the hash map already,
we just have to see if we can use it to match the same length of the string.
For example, let's say we have the following map:

'a': "red"

'b': "blue"

now when we see 'a' again, we know that it should match "red", the length is 3, then let's see if str[i ... i+3]
matches 'a', where i is the current index of the input string. Thanks to StefanPochmann's suggestion,
in Java we can elegantly use str.startsWith(s, i) to do the check.

Also thanks to i-tikhonov's suggestion, we can use a hash set to avoid duplicate matches,
if character a matches string "red", then character b cannot be used to match "red".
In my opinion though, we can say apple (pattern 'a') is "fruit", orange (pattern 'o') is "fruit",
so they can match the same string, anyhow, I guess it really depends on how the problem states.

The following code should pass OJ now, if we don't need to worry about the duplicate matches,
just remove the code that associates with the hash set.

#44.14% 102 ms
public class Solution {
    public boolean wordPatternMatch(String pattern, String str) {
        Map<Character, String> map = new HashMap<>();
        Set<String> visited = new HashSet<>();
        return isMatch(str, 0, pattern, 0, map, visited);
    }

    private boolean isMatch(String str, int idxStr, String pat, int idxPat, Map<Character, String> map, Set<String> visited) {
        if (idxStr == str.length() && idxPat == pat.length()) return true;
        if (idxStr == str.length() || idxPat == pat.length()) return false;

        //if in map
        char key = pat.charAt(idxPat);
        if (map.containsKey(key)) {
            String s = map.get(key);
            if (!str.startsWith(s, idxStr)) {  //check if str starts with s at idx idxStr
                return false;
            } else {
                return isMatch(str, idxStr + s.length(), pat, idxPat+1, map, visited);
            }
        }

        //else
        for (int i = idxStr; i < str.length(); i++) {
            String cur = str.substring(idxStr, i + 1);
            if (!visited.contains(cur)) {
                map.put(key, cur);
                visited.add(cur);
                if (isMatch(str, i + 1, pat, idxPat+1, map, visited)) return true;
                visited.remove(cur);
                map.remove(key);
            }
        }
        return false;
    }
}

# use String[] instead of map
#83.26% 63ms
public class Solution {
    public boolean wordPatternMatch(String pattern, String str) {
        return isMatch(str, 0, pattern, 0, new String[26], new HashSet<>());
    }

    private boolean isMatch(String str, int idxStr, String pat, int idxPat, String[] map, Set<String> visited) {
        if (idxStr == str.length() && idxPat == pat.length()) return true;
        if (idxStr == str.length() || idxPat == pat.length()) return false;

        //if in map
        int key = pat.charAt(idxPat) - 'a';
        if (map[key] != null) {
            String s = map[key];
            if (!str.startsWith(s, idxStr)) {  //check if str starts with s at idx idxStr
                return false;
            } else {
                return isMatch(str, idxStr + s.length(), pat, idxPat+1, map, visited);
            }
        }

        //else
        for (int i = idxStr; i < str.length(); i++) { //if i loop to the end
            String cur = str.substring(idxStr, i + 1);
            if (!visited.contains(cur)) {
                map[key] = cur;
                visited.add(cur);
                if (isMatch(str, i + 1, pat, idxPat+1, map, visited)) return true;
                visited.remove(cur);
                map[key] = null;
            }
        }
        return false;
    }
}


# 94.14% 4ms
public class Solution {
    public boolean wordPatternMatch(String pattern, String str) {
        return isMatch(str, 0, pattern, 0, new String[26], new HashSet<>());
    }

    private boolean isMatch(String str, int idxStr, String pat, int idxPat, String[] map, Set<String> visited) {
        if (idxStr == str.length() && idxPat == pat.length()) return true;
        if (idxStr == str.length() || idxPat == pat.length()) return false;

        //if in map
        int key = pat.charAt(idxPat) - 'a';
        if (map[key] != null) {
            String s = map[key];
            if (!str.startsWith(s, idxStr)) {  //check if str starts with s at idx idxStr
                return false;
            } else {
                return isMatch(str, idxStr + s.length(), pat, idxPat+1, map, visited);
            }
        }

        //else
        for (int i = idxStr; i <= str.length() - (pat.length() - idxPat); i++) { //if i ends earlier
            String cur = str.substring(idxStr, i + 1);
            if (!visited.contains(cur)) {
                map[key] = cur;
                visited.add(cur);
                if (isMatch(str, i + 1, pat, idxPat+1, map, visited)) return true;
                visited.remove(cur);
                map[key] = null;
            }
        }
        return false;
    }
}

#95.82% 3ms
public class Solution {
    public boolean wordPatternMatch(String pattern, String str) {
        return wordPattern(pattern, str, 0, 0, new String[26], new HashSet<>());
    }

    private boolean wordPattern(String pattern, String str, int patternIndex, int strIndex, String[] patternMatch, Set<String> visitedStr) {
        if (patternIndex == pattern.length() && strIndex == str.length()) {
            return true;
        } else if (patternIndex == pattern.length() || strIndex == str.length()) {
            return false;
        }
        int curPattern = pattern.charAt(patternIndex) - 'a';
        if (patternMatch[curPattern] == null) {
            for (int i = strIndex; i <= str.length() - (pattern.length() - patternIndex); i++) {
                String curStr = str.substring(strIndex, i + 1);
                if (!visitedStr.contains(curStr)) {
                    patternMatch[curPattern] = curStr;
                    visitedStr.add(curStr);
                    if (wordPattern(pattern, str, patternIndex + 1, i + 1, patternMatch, visitedStr)) {
                        return true;
                    }
                    patternMatch[curPattern] = null;
                    visitedStr.remove(curStr);
                }
            }
        } else if (str.length() - strIndex >= patternMatch[curPattern].length()) {
            String curStr = str.substring(strIndex, strIndex + patternMatch[curPattern].length());
            if (curStr.equals(patternMatch[curPattern])) {
                return wordPattern(pattern, str, patternIndex + 1, strIndex + patternMatch[curPattern].length(), patternMatch, visitedStr);
            }
        }
        return false;
    }
}
'''