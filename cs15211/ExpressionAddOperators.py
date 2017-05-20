__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/expression-add-operators.py
# Time:  O(4^n)
# Space: O(n)
#
# Given a string that contains only digits 0-9
# and a target value, return all possibilities
# to add operators +, -, or * between the digits
# so they evaluate to the target value.
#
# Examples:
# "123", 6 -> ["1+2+3", "1*2*3"]
# "232", 8 -> ["2*3+2", "2+3*2"]
# "00", 0 -> ["0+0", "0-0", "0*0"]
# "3456237490", 9191 -> []
# Google Cryptic Studios
#

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        result, expr = [], []
        val, i = 0, 0
        val_str = ""
        while i < len(num):
            val = val * 10 + ord(num[i]) - ord('0')
            val_str += num[i]
            #Avoid "00...".
            if str(val) != val_str:
                break
            expr.append(val_str)
            self.addOperatorsDFS(num, target, i + 1, 0, val, expr, result)
            expr.pop()
            i += 1
        return result

    def addOperatorsDFS(self, num, target, pos, operand1, operand2, expr, result):
        if pos == len(num) and operand1 + operand2 == target:
            result.append("".join(expr))
        else:
            val, i = 0, pos
            val_str = ""
            while i < len(num):
                val = val * 10 + ord(num[i]) - ord('0')
                val_str += num[i]
                # Avoid "00..."
                if str(val) != val_str:
                    break

                # Case '+':
                expr.append("+" + val_str)
                self.addOperatorsDFS(num, target, i + 1, operand1 + operand2, val, expr, result)
                expr.pop()

                # Case '-':
                expr.append("-" + val_str)
                self.addOperatorsDFS(num, target, i + 1, operand1 + operand2, -val, expr, result)
                expr.pop()

                # Case '*':
                expr.append("*" + val_str)
                self.addOperatorsDFS(num, target, i + 1, operand1, operand2 * val, expr, result)
                expr.pop()

                i += 1

#java
js = '''
public class Solution {
    public List<String> addOperators(String num, int target) {
        List<String> result = new ArrayList<String>();
        calculate(num, target, result, "", 0, 0);
        return result;
    }

    private void calculate(String num, int target, List<String> result, String lastString, long lastResult, long prevNum) {
        if (num.length() == 0 && lastResult == target) {
            result.add(lastString);
            return;
        }
        for (int i = 1; i <= num.length(); i++) {
            String currString = num.substring(0, i);
            if (currString.length() > 1 && currString.charAt(0) == '0') {
                return;
            }
            long currNum = Long.parseLong(currString);
            String next = num.substring(i, num.length());
            if (lastString.length() == 0) {
                calculate(next, target, result, currString, currNum, currNum);
            } else {
                calculate(next, target, result, lastString + '+' + currString, lastResult + currNum, currNum);
                calculate(next, target, result, lastString + '-' + currString, lastResult - currNum, -currNum);
                calculate(next, target, result, lastString + '*' + currString, lastResult - prevNum + prevNum * currNum, prevNum * currNum);
            }
        }
    }
}
'''