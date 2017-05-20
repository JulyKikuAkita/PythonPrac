__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/string-to-integer-atoi.py
# Time:  O(n)
# Space: O(1)
#
# Implement atoi to convert a string to an integer.
#
# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below
# and ask yourself what are the possible input cases.
#
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
# You are responsible to gather all the input requirements up front.
#
# spoilers alert... click to show requirements for atoi.
#
# Requirements for atoi:
# The function first discards as many whitespace characters as necessary
# until the first non-whitespace character is found. Then, starting from this character,
# takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that
# form the integral number, which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number,
# or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
# If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
#

class Solution:
    # @return an integer
    def atoi(self, str):
        #python define sys.maxsize to 2^63 -1
        INT_MAX = 2147483647
        INT_MIN = -2147483647

        result = 0

        if not str:
            return result

        i = 0
        while i < len(str) and str[i] == " ":
            i += 1

        sign = 1
        if str[i] == "+":
            i += 1
        elif str[i] == "-":
            sign = -1
            i += 1

        while i < len(str) and str[i] >= '0' and str[i] <= '9':
            if result > INT_MAX / 10 or (result == INT_MAX / 10 and (ord(str[i]) - ord('0')) > INT_MAX % 10):
                if sign > 0:
                    return INT_MAX
                else:
                    return INT_MIN

            result = result * 10 + ord(str[i]) - ord('0')
            i += 1
        return sign * result

class SolutionOther:
    # @return an integer
    def atoi(self, str):
        if len(str) == 0:
            return 0
        sign, num , p = 0, 0, 0
        imin, imax = -1 <<31, (1<<31)-1
        while str[p] == ' ':
            p = p+1

        if str[p] == '-' or str[p] == '+' :
            sign =1 if str[p] == '-' else 0
            p = p +1
        while p < len(str) and str[p] >= '0' and str[p] <= '9':
            num = num * 10 + ord(str[p]) - ord('0')
            print ord(str[p]) - ord('0'),num, ord(str[p]), ord('0')
            x = -num if sign else num
            if x < imin: return imin
            if x > imax: return imax
            p = p + 1
        return -num if sign else num

#Java solution
# http://www.programcreek.com/2012/12/leetcode-string-to-integer-atoi/
'''
1. null or empty string
2. white spaces
3. +/- sign
4. calculate real value
5. handle min & max
'''
#test
test = Solution()
#print test.atoi(' -121')
print test.atoi('    010')

if __name__ == "__main__":
    print Solution().atoi("")
    print Solution().atoi("-1")
    print Solution().atoi("2147483647")
    print Solution().atoi("2147483648")
    print Solution().atoi("-2147483648")
    print Solution().atoi("-2147483649")