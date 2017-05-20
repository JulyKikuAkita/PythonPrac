__author__ = 'July'
# Time:  O(n)
# Space: O(1)
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
#
#
#
#

class Solution:
    # @return a string
    def convert(self, s, nRows):
        step, zigzag = 2 * nRows -2, ""
        if s == None or len(s) == 0 or nRows <= 0:
            return ""
        if nRows == 1:
            return s
        for i in xrange(nRows):
            for j in xrange(i, len(s), step):
                zigzag += s[j]
                # print 1->7 ->9; do not derive 7 from 9 otherwise, it prints 1 -> 9 -> 7
                if i > 0 and i < nRows - 1 and j + step  - 2 * i < len(s):
                    zigzag += s[j+ step - 2 * i]
        return zigzag


'''
#explanation
nRows= 5, then step = 2 * nRows - 2 ( derived by, 0, the next expected to be 10, but show up 8)
0     8         16          24
1   7 9      15 17       23 25
2  6  10   14   18    22    26
3 5   11 13     19 21       27
4     12        20          28

-> print result
0  8  16  24    <-----2*nRows -2
1  7 9  15 17 23 25  <--- 2*nRows -2 for 1, 9, 17, 25 ; i + (2*nRows -2) - (2 * i) for 7, 15, 23
2  6 10 14 18 22 26  <--- 2*nRows -2 for 2, 10, 18, 26 ; i + (2*nRows -2) - (2 * i) for 6, 14, 22
3  5 11 13 19 21 27  <--- 2*nRows -2 for 3, 11, 19, 27 ; i + (2*nRows -2) - (2 * i) for 5, 13, 21
4  12  20 28
'''

if __name__ == "__main__":
    #print Solution().convert("PAYPALISHIRING", 3)
    #print Solution().convertiflee("PAYPALISHIRING", 3)
    print Solution().convert("0123456789", 3)
    print Solution().convertiflee("0123456789", 3)


class SolutionOther:
    # @return a string
    def convert(self, s, nRows):
        if len(s) == 0 or nRows == 1 :
            return s
        tmp = ['' for i in range(nRows)]

        index = -1
        step = 1

        for i in range(len(s)):
            index += step
            if index == nRows:
                index -= 2 ; step = -1
            elif index == -1 :
                index = 1; step =1

            tmp[index] += s[i]
            print tmp
        return ''.join(tmp)

# java solution:
# http://www.programcreek.com/2014/05/leetcode-zigzag-conversion-java/

#test
test = SolutionOther()
#print test.convert("PAYPALISHIRING", 3)
#should return "PAHNAPLSIIGYIR".

#print test.convert("PAYPALISHIRING", 4)
#should return "PINALSHIGYAHRPI"

print test.convert("abcd",3)