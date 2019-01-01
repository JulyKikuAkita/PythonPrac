__source__ = 'https://leetcode.com/problems/generate-parentheses/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/generate-parentheses.py
# Time:  O(4^n / n^(1/2)) ~= Catalan numbers # https://leetcode.windliang.cc/leetCode-22-Generate-Parentheses.html
# Space: O(n)
# more about Catalan numbers # https://leetcode.windliang.cc/leetCode-22-Generate-Parentheses.html
#
# Note: if asking given n, how many possible combination of valid parentheses,
# the answer would be a catalan number: 1/ (n + 1) (2n over n) = 2n! / ((n +1)! * n!)
 #
# Description: Leetcode # 22. Generate Parentheses
#
# Given n pairs of parentheses, write a function to generate
# all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# "((()))", "(()())", "(())()", "()(())", "()()()"
# Companies
# Google Uber Zenefits Tesla
# Related Topics
# Backtracking String
# Similar Questions
# Letter Combinations of a Phone Number Valid Parentheses
#
import unittest
class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        result = []
        self.generateParenthesisRecu(result, "", n, n)
        return result

    def generateParenthesisRecu(self, result, current, left, right):
        if left == 0 and right == 0:
            result.append(current)

        if left > 0:
            self.generateParenthesisRecu(result, current + "(", left - 1, right)

        if left < right :
            self.generateParenthesisRecu(result, current + ")", left, right - 1)

class SolutionOther:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        self.ans, tmp = [], []
        lb = 0
        self.dfs(lb, 0, n , tmp)
        return self.ans

    def dfs(self, lb, totalp , n ,tmp):
        if totalp == n * 2:
            self.ans.append(''.join(tmp))
            #print lb, tmp ,totalp, self.ans
            return
        if lb < n:
            #print lb, tmp ,totalp, self.ans
            tmp.append('(')
            self.dfs(lb+1, totalp+1, n, tmp)
            tmp.pop()
            #print "tmppop", lb, tmp ,totalp
        if totalp - lb < lb:
            #print lb , tmp, totalp, self.ans
            tmp.append(')')
            self.dfs(lb, totalp+1, n, tmp)
            tmp.pop()
            #print "tmppop", lb, tmp ,totalp

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().generateParenthesis(3)
        #test
        test = SolutionOther()

        #print test.generateParenthesis(-1)
        #print test.generateParenthesis(0)
        #print test.generateParenthesis(1)
        #print test.generateParenthesis(2)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/generate-parentheses/solution/
# https://leetcode.windliang.cc/leetCode-22-Generate-Parentheses.html

# 1ms 100%
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        generate(result, new char[n << 1], 0, n, n);
        return result;
    }

    private void generate(List<String> result, char[] arr, int index, int left, int right) {
        if (index == arr.length) {
            result.add(new String(arr));
            return;
        }

        if (left > 0) {
            arr[index] = '(';
            generate(result, arr, index + 1, left - 1, right);
        }
        if (right > left) {
            arr[index] = ')';
            generate(result, arr, index + 1, left, right - 1);
        }
    }
}

# 1ms 100%
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        if (n <= 0) {
            return result;
        }
        generate(result, new StringBuilder(), n, n);
        return result;
    }

    private void generate(List<String> result, StringBuilder sb, int left, int right) {
        if (left == 0 && right == 0) {
            result.add(sb.toString());
            return;
        }
        int length = sb.length();
        if (left > 0) {
            sb.append('(');
            generate(result, sb, left - 1, right);
            sb.setLength(length);
        }
        if (right > left) {
            sb.append(')');
            generate(result, sb, left, right - 1);
            sb.setLength(length);
        }
    }
}

# Complexity Analysis
# Our complexity analysis rests on understanding how many elements there are in generateParenthesis(n). 
# This analysis is outside the scope of this article, 
# but it turns out this is the n-th Catalan number 1 / (n + 1) (2n over n), 
# which is bounded asymptotically by 4^n / n * (n ^ 1/2)
# Time Complexity : O(4^n / n * (n ^ 1/2)). Each valid sequence has at most n steps during the backtracking procedure.
# Space Complexity : O(4^n / n * (n ^ 1/2)), as described above, and using O(n) space to store the sequence. 
# 2ms 66.17%
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> list = new ArrayList<String>();
        backtrack(list, "", 0, 0, n);
        return list;
    }

    public void backtrack(List<String> list, String str, int open, int close, int max){
        if(str.length() == max*2){
            list.add(str);
            return;
        }
        if(open < max)
            backtrack(list, str+"(", open+1, close, max);
        if(close < open)
            backtrack(list, str+")", open, close+1, max);
    }
}

# Iteration:
# 26.31% 5ms

My method is DP. First consider how to get the result f(n) from previous result f(0)...f(n-1).
Actually, the result f(n) will be put an extra () pair to f(n-1). Let the "(" always at the first position,
to produce a valid result, we can only put ")" in a way that
there will be i pairs () inside the extra () and n - 1 - i pairs () outside the extra pair.

Let us consider an example to get clear view:

f(0): ""

f(1): "("f(0)")"

f(2): "("f(0)")"f(1), "("f(1)")"

f(3): "("f(0)")"f(2), "("f(1)")"f(1), "("f(2)")"

So f(n) = "("f(0)")"f(n-1) , "("f(1)")"f(n-2) "("f(2)")"f(n-3) ... "("f(i)")"f(n-1-i) ... "(f(n-1)")"


# 2ms 66.17%
class Solution {
    public List<String> generateParenthesis(int n) {
        List<List<String>> lists = new ArrayList<>();
        lists.add(Collections.singletonList(""));

        for (int i = 1; i <= n; ++i){
            List<String> list = new ArrayList<>();
            for (int j = 0; j < i; ++j) {
                for (String first : lists.get(j)) {
                    for (String sec: lists.get(i - 1 - j)) {
                        list.add('(' + first + ')' + sec);
                    }
                }
            }
            lists.add(list);
        }
        return lists.get(lists.size() - 1);
    }
}

# same idea
# 7ms 9.25%
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> ans = new ArrayList();
        if (n == 0) {
            ans.add("");
        } else {
            for (int a = 0; a < n; a++) {
                for (String left : generateParenthesis(a)) {
                    for (String right : generateParenthesis(n - a - 1)) {
                        ans.add("(" + left + ")" + right);
                    }
                }
            }
        }
        return ans;
    }
}

# @Tesla interview
// the input n is total length of parenthesis
// need to validate if n is even number
# 1ms 100%
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        dfs(n, n, res, new StringBuilder());
        return res;
    }

    private void dfs(int left, int right, List<String> res, StringBuilder sb) {
        if (left < 0 || right < 0) return;
        if (right == 0) {
            //System.out.println(sb.toString());
            res.add(sb.toString());
            return;
        }
        sb.append("(");
        dfs(left - 1, right, res, sb);
        sb.setLength(sb.length() - 1);

        if (right > left) {
            sb.append(")");
            dfs(left, right -1, res, sb);
            sb.setLength(sb.length() - 1);
        }
    }
}
'''
