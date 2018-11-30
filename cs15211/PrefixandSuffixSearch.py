import collections

__source__ = 'https://leetcode.com/problems/prefix-and-suffix-search/description/'
# Time: O(NK^2 + QK) where N is the number of words,
# K is the maximum length of a word, and Q is the number of queries.
# Space:  O(NK^2), the size of the trie.
#
# Description: Leetcode # 745. Prefix and Suffix Search
#
# Given many words, words[i] has weight i.
#
# Design a class WordFilter that supports one function,
# WordFilter.f(String prefix, String suffix).
# It will return the word with given prefix and suffix with maximum weight.
# If no word exists, return -1.
#
# Examples:
# Input:
# WordFilter(["apple"])
# WordFilter.f("a", "e") // returns 0
# WordFilter.f("b", "") // returns -1
# Note:
# words has length in range [1, 15000].
# For each test case, up to words.length queries WordFilter.f may be made.
# words[i] has length in range [1, 10].
# prefix, suffix have lengths in range [0, 10].
# words[i] and prefix, suffix queries consist of lowercase letters only.
#
import unittest

# Approach #1: Trie + Set Intersection [Time Limit Exceeded]
Trie = lambda: collections.defaultdict(Trie)
WEIGHT= False

class WordFilterTLE(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie1 = Trie() #prefix
        self.trie2 = Trie() #suffix
        for weight, word in enumerate(words):
            cur = self.trie1
            self.addw(cur, weight)
            for letter in word:
                cur = cur[letter]
                self.addw(cur, weight)

            cur = self.trie2
            self.addw(cur, weight)
            for letter in word[::-1]:
                cur = cur[letter]
                self.addw(cur, weight)

    def addw(self, node, w):
        if WEIGHT not in node:
            node[WEIGHT] = {w}
        else:
            node[WEIGHT].add(w)

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        cur1 = self.trie1
        for letter in prefix:
            if letter not in cur1: return -1
            cur1 = cur1[letter]

        cur2 = self.trie2
        for letter in suffix[::-1]:
            if letter not in cur2: return -1
            cur2 = cur2[letter]

        return max(cur1[WEIGHT] & cur2[WEIGHT])

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

# Complexity Analysis

# Time Complexity: O(NK+Q(N+K)) where N is the number of words,
# K is the maximum length of a word, and Q is the number of queries.
# If we use memoization in our solution, we could produce tighter bounds for this complexity,
# as the complex queries are somewhat disjoint.
#
# Space Complexity: O(NK), the size of the tries.
#

# Approach #2: Paired Trie [Accepted]

# Complexity Analysis
#
# Time Complexity: O(NK^2 + QK) where N is the number of words,
# K is the maximum length of a word, and Q is the number of queries.
# Space Complexity: O(NK^2), the size of the trie.

# Approach #3: Trie of Suffix Wrapped Words [Accepted]
# 92.82% 364ms
class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.weights = {}
        self.pre=collections.defaultdict(set)
        self.suf=collections.defaultdict(set)
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                self.pre[word[:j]].add(word)
                self.suf[word[j:]].add(word)
            self.weights[word] = i


    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        #print(self.pre, self.suf)
        weight = -1
        for word in self.pre[prefix] & self.suf[suffix]:
            if self.weights[word] > weight:
                weight = self.weights[word]
        return weight

# Complexity Analysis
#
# Time Complexity: O(NK^2 + QK) where N is the number of words,
# K is the maximum length of a word, and Q is the number of queries.
#
# Space Complexity: O(NK^2), the size of the trie.
#


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/prefix-and-suffix-search/solution/

Approach #3: Trie of Suffix Wrapped Words [Accepted]

Consider the word 'apple'.
For each suffix of the word, we could insert that suffix,
followed by '#', followed by the word, all into the trie.
For example, we will insert
'#apple', 'e#apple', 'le#apple', 'ple#apple', 'pple#apple', 'apple#apple' into the trie.
Then for a query like prefix = "ap", suffix = "le", we can find it by querying our trie for le#ap.

#295ms 84.50%
class WordFilter {
    TrieNode trie;

    public WordFilter(String[] words) {
        trie = new TrieNode();
        for (int weight = 0; weight < words.length; ++weight) {
            String word = words[weight] + "{";
            for (int i = 0; i < word.length(); ++i) {
                TrieNode cur = trie;
                cur.weight = weight;
                for (int j = i; j < 2 * word.length() - 1; ++j) {
                    int k = word.charAt(j % word.length()) - 'a';
                    if (cur.children[k] == null) cur.children[k] = new TrieNode();
                    cur = cur.children[k];
                    cur.weight = weight;
                }
            }
        }
    }

    public int f(String prefix, String suffix) {
        TrieNode cur= trie;
        for (char letter: (suffix + '{' + prefix).toCharArray()) {
            if (cur.children[letter - 'a'] == null) return -1;
            cur = cur.children[letter - 'a'];
        }
        return cur.weight;
    }

    class TrieNode {
        TrieNode[] children;
        int weight;
        public TrieNode() {
            children = new TrieNode[27];
            weight = 0;
        }
    }
}


# 99.87% 224ms # cheating -> use String.endWith(suffix)
class WordFilter {

    class TrieNode {
        TrieNode[] children;
        List<String> words;
        public TrieNode() {
            children = new TrieNode[26];
            words = new ArrayList();
        }
    }

    private TrieNode root;
    private Map<String, Integer> map;

    private void insert(String word) {
        if (word == null || word.length() == 0) return;
        TrieNode cur = root;
        for (int i = 0; i < word.length(); i++) {
            cur.words.add(word);
            TrieNode next = cur.children[word.charAt(i) - 'a'];
            if (next == null) {
                next = new TrieNode();
                cur.children[word.charAt(i) - 'a'] = next;
            }
            cur = next;
        }
        cur.words.add(word);
    }

    private List<String> find(String prefix) {
        if (prefix == null || prefix.length() == 0) return root.words;
        TrieNode cur = root;
        for (int i = 0; i < prefix.length(); i++) {
            TrieNode next = cur.children[prefix.charAt(i) - 'a'];
            if (next == null) return null;
            cur = next;
        }
        return cur.words;
    }

    public WordFilter(String[] words) {
        if (words == null || words.length == 0) return;
        root = new TrieNode();
        map = new HashMap();
        for (int i = words.length - 1; i >= 0; i--) {
            if (!map.containsKey(words[i])) map.put(words[i], i);
            insert(words[i]);
        }
    }

    public int f(String prefix, String suffix) {
        List<String> words = find(prefix);
        if (words == null) return -1;
        for (String word: words) {
            if (word.endsWith(suffix)) return map.get(word);
        }
        return -1;
    }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter obj = new WordFilter(words);
 * int param_1 = obj.f(prefix,suffix);
 */

'''