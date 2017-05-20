__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/palindrome-number.py
# Time:  O(1)
# Space: O(1)
# Math  ~= reverse integer
#
# Determine whether an integer is a palindrome. Do this without extra space.
#
# Some hints:
# Could negative integers be palindromes? (ie, -1)
#
# If you are thinking of converting the integer to string, note the restriction of using extra space.
#
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer",
# you know that the reversed integer might overflow. How would you handle such case?
#
# There is a more generic way of solving this problem.
#

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        copy,reverse = x, 0
        while copy:
            reverse *= 10
            reverse += copy % 10
            copy /= 10
        return x == reverse

class Solution2:
    # @return a boolean
    def isPalindromeTwoPointers(self, x):
        if x < 0 :
            return False
        while x != 0:
            div = 1
            while (x / div ) >= 10:
                div = div * 10

            left = x / div
            right = x % 10

            if left != right:
                return False
            else:
                x = (x % div) / 10
                #div = div / 100

        return True

if __name__ == "__main__":
    print Solution().isPalindrome(12321)
    print Solution().isPalindrome(12320)
    print Solution().isPalindrome(-12321)



class SolutionOther:
    # @return a boolean
    def isPalindrome(self, x):
        if x <= 0 :
            return False if x < 0 else True
        a, b = x, 0
        while a:
            b, a = b * 10 + a % 10, a /10
            #print b , a
        return b == x

#test
test = SolutionOther()
#print test.isPalindrome(121)
#print test.isPalindrome(1121)