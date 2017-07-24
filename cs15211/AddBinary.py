__source__ = 'https://leetcode.com/problems/add-binary/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/add-binary.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 67. Add Binary
#
# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".
#
# Companies
# Facebook
# Related Topics
# Math String
# Similar Questions
# Add Two Numbers Multiply Strings Plus One
#
import unittest
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        result, carry, val, len_a, len_b, i = "", 0,0, len(a), len(b), 0

        for i in xrange(max(len_a, len_b)):
            val = carry
            if i < len_a:
                val += int(a[-(i + 1)])
            if i < len_b:
                val += int(b[-(i + 1)])
            carry, val = val / 2, val % 2
            print carry, val, result
            # format example: https://docs.python.org/3/library/string.html#formatspec
            result = "{0}{1}".format(val, result)

        if carry == 1:
            result = "1" + result
        return result

class Solution2:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        a = [ord(c) - ord('0') for c in a][::-1]
        b = [ord(c) - ord('0') for c in b][::-1]
        print a,b
        if len(a) < len(b):
            a,b = b,a
        flag = 0
        for i in range(len(a)):
            if  i < len(b):
                a[i] += b[i]
            a[i] += flag
            flag = a[i]//2
            a[i] %= 2
            print "loop", flag, a[i], i

        if flag:
            a.append(1)
        return ''.join([chr(c + ord('0'))for c in a][::-1])

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        result = Solution().addBinary('11', '1')
        print result

        #test
        test = Solution2()
        print test.addBinary('11', '1')
        #print [ord(c) - ord('0') for c in '10'][::-1]

if __name__ == '__main__':
    unittest.main()

Java = '''
# 46.06% 4ms
public class Solution {
    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int i = a.length() - 1, j = b.length() -1, carry = 0;
        while (i >= 0 || j >= 0) {
            int sum = carry;
            if (j >= 0) sum += b.charAt(j--) - '0';
            if (i >= 0) sum += a.charAt(i--) - '0';
            sb.append(sum % 2);
            carry = sum / 2;
        }
        if (carry != 0) sb.append(carry);
        return sb.reverse().toString();
    }
}

# 81.92% 3ms
public class Solution {
    public String addBinary(String a, String b) {
        int lenA = a.length();
        int lenB = b.length();
        char[] result = new char[lenA + lenB];
        Arrays.fill(result, '0');
        int index = result.length - 1;
        int carry = 0;
        for (int i = lenA - 1, j = lenB - 1; i >= 0 || j >= 0; i--, j--, index--) {
            int m = i >= 0 ? a.charAt(i) - '0' : 0;
            int n = j >= 0 ? b.charAt(j) - '0' : 0;
            int sum = m + n + carry;
            result[index] = (char) (sum % 2 + '0');
            carry = sum / 2;
        }
        result[index] = (char) (carry + '0');
        int start = 0;
        while (start < result.length - 1 && result[start] == '0') {
            start++;
        }
        return new String(result).substring(start);
    }
}

'''

