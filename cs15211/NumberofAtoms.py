import collections

__source__ = 'https://leetcode.com/problems/number-of-atoms/'
# Time:  O(N^2)
# Space: O(N)
#
# Description: Leetcode # 726. Number of Atoms
#
# Given a chemical formula (given as a string), return the count of each atom.
#
# An atomic element always starts with an uppercase character, then zero or more lowercase letters,
# representing the name.
#
# 1 or more digits representing the count of that element may follow if the count is greater than 1.
# If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.
#
# Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.
#
# A formula placed in parentheses, and a count (optionally added) is also a formula.
# For example, (H2O2) and (H2O2)3 are formulas.
#
# Given a formula, output the count of all elements as a string in the following form:
# the first name (in sorted order), followed by its count (if that count is more than 1),
# followed by the second name (in sorted order),
# followed by its count (if that count is more than 1), and so on.
#
# Example 1:
# Input:
# formula = "H2O"
# Output: "H2O"
# Explanation:
# The count of elements are {'H': 2, 'O': 1}.
# Example 2:
# Input:
# formula = "Mg(OH)2"
# Output: "H2MgO2"
# Explanation:
# The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
# Example 3:
# Input:
# formula = "K4(ON(SO3)2)2"
# Output: "K4N2O14S4"
# Explanation:
# The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
# Note:
#
# All atom names consist of lowercase letters,
# except for the first character which is uppercase.
# The length of formula will be in the range [1, 1000].
# formula will only consist of letters, digits, and round parentheses,
# and is a valid formula as defined in the problem.
#
import unittest

#24ms 78.3%
class Solution:
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        res = collections.defaultdict(int)
        stack = []
        i = 0
        n = len(formula)
        while i < n:
            c = formula[i]
            if c == '(':
                stack.append(c)
                i += 1
            elif c == ')':
                j = i + 1
                cnt = 0
                if j == n or not formula[j].isdigit():
                    cnt = 1
                else:
                    while j < n and formula[j].isdigit():
                        cnt = cnt * 10 + int(formula[j])
                        j += 1
                i = j
                temp = []
                while stack[-1] != '(':
                    s, num = stack.pop()
                    temp.append([s, num * cnt])
                stack.pop()
                if len(stack) == 0:
                    while temp:
                        s, num = temp.pop()
                        res[s] += num

                else:
                    stack += temp[::-1]
            else:
                s = c
                j = i + 1
                while j < n and formula[j] >= 'a' and formula[j] <= 'z':
                    s += formula[j]
                    j += 1
                cnt = 0
                while j < n and formula[j].isdigit():
                    cnt = cnt * 10 + int(formula[j])
                    j += 1
                if cnt == 0:
                    cnt = 1
                i = j
                if len(stack) == 0:
                    res[s] += cnt
                else:
                    stack.append([s, cnt])
        rep = ''
        for k in sorted(res.keys()):
            if res[k] > 1:
                rep += k + str(res[k])
            else:
                rep += k
        return rep

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/number-of-atoms/solution/
# Approach #1: Recursion [Accepted]
# Complexity Analysis
# Time Complexity: O(N^2), where N is the length of the formula.
# It is O(N) to parse through the formula,
# but each of O(N) multiplicities after a bracket may increment the count of each name in the formula
# (inside those brackets), leading to an O(N^2) complexity.
# Space Complexity: O(N). We aren't recording more intermediate information than what is contained in the formula.
#
#7ms, 70.79%

class Solution {
    private int i;

    public String countOfAtoms(String formula) {
        StringBuilder sb = new StringBuilder();
        i = 0;
        Map<String, Integer> count = parse(formula);
        for (String name: count.keySet()) {
            sb.append(name);
            int multiplicity = count.get(name);
            if (multiplicity > 1) sb.append("" + multiplicity);
        }
        return sb.toString();
    }

