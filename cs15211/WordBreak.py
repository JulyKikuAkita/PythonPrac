__author__ = 'July'
# Time:  O(n^2)
# Space: O(n)
# DP
# still not understand
#
# Given a string s and a dictionary of words dict,
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
#
# Return true because "leetcode" can be segmented as "leet code".
#
#  Bloomberg



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


#test
test = Solution2()
#print test.wordBreak("leetcode", ["leet", "code"])

if __name__ == "__main__":
    #print Solution().wordBreak("leetcode", ["leet", "code"])
    print Naive().wordBreak("programcreek", ["programcree","program","creek"])
    print javaDP().wordBreak("programcreek", ["programcree","program","creek"])


#java
js = '''
public class Solution {
    public boolean wordBreak(String s, Set<String> wordDict) {
        int len = s.length();
        int maxLen = getMaxLength(wordDict);
        boolean[] dp = new boolean[len + 1];
        dp[0] = true;
        for (int i = 0; i < s.length(); i++) {
            if (!dp[i]) {
                continue;
            }
            for (int j = i + 1; j <= Math.min(i + maxLen, len); j++) {
                if (dp[j] || wordDict.contains(s.substring(i, j))) {
                    dp[j] = true;
                }
            }
        }
        return dp[len];
    }

    private int getMaxLength(Set<String> wordDict) {
        int max = 0;
        for (String word : wordDict) {
            max = Math.max(max, word.length());
        }
        return max;
    }
}

public class Solution {
    public boolean wordBreak(String s, Set<String> wordDict) {
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;

        for(int i = 1; i<= s.length() ;++i){
            for(int j = 0; j < i; j++){
                if(dp[j] == true && wordDict.contains(s.substring(j,i)) ){
                    dp[i] = true;
                }
            }

        }
        return dp[s.length()];
    }
}
'''