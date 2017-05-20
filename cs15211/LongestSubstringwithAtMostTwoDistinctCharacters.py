__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/longest-substring-with-at-most-two-distinct-characters.py
# Time:  O(n^2)
# Space: O(1)
# Hashtable
#
# Given a string, find the length of the longest substring T
# that contains at most 2 distinct characters.
#
# For example, Given s = "eceba",
#
# T is "ece" which its length is 3.
#
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLongestSubstringTwoDistinct(self, s):
        longest, start, distinct_count = 0,0,0
        visited = [0 for _ in xrange(256)]

        for i, char in enumerate(s):
            #print i, char, "longest = ", longest
            if visited[ord(char)] == 0:
                distinct_count += 1
            visited[ord(char)] += 1

            while distinct_count > 2:
                #print i, char, distinct_count, start, ord(s[i]), visited[ord(s[start])]
                visited[ord(s[start])] -= 1
                if visited[ord(s[start])] == 0:
                    distinct_count -= 1
                start += 1

            longest = max(longest, i - start + 1)

        return longest
    # considering "aaabbc"
    # i: at the position of 2nd distinct char
    # j: at the last occurrence of 1st distinct char
    # lastStart : same as j if only 2 different char, or at the first occurrence of
    #            2nd distinct char if there's 3 distinct char
    def lengthOfLongestSubstringTwoDistinctleetcode(self, s):
        longest, lastStart =  0, 0
        j = -1

        for i in xrange(1, len(s)):
            if s[i] == s[i-1]:
                continue
            if j >= 0 and s[j] != s[i]:
                longest = max(longest, i - lastStart)
                lastStart = j + 1
            j = i - 1

        return max(longest, len(s) - lastStart)


#test

if __name__ =="__main__":
    print Solution().lengthOfLongestSubstringTwoDistinct("eceba")
    print Solution().lengthOfLongestSubstringTwoDistinctleetcode("eceba")