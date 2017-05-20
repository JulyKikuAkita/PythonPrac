__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/word-break-ii.py
# Time:  O(2^n)
# Space: O(n)
# DP
# still not understand
#
# Given a string s and a dictionary of words dict,
# add spaces in s to construct a sentence where each word is a valid dictionary word.
#
# Return all such possible sentences.
#
# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
#
# A solution is ["cats and dog", "cat sand dog"].
# Google Uber



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


#test
test = Solution2()
#print test.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
#print test.wordBreak("a", ["a"])

if __name__ == "__main__":
    print Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])

#java
js = '''
public class Solution {
    public List<String> wordBreak(String s, Set<String> wordDict) {
        List<String> result = new ArrayList<String>();
        boolean[] isImpossible = new boolean[s.length() + 1];
        if (s == null || s.length() == 0 || wordDict.size() == 0) {
            return result;
        }
        wordBreak(s, wordDict, result, new ArrayList<String>(), isImpossible, 0);
        return result;
    }

    private boolean wordBreak(String s, Set<String> wordDict, List<String> result, List<String> curr, boolean[] isImpossible, int index) {
        if (isImpossible[index]) {
            return false;
        }
        if (s.length() == 0) {
            result.add(convertString(curr));
            return true;
        }
        boolean found = false;
        for (String str : wordDict) {
            if (s.startsWith(str)) {
                curr.add(str);
                found |= wordBreak(s.substring(str.length()), wordDict, result, curr, isImpossible, index + str.length());
                curr.remove(curr.size() - 1);
            }
        }
        if (!found) {
            isImpossible[index] = true;
        }
        return found;
    }

    private String convertString(List<String> curr) {
        if (curr.size() == 0) {
            return null;
        }
        StringBuilder sb = new StringBuilder();
        for (String str : curr) {
            sb.append(str);
            sb.append(' ');
        }
        sb.delete(sb.length() - 1, sb.length());
        return sb.toString();
    }
}
'''