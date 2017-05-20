__author__ = 'July'

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        dicts, dictt = {}, {}
        for i in xrange(len(s)):
            if s[i] in dicts and dicts[s[i]] != t[i]:
                return False
            if t[i] in dictt and dictt[t[i]] != s[i]:
                return False

            dicts[s[i]] = t[i]
            dictt[t[i]] = s[i]
        return True

#test
if __name__ == "__main__":
    print Solution().isIsomorphic("aa", "ab")
    print Solution().isIsomorphic("aa", "bb")