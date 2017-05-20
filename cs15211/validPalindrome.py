__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/valid-palindrome.py
# Time:  O(n)
# Space: O(1)
# String
#
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
#
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
#
# For the purpose of this problem, we define empty string as valid palindrome.
#

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not (s[i].isalnum()):
                i += 1
            while i < j and not (s[j].isalnum()):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i, j = i+1, j-1

        return True


if __name__ == "__main__":
    print Solution().isPalindrome("A man, a plan, a canal: Panama")


class SolutionOther:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        text = [x.lower() for x in s if x.isalpha() or x.isdigit()]
        revtext = text[::-1]
        num = len(text)
        #print revtext
        if num == 0:
            return True
        else:
            if num % 2 == 0:
                for i in range(num/2) :
                    if text[i] != revtext[i]:
                        return False
                else:
                    return True
            else:
                for i in range((num-1)/2) :
                    if text[i] != revtext[i]:
                        #print text[num-1-i]
                        return False
                else:
                    return True

#java solution
# http://www.programcreek.com/2013/01/leetcode-valid-palindrome-java/
class stackSolution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        stack = []
        if len(s) < 2:
            return True
        index = 0
        while index < len(s) / 2:
            stack.append(s[index])
            index += 1

        if len(s) % 2 == 1:
            index += 1

        while index < len(s):
            if len(stack) == 0:
                return False
            if stack.pop() != s[index]:
                return False
            else:
                index += 1
        return True


# tc
t1 = Solution()
t2 = stackSolution()
#print t1.isPalindrome("A man, a plan, a canal: Panama")
#print t1.isPalindrome("race a car")
#print  t1.isPalindrome("a.")
#print  t1.isPalindrome(".,")
#print  t1.isPalindrome("......a.....")
print  t1.isPalindrome("1a2")
print t2.isPalindrome("1a2")
