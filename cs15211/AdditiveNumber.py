__source__ = 'https://leetcode.com/problems/additive-number/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/additive-number.py
# Time:  O(n^3)
# Space: O(n)
#
# Description: Leetcode # 306. Additive Number
#
# Additive number is a positive integer whose digits can form additive sequence.
#
# A valid additive sequence should contain at least three numbers.
# Except for the first two numbers, each subsequent number in the sequence
# must be the sum of the preceding two.
#
# For example:
# "112358" is an additive number because the digits can form an additive sequence:
#   1, 1, 2, 3, 5, 8.
#
# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# "199100199" is also an additive number, the additive sequence is:
# 1, 99, 100, 199.
#
# 1 + 99 = 100, 99 + 100 = 199
# Note: Numbers in the additive sequence cannot have leading zeros,
# so sequence 1, 2, 03 or 1, 02, 3 is invalid.
#
# Given a string represents an integer, write a function to determine
# if it's an additive number.
#
# Follow up:
# How would you handle overflow for very large input integers?
#
# Companies
# Epic Systems
import unittest
# https://leetcode.com/discuss/70119/backtracking-with-pruning-java-solution-and-python-solution
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num or len(num) < 3:
            return False

        n = len(num)
        for i in xrange(1, n):
            if i > 1 and num[0] == '0':
                break

            for j in xrange(i+1, n):
                first, second, third = 0, i, j
                if num[second] == '0' and third > second + 1:
                    break
                while third < n:
                    res = str(int(num[first:second]) + int(num[second:third]))
                    if num[third:].startswith(res):
                        first, second, third = second, third, third + len(res)
                    else:
                        break
                if third == n:
                    return True
        return False

class Solution2(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def add(a, b):
            res, carry, val = "", 0, 0
            for i in xrange(max(len(a), len(b))):
                val = carry
                if i < len(a):
                    val += int(a[-(i + 1)])
                if i < len(b):
                    val += int(b[-(i + 1)])
                carry, val = val / 10, val % 10
                res += str(val)
            if carry:
                res += str(carry)
            return res[::-1]


        for i in xrange(1, len(num)):
            for j in xrange(i + 1, len(num)):
                s1, s2 = num[0:i], num[i:j]
                if (len(s1) > 1 and s1[0] == '0') or \
                   (len(s2) > 1 and s2[0] == '0'):
                    continue

                expected = add(s1, s2)
                cur = s1 + s2 + expected
                while len(cur) < len(num):
                    s1, s2, expected = s2, expected, add(s2, expected)
                    cur += expected
                if cur == num:
                    return True
        return False

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().containsDuplicate([12344555,12344555])

if __name__ == '__main__':
    unittest.main()

Java = '''
#97.92% 1ms
class Solution {
    public boolean isAdditiveNumber(String num) {
        for(int i = 0; i < num.length(); i++) {
            for( int j = i + 1; j < num.length() - 1; j++) {
                String fir = num.substring(0, i + 1)    ;
                String sec = num.substring(i + 1, j + 1);
                if (dfs(num, j + 1, fir, sec)) return true;
            }
        }
        return false;
    }

    public boolean dfs(String num, int idx, String fir, String sec){
        if (idx == num.length()) return true;
        if (fir.length() > 1 && fir.charAt(0) == '0') return false;
        if (sec.length() > 1 && sec.charAt(0) == '0') return false;
        long sum = Long.parseLong(fir) + Long.parseLong(sec);
        String cur = Long.toString(sum);
        if (! num.substring(idx).startsWith(cur)) return false;
        return dfs(num, idx + cur.length(), sec, cur);
    }
}

#DFS
#31.76% 3ms
import java.math.BigInteger;

class Solution {
    public boolean isAdditiveNumber(String num) {
        int n = num.length();
        for (int i = 1; i <= n / 2; ++i) {
            if (num.charAt(0) == '0' && i > 1) return false;
            BigInteger x1 = new BigInteger(num.substring(0, i));
            for (int j = 1; Math.max(j, i) <= n - i - j; ++j) {
                if (num.charAt(i) == '0' && j > 1) break;
                BigInteger x2 = new BigInteger(num.substring(i, i + j));
                if (isValid(x1, x2, j + i, num)) return true;
            }
        }
        return false;
    }
    private boolean isValid(BigInteger x1, BigInteger x2, int start, String num) {
        if (start == num.length()) return true;
        x2 = x2.add(x1);
        x1 = x2.subtract(x1);
        String sum = x2.toString();
        return num.startsWith(sum, start) && isValid(x1, x2, start + sum.length(), num);
    }
}

#97.92% 1ms
class Solution {
    public boolean isAdditiveNumber(String num) {
        int n = num.length();
        for (int i = 1; i <= n / 2; ++i)
            for (int j = 1; Math.max(j, i) <= n - i - j; ++j)
                if (isValid(i, j, num)) return true;
        return false;
    }
    private boolean isValid(int i, int j, String num) {
        if (num.charAt(0) == '0' && i > 1) return false;
        if (num.charAt(i) == '0' && j > 1) return false;
        String sum;
        Long x1 = Long.parseLong(num.substring(0, i));
        Long x2 = Long.parseLong(num.substring(i, i + j));
        for (int start = i + j; start != num.length(); start += sum.length()) {
            x2 = x2 + x1;
            x1 = x2 - x1;
            sum = x2.toString();
            if (!num.startsWith(sum, start)) return false;
        }
        return true;
    }
}

#97.92% 1ms
class Solution {
    public boolean isAdditiveNumber(String num) {
        int len = num.length();
        for (int i = 0; i <= len / 2; i++) {
            if (num.charAt(0) == '0' && i > 0) {
                break;
            }
            for (int j = i + 1; j < len * 2 / 3; j++) {
                if (num.charAt(i + 1) == '0' && j > i + 1) {
                    break;
                }
                if (isAdditiveNumber(num.substring(0, i + 1), num.substring(i + 1, j + 1), num.substring(j + 1))) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean isAdditiveNumber(String num1, String num2, String remain) {
        if (remain.length() == 0) {
            return true;
        } else if (remain.length() > 1 && remain.charAt(0) == '0') {
            return false;
        }
        String sum = sum(num1, num2);
        if (remain.startsWith(sum)) {
            return isAdditiveNumber(num2, sum, remain.substring(sum.length()));
        }
        return false;
    }

    private String sum(String num1, String num2) {
        num1 = new StringBuilder(num1).reverse().toString();
        num2 = new StringBuilder(num2).reverse().toString();
        int len1 = num1.length();
        int len2 = num2.length();
        int minLen = Math.min(len1, len2);
        StringBuilder sb = new StringBuilder();
        int carry = 0;
        for (int i = 0; i < minLen; i++) {
            int sum = (num1.charAt(i) - '0') + (num2.charAt(i) - '0') + carry;
            sb.append(sum % 10);
            carry = sum / 10;
        }
        for (int i = minLen; i < len1; i++) {
            int sum = num1.charAt(i) - '0' + carry;
            sb.append(sum % 10);
            carry = sum / 10;
        }
        for (int i = minLen; i < len2; i++) {
            int sum = num2.charAt(i) - '0' + carry;
            sb.append(sum % 10);
            carry = sum / 10;
        }
        if (carry > 0) {
            sb.append(carry);
        }
        return sb.reverse().toString();
    }
}
'''