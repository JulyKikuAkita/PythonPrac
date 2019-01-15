__source__ = 'https://leetcode.com/problems/implement-magic-dictionary/'
# Time:  O(N*K)
# Space: O(S)
#
# Description: Leetcode # 676. Implement Magic Dictionary
#
# Implement a magic directory with buildDict, and search methods.
#
# For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.
#
# For the method search, you'll be given a word,
# and judge whether if you modify exactly one character into another character in this word,
# the modified word is in the dictionary you just built.
#
# Example 1:
# Input: buildDict(["hello", "leetcode"]), Output: Null
# Input: search("hello"), Output: False
# Input: search("hhllo"), Output: True
# Input: search("hell"), Output: False
# Input: search("leetcoded"), Output: False
# Note:
# You may assume that all the inputs are consist of lowercase letters a-z.
# For contest purpose, the test data is rather small by now.
# You could think about highly efficient algorithm after the contest.
# Please remember to RESET your class variables declared in class MagicDictionary,
# as static/class variables are persisted across multiple test cases. Please see here for more details.
#
# Related Topics
# Hash Table Trie Google
# Similar Questions
# Implement Trie (Prefix Tree)

import unittest
import collections

# 32ms 19.92%
class MagicDictionary(object):
    def __init__(self):
        self.buckets = collections.defaultdict(list)

    def buildDict(self, words):
        for word in words:
            self.buckets[len(word)].append(word)

    def search(self, word):
        return any(sum(a!=b for a,b in zip(word, candidate)) == 1
                   for candidate in self.buckets[len(word)])

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/implement-magic-dictionary/solution/

# 83ms 22.96%
class MagicDictionary {
    private String[] dict;
    /** Initialize your data structure here. */
    public MagicDictionary() {
    }

    /** Build a dictionary through a list of words */
    public void buildDict(String[] dict) {
        this.dict = dict;
    }

    /** Returns if there is any word in the trie that equals to the given word
    after modifying exactly one character */
    public boolean search(String word) {
        for(int i=0;i<dict.length;i++){
            if(word.length()==dict[i].length()){
                int c=0;
                for(int j=0;j<dict[i].length();j++){
                    if(dict[i].charAt(j)==word.charAt(j))c++;
                    if(j-2==c)break;
                }
                if(c==dict[i].length()-1) return true;
            }
        }
        return false;
    }
}

# 60ms 95.02%
class MagicDictionary {

    Map<String, List<int[]>> map = new HashMap<>();
    /** Initialize your data structure here. */
    public MagicDictionary() {
    }

    /** Build a dictionary through a list of words */
    public void buildDict(String[] dict) {
        for (String s : dict) {
            for (int i = 0; i < s.length(); i++) {
                String key = s.substring(0, i) + s.substring(i + 1);
                int[] pair = new int[] {i, s.charAt(i)};

                List<int[]> val = map.getOrDefault(key, new ArrayList<int[]>());
                val.add(pair);

                map.put(key, val);
            }
        }
    }

    /** Returns if there is any word in the trie that equals to the given word
    after modifying exactly one character */
    public boolean search(String word) {
        for (int i = 0; i < word.length(); i++) {
            String key = word.substring(0, i) + word.substring(i + 1);
            if (map.containsKey(key)) {
                for (int[] pair : map.get(key)) {
                    if (pair[0] == i && pair[1] != word.charAt(i)) return true;
                }
            }
        }
        return false;
    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary obj = new MagicDictionary();
 * obj.buildDict(dict);
 * boolean param_2 = obj.search(word);
 */
'''