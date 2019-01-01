__source__ = 'https://leetcode.com/problems/least-operators-to-express-number/solution/'
# Time:  (Logx target)
# Space: (Log target)
#
# Description: Leetcode # 964. Least Operators to Express Number
#
# Given a single positive integer x,
# we will write an expression of the form x (op1) x (op2) x (op3) x ...
# where each operator op1, op2, etc. is either addition, subtraction, multiplication, or division (+, -, *, or /).
# For example, with x = 3, we might write 3 * 3 / 3 + 3 - 3 which is a value of 3.
#
# When writing such an expression, we adhere to the following conventions:
#
#     The division operator (/) returns rational numbers.
#     There are no parentheses placed anywhere.
#     We use the usual order of operations: multiplication and division happens before addition and subtraction.
#     It's not allowed to use the unary negation operator (-).
#     For example, "x - x" is a valid expression as it only uses subtraction,
#       but "-x + x" is not because it uses negation.
#
# We would like to write an expression with the least number of operators
# such that the expression equals the given target.  Return the least number of operators used.
#
# Example 1:
#
# Input: x = 3, target = 19
# Output: 5
# Explanation: 3 * 3 + 3 * 3 + 3 / 3.  The expression contains 5 operations.
#
# Example 2:
#
# Input: x = 5, target = 501
# Output: 8
# Explanation: 5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5.  The expression contains 8 operations.
#
# Example 3:
#
# Input: x = 100, target = 100000000
# Output: 3
# Explanation: 100 * 100 * 100 * 100.  The expression contains 3 operations.
#
# Note:
#
#     2 <= x <= 100
#     1 <= target <= 2 * 10^8
#
import unittest


class Solution:
    pass  # start coding


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/least-operators-to-express-number/solution/
#
Approach 1: Dynamic Programming
Complexity Analysis
Time Complexity: O(Logx target). We can prove that we only visit up to two states for each base-x digit of target.
Space Complexity: O(Log target)

# 13ms 47.47%
class Solution {
    Map<String, Integer> memo;
    int x;
    public int leastOpsExpressTarget(int x, int target) {
        memo = new HashMap();
        this.x = x;
        return dp(0, target) - 1;
    }

    public int dp(int i, int target) {
        String code = "" + i + "#" + target;
        if (memo.containsKey(code))
            return memo.get(code);

        int ans;
        if (target == 0) {
            ans = 0;
        } else if (target == 1) {
            ans = cost(i);
        } else if (i >= 39) {
            ans = target + 1;
        } else {
            int t = target / x;
            int r = target % x;
            ans = Math.min(r * cost(i) + dp(i+1, t),
                           (x-r) * cost(i) + dp(i+1, t+1));
        }

        memo.put(code, ans);
        return ans;
    }

    public int cost(int x) {
        return x > 0 ? x : 2;
    }
}

# https://leetcode.com/problems/least-operators-to-express-number/discuss/208349/JavaC%2B%2BPython-O(logY)-Time-and-O(1)-Space
# 9ms 80.70%
class Solution {
    public int leastOpsExpressTarget(int x, int target) {
        int pos = 0, neg = 0, k = 0, pos2, neg2, cur;
        while (target > 0) {
            cur = target % x;
            target /= x;
            if (k > 0) {
                pos2 = Math.min(cur * k + pos, (cur + 1) * k + neg);
                neg2 = Math.min((x - cur) * k + pos, (x - cur - 1) * k + neg);
                pos = pos2;
                neg = neg2;
            } else {
                pos = cur * 2;
                neg = (x - cur) * 2;
            }
            k++;
        }
        return Math.min(pos, k + neg) - 1;
    }
}   
'''
