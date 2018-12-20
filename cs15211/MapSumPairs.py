__source__ = 'https://leetcode.com/problems/map-sum-pairs/'
# Time:  O(K)
# Space: O(K)
#
# Description: Leetcode # 677. Map Sum Pairs
#
# Implement a MapSum class with insert, and sum methods.
#
# For the method insert, you'll be given a pair of (string, integer).
# The string represents the key and the integer represents the value.
# If the key already existed, then the original key-value pair will be overridden to the new one.
#
# For the method sum, you'll be given a string representing the prefix,
# and you need to return the sum of all the pairs' value whose key starts with the prefix.
#
# Example 1:
# Input: insert("apple", 3), Output: Null
# Input: sum("ap"), Output: 3
# Input: insert("app", 2), Output: Null
# Input: sum("ap"), Output: 5
#
# Companies
# Akuna Capital
# Related Topics
# Trie
#
import unittest
# 20ms 100%
class TrieNode():
    def __init__(self, count = 0):
        self.count = count
        self.children = {}

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.keys = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        # Time: O(k)
        curr = self.root
        delta = val - self.keys.get(key, 0)
        self.keys[key] = val

        curr = self.root
        curr.count += delta
        for char in key:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.count += delta

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        # Time: O(k)
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.count

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/map-sum-pairs/solution/

# Trie + hashmap
# 80ms 40.45%
class MapSum {
    class TrieNode {
        Map<Character, TrieNode> children;
        boolean isWord;
        int value;

        public TrieNode() {
            children = new HashMap<Character, TrieNode>();
            isWord = false;
            value = 0;
        }
    }

    TrieNode root;

    /** Initialize your data structure here. */
    public MapSum() {
        root = new TrieNode();
    }

    public void insert(String key, int val) {
        TrieNode curr = root;
        for (char c : key.toCharArray()) {
            TrieNode next = curr.children.get(c);
            if (next == null) {
                next = new TrieNode();
                curr.children.put(c, next);
            }
            curr = next;
        }
        curr.isWord = true;
        curr.value = val;
    }

    public int sum(String prefix) {
        TrieNode curr = root;
	    for (char c : prefix.toCharArray()) {
            TrieNode next = curr.children.get(c);
            if (next == null) {
                return 0;
            }
            curr = next;
        }

        return dfs(curr);
    }

    private int dfs(TrieNode root) {
        int sum = 0;
        for (char c : root.children.keySet()) {
            sum += dfs(root.children.get(c));
        }
        return sum + root.value;
    }
}
'''
