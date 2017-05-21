__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/letter-combinations-of-a-phone-number.py
# Time:  O(n * 4^n)
# Space: O(n)
# Brute Force Search
#
# Given a digit string, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.
#
# lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
#
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.
#
#  Amazon Dropbox Google Uber Facebook
# Hide Tags Backtracking String
# Hide Similar Problems (M) Generate Parentheses (M) Combination Sum (E) Binary Watch

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if '' == digits: return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])
#
# Iterative Solution
class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        lookup, result = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"], [""]
        for digit in digits:
            choices = lookup[int(digit)]
            m, n = len(choices), len(result)
            result.extend(result[i % n] for i in xrange(n, m * n))
            print result, m ,n

            for i in xrange(m * n):
                result[i] += choices[i/n]
        return result


# Time:  O(n * 4^n)
# Space: O(n)
# Recursive Solution
class Solution2:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        lookup, result = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"], []
        self.letterCombinationsRecu(result, digits, lookup, "", 0)
        return result

    def letterCombinationsRecu(self, result, digits, lookup, cur, n):
        if n == len(digits):
            result.append(cur)
        else:
            for choice in lookup[int(digits[n])]:
                self.letterCombinationsRecu(result, digits, lookup, cur + choice, n + 1)

if __name__ == "__main__":
    print Solution().letterCombinations("23")
    print Solution2().letterCombinations("23")
    print [].extend("abc")

class SolutionOther:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return [""]
        self.mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.ans , tmp = [],[]
        self.dfs(digits, 0, tmp)
        return self.ans

    def dfs(self, digits, p, tmp):
        if (p == len(digits)):
            self.ans.append(''.join(tmp))
            print self.ans
            return

        for char in self.mapping[ord(digits[p]) - ord('0')]:
            print char, ord(digits[p]), ord('0'), self.mapping[ord(digits[p]) -ord('0')]
            tmp.append(char)
            self.dfs(digits,p+1, tmp)
            tmp.pop()

#test
test = SolutionOther()
#print test.letterCombinations("23")

# ord('3')- ord('0')  # an easy way to stoi
# any iterable will do for extend (not just list)
# extend outperforms append, as the loop is implemented in C.
# [].extend("string") will give you ["s", "t", "r", "i", "n", "g"]
# [].append("string") will give you ["string"]
# [].extend("") = []

#java
js = '''
Recursion:
public class Solution {
    private static final String[] PHONE_NUMBERS = new String[] {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits.length() == 0) {
            return result;
        }
        letterCombinations(digits, 0, result, new StringBuilder());
        return result;
    }

    private void letterCombinations(String digits, int index, List<String> result, StringBuilder sb) {
        if (index == digits.length()) {
            result.add(sb.toString());
            return;
        }
        for (char c : PHONE_NUMBERS[digits.charAt(index) - '2'].toCharArray()) {
            sb.append(c);
            letterCombinations(digits, index + 1, result, sb);
            sb.setLength(sb.length() - 1);
        }
    }
}

//use template but need to take care of 2 double while loop
public class Solution {
    public static String[] dict = new String[] {null, null, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public List<String> letterCombinations(String digits) { //"23"
        List<String> res = new LinkedList<>();
        if (digits == null || digits.length() == 0) return res;
        backtrack(res, new StringBuilder(), digits, 0);
        return res;
    }

    private void backtrack(List<String> res, StringBuilder sb, String digits, int start) {
        if (sb.length() == digits.length()) {
            res.add(sb.toString());
            return;
        }
        for (int j = start; j < digits.length(); j++) {
            char c = digits.charAt(j);
            char[] poolChars = dict[ c- '0'].toCharArray();
            for (int i = 0; i < poolChars.length; i++) {
                sb.append(poolChars[i]);
                backtrack(res, sb, digits, j + 1); //use j here
                sb.setLength(sb.length() - 1);
            }
        }
    }
}
Iteration:

 public class Solution {
        public static String[] dict = new String[] {null, null, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public List<String> letterCombinations(String digits) {
        LinkedList<String> res = new LinkedList<>();
        if (digits == null || digits.length() == 0) return res;

        res.add(""); //why? -> enter the first peek() while loop
        for (int i = 0; i < digits.length();i++){
            int idx = digits.charAt(i) - '0';
            //int idx = Integer.parseInt(digits.substring(i, i + 1));
            while (res.peek().length() == i) {
                String top = res.remove();
                for (char c : dict[idx].toCharArray()) {
                    res.add(top + c);
                }
            }
        }
        return res;
    }
}
'''