    public Map<String, Integer> parse(String formula) {
        int N = formula.length();
        Map<String, Integer> count = new TreeMap();
        while (i < N && formula.charAt(i) != ')') {
            if (formula.charAt(i) == '(') {
                i++;
                for(Map.Entry<String, Integer> entry: parse(formula).entrySet()) {
                    count.put(entry.getKey(), count.getOrDefault(entry.getKey(), 0) + entry.getValue());
                }
            } else {
                int iStart = i++;
                while (i < N && Character.isLowerCase(formula.charAt(i))) i++;
                String name = formula.substring(iStart, i);
                iStart = i;
                while (i < N && Character.isDigit(formula.charAt(i))) i++;
                int multiplicity = iStart < i ? Integer.parseInt(formula.substring(iStart, i)) : 1;
                count.put(name, count.getOrDefault(name, 0) + multiplicity);
            }
        }
        int iStart = ++i;
        while( i < N && Character.isDigit(formula.charAt(i))) i++;
        if (iStart < i) {
            int multiplicity = Integer.parseInt(formula.substring(iStart, i));
            for (String key : count.keySet()) {
                count.put(key, count.get(key) * multiplicity);
            }
        }
        return count;
    }
}


# Approach #2: Stack [Accepted]
# Time Complexity O(N^2), and Space Complexity O(N)O(N)

# 7ms 69.75%
class Solution {
    public String countOfAtoms(String formula) {
        int N = formula.length();
        Stack<Map<String, Integer>> stack = new Stack();
        stack.push(new TreeMap());

        for(int i = 0; i < N;) {
            if (formula.charAt(i) == '(') {
                stack.push(new TreeMap());
                i++;
            } else if (formula.charAt(i) == ')') {
                Map<String, Integer> top = stack.pop();
                int iStart = ++i, multiplicity = 1;
                while (i < N && Character.isDigit(formula.charAt(i))) i++;
                if (i > iStart) multiplicity = Integer.parseInt(formula.substring(iStart, i));
                for(String c : top.keySet()) {
                    int v = top.get(c);
                    stack.peek().put(c, stack.peek().getOrDefault(c, 0) + v * multiplicity);
                }
            } else {
                int iStart = i++;
                while (i < N && Character.isLowerCase(formula.charAt(i))) i++;
                String name = formula.substring(iStart, i);
                iStart = i;
                while (i < N && Character.isDigit(formula.charAt(i))) i++;
                int multiplicity = i > iStart ? Integer.parseInt(formula.substring(iStart, i)) : 1;
                stack.peek().put(name, stack.peek().getOrDefault(name, 0) + multiplicity);
            }
        }

        StringBuilder sb = new StringBuilder();
        for (String name :stack.peek().keySet()) {
            sb.append(name);
            int cnt = stack.peek().get(name);
            if (cnt > 1) sb.append("" + cnt);
        }
        return sb.toString();
    }
}

# Approach #3: Regular Expressions [Accepted]
# Complexity Analysis
# Time Complexity O(N^2), and Space Complexity O(N).
# The analysis is the same as Approach #1, as this regular expression did not look backwards when parsing.
#


# 2ms 100%
class Solution {
    public String countOfAtoms(String formula) {
        int size = 26 * 27;
        int[] counter = new int[size];
        Stack<Integer> multipliers = new Stack<>();

        int curMultiplier = 1;
        int val = 0;
        int x10 = 1;
        int endAtom = -1;
        int charPos = 0;

        for(int i = formula.length() - 1; i >= 0; i--) {
            char ch = formula.charAt(i);

            if (ch == ')') {
                if (val == 0) {
                    val = 1;
                }
                multipliers.push(val);
                curMultiplier *= val;

                val = 0;
                x10 = 1;

            } else if (ch == '(') {
                curMultiplier /= multipliers.pop();

            } else if (ch <= '9' && ch >= '0') {
                val += x10 * (ch - '0');
                x10 *= 10;

            } else if (ch >= 'a' && ch <= 'z') {
                charPos = ch - 'a' + 1;

            } else {
                charPos += (ch - 'A') * 27;

                if (val == 0) {
                    val = 1;
                }
                counter[charPos] = counter[charPos] + val * curMultiplier;

                val = 0;
                x10 = 1;
                charPos = 0;
            }
        }

        // Convert from HashMap back to String
        StringBuilder res = new StringBuilder();
        for(int i = 0; i< size; i++) {
            if (counter[i] > 0) {
                char ch = (char) ('A' + i/27);
                res.append(ch);
                if (i % 27 > 0) {
                    ch = (char) ('a' + (i % 27) - 1);
                    res.append(ch);
                }

                if (counter[i] > 1) {
                    res.append(counter[i]);
                }
            }
        }

        return res.toString();
    }
}
'''