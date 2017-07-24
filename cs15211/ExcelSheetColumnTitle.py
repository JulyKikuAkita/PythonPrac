__source__ = 'https://leetcode.com/problems/excel-sheet-column-title/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/excel-sheet-column-title.py
# Time:  O(logn)
# Space: O(1)
# Math
#
# Description: Leetcode # 168. Excel Sheet Column Title
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
# Companies
# Microsoft Facebook Zenefits
# Related Topics
# Math
# Similar Questions
# Excel Sheet Column Number
#
import unittest
# 39ms
class Solution2(object):
    def convertToTitle(self, num):
        """
        :type n: int
        :rtype: str
        """
        return "" if num == 0 else self.convertToTitle((num - 1) / 26) + chr((num - 1) % 26 + ord('A'))

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

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().containsDuplicate([12344555,12344555])

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:

# 7.37% 0ms
public class Solution {
    public String convertToTitle(int n) {
        return n == 0 ? "" : convertToTitle(--n / 26) + (char)('A' + (n % 26));
    }
}

# 7.37% 0ms
public class Solution {
    public String convertToTitle(int n) {
        StringBuilder sb = new StringBuilder();
        while (--n >= 0) {
            sb.append((char) (n % 26 + 'A'));
            n /= 26;
        }
        return sb.reverse().toString();
    }
}

# 7.37% 0ms
public class Solution {
    public String convertToTitle(int n) {
        StringBuilder b = new StringBuilder();

        do {
            n--;
            int r = n % 26;
            b.append(getLetter(r));
            n -= r;
            n /= 26;
        } while (n > 0);

        return b.reverse().toString();
    }

    private char getLetter(int n) {
        int a = (int) 'A';
        return (char) (a + n);
    }
}
'''