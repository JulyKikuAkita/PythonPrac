__author__ = 'July'
'''
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers.
Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Follow up:
How would you handle overflow for very large input integers?

Epic Systems

'''
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



#java
js = '''
public class Solution {
    public boolean isAdditiveNumber(String num) {
        for(int i = 0 ; i < num.length(); i++){
            for(int j = i+1; j < num.length() - 1; j++){
                String fir = num.substring(0, i+1);
                String sec= num.substring(i+1, j+1);

                if( dfs(num, j+1, fir, sec)) return true;
            }
        }
        return false;
    }

    private boolean dfs(String input, int idx, String fir, String sec){
        if( idx == input.length()) return true;

        if(fir.length() > 1 && fir.charAt(0) == '0') {
            return false;
        }

        if(sec.length() > 1 && sec.charAt(0) == '0') {
            return false;
        }

        long sum = Long.parseLong(fir) + Long.parseLong(sec);
        String cur = Long.toString(sum);

        if(!input.substring(idx).startsWith(cur)){
            return false;
        }

        return dfs(input, idx + cur.length(), sec, cur);

    }
}

public class Solution {
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