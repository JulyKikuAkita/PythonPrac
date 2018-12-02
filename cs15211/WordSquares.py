__source__ = 'https://github.com/kamyu104/LeetCode/blob/master/Python/word-squares.py'
# https://leetcode.com/problems/word-squares/#/description
# Time:  O(n^2 * n!)
# Space: O(n^2)
#
# Description: 425. Word Squares
#
# Given a set of words (without duplicates), find all word squares you can build from them.
#
# A sequence of words forms a valid word square if the kth row and column read the exact same string,
# where 0 <= k < max(numRows, numColumns).
#
# For example, the word sequence ["ball","area","lead","lady"] forms a word square
# because each word reads the same both horizontally and vertically.
#
# b a l l
# a r e a
# l e a d
# l a d y
# Note:
# There are at least 1 and at most 1000 words.
# All words will have the exact same length.
# Word length is at least 1 and at most 5.
# Each word contains only lowercase English alphabet a-z.
# Example 1:
#
# Input:
# ["area","lead","wall","lady","ball"]
#
# Output:
# [
#   [ "wall",
#     "area",
#     "lead",
#     "lady"
#   ],
#   [ "ball",
#     "area",
#     "lead",
#     "lady"
#   ]
# ]
#
# Explanation:
# The output consists of two word squares. The order of output does not matter
# (just the order of words in each word square matters).
# Example 2:
#
# Input:
# ["abat","baba","atan","atal"]
#
# Output:
# [
#   [ "baba",
#     "abat",
#     "baba",
#     "atan"
#   ],
#   [ "baba",
#     "abat",
#     "baba",
#     "atal"
#   ]
# ]
#
# Explanation:
# The output consists of two word squares. The order of output does not matter
# (just the order of words in each word square matters).
#
# Hide Company Tags Google
# Hide Tags Backtracking Trie
# Hide Similar Problems (E) Valid Word Square


# I try every word for the first row. For each of them, try every fitting word for the second row.
# And so on. The first few rows determine the first few columns and thus determine how the next row's word must start.
# For example:
#
# wall      Try words      wall                     wall                      wall
# a...   => starting  =>   area      Try words      area                      area
# l...      with "a"       le..   => starting  =>   lead      Try words       lead
# l...                     la..      with "le"      lad.   => starting   =>   lady
#                                                             with "lad"
#
import unittest
# 659ms 32.52%
class TrieNode(object):
    def __init__(self):
        self.indices = []
        self.children = [None] * 26

    def insert(self, words, i):
        cur = self
        for c in words[i]:
            if not cur.children[ord(c)-ord('a')]:
                cur.children[ord(c)-ord('a')] = TrieNode()
            cur = cur.children[ord(c)-ord('a')]
            cur.indices.append(i)


class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        result = []

        trie = TrieNode()
        for i in xrange(len(words)):
            trie.insert(words, i)

        curr = []
        for s in words:
            curr.append(s)
            self.wordSquaresHelper(words, trie, curr, result)
            curr.pop()

        return result

    def wordSquaresHelper(self, words, trie, curr, result):
        if len(curr) >= len(words[0]):
            return result.append(list(curr))

        node = trie
        for s in curr:
            node = node.children[ord(s[len(curr)]) - ord('a')]
            if not node:
                return

        for i in node.indices:
            curr.append(words[i])
            self.wordSquaresHelper(words, trie, curr, result)
            curr.pop()

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
#
Java DFS+Trie 54 ms, 98% so far
By considering the word squares as a symmetric matrix, my idea is to go through the top right triangular matrix
in left-to-right and then down order.
For example, with the case of ["area","lead","wall","lady","ball"] where length = 4,
we start with 4 empty string
""
""
""
""
Next, [0,0] , "a","b", "l", "w" can be placed, we start with "a"
"a"
""
""
""
[0,1] go right, "r" can be placed after "a", but no words start with "r" at [1,0], so this DFS ends.
"ar"
""
""
""
Now, start with "b" at [0,0]
"b"
""
""
""
We can have "ba" at [0,1] and there is a word start with "a"
"ba"
"a"
""
""
Next
"bal"
"a"
"l"
""
Next
"ball"
"a"
"l"
"l"
When finish the first row, go down to next row and start at [1,1]
"ball"
"ar"
"l"
"l"
..... so on and so forth until reaching [4,4]

# https://discuss.leetcode.com/topic/63516/explained-my-java-solution-using-trie-126ms-16-16/5
A better approach is to check the validity of the word square while we build it.
Example: ["area","lead","wall","lady","ball"]
We know that the sequence contains 4 words because the length of each word is 4.
Every word can be the first word of the sequence, let's take "wall" for example.
Which word could be the second word? Must be a word start with "a" (therefore "area"),
because it has to match the second letter of word "wall".
Which word could be the third word? Must be a word start with "le" (therefore "lead"),
because it has to match the third letter of word "wall" and the third letter of word "area".
What about the last word? Must be a word start with "lad" (therefore "lady"). For the same reason above.


In order for this to work, we need to fast retrieve all the words with a given prefix. There could be 2 ways doing this:

Using a hashtable, key is prefix, value is a list of words with that prefix.
Trie, we store a list of words with the prefix on each trie node.
1. With Trie:
#101ms 45.18%
class Solution {
    class TrieNode {
        List<String> startWith;
        TrieNode[] children;

        TrieNode() {
            startWith = new ArrayList<>();
            children = new TrieNode[26];
        }
    }

    class Trie {
        TrieNode root;

