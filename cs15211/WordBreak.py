__source__ = 'https://leetcode.com/problems/word-break/#/description'
# Time:  O(n^2)
# Space: O(n)
# DP
#
# Description: Leetcode # 139. Word Break
#
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# You may assume the dictionary does not contain duplicate words.
#
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
#
# Return true because "leetcode" can be segmented as "leet code".
#
# UPDATE (2017/1/4):
# The wordDict parameter had been changed to a list of strings (instead of a set of strings).
# Please reload the code definition to get the latest changes.
#
# Companies
# Google Uber Facebook Amazon Yahoo Bloomberg Pocket Gems
# Related Topics
# Dynamic Programming
# Similar Questions
# Word Break II
#
import unittest
class Solution2:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        n = len(s)
        possible = [False for _ in xrange(n)]

        for i in xrange(n):
            if s[:i+1] in dict:
                possible[i] = True
            for j in xrange(i):
                if possible[j] and s[j+1:i+1] in dict:
                    possible[i] = True
                    break
        return possible[n-1]

class Solution3:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        dp = [ False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s)+1) :
            for k in range(i):
                if dp[k] and s[k:i] in dict:
                    dp[i] = True
        return dp[len(s)]

# http://www.programcreek.com/2012/12/leetcode-solution-word-break/
# Time:  O(n^2) , OT
# Space: O(n)
class Naive:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        return self.wordBreakRecu(s, dict, 0)

    def wordBreakRecu(self, s, dict, start):
        if start == len(s):
            return True

        for item in dict:
            length = len(item)
            end = start + length
            # end index should be <= string length
            if end > len(s):
                continue
            if s[start:(start+length)] == item:
                if self.wordBreakRecu(s, dict, start+length):
                    return True
        return False

class javaDP:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        dp = [False for i in xrange(len(s) + 1)]
        dp[0] = True # set first to be true, why? #Because we need initial state

        for i in xrange(len(s)):
            #should continue from match position
            if not dp[i]:
                continue
            for item in dict:
                length = len(item)
                end = i + length
                if end > len(s):
                    continue
                if dp[end]:
                    continue
                if s[i:end] == item:
                    dp[end] = True
        return dp[len(s)]

#Test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        test = Solution2()
        #print test.wordBreak("leetcode", ["leet", "code"])

        #print Solution().wordBreak("leetcode", ["leet", "code"])
        print Naive().wordBreak("programcreek", ["programcree","program","creek"])
        print javaDP().wordBreak("programcreek", ["programcree","program","creek"])

if __name__ == '__main__':
    unittest.main()

Java = '''
Thought: https://leetcode.com/problems/word-break/solution/

public class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        //return dfs(s, new HashSet(wordDict), 0);
        //return dfsMemo(s, new HashSet(wordDict), 0, new Boolean[s.length()]);
        return bfs(s, wordDict);
        //return dp(s, wordDict);
        //return dpLen(s, wordDict);
    }

    // Time" O(n^n) considering "aaaaa", Space:O(n)
    // TLE
    public boolean dfs(String s, Set<String> wordDict, int start) {
        if (start == s.length()) return true;
        for (int i = start + 1; i <= s.length(); i++) {
            String cur = s.substring(start, i);
            if (wordDict.contains(cur) && dfs(s, wordDict, i)) return true;
        }
        return false;
    }

     // Time" O(n^2), Space:O(n)  26%
     // 47.51% 16ms
    public boolean dfsMemo(String s, Set<String> wordDict, int start, Boolean[] memo) {
        if (start == s.length()) return true;
        if (memo[start] != null) return memo[start];
        for (int i = start + 1; i <= s.length(); i++) {
            String cur = s.substring(start, i);
            if (wordDict.contains(cur) && dfsMemo(s, wordDict, i, memo))
                return memo[start] = true;
        }
        return memo[start] = false;
    }

    //BFS // Time" O(n^2), Space:O(n)
    # 24.39% 19ms
    public boolean bfs(String s, List<String> wordDict) {
        Set<String> wordDictSet=new HashSet(wordDict);
        Queue<Integer> queue = new LinkedList<>();
        int[] visited = new int[s.length()];
        queue.add(0);
        while (!queue.isEmpty()) {
            int start = queue.poll();
            if (visited[start] == 0) {
                for (int end = start + 1; end <= s.length(); end++) {
                    if (wordDictSet.contains(s.substring(start, end))) {
                        if (end == s.length()) return true;
                        queue. add(end);
                    }
                }
                visited[start] = 1;
            }
        }
        return false;
    }

    //DP: Time" O(n^2), Space:O(n)
    //30.67% 18ms
    public boolean dp(String s, List<String> wordDict) {
        Set<String> wordDictSet=new HashSet(wordDict);
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        for (int i = 1; i <= s.length(); i++) { //i need to extends to s.length()
            for (int j = 0; j < i; j++) {
                if (dp[j] && wordDictSet.contains(s.substring(j, i)))
                    dp[i] = true;
                    //break <-- here gave wrong answer when s = leetcode
            }
        }
        return dp[s.length()];
    }

    //DP: Time" O(n^2), Space:O(n)
    //94.69% 7ms
    public boolean dpLen(String s, List<String> wordDict) {
        Set<String> wordDictSet=new HashSet(wordDict);
        int len = s.length();
        int maxLen = getMaxLength(wordDictSet);
        boolean[] dp = new boolean[len + 1];
        dp[0] = true;
        for (int i = 0; i < s.length(); i++) {
            if(!dp[i]) continue;
            for (int j = i + 1; j <= Math.min(len, i + maxLen); j++) {
                if (dp[j] || wordDictSet.contains(s.substring(i, j)))
                    dp[j] = true;
            }
        }
        return dp[len];
    }

    private int getMaxLength(Set<String> wordDict) {
        int max = 0;
        for (String s : wordDict) {
            max = Math.max(max, s.length());
        }
        return max;
    }
}
'''