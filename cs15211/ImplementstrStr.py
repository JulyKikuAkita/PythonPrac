__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/implement-strstr.py
# Time:  O(n + m)
# Space: O(m)
# String - KMP algo
#
# Implement strStr().
#
# Returns a pointer to the first occurrence of needle in haystack,
#  or null if needle is not part of haystack.
#
# Microsoft Facebook

# Wiki of KMP algorithm:
# http://en.wikipedia.org/wiki/Knuth-Morris-Pratt_algorithm
# Easy explanation: http://jakeboxer.com/blog/2009/12/13/the-knuth-morris-pratt-algorithm-in-my-own-words/
class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        if len(haystack) < len(needle):
            return -1

        i = self.KMP(haystack, needle)
        if i > -1:
            return i
        else:
            return -1

    def KMP(self, text, pattern):
        prefix = self.getPrefix(pattern)
        j = -1
        for i in xrange(len(text)):
            while j > -1 and pattern[j + 1] != text[i]:
                j = prefix[j]
            if pattern[j + 1] == text[i]:
                j += 1
            if j == len(pattern) - 1:
                return i - j
        return -1

    def getPrefix(self, pattern):
        prefix = [-1] * len(pattern)
        j = -1
        for i in xrange(1, len(pattern)):
            while j > -1 and pattern[j + 1] != pattern[i]:
                j = prefix[j]
            if pattern[j + 1] == pattern[i]:
                j += 1
            prefix[i] = j
        return prefix

# Time:  (n * m)
# Space: (1)
class Solution2:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        for i in xrange(len(haystack) - len(needle)):
            if haystack[i : i + len(needle)] == needle:
                return haystack[i:]
        return None

class SolutionOther:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None

     def strStrKMP(self, haystack, needle):
        lenh, lenn = len(haystack), len(needle)
        if lenn == 0:
            return haystack
        next, p = [-1] * (lenn), -1
        for i in range(1, lenn):
            print i,p, needle[i] , needle[p + 1], next, lenn
            while p >= 0 and needle[i] != needle[p + 1]:
                p = next[p]
            if needle[i] == needle[p + 1]:
                p  = p + 1
            next[i] = p

        p = -1
        for i in range(lenh):
            print i,p, haystack[i] , next, haystack[i - p:],lenh ,needle[p + 1]
            while p >= 0 and haystack[i] != needle[p + 1]:
                p = next[p]
            if haystack[i] == needle[p + 1]:
                p = p + 1
            if p + 1 == lenn:
                   return haystack[i - p:]
        return None

     def strStr(self, haystack, needle):
        j =0
        if len(needle) ==0 and len(haystack)==0:
            return ""
        elif len(haystack)!=0 and len(needle)==0:
            return haystack
        elif len(haystack)!=0 and len(needle)!=0:

            for i in range(len(haystack)):
                if (i + len(needle) )> len(haystack):
                    break
                for j in range(len(needle)):
                    print i, haystack[i+j], j, needle[j]
                    if haystack[i+j] != needle[j]:
                        break

                else:
                    print i
                    return haystack[i::]


            return None

class Naive:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
     def strStr(self, haystack, needle):
        if not haystack or not needle:
            return 0
        if len(needle) == 0:
            return 0
        for i in xrange(len(haystack)):
            if i + len(needle) > len(haystack):
                return -1
            m = i
            for j in xrange(len(needle)):
                if needle[j] == haystack[m]:
                    if j == len(needle) - 1:
                        return i
                    m += 1
                else:
                    break
        return -1
# Java Solution
# http://www.programcreek.com/2012/12/leetcode-implement-strstr-java/

t1=SolutionOther()
#print t1.strStr("haystackneedle","needle")
#print t1.strStr("haystackneedle","neekle")
#print t1.strStr("haystackneedle","")
#print t1.strStr("","a")  #null
#print t1.strStr("","") # ""
#print t1.strStr("aaa","a") #aaa
#print t1.strStr("mississippi", "issip") #issippi
#print t1.strStr("a","")
#print t1.strStr("mississippi", "a")
#p = [-1] * (len("needle"))
#print p
#print t1.strStrKMP("haystackneedle","needle")
#print t1.strStrKMP("aaa","a") #aaa
#print t1.strStrKMP("mississippi", "a")
#print t1.strStrKMP("mississippi", "issip")

if __name__ == "__main__":
    print Solution2().strStr("a", "")
    print Solution2().strStr("abababcdab", "ababcdx")
    print Naive().strStr("abababcdab", "ababcdx")