        Trie(String[] words) {
            root = new TrieNode();
            for (String w : words) {
                TrieNode cur = root;
                for (char ch : w.toCharArray()) {
                    int idx = ch - 'a';
                    if (cur.children[idx] == null)
                        cur.children[idx] = new TrieNode();
                    cur.children[idx].startWith.add(w);
                    cur = cur.children[idx];
                }
            }
        }

        List<String> findByPrefix(String prefix) {
            List<String> ans = new ArrayList<>();
            TrieNode cur = root;
            for (char ch : prefix.toCharArray()) {
                int idx = ch - 'a';
                if (cur.children[idx] == null)
                    return ans;

                cur = cur.children[idx];
            }
            ans.addAll(cur.startWith);
            return ans;
        }
    }

    public List<List<String>> wordSquares(String[] words) {
        List<List<String>> ans = new ArrayList<>();
        if (words == null || words.length == 0)
            return ans;
        int len = words[0].length();
        Trie trie = new Trie(words);
        List<String> ansBuilder = new ArrayList<>();
        for (String w : words) {
            ansBuilder.add(w);
            search(len, trie, ans, ansBuilder);
            ansBuilder.remove(ansBuilder.size() - 1);
        }

        return ans;
    }

    private void search(int len, Trie tr, List<List<String>> ans,
            List<String> ansBuilder) {
        if (ansBuilder.size() == len) {
            ans.add(new ArrayList<>(ansBuilder));
            return;
        }

        int idx = ansBuilder.size();
        StringBuilder prefixBuilder = new StringBuilder();
        for (String s : ansBuilder)
            prefixBuilder.append(s.charAt(idx));
        List<String> startWith = tr.findByPrefix(prefixBuilder.toString());
        for (String sw : startWith) {
            ansBuilder.add(sw);
            search(len, tr, ans, ansBuilder);
            ansBuilder.remove(ansBuilder.size() - 1);
        }
    }
}


#Improved Trie
#25ms 92.50%
class Solution {
    public List<List<String>> wordSquares(String[] words) {
        List<List<String>> res = new ArrayList<>();
        if (words==null || words.length==0) return res;
        Trie root = new Trie();
        int len = words[0].length();
        for (String word: words) {
            root.add(root, word);
        }
        Trie[] rows = new Trie[len];
        for (int i = 0; i < len; i++) {
            rows[i] = root;
        }
        helper(0, 0, len, rows, res);
        return res;
    }

    public void helper(int row, int col, int len, Trie[] rows, List<List<String>> res) {
            if ( (col == row) && (row == len) ) { //last char
                List<String> tmp = new ArrayList<>();
                for (int i = 0; i < len; i++) {
                    tmp.add(new String(rows[i].word));
                }
                res.add(tmp);
            } else {  // from left to right and then go down to the next row
                if (col < len) { // left to right first
                    Trie pre_row = rows[row];
                    Trie pre_col = rows[col];
                    for (int i = 0; i<26; i++) { // find all the possible next char
                        if ((rows[row].tries[i] != null) && (rows[col].tries[i] != null)) {
                            rows[row] = rows[row].tries[i];
                            if (col != row) rows[col] = rows[col].tries[i];
                            helper(row, col + 1, len, rows, res);
                            rows[row] = pre_row;
                            if (col != row) rows[col] = pre_col;
                        }
                    }
                } else { // reach the end of column, go to the next row
                    helper(row + 1, row + 1, len, rows, res);
                }
        }
    }

    class Trie{
        Trie[] tries;
        String word;
        Trie() {
            this.tries = new Trie[26];
            this.word = null;
        }

        public void add(Trie root, String word) {
            Trie trie = root;
            for (char c : word.toCharArray()) {
                int idx = c - 'a';
                if (trie.tries[idx] == null) {
                    trie.tries[idx] = new Trie();
                }
                trie = trie.tries[idx];
            }
            trie.word = word;
        }
    }
}

2. Hashtable to store index
The idea is borrowed from the discussion
(https://discuss.leetcode.com/topic/63516/explained-my-java-solution-using-trie-126ms-16-16) ,
which is to first calculating all possible prefix, then do backtracking.

We can use Trie or hashMap to store the prefix information, while I think Trie might be more hard to implement,
without saving any space. So I use hashMap to store prefix information.

#69ms 76.79%
class Solution {
    public List<List<String>> wordSquares(String[] words) {
        List<List<String>> ret = new ArrayList<List<String>>();
        if(words.length==0 || words[0].length()==0) return ret;
        Map<String, Set<String>> map = new HashMap<>();
        int squareLen = words[0].length();
        // create all prefix
        for(int i=0;i<words.length;i++){
            for(int j=-1;j<words[0].length();j++){
                if(!map.containsKey(words[i].substring(0, j+1))) map.put(words[i].substring(0, j+1), new HashSet<String>());
                map.get(words[i].substring(0, j+1)).add(words[i]);
            }
        }
        helper(ret, new ArrayList<String>(), 0, squareLen, map);
        return ret;
    }
    public void helper(List<List<String>> ret, List<String> cur, int matched, int total, Map<String, Set<String>> map){
        if(matched == total) {ret.add(new ArrayList<String>(cur));return;}
        // build search string
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<=matched-1;i++) sb.append(cur.get(i).charAt(matched));
        // bachtracking
        Set<String> cand = map.get(sb.toString());
        if(cand==null) return;
        for(String str:cand){
            cur.add(str);
            helper(ret, cur, matched+1, total, map);
            cur.remove(cur.size()-1);
        }
    }
}
'''