
__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/longest-substring-without-repeating-characters.py
# Time:  O(n)
# Space: O(1)
# Hash table
#
# Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
# For "bbbbb" the longest substring is "b", with the length of 1.
#
class Solution:
    # Time:  O(2n)
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        longest, start, visited = 0, 0, [False for _ in xrange(256)]
        for i, char in enumerate(s):
            #when repetition found, record the current max and proceed to next non-repeted char
            if visited[ord(char)]:  # Convert a string to ASCII values.
                while char != s[start]:
                    #print i, char, ord(char), longest, "start =", start, visited[ord(s[start])], s[start]
                    visited[ord(s[start])] = False
                    start += 1
                start += 1
            else:
                visited[ord(char)] = True
            longest = max(longest, i - start + 1)
            #print i, char, ord(char), longest, "start =", start
        return longest

    # for every repeating char, set start to last repeating position of that char
    # O(n) runtime, O(1)space, single iteration
    def lengthOfLongestSubstringif(self, s):
        dict = {}
        nextStart = 0
        candidate =  0
        for i in xrange(len(s)):
            if s[i] in dict and dict[s[i]] >= nextStart : # in case of bbcccccb, nextStart don't go back to s[1] when encounter the last b
                nextStart = dict[s[i]] + 1
            candidate = max(candidate, i - nextStart +1)
            dict[s[i]] = i
        return candidate


class SolutionOther:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        dict, ans, p1, p2 = {} , 0, 0, 0
        while p2 < len(s):
            #Return the value for key if key is in the dictionary, else default. If default is not given,
            # it defaults to None, so that this method never raises a KeyError.
            p = dict.get(s[p2], None)
            print p2, s[p2], "=> ", p , dict, p1
            if p == None:
                dict[s[p2]] = p2
                p2 += 1
                ans = max(ans,p2-p1)
            else:
                while p1 <= p:
                    dict.pop(s[p1])
                    p1 += 1
                p1 = p + 1

        return ans



    def lengthOfLongestSubstring2(self, s):
        lastRepeating = -1 # so that len for s[0] = 1,
        ans = 0
        positions = {}
        for i in range(len(s)):
            if s[i] in positions and lastRepeating < positions[s[i]]:
                lastRepeating = positions[s[i]]
            #if i - lastRepeating > ans:
            #    ans = i-lastRepeating
            ans = max(ans, i - lastRepeating)
            positions[s[i]] = i
        return ans

#test
test = SolutionOther()
#print test.lengthOfLongestSubstring("aab")
#print test.lengthOfLongestSubstring("abcabcbb")
#print test.lengthOfLongestSubstring2("abcabcbb")
#print test.lengthOfLongestSubstring("bbbbb")

if __name__ == "__main__":
    s1 = "dvdfghij"
    s2 = "abcabcbb"
    s3 = "bbbbb"
    s4 = "tmmzuxt"
    s5 = "qwert"
    print Solution().lengthOfLongestSubstring(s1)
    print Solution().lengthOfLongestSubstringif(s1)
    print SolutionOther().lengthOfLongestSubstring2(s1)
