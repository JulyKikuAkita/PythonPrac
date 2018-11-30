import collections

__source__ = 'https://leetcode.com/problems/parse-lisp-expression/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 736. Parse Lisp Expression
#
# You are given a string expression representing a Lisp-like expression to return the integer value of.
#
# The syntax for these expressions is given as follows.
#
# An expression is either an integer,
# a let-expression, an add-expression,
# a mult-expression, or an assigned variable.
#
# Expressions always evaluate to a single integer.
# (An integer could be positive or negative.)
# A let-expression takes the form (let v1 e1 v2 e2 ... vn en expr),
# where let is always the string "let", then there are 1 or more pairs of alternating variables and expressions,
# meaning that the first variable v1 is assigned the value of the expression e1,
# the second variable v2 is assigned the value of the expression e2, and so on sequentially;
# and then the value of this let-expression is the value of the expression expr.
# An add-expression takes the form (add e1 e2) where add is always the string "add",
# there are always two expressions e1, e2,
# and this expression evaluates to the addition of the evaluation of e1 and the evaluation of e2.
# A mult-expression takes the form (mult e1 e2) where mult is always the string "mult",
# there are always two expressions e1, e2,
# and this expression evaluates to the multiplication of the evaluation of e1 and the evaluation of e2.
# For the purposes of this question, we will use a smaller subset of variable names.
# A variable starts with a lowercase letter, then zero or more lowercase letters or digits.
# Additionally for your convenience, the names "add", "let",
# or "mult" are protected and will never be used as variable names.
# Finally, there is the concept of scope. When an expression of a variable name is evaluated,
# within the context of that evaluation,
# the innermost scope (in terms of parentheses) is checked first for the value of that variable,
# and then outer scopes are checked sequentially.
# It is guaranteed that every expression is legal.
# Please see the examples for more details on scope.
#
# Evaluation Examples:
# Input: (add 1 2)
# Output: 3
#
# Input: (mult 3 (add 2 3))
# Output: 15
#
# Input: (let x 2 (mult x 5))
# Output: 10
#
# Input: (let x 2 (mult x (let x 3 y 4 (add x y))))
# Output: 14
# Explanation: In the expression (add x y), when checking for the value of the variable x,
# we check from the innermost scope to the outermost in the context of the variable we are trying to evaluate.
# Since x = 3 is found first, the value of x is 3.
#
# Input: (let x 3 x 2 x)
# Output: 2
# Explanation: Assignment in let statements is processed sequentially.
#
# Input: (let x 1 y 2 x (add x y) (add x y))
# Output: 5
# Explanation: The first (add x y) evaluates as 3, and is assigned to x.
# The second (add x y) evaluates as 3+2 = 5.
#
# Input: (let x 2 (add (let x 3 (let x 4 x)) x))
# Output: 6
# Explanation: Even though (let x 4 x) has a deeper scope, it is outside the context
# of the final x in the add-expression.  That final x will equal 2.
#
# Input: (let a1 3 b2 (add a1 1) b2)
# Output 4
# Explanation: Variable names can contain digits after the first character.
#
# Note:
#
# The given string expression is well formatted: There are no leading or trailing spaces,
# there is only a single space separating different components of the string,
# and no space between adjacent parentheses. The expression is guaranteed to be legal and evaluate to an integer.
# The length of expression is at most 2000. (It is also non-empty, as that would not be a legal expression.)
# The answer and all intermediate calculations of that answer are guaranteed to fit in a 32-bit integer.
#
import unittest

#24ms 100%
class Solution(object):
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        def tokenizer(expression):
            return collections.deque(expression.replace('(', '( ').replace(')', ' )').split(' '))

        def eval(env, tokens):
            if tokens[0] != '(':
                token = tokens.popleft()
                if token[0] in '0123456789-':
                    return int(token)
                else:
                    return env[token]

            else:
                tokens.popleft()
                if tokens[0] in ('add', 'mult'):
                    op = tokens.popleft()
                    left, right = eval(env, tokens), eval(env, tokens)
                    val = left+right if op == 'add' else left*right
                else:
                    #let
                    tokens.popleft()
                    local = env.copy()
                    while tokens[0] != '(' and tokens[1] != ')':
                        name = tokens.popleft()
                        local[name] = eval(local, tokens)
                    val = eval(local, tokens)
                tokens.popleft()
                return val
        return eval({}, tokenizer(expression))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/parse-lisp-expression/solution/

Complexity Analysis
Approach #1: Recursive Parsing [Accepted]
Time Complexity: O(N^2), where N is the length of expression.
Each expression is evaluated once, but within that evaluation we may search the entire scope.
Space Complexity: O(N^2).
We may pass O(N) new strings to our evaluate function when making intermediate evaluations, each of length O(N).
With effort, we could reduce the total space complexity to O(N) with interning or passing pointers.

