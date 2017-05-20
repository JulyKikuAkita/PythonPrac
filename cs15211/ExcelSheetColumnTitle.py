__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/excel-sheet-column-title.py
# Time:  O(logn)
# Space: O(1)
# Math
#
# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#

class Solution:
    # @return a string
    def convertToTitle(self, num):
        result, dvd = "", num
        while dvd :
            tmp = (dvd - 1 ) % 26 + ord('A') # base case is 'A' when 0 + 'A'
            result += chr(tmp)
            dvd = ( dvd - 1) / 26
        return result[::-1]

if __name__ == "__main__":
    for i in xrange(1, 52):
        print Solution().convertToTitle(i)

# http://bookshadow.com/weblog/2014/12/20/leetcode-excel-sheet-column-title/
class SolutionOther:
    # @return a string
    def convertToTitle(self, num):
        alpha = [chr(i) for i in range(65, 91)]
        res = []
        while num > 0:
            t = num % 26
            res.append(alpha[t-1])
            num = (num / 26)
            if t == 0:
                num -= 1
        return ''.join(res[::-1])

    def convertToTitleWrong(self, num):
        ans = ''
        while num:
            ans = chr(ord('A') + (num - 1) % 26) + ans
            num = (num - 1 ) / 26
        return ans



#test
test = SolutionOther()
#print test.convertToTitle(27)
#print test.convertToTitleWrong(27)