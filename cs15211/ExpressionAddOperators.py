__source__ = 'https://leetcode.com/problems/expression-add-operators/#/description'
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
#  Google Facebook
# Hide Tags Divide and Conquer
# Hide Similar Problems (M) Evaluate Reverse Polish Notation
# (H) Basic Calculator (M) Basic Calculator II (M) Different Ways to Add Parentheses (M) Target Sum


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
java = '''
Thought:
This problem has a lot of edge cases to be considered:

overflow: we use a long type once it is larger than Integer.MAX_VALUE or minimum, we get over it.
0 sequence: because we can't have numbers with multiple digits started with zero, we have to deal with it too.
a little trick is that we should save the value that is to be multiplied in the next recursion.

# 53%
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

# 90%
public class Solution {
    public List<String> addOperators(String num, int target) {
        List<String> result = new ArrayList<>();
        addOperators(num, target, 0, result, new StringBuilder(), 0, 0);
        return result;
    }

    private void addOperators(String num, long target, int index, List<String> result, StringBuilder sb, long curNum, long lastNum) {
        if (index == num.length()) {
            if (curNum == target) {
                result.add(sb.toString());
            }
            return;
        }
        int len = sb.length();
        long cur = 0;
        for (int i = index; i < num.length(); i++) {
            cur = cur * 10 + num.charAt(i) - '0';
            if (len == 0) {
                addOperators(num, target, i + 1, result, sb.append(cur), cur, cur);
                sb.setLength(len);
            } else {
                addOperators(num, target, i + 1, result, sb.append('+').append(cur), curNum + cur, cur);
                sb.setLength(len);
                addOperators(num, target, i + 1, result, sb.append('-').append(cur), curNum - cur, -cur);
                sb.setLength(len);
                addOperators(num, target, i + 1, result, sb.append('*').append(cur), curNum - lastNum + lastNum * cur, lastNum * cur);
                sb.setLength(len);
            }
            if (num.charAt(index) == '0') { // check index (not i) do not start with 0
                break;
            }
        }
    }
}

'''