# coding=utf-8
__source__ = 'https://leetcode.com/problems/short-encoding-of-words/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 820. Short Encoding of Words
#
# Given a list of words, we may encode it by writing a reference string S and a list of indexes A.
#
# For example, if the list of words is ["time", "me", "bell"],
# we can write it as S = "time#bell#" and indexes = [0, 2, 5].
#
# Then for each index,
# we will recover the word by reading from the reference string from that index until we reach a "#" character.
#
# What is the length of the shortest reference string S possible that encodes the given words?
#
# Example:
#
# Input: words = ["time", "me", "bell"]
# Output: 10
# Explanation: S = "time#bell#" and indexes = [0, 2, 5].
#
# Note:
#
#     1 <= words.length <= 2000.
#     1 <= words[i].length <= 7.
#     Each word has only lowercase letters.
#
import unittest
import collections
# 96ms 50.67%
class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])
        return sum(len(word) + 1 for word in good)

# Trie
# 256ms 17.33%
class SolutionTrie(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = list(set(words)) #remove duplicates
        #Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        #reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]

        #Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/short-encoding-of-words/solution/
#
Approach #1: Store Prefixes [Accepted]
Complexity Analysis
Time Complexity: O(∑wi^2), where wi is the length of words[i].
Space Complexity: O(∑wi), the space used in storing suffixes.
The final answer would be sum(word.length + 1 for word in words)

# 36ms 44.25%
class Solution {
    public int minimumLengthEncoding(String[] words) {
        Set<String> good = new HashSet(Arrays.asList(words));
        for (String word : words) {
            for (int k = 1; k < word.length(); k++) {
                good.remove(word.substring(k));
            }
        }
        int ans = 0;
        for (String word: good) ans += word.length() + 1;
        return ans;
    }
}

Approach #2: Trie [Accepted]
Complexity Analysis
Time Complexity: O(∑wi​), where wi​ is the length of words[i].
Space Complexity: O(∑wi​), the space used by the trie.
# 44ms 32.74%
class Solution {
    public int minimumLengthEncoding(String[] words) {
        TrieNode trie = new TrieNode();
        Map<TrieNode, Integer> nodes = new HashMap();
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            TrieNode cur = trie;
            for (int j = word.length() - 1; j >= 0; j--) {
                cur = cur.get(word.charAt(j));
            }
            nodes.put(cur, i);
        }
        int ans = 0;
        for (TrieNode node: nodes.keySet()) {
            if (node.count == 0) ans += words[nodes.get(node)].length() + 1;
        }
        return ans;
    }
    
    class TrieNode {
        TrieNode[] children;
        int count;
        TrieNode() {
            children = new TrieNode[26];
            count = 0;
        }
        
        public TrieNode get(char c) {
            if (children[c - 'a'] == null) {
                children[c - 'a'] = new TrieNode();
                count++;
            }
            return children[c - 'a'];
        }
    }
}

# Trie
# 16ms 95.13%
class Solution {
    public int minimumLengthEncoding(String[] words) {
        int res = 0;
        TrieNode root = new TrieNode();
        for (String word : words) {
            res += insert(root, word);
        }
        return res;
    }
    
    private int insert(TrieNode root, String word) {
        int num = 0, depth = 1;
        for (int i = word.length() - 1; i >= 0; i--) {
            int j = word.charAt(i) - 'a';
            if (root.next[j] == null) root.next[j] = new TrieNode();
            if (root.next[j].end) {
                root.next[j].end = false;
                num -= depth + 1;
            }
            root.hasNext = true;
            root = root.next[j];
            depth = depth + 1;
        }
        if (root.hasNext) return 0;
        else {
            root.end = true;
            return num + word.length() + 1;
        }
    }
    
    private static class TrieNode {
        TrieNode[] next = new TrieNode[26];
        boolean end = false;
        boolean hasNext = false;
    }
}

'''
