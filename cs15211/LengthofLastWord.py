__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/length-of-last-word.py
# Time:  O(n)
# Space: O(1)
# String
#
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# For example,
# Given s = "Hello World",
# return 5.
#

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        length = 0
        for i in reversed(s):
            if i == ' ':
                if length:
                    break
            else:
                length += 1
        return length

# Time:  O(n)
# Space: O(n)
class Solution2:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        return len(s.strip().split(" ")[-1])


if __name__ == "__main__":
    print Solution().lengthOfLastWord("Hello World ")
    print Solution2().lengthOfLastWord("")

class SolutionOther:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if s == "" or s == None or s.isspace():
            return 0

        lastword= s.split()[::-1][0]
        return len(lastword)

# java solution
# http://www.programcreek.com/2014/05/leetcode-length-of-last-word-java/

t1=SolutionOther()
#print t1.lengthOfLastWord("Hello World")
#print t1.lengthOfLastWord("")
#print t1.lengthOfLastWord("    ")