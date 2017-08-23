__source__ = 'https://leetcode.com/problems/word-break-ii/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/word-break-ii.py
# Time:  O(2^n)
# Space: O(n)
# DP
#
# Description: Leetcode # 217. 140. Word Break II
#
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# add spaces in s to construct a sentence where each word is a valid dictionary word.
# You may assume the dictionary does not contain duplicate words.
#
# Return all such possible sentences.
#
# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
#
# A solution is ["cats and dog", "cat sand dog"].
#
# UPDATE (2017/1/4):
# The wordDict parameter had been changed to a list of strings (instead of a set of strings).
# Please reload the code definition to get the latest changes.
#
# Companies
# Dropbox Google Uber Snapchat Twitter
# Related Topics
# Dynamic Programming Backtracking
# Similar Questions
# Word Break Concatenated Words
#

import unittest
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        n = len(s)
        possible = [False for _ in xrange(n)]
        valid = [[False] * n for _ in xrange(n)] #[False]*n repeater for n times

        for i in xrange(n):
            print
            if s[:i+1] in dict:
                possible[i] = True
                valid[0][i] = True
            for j in xrange(i):
                if possible[j] and s[j+1:i+1] in dict:
                    valid[j+1][i] = True
                    possible[i] = True
        result = []

        ##########################
        #just for my understanding
        print "Valid Table: "
        for i in range(len(valid)):
            print i, valid[i]
        print
        ##########################

        if possible[n - 1]:
            self.genPath(s, valid, 0, [], result)
        return result

    def genPath(self, s, valid, start, path, result):
        if start == len(s):
            result.append(" ".join(path)) # join words in path to one string
            #result += (path) # all word in path is single string
            return
        for i in xrange(start, len(s)):
            if valid[start][i]:
                path += [s[start:i+1]]
                print "in dfs", i, path
                self.genPath(s, valid, i+1, path, result)
                path.pop()

class Solution2:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        Solution.res = []
        self.dfs(s, dict, '')
        return Solution.res

    def check(self, s, dict):
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for k in range(0, i):
                if dp[k] and s[k:i] in dict:
                    dp[i] = True
        #print dp, dp[len(s)]
        return dp[len(s)]

    def dfs(self, s, dict, stringlist):
        if self.check(s, dict):
            if len(s) == 0:
                Solution.res.append(stringlist[1:])
                print Solution.res, stringlist[1:], stringlist[0], '<-'
            for i in range(1, len(s)+1):
                   if s[:i] in dict:
                       self.dfs(s[i:], dict, stringlist+' '+ s[:i])

#OT
class Solution3(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        if not s or not wordDict:
            return []
        res = []
        imp = [False for _ in xrange(len(s) + 1)]
        self.dfs(s, wordDict, imp, 0, res, [])
        return res

    def dfs(self, s, wordDict, imp, idx, res, cur):
        if len(s) == 0:
            res.append("".join(cur).strip(" "))
            return True

        found = False
        for word in wordDict:
            if s[0] == word[0] and len(s) >= len(word):
                cur.append(word + " ")
                found |= self.dfs(s[len(word):], wordDict, imp, idx + len(word), res, cur)
                cur.pop()

        if not found:
            imp[idx] = True
        return found

# Test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
        test = Solution2()
        #print test.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
        #print test.wordBreak("a", ["a"])

if __name__ == '__main__':
    unittest.main()

Java = '''
Thought: https://leetcode.com/articles/word-break-ii/

77.82% 14ms
Time O(n^3), Size of recursion tree can go up to n^2. The creation of list takes n time.
Space O(n^3) The depth of the recursion tree can go up to n and each activation record can contains a string list of size n.

public class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
            return DFS(s, wordDict, new HashMap<String, LinkedList<String>>());
    }

    // DFS function returns an array including all substrings derived from s.
    List<String> DFS(String s, List<String> wordDict, HashMap<String, LinkedList<String>> map) {
        if (map.containsKey(s)) return map.get(s);

        LinkedList<String>res = new LinkedList<String>();
        if (s.length() == 0) {
            res.add("");
            return res;
        }

        for (String word: wordDict) {
            if (s.startsWith(word)) {
                List<String>sublist = DFS(s.substring(word.length()), wordDict, map);
                for (String sub : sublist) {
                    res.add(word + (sub.isEmpty() ? "" : " ") + sub);
                    //res.add(sub + (sub.equals("") ? "" : " ") + word); // guess what's the result?
                                                                        //Output: ["dog sand cat","dog and cats"]
                }
            }
        }

        map.put(s, res);
        return res;
    }
}

#DP TLE
public class Solution {
    public List<String> wordBreak(String s, Set<String> wordDict) {
        LinkedList<String>[] dp = new LinkedList[s.length() + 1];
        LinkedList<String> initial = new LinkedList<>();
        initial.add("");
        dp[0] = initial;
        for (int i = 1; i <= s.length(); i++) {
            LinkedList<String> list = new LinkedList<>();
            for (int j = 0; j < i; j++) {
                if (dp[j].size() > 0 && wordDict.contains(s.substring(j, i))) {
                    for (String l : dp[j]) {
                        list.add(l + (l.equals("") ? "" : " ") + s.substring(j, i));
                    }
                }
            }
            dp[i] = list;
        }
        return dp[s.length()];
    }
}

# 98.96% 8ms
public class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        List<String> result = new ArrayList<>();
        if (s == null || s.length() <= 0 || wordDict == null || wordDict.size() <= 0) return result;
        int maxWordSize = 0;
        HashSet<String> dict = new HashSet<>();
        for (String str : wordDict) {
            maxWordSize = Math.max(maxWordSize, str.length());
            dict.add(str);
        }
        helper(s, 0, new boolean[s.length()], dict, maxWordSize, new StringBuilder(), result);
        return result;
    }

    private boolean helper(String s, int start, boolean[] marked, HashSet<String> dict, int maxWordSize, StringBuilder sol, List<String> result) {
        if (start >= s.length()) {
            result.add(sol.toString().trim());
            return true;
        }
        if (marked[start]) return false;
        boolean r = false;
        for (int i = start; i < Math.min(s.length(), start+maxWordSize); i++) {
            String tmp = s.substring(start, i+1);
            if (dict.contains(tmp)) {
                sol.append(tmp);
                sol.append(" ");
                r |= helper(s, i+1, marked, dict, maxWordSize, sol, result);
                sol.delete(sol.length()-1-tmp.length(), sol.length());
            }
        }
        if (r) return true;
        marked[start] = true;
        return false;
    }
}


'''