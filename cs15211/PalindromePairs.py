__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/palindrome-pairs.py
# Time:  O(n * k^2), n is the number of the words, k is the max length of the words.
# Space: O(n * k)

# Given a list of unique words. Find all pairs of indices (i, j)
# in the given list, so that the concatenation of the two words,
# i.e. words[i] + words[j] is a palindrome.
#
# Example 1:
# Given words = ["bat", "tab", "cat"]
# Return [[0, 1], [1, 0]]
# The palindromes are ["battab", "tabbat"]
# Example 2:
# Given words = ["abcd", "dcba", "lls", "s", "sssll"]
# Return [[0, 1], [1, 0], [3, 2], [2, 4]]
# The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
#  Google Airbnb
# Hide Tags Hash Table String Trie

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        lookup = {}
        for i, word in enumerate(words):
            lookup[word] = i

        for i in xrange(len(words)):
            for j in xrange(len(words[i]) + 1):
                prefix = words[i][j:]
                suffix = words[i][:j]
                if prefix == prefix[::-1] and \
                   suffix[::-1] in lookup and lookup[suffix[::-1]] != i:
                    res.append([i, lookup[suffix[::-1]]])
                if j > 0 and suffix == suffix[::-1] and \
                   prefix[::-1] in lookup and lookup[prefix[::-1]] != i:
                    res.append([lookup[prefix[::-1]], i])
        return res

# Time:  O(n * k^2), n is the number of the words, k is the max length of the words.
# Space: O(n * k^2)
# Manacher solution.
class Solution_TLE(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def manacher(s, P):
            def preProcess(s):
                if not s:
                    return ['^', '$']
                T = ['^']
                for c in s:
                    T +=  ["#", c]
                T += ['#', '$']
                return T

            T = preProcess(s)
            center, right = 0, 0
            for i in xrange(1, len(T) - 1):
                i_mirror = 2 * center - i
                if right > i:
                    P[i] = min(right - i, P[i_mirror])
                else:
                    P[i] = 0
                while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                    P[i] += 1
                if i + P[i] > right:
                    center, right = i, i + P[i]

        prefix, suffix = collections.defaultdict(list), collections.defaultdict(list)
        for i, word in enumerate(words):
            P = [0] * (2 * len(word) + 3)
            manacher(word, P)
            for j in xrange(len(P)):
                if j - P[j] == 1:
                    prefix[word[(j + P[j]) / 2:]].append(i)
                if j + P[j] == len(P) - 2:
                    suffix[word[:(j - P[j]) / 2]].append(i)
        res = []
        for i, word in enumerate(words):
            for j in prefix[word[::-1]]:
                if j != i:
                    res.append([i, j])
            for j in suffix[word[::-1]]:
                if len(word) != len(words[j]):
                    res.append([j, i])
        return res


# Time:  O(n * k^2), n is the number of the words, k is the max length of the words.
# Space: O(n * k)
# Trie solution.
class TrieNode:
    def __init__(self):
        self.word_idx = -1
        self.leaves = {}

    def insert(self, word, i):
        cur = self
        for c in word:
            if not c in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]
        cur.word_idx = i

    def find(self, s, idx, res):
        cur = self
        for i in reversed(xrange(len(s))):
            if s[i] in cur.leaves:
                cur = cur.leaves[s[i]]
                if cur.word_idx not in (-1, idx) and \
                   self.is_palindrome(s, i - 1):
                    res.append([cur.word_idx, idx])
            else:
                break

    def is_palindrome(self, s, j):
        i = 0
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

class Solution_MLE(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        trie = TrieNode()
        for i in xrange(len(words)):
            trie.insert(words[i], i)

        for i in xrange(len(words)):
            trie.find(words[i], i, res)

        return res

#java
js = '''
public class Solution {
    public List<List<Integer>> palindromePairs(String[] words) {
        List<List<Integer>> result = new ArrayList<>();
        Trie trie = new Trie();
        for (int i = 0; i < words.length; i++) {
            trie.addWord(words[i], i);
        }
        for (int i = 0; i < words.length; i++) {
            for (int other : trie.searchPalindrome(words[i], i)) {
                result.add(Arrays.asList(i, other));
            }
        }
        return result;
    }
}

class TrieNode {
    TrieNode[] children;
    int index;
    List<Integer> palindromePrefix;

    public TrieNode() {
        children = new TrieNode[26];
        index = -1;
        palindromePrefix = new ArrayList<>();
    }
}

class Trie {
    TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    public void addWord(String word, int index) {
        TrieNode cur = root;
        for (int i = word.length() - 1; i >= 0; i--) {
            if (isPalindrome(word, 0, i)) {
                cur.palindromePrefix.add(index);
            }
            int c = word.charAt(i) - 'a';
            if (cur.children[c] == null) {
                cur.children[c] = new TrieNode();
            }
            cur = cur.children[c];
        }
        cur.index = index;
    }

    public List<Integer> searchPalindrome(String word, int index) {
        TrieNode cur = root;
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < word.length(); i++) {
            if (cur.index >= 0 && cur.index != index && isPalindrome(word, i, word.length() - 1)) {
                result.add(cur.index);
            }
            int c = word.charAt(i) - 'a';
            cur = cur.children[c];
            if (cur == null) {
                return result;
            }
        }
        if (cur.index >= 0 && cur.index != index) {
            result.add(cur.index);
        }
        for (int other : cur.palindromePrefix) {
            if (other != index) {
                result.add(other);
            }
        }
        return result;
    }

    private static boolean isPalindrome(String word, int start, int end) {
        while (start < end) {
            if (word.charAt(start++) != word.charAt(end--)) {
                return false;
            }
        }
        return true;
    }
}
'''