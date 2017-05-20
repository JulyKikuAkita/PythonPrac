__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/palindrome-partitioning-ii.py
# Time:  O(n^2)
# Space: O(n^2)
# DP
#
# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
#

class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        lookup = [[False for j in xrange(len(s))] for i in xrange(len(s))]
        mincut = [len(s) - 1 - i for i in xrange(len(s) + 1)]
        print mincut
        for i in reversed(xrange(len(s))):
            for j in xrange(i, len(s)):
                if s[i] == s[j] and (j - i < 2 or lookup[i + 1][j - 1]):
                    lookup[i][j] = True
                    mincut[i] = min(mincut[i], mincut[j + 1] + 1)
                #print i, j, lookup, mincut

        return mincut[0]


# http://www.programcreek.com/2014/04/leetcode-palindrome-partitioning-ii-java/
class SolutionJava:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        lookup = [[False for j in xrange(len(s))] for i in xrange(len(s))]
        mincut = [i for i in xrange(len(s) + 1)] # set maximum # of cut
        print mincut

        for j in (xrange(len(s))):
            for i in xrange(j + 1):
                if s[i] == s[j] and (j - i < 2 or lookup[i + 1][j - 1]):
                    lookup[i][j] = True
                    if i > 0: # if need to cut, add 1 to the previous cut[i-1]
                        mincut[j] = min(mincut[j], mincut[i - 1] + 1)
                    else:
                        mincut[j] = 0  # if [0...j] is palindrome, no need to cut

        return mincut[j]


class SolutionOther:
    # @param s, a string
    # @return an integer
    #http://www.cnblogs.com/zuoyuan/p/3758783.html
    def minCut(self, s):
        dp = [ 0 for i in range(len(s)+ 1)]
        p = [[False for i in range(len(s))] for j in range(len(s))]

        #print dp, p

        for i in range(len(s)+1):
            dp[i] = len(s) - i
        #print dp
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (((j-i) < 2 ) or p[i+1][j-1]):
                    p[i][j] = True
                    dp[i] = min(1+dp[j+1], dp[i])
        #            print i, j, p, dp
        return dp[0]-1

#test
#test = SolutionOther()
#print test.minCut("aab")

if __name__ == "__main__":
    print Solution().minCut("aab")
    print SolutionJava().minCut("aab")