__source__ = 'https://leetcode.com/problems/generalized-abbreviation/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/generalized-abbreviation.py
# Time:  O(n * 2^n)
# Space: O(n)
#
# Description: Leetcode # 320. Generalized Abbreviation
# Write a function to generate the generalized abbreviations of a word.
#
# Example:
# Given word = "word", return the following list (order does not matter):
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
#
# Companies
# Google
# Related Topics
# Backtracking Bit Manipulation
# Similar Questions
# Subsets Unique Word Abbreviation Minimum Unique Word Abbreviation
#
import unittest
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def generateAbbreviationsHelper(word, i, cur, res):
            if i == len(word):
                res.append("".join(cur))
                return
            cur.append(word[i])
            generateAbbreviationsHelper(word, i + 1, cur, res)
            cur.pop()
            if not cur or not cur[-1][-1].isdigit():
                for l in xrange(1, len(word) - i + 1):
                    cur.append(str(l))
                    generateAbbreviationsHelper(word, i + l, cur, res)
                    cur.pop()
        res, cur = [], []
        generateAbbreviationsHelper(word, 0, cur, res)
        return res

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/generalized-abbreviation/

# Approach #2 (Bit Manipulation)
# 17.59% 37ms
public class Solution {
    public List<String> generateAbbreviations(String word) {
        List<String> ans = new ArrayList<>();
        for (int x = 0; x < (1 << word.length()); ++x) // loop through all possible x
            ans.add(abbr(word, x));
        return ans;
    }

    // build the abbreviation for word from number x
    private String abbr(String word, int x) {
        StringBuilder builder = new StringBuilder();
        int k = 0, n = word.length(); // k is the count of consecutive ones in x
        for (int i = 0; i < n; ++i, x >>= 1) {
            if ((x & 1) == 0) { // bit is zero, we keep word.charAt(i)
                if (k != 0) { // we have abbreviated k characters
                    builder.append(k);
                    k = 0; // reset the counter k
                }
                builder.append(word.charAt(i));
            }
            else // bit is one, increase k
                ++k;
        }
        if (k != 0) builder.append(k); //don't forget to append the last k if non zero
        return builder.toString();
    }
}

#79.42% 16ms
public class Solution {
    public List<String> generateAbbreviations(String word) {
        List<String> result = new ArrayList<>();
        generateAbbr(word, 0, result, new StringBuilder(), false);
        return result;
    }

    private void generateAbbr(String word, int index, List<String> result, StringBuilder sb, boolean lastAbbr) {
        if (index == word.length()) {
            result.add(sb.toString());
            return;
        }
        int len = sb.length();
        sb.append(word.charAt(index));
        generateAbbr(word, index + 1, result, sb, false);
        sb.setLength(len);
        if (!lastAbbr) {
            for (int i = index; i < word.length(); i++) {
                sb.append(i - index + 1);
                generateAbbr(word, i + 1, result, sb, true);
                sb.setLength(len);
            }
        }
    }
}

#85.30% 15ms
class Solution {
    public List<String> generateAbbreviations(String word) {
        List<String> ans = new ArrayList<String>();
        dfs(ans, new StringBuilder(), word, 0, 0);
        return ans;
    }

     // i is the current position
    // k is the count of consecutive abbreviated characters
    private void dfs(List<String> res, StringBuilder sb, String word, int i, int k){
        int len = sb.length();
        //System.out.println("len :" + len + " " + sb.toString());
        if (i == word.length()) {
            if (k != 0) sb.append(k);
            res.add(sb.toString());
        } else {
            // the branch that word.charAt(i) is abbreviated
            dfs(res, sb, word, i + 1, k + 1);

            // the branch that word.charAt(i) is kept
            if (k != 0) sb.append(k);
            sb.append(word.charAt(i));
            dfs(res, sb, word, i + 1, 0);
        }
        sb.setLength(len);
    }

}

#100% 10ms
class Solution {
    private List<String> res = new LinkedList();
    private char[] pool;
    public List<String> generateAbbreviations(String word) {
        if(word.length() == 0) {
            res.add("");
            return res;
        }
        pool = word.toCharArray();
        helper("", 0, 0);
        return res;
    }

    private void helper(String word, int start, int len){
        if(start == pool.length){
            if(len != 0)
                word += len;
            res.add(word);
            return;
        }
        helper(word, start + 1, len + 1);
        if(len != 0){
            word += len;
        }
        helper(word + pool[start], start + 1, 0);
    }
}
'''