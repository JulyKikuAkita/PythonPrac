# https://github.com/kamyu104/LeetCode/blob/master/Python/add-strings.py
# Time:  O(n)
# Space: O(1)

# Given two non-negative numbers num1 and num2 represented as string,
# return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or
# convert the inputs to integer directly.
#
#
# Google Airbnb
# Hide Tags Math
# Hide Similar Problems (M) Add Two Numbers (M) Multiply Strings

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = []
        i, j, carry = len(num1) - 1, len(num2) - 1, 0

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += ord(num1[i]) - ord('0');
                i -= 1
            if j >= 0:
                carry += ord(num2[j]) - ord('0');
                j -= 1
            result.append(str(carry % 10))
            carry /= 10
        result.reverse()

        return "".join(result)

    def addStrings2(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        length = max(len(num1), len(num2))
        num1 = num1.zfill(length)[::-1]
        num2 = num2.zfill(length)[::-1]
        res, plus = '', 0
        for index, num in enumerate(num1):
            tmp = str(int(num) + int(num2[index]) + plus)
            res += tmp[-1]
            if int(tmp) > 9:
                plus = 1
            else:
                plus = 0
        if plus:
            res += '1'
        return res[::-1]

java = '''
public class Solution {
    public String addStrings(String num1, String num2) {
        StringBuilder sb = new StringBuilder();
        int carry = 0;

        for (int i = num1.length() - 1, j = num2.length() - 1; i >= 0 || j >= 0 || carry == 1; i--, j--) {
            int x = i < 0 ? 0 : num1.charAt(i) - '0';
            int y = j < 0 ? 0 : num2.charAt(j) - '0';
            sb.append((x + y +carry) % 10);
            carry = ( x+ y + carry) / 10;
        }
        return sb.reverse().toString();
    }
}
'''