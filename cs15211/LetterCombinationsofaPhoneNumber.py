__source__ = 'https://leetcode.com/problems/letter-combinations-of-a-phone-number/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/letter-combinations-of-a-phone-number.py
# Time:  O(n * 4^n)
# Space: O(n)
# Brute Force Search
#
# Description: Leetcode # 17. Letter Combinations of a Phone Number
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
# Companies
# Amazon Dropbox Google Uber Facebook
# Related Topics
# Backtracking String
# Similar Questions
# Generate Parentheses Combination Sum Binary Watch
#
import unittest
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

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        #print test.letterCombinations("23")

        # ord('3')- ord('0')  # an easy way to stoi
        # any iterable will do for extend (not just list)
        # extend outperforms append, as the loop is implemented in C.
        # [].extend("string") will give you ["s", "t", "r", "i", "n", "g"]
        # [].append("string") will give you ["string"]
        # [].extend("") = []

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
Recursion:
#79.78% 3ms
public class Solution {
    public static String[] dict = new String[] {null, null, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public List<String> letterCombinations(String digits) {
        LinkedList<String> res = new LinkedList<>();
        if (digits == null || digits.length() == 0) return res;
        dfs(digits, 0, new StringBuilder(), res);
        return res;
    }

    private void dfs(String digits, int idx, StringBuilder sb, List<String> res) {
        if (sb.length() == digits.length()) {
            res.add(sb.toString());
            return;
        }
        String cur = dict[digits.charAt(idx) - '0'];
        for (char c : cur.toCharArray()) {
            sb.append(c);
            dfs(digits, idx + 1, sb, res);
            sb.setLength(sb.length() - 1);
        }
    }
}

Iteration:
# 16.28% 5ms
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

# recursion
#81.78% 3ms

public class Solution {
    public List<String> letterCombinations(String digits) {
        if(digits.length() == 0){return new ArrayList<String>();}
        String[] letters = new String[digits.length()];

        for(int i = 0; i < letters.length; i++){
            if(digits.charAt(i) == '2'){
                letters[i] = "abc";
            }
            else if(digits.charAt(i) == '3'){
                letters[i] = "def";
            }
            else if(digits.charAt(i) == '4'){
                letters[i] = "ghi";
            }
            else if(digits.charAt(i) == '5'){
                letters[i] = "jkl";
            }
            else if(digits.charAt(i) == '6'){
                letters[i] = "mno";
            }
            else if(digits.charAt(i) == '7'){
                letters[i] = "pqrs";
            }
            else if(digits.charAt(i) == '8'){
                letters[i] = "tuv";
            }
            else if(digits.charAt(i) == '9'){
                letters[i] = "wxyz";
            }
        }

        List<String> result = new ArrayList<String>();
        helper(letters, result, new char[digits.length()], 0);

        return result;
    }

    private void helper(String[] letters, List<String> result, char[] current, int index){
        if(index == letters.length){
            result.add(new String(current));
            return;
        }

        String s = letters[index];

        for(int j = 0; j < s.length(); j++){
            current[index] = s.charAt(j);
            helper(letters, result, current, index+1);
        }
    }
}
'''