#11ms 57.32%
class Solution {
    ArrayList<Map<String, Integer>> scope;
    public Solution() {
        scope = new ArrayList();
        scope.add(new HashMap());
    }

    public int evaluate(String expression) {
        scope.add(new HashMap());
        int ans = evaluate_inner(expression);
        scope.remove(scope.size() - 1);
        return ans;
    }

    private int evaluate_inner(String expression) {
        if (expression.charAt(0) != '(') {
            if (Character.isDigit(expression.charAt(0)) || expression.charAt(0) == '-') {
                return Integer.parseInt(expression);
            }

            for(int i = scope.size() - 1; i >= 0; i--) {
                if (scope.get(i).containsKey(expression)) return scope.get(i).get(expression);
            }
        }

        List<String> tokens = parse(expression.substring(expression.charAt(1) == 'm' ? 6: 5, expression.length() - 1));
        if (expression.startsWith("add", 1)) {
            return evaluate(tokens.get(0)) + evaluate(tokens.get(1));
        } else if(expression.startsWith("mult", 1)) {
            return evaluate(tokens.get(0)) * evaluate(tokens.get(1));
        } else {
            for (int j = 1; j < tokens.size(); j += 2) {
                scope.get(scope.size() - 1).put(tokens.get(j - 1), evaluate(tokens.get(j)));
            }
            return evaluate(tokens.get(tokens.size() - 1));
        }
    }

    private List<String> parse(String expression) {
        List<String> ans = new ArrayList();
        int bal = 0;
        StringBuilder sb = new StringBuilder();
        for (String token : expression.split(" ")) {
            for (char c: token.toCharArray()) {
                if (c == '(') bal++;
                if (c == ')') bal--;
            }
            if (sb.length() > 0) sb.append(" ");
            sb.append(token);
            if (bal == 0) {
                ans.add(sb.toString());
                sb = new StringBuilder();
            }
        }

        if (sb.length() > 0) ans.add(sb.toString());
        return ans;
    }
}

#7ms 98.73%
class Solution {
    public int evaluate(String expression) {
        Map<String, Stack<Integer>> map = new HashMap<>();
        int[] res = helper(expression, 0, map);
        return res[1];
    }

    private int[] helper(String s, int i, Map<String, Stack<Integer>> map) {
        i++;
        char op = s.charAt(i);
        if (op == 'l') { // let
            i += 4;
            List<String> vs = new ArrayList();
            while (i < s.length()) {
                if (s.charAt(i) == '(') {
                    int[] res = helper(s, i, map);
                    for (String v : vs) {
                        Stack<Integer> st = map.get(v);
                        st.pop();
                        if (st.isEmpty()) map.remove(v);
                    }
                    return new int[]{res[0] + 1, res[1]};
                } else {
                    int start = i;
                    while (s.charAt(i) != ')' && s.charAt(i) != ' ') i++;
                    if (s.charAt(i) == ')') {
                        int[] tmp = parseValue(s, start, map);
                        for (String v : vs) {
                            Stack<Integer> st = map.get(v);
                            st.pop();
                            if (st.isEmpty()) map.remove(v);
                        }
                        return new int[]{i, tmp[1]};
                    }
                    int end = i;
                    String v = s.substring(start, end);
                    i++;
                    int[] tmp = parseValue(s, i, map);
                    vs.add(v);
                    Stack<Integer> st = map.getOrDefault(v, new Stack<>());
                    st.push(tmp[1]);
                    map.put(v, st);
                    i = tmp[0] + 2;
                }
            }
        } else if (op == 'a') { //add
            i = i + 4;
            int[] tmp = parseValue(s, i, map);
            int val1 = tmp[1];
            tmp = parseValue(s, tmp[0] + 2, map);
            int val2 = tmp[1];
            return new int[]{tmp[0] + 1, val1 + val2};
        } else {
            i = i + 5; //multi
            int[] tmp = parseValue(s, i, map);
            int val1 = tmp[1];
            tmp = parseValue(s, tmp[0] + 2, map);
            int val2 = tmp[1];
            return new int[]{tmp[0] + 1, val1 * val2};
        }
        return new int[]{-1, -1};
    }

    private int[] parseValue(String s, int i, Map<String, Stack<Integer>> map) {
      if (s.charAt(i) == '(') return helper(s, i, map);
        int start = i;
        while (s.charAt(i) != ')' && s.charAt(i) != ' ') i++;
        int end = i;
        int val;
        if (Character.isDigit(s.charAt(start)) || s.charAt(start) == '-') {
            val = Integer.parseInt(s.substring(start, end));
        } else {
            Stack<Integer> stack = map.get(s.substring(start, end));
            val = stack.peek();
        }
        return new int[]{end - 1, val};
    }
}
'''