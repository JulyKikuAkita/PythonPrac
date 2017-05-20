__author__ = 'July'

# Time:  O(n^2 ~ 2^n)
# Space: O(n^2)
#
# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# For example, given s = "aab",
# Return
#
#   [
#     ["aa","b"],
#     ["a","a","b"]
#   ]

# Time:  O(n^2 ~ 2^n)
# Space: O(n^2)
# dynamic programming solution
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        n = len(s)
        is_palindrome = [[0 for j in xrange(n)] for i in xrange(n)]
        for i in reversed(xrange(0,n)):
            for j in xrange(i, n):
                is_palindrome[i][j] = s[i] == s[j] and((j - i < 2) or is_palindrome[i + 1][j - 1])

        sub_partition = [[] for i in xrange(n)]
        #print sub_partition
        for i in reversed(xrange(n)):
            for j in xrange(i, n):
                if is_palindrome[i][j]:
                    if j + 1 < n:
                        for p in sub_partition[ j + 1]:
                            sub_partition[i].append([s[i:j +1]] + p)
                           # print i, j, s[i:j +1], p
                    else:
                        sub_partition[i].append([s[i:j+1]])

        return sub_partition[0]

# Time:  O(2^n)
# Space: O(n)
# recursive solution
class Solution2:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        result = []
        self.partitionRecu(result, [], s, 0)
        return result

    def partitionRecu(self, result, cur, s, i):
        if i == len(s):
            result.append(list(cur)) # Converts a tuple into list.
        else:
            for j in xrange(i, len(s)):
                #print i, j, s[i:j + 1], cur
                if self.isPalindrome(s[i:j + 1]):
                    cur.append(s[i: j + 1])
                    self.partitionRecu(result, cur, s, j + 1)
                    cur.pop()

    def isPalindrome(self, s):
        for i in xrange(len(s) / 2):
            if s[i] != s[-(i+1)]:
                return False
        return True



class SolutionOther:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        Solution.res = []
        self.dfs(s, [])
        return Solution.res

    def isPalindrome(self, s):
        for i in range(len(s)):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True

    def dfs(self, s, stringlist):
        if len(s) == 0:
            Solution.res.append(stringlist)
        for i in range(1, len(s) +1):
            print i, s[:i],self.isPalindrome(s[:i]), stringlist ,s[i:]
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], stringlist+[s[:i]])


# http://www.programcreek.com/2013/03/leetcode-palindrome-partitioning-java/
# java - DP
# wrong answer
class DP:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if not s or len(s) <= 1:
            return [s]
        result = []
        dptable = [[ -1 for i in xrange(len(s))] for j in xrange(len(s))]

        #for i in xrange(len(s)):
        #    dptable[i][i] = 1

        # l is length, i is index of left boundary, j is index of right boundary
        for l in xrange(1, len(s)+1):
            for i in xrange(len(s) - l + 1):
                j = i + l - 1
                if s[i] == s[j]:
                    if l == 1 or l == 2:
                        #print "({},{})".format(i, j)
                        dptable[i][j] = 1
                    else:
                        dptable[i][j] = dptable[i+1][j-1]

                    if dptable[i][j] == 1:
                        result.append(s[i:j+1])
                else:
                    dptable[i][j] = 0
        print dptable
        return result


#test
test = SolutionOther()
#print test.partition("aab")

if __name__ == "__main__":
    #print Solution().partition("aab")
    print Solution2().partition("aab")
    #print DP().partition("aab")