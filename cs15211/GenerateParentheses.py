__author__ = 'July'
# Time:  O(4^n / n^(3/2)) ~= Catalan numbers
# Space: O(n)
#
# Given n pairs of parentheses, write a function to generate
# all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# "((()))", "(()())", "(())()", "()(())", "()()()"
# Google Uber Zenefits
# Hide Tags Backtracking String


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

#test
test = SolutionOther()

#print test.generateParenthesis(-1)
#print test.generateParenthesis(0)
#print test.generateParenthesis(1)
#print test.generateParenthesis(2)

if __name__ == "__main__":
    print Solution().generateParenthesis(3)

#java
js = '''
public class Solution {
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
'''