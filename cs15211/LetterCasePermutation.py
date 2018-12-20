__source__ = 'https://leetcode.com/problems/letter-case-permutation/'
# Time:  O(2^{N} * N)
# Space: O(2^{N} * N)
#
# Description: Leetcode # 784. Letter Case Permutation
#
# Given a string S, we can transform every letter individually to be lowercase or uppercase
# to create another string.  Return a list of all possible strings we could create.
#
# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
#
# Input: S = "3z4"
# Output: ["3z4", "3Z4"]
#
# Input: S = "12345"
# Output: ["12345"]
# Note:
#
# S will be a string with length between 1 and 12.
# S will consist only of letters or digits.

import unittest
import itertools
# Time and Space Complexity: O(2^{N} * N)
# 104ms 22.31%
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        f = lambda x: (x.lower(), x.upper()) if x.isalpha() else x
        return map("".join, itertools.product(*map(f, S)))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/letter-case-permutation/solution/

# 5ms 96,17%
class Solution {
    public List<String> letterCasePermutation(String S) {
        List<String> res = new ArrayList<>();
        char[] chr = S.toCharArray();
        Visit(res, chr, 0);
        return res;
    }

    private void Visit(List<String> res, char[] chr, int start) {
        res.add(new String(chr));

        for (int i = start; i < chr.length; i++) {
            char c = chr[i];
            if (c <= 'z' && c >= 'a') {
                chr[i] = (char)(c - 'a' + 'A');
                Visit(res, chr, i + 1);
                chr[i] = c;
            }else if (c >= 'A' && c <= 'Z') {
                chr[i] = (char)(c - 'A' + 'a');
                Visit(res, chr, i + 1);
                chr[i] = c;
            }
        }
    }
}

Approach #1: Recursion [Accepted] 
# 8ms 64.84%
class Solution {
    public List<String> letterCasePermutation(String S) {
        List<StringBuilder> res = new ArrayList<>();
        res.add(new StringBuilder());

        for (char c: S.toCharArray()) {
            int n = res.size();
            if (Character.isLetter(c)) {
                for (int i = 0; i < n; i++) {
                    res.add(new StringBuilder(res.get(i)));
                    res.get(i).append(Character.toLowerCase(c));
                    res.get(n + i).append(Character.toUpperCase(c));
                }
            } else {
                for (int i = 0; i < n; i++) {
                    res.get(i).append(c);
                }
            }
        }

        List<String> ans = new ArrayList<>();
        for (StringBuilder sb : res) {
            ans.add(sb.toString());
        }
        return ans;
    }
}

Approach #2: Binary Mask [Accepted] 
# 21ms 12.14%
class Solution {
    public List<String> letterCasePermutation(String S) {
        int B = 0;
        for (char c: S.toCharArray()) {
            if (Character.isLetter(c)) B++;
        }

        List<String> res = new ArrayList<>();
        for (int bits = 0; bits < 1<<B; bits++) {
            int b = 0;
            StringBuilder sb = new StringBuilder();
            for (char c : S.toCharArray()) {
                if (Character.isLetter(c)) {
                    if (((bits >> b++) & 1 ) == 1) {
                        sb.append(Character.toLowerCase(c));
                    } else {
                        sb.append(Character.toUpperCase(c));
                    }
                } else {
                    sb.append(c);
                }
            }
            res.add(sb.toString());
        }
        return res;
    }
}
'''
