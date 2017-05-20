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
# Uber Facebook
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
public class Solution {
    public static String[] dict = new String[] {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits == null || digits.length() == 0) {
            return result;
        }
        letterCombinations(digits, 0, new char[digits.length()], result);
        return result;
    }

    private void letterCombinations(String digits, int index, char[] curr, List<String> result) {
        if (index == digits.length()) {
            result.add(new String(curr));
            return;
        }
        String chars = dict[digits.charAt(index) - '2'];
        for (int i = 0; i < chars.length(); i++) {
            curr[index] = chars.charAt(i);
            letterCombinations(digits, index + 1, curr, result);
        }
    }
}
'''
