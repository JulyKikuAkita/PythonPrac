__source__ = 'https://leetcode.com/problems/zigzag-conversion/#/solutions'
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 6. ZigZag Conversion
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
# String
#
import unittest
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

explanation = '''
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

/*n=numRows
#=2n-2    1                           2n-1                         4n-3
#=        2                     2n-2  2n                    4n-4   4n-2
#=        3               2n-3        2n+1              4n-5       .
#=        .           .               .               .            .
#=        .       n+2                 .           3n               .
#=        n-1 n+1                     3n-3    3n-1                 5n-5
#=2n-2    n                           3n-2                         5n-4
*/
'''

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

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        test = SolutionOther()
        #print test.convert("PAYPALISHIRING", 3)
        #should return "PAHNAPLSIIGYIR".

        #print test.convert("PAYPALISHIRING", 4)
        #should return "PINALSHIGYAHRPI"

        print test.convert("abcd",3)

        #print Solution().convert("PAYPALISHIRING", 3)
        #print Solution().convertiflee("PAYPALISHIRING", 3)
        print Solution().convert("0123456789", 3)
        print Solution().convertiflee("0123456789", 3)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/zigzag-conversion/solution/

# 23ms 94.20%
class Solution {
    public String convert(String s, int numRows) {
        char[] c = s.toCharArray();
        int len = c.length;
        StringBuilder[] sb = new StringBuilder[numRows];
        for (int i = 0; i < sb.length; i++)
            sb[i] = new StringBuilder();

        int i = 0;
        while ( i < len) {
            for (int down = 0; down < numRows && i < len; down++) { // vertically down
                sb[down].append(c[i++]);
            }

            for (int slash = numRows - 2; slash >= 1 && i < len; slash--) { // obliquely up
                sb[slash].append(c[i++]);
            }
        }

        for (int k = 1; k < sb.length; k++) {
            sb[0].append(sb[k]);
        }
        return sb[0].toString();
    }
}

#32ms 69.51%
class Solution {
    public String convert(String s, int numRows) {
        if (numRows <= 1) {
            return s;
        }
        int len = s.length();
        StringBuilder sb = new StringBuilder();
        int interval = (numRows - 1) << 1;
        for (int i = 0; i < len; i += interval) {
            sb.append(s.charAt(i));
        }
        for (int i = 1; i < numRows - 1; i++) {
            int next = interval - ((numRows - i - 1) << 1);
            for (int j = i; j < len; j += next) {
                sb.append(s.charAt(j));
                next = interval - next;
            }
        }
        for (int i = numRows - 1; i < len; i += interval) {
            sb.append(s.charAt(i));
        }
        return sb.toString();
    }
}
'''