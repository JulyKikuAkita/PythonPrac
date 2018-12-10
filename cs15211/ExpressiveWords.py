__source__ = 'https://leetcode.com/problems/expressive-words/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 809. Expressive Words
#
# Sometimes people repeat letters to represent extra feeling,
# such as "hello" -> "heeellooo", "hi" -> "hiiii".
# Here, we have groups,
# of adjacent letters that are all the same character, and adjacent characters to the group are different.
# A group is extended if that group is length 3 or more, so "e" and "o" would be extended in the first example,
# and "i" would be extended in the second example.  As another example,
# the groups of "abbcccaaaa" would be "a", "bb", "ccc", and "aaaa";
# and "ccc" and "aaaa" are the extended groups of that string.
#
# For some given string S, a query word is stretchy if it can be made to be equal to S by extending some groups.
# Formally, we are allowed to repeatedly choose a group (as defined above) of characters c,
# and add some number of the same character c to it so that the length of the group is 3 or more.
# Note that we cannot extend a group of size one like "h" to a group of size two like "hh" -
# all extensions must leave the group extended - ie., at least 3 characters long.
#
# Given a list of query words, return the number of words that are stretchy.
#
# Example:
# Input:
# S = "heeellooo"
# words = ["hello", "hi", "helo"]
# Output: 1
# Explanation:
# We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not extended.
#
# Notes:
#
#     0 <= len(S) <= 100.
#     0 <= len(words) <= 100.
#     0 <= len(words[i]) <= 100.
#     S and all words in words consist only of lowercase letters
#
import unittest
import itertools
# 60ms 17.43%
class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        def RLE(S):
            return zip(*[(k, len(list(grp)))
                         for k, grp in itertools.groupby(S)])

        R, count = RLE(S)
        ans = 0
        for word in words:
            R2, count2 = RLE(word)
            if R2 != R: continue
            ans += all(c1 >= max(c2, 3) or c1 == c2
                       for c1, c2 in zip(count, count2))

        return ans
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/expressive-words/solution/

Approach #1: Run Length Encoding [Accepted]
Complexity Analysis
Time Complexity: O(QK), where Q is the length of words (at least 1), and K is the maximum length of a word.
Space Complexity: O(K)

# 10ms 22.82%
class Solution {
    public int expressiveWords(String S, String[] words) {
        RLE R = new RLE(S);
        int ans = 0;

        search: for (String word: words) {
            RLE R2 = new RLE(word);
            if (!R.key.equals(R2.key)) continue;
            for (int i = 0; i < R.counts.size(); ++i) {
                int c1 = R.counts.get(i);
                int c2 = R2.counts.get(i);
                if (c1 < 3 && c1 != c2 || c1 < c2)
                    continue search;
            }
            ans++;
        }
        return ans;
    }
}

class RLE {
    String key;
    List<Integer> counts;

    public RLE(String S) {
        StringBuilder sb = new StringBuilder();
        counts = new ArrayList();

        char[] ca = S.toCharArray();
        int N = ca.length;
        int prev = -1;
        for (int i = 0; i < N; ++i) {
            if (i == N-1 || ca[i] != ca[i+1]) {
                sb.append(ca[i]);
                counts.add(i - prev);
                prev = i;
            }
        }

        key = sb.toString();
    }
}

# 3ms 95.16%
class Solution {
    public int expressiveWords(String S, String[] words) {
        int count = 0;
        for (String w : words) {
            if (helper(S, w)) count++;
        }

        return count;
    }

    private boolean helper(String s, String w) {
        int i = 0, j = 0;
        int m = s.length(), n = w.length();

        while (i < m && j < n) {
            char c1 = s.charAt(i);
            char c2 = w.charAt(j);

            if (c1 != c2) return false;
            int count1 = getCount(s, i);
            int count2 = getCount(w, j);

            if ((count1 == 2 && count2 == 1)
                || (count1 < count2)) return false;
            i += count1;
            j += count2;
        }


        return i == m && j == n;
    }

    private int getCount(String s, int i) {
        int count = 1;
        i++;
        while (i < s.length()) {
            if (s.charAt(i) == s.charAt(i - 1)) count++;
            else break;
            i++;
        }

        return count;
    }
}
'''