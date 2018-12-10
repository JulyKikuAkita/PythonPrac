__source__ = 'https://leetcode.com/problems/design-search-autocomplete-system/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 642. Design Search Autocomplete System
#
# Design a search autocomplete system for a search engine.
# Users may input a sentence (at least one word and end with a special character '#').
# For each character they type except '#', you need to return the top 3 historical hot sentences
# that have prefix the same as the part of sentence already typed. Here are the specific rules:
#
# The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
# The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one).
# If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
# If less than 3 hot sentences exist, then just return as many as you can.
# When the input is a special character, it means the sentence ends, and in this case,
# you need to return an empty list.
# Your job is to implement the following functions:
#
# The constructor function:
#
# AutocompleteSystem(String[] sentences, int[] times): This is the constructor.
# The input is historical data. Sentences is a string array consists of previously typed sentences.
# Times is the corresponding times a sentence has been typed. Your system should record these historical data.
#
# Now, the user wants to input a new sentence.
# The following function will provide the next character the user types:
#
# List<String> input(char c): The input c is the next character typed by the user.
# The character will only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#').
# Also, the previously typed sentence should be recorded in your system.
# The output will be the top 3 historical hot sentences
# that have prefix the same as the part of sentence already typed.
#
#
# Example:
# Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
# The system have already tracked down the following sentences and their corresponding times:
# "i love you" : 5 times
# "island" : 3 times
# "ironman" : 2 times
# "i love leetcode" : 2 times
# Now, the user begins another search:
#
# Operation: input('i')
# Output: ["i love you", "island","i love leetcode"]
# Explanation:
# There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree.
# Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman".
#  Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
#
# Operation: input(' ')
# Output: ["i love you","i love leetcode"]
# Explanation:
# There are only two sentences that have prefix "i ".
#
# Operation: input('a')
# Output: []
# Explanation:
# There are no sentences that have prefix "i a".
#
# Operation: input('#')
# Output: []
# Explanation:
# The user finished the input, the sentence "i a" should be saved as a historical sentence in system.
# And the following input will be counted as a new search.
#
# Note:
# The input sentence will always start with a letter and end with '#',
# and only one blank space will exist between two words.
# The number of complete sentences that to be searched won't exceed 100.
# The length of each sentence including those in the historical data won't exceed 100.
# Please use double-quote instead of single-quote when you write test cases even for a character input.
# Please remember to RESET your class variables declared in class AutocompleteSystem,
# as static/class variables are persisted across multiple test cases. Please see here for more details.
#
# Companies
# Microsoft Facebook Lyft
# Related Topics
# Design Trie
# Similar Questions
# Implement Trie (Prefix Tree)
#
import unittest
import collections
# Let's use a trie. Because the requirement to enter the top 3 at a node can only get stronger,
# we do not have to recall discarded information.
# Thus, we can freely store the answer (top 3 sentences) directly on each node. When we get queries,
# we simply read off the answer.
#
# Whenever we add a sentence, at each node of the corresponding trie,
# we will update that node's info appropriately in case its top 3 answers changes.
# We'll use a "ShortList" to store our answer, which will keep track of only the top 3 answers.
#
# Our implementation could be better (for example, handling ShortList better,
# or storing sentence indices instead of full sentences), but because the limits are small,
# it doesn't matter for the question, so we choose the most straightforward approach.
# 925ms
_trie = lambda: collections.defaultdict(_trie)
INFO, END = True, False

# 548ms 96.59%
class ShortList(list):
    def append(self, val):
        for i, (nt, s) in enumerate(self):
            if s == val[1]:
                self[i] = val
                break
        else:
            list.append(self, val)

        self.sort()
        if len(self) > 3:
            self.pop()

class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.curnode = self.trie = _trie()
        self.sentence_to_count = collections.Counter()
        self.search = ''

        for sentence, count in zip(sentences, times):
            self.add(sentence, count)

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c != '#':
            self.search += c
            if self.curnode is None:
                return []
            if c not in self.curnode:
                self.curnode = None
                return []

            self.curnode = self.curnode[c]
            return [s for nt, s in self.curnode[INFO]]
        else:
            self.sentence_to_count[self.search] += 1
            self.add(self.search, self.sentence_to_count[self.search])
            self.search = ''
            self.curnode = self.trie
            return []

    def add(self, sentence, count):
        self.sentence_to_count[sentence] = count
        cur = self.trie
        self._add_info(cur, sentence, count)
        for letter in sentence:
            cur = cur[letter]
            self._add_info(cur, sentence, count)
        cur[END] = sentence

    def _add_info(self, node, sentence, count):
        if INFO not in node:
            node[INFO] = ShortList()
        node[INFO].append((-count, sentence))

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/design-search-autocomplete-system/solution/

Only thing more than a normal Trie is added a map of sentence to count
in each of the Trie node to facilitate process of getting top 3 results.

# 288ms 63.83%
class AutocompleteSystem {
    class TrieNode {
        Map<Character, TrieNode> children;
        Map<String, Integer> counts;
        boolean isWord;
        public TrieNode() {
            children = new HashMap<Character, TrieNode>();
            counts = new HashMap<String, Integer>();
            isWord = false;
        }
    }

    class Pair {
        String s;
        int c;
        public Pair(String s, int c) {
            this.s = s; this.c = c;
        }
    }

    TrieNode root;
    String prefix;


    public AutocompleteSystem(String[] sentences, int[] times) {
        root = new TrieNode();
        prefix = "";

        for (int i = 0; i < sentences.length; i++) {
            add(sentences[i], times[i]);
        }
    }

    private void add(String s, int count) {
        TrieNode curr = root;
        for (char c : s.toCharArray()) {
            TrieNode next = curr.children.get(c);
            if (next == null) {
                next = new TrieNode();
                curr.children.put(c, next);
            }
            curr = next;
            curr.counts.put(s, curr.counts.getOrDefault(s, 0) + count);
        }
        curr.isWord = true;
    }

    public List<String> input(char c) {
        if (c == '#') {
            add(prefix, 1);
            prefix = "";
            return new ArrayList<String>();
        }

        prefix = prefix + c;
        TrieNode curr = root;
        for (char cc : prefix.toCharArray()) {
            TrieNode next = curr.children.get(cc);
            if (next == null) {
                return new ArrayList<String>();
            }
            curr = next;
        }

        PriorityQueue<Pair> pq = new PriorityQueue<>((a, b) -> (a.c == b.c ? a.s.compareTo(b.s) : b.c - a.c));
        for (String s : curr.counts.keySet()) {
            pq.add(new Pair(s, curr.counts.get(s)));
        }

        List<String> res = new ArrayList<String>();
        for (int i = 0; i < 3 && !pq.isEmpty(); i++) {
            res.add(pq.poll().s);
        }
        return res;
    }
}


# 288ms 63.83%
class AutocompleteSystem {
    // trienode, with top 3 string and time
    // hashmap hash sentences and time
    // update triad with sentences, for path from root to leave, check trienode top 3 string
    // maintain current trienode for previous char
    // 26 + 1 character
    public HashMap<String, Integer> hm;
    private StringBuilder sb;
    private TrieNode root;
    private TrieNode curNode;
    public AutocompleteSystem(String[] sentences, int[] times) {
        hm = new HashMap<String, Integer>();
        sb = new StringBuilder();
        root = new TrieNode();
        curNode = root;
        for(int i =0; i<sentences.length; i++){
            hm.put(sentences[i], times[i]); // forget initialize
            updateTrie(root, sentences[i], times[i]);
        }
    }

    public List<String> input(char c) {
        //c = #, ' ', a-z , stringbuilder,  hashmap update
        List<String> ls = new LinkedList<String>();
        if(c == '#'){
            //reset
            String s = sb.toString();
            sb.setLength(0);
            curNode = root;
            int f = 1;
            if(!hm.containsKey(s)) f = 1;
            else f = hm.get(s)+1;
            hm.put(s, f);
            //update trie
            updateTrie(root, s, f);
        }else{
            // base value setup, sb, curNode
            sb.append(c);
            if(curNode ==null) return ls;
            int nIdx = c - 'a';
            if(nIdx < 0 || nIdx>25) nIdx = 26;
            curNode = curNode.child[nIdx];
            if(curNode!=null){
                for(String s: curNode.top){
                    if(s==null) break;
                    ls.add(s);
                }
            }
        }
        return ls;
    }

    private void updateTrie(TrieNode node, String s, int f){
        int idx = 0;
        int nIdx = 0;
        while(idx<s.length()){
            nIdx = s.charAt(idx++) - 'a';
            if(nIdx<0 || nIdx>25) nIdx = 26;
            if(node.child[nIdx]==null) node.child[nIdx] = new TrieNode();
            node = node.child[nIdx];
            node.updateTop(s, f);
        }
    }

    private class TrieNode{
        private String[] top;
        private int[] freqs;
        public TrieNode[] child;
        public TrieNode(){
            top = new String[3];
            freqs = new int[3];
            child = new TrieNode[27];
        }

        public void updateTop(String s, int f){
            String str = s, tmp = null;
            // System.out.print(s+","+f+": ");
            // for(String ss:top) System.out.print(ss+","); System.out.print("-> ");
            int cnt = f;
            for(int i=0; i<3; i++){
                if(top[i]==null){
                    top[i] = str; // should not be 's'
                    freqs[i] = f; // should not be 'f'
                    break;
                }else if(f<freqs[i] || (f==freqs[i] && str.compareTo(top[i])>0)) continue;
                else{
                    if(top[i].equals(str)){
                        freqs[i] = f;
                        break;
                    }else{
                        tmp = top[i];
                        top[i] = str;
                        str = tmp;
                        cnt = freqs[i];
                        freqs[i] = f;
                        f = cnt;
                        if(s.equals(str)) break;
                    }
                }
            }
            // for(String ss: top) System.out.print(ss+" ");
            // System.out.println("| "+ s);
        }
    }
}

/**
 * Your AutocompleteSystem object will be instantiated and called as such:
 * AutocompleteSystem obj = new AutocompleteSystem(sentences, times);
 * List<String> param_1 = obj.input(c);
 */

# Runtime error at leetcode
import java.util.*;
import java.util.Map.Entry;

public class AutocompleteSystem {
    private final static int FREQ = 3;
    AutoCompleteTrie root;
    String prefix;
    public AutocompleteSystem(String[] sentences, int[] times) {
        root = new AutoCompleteTrie();
        prefix = "";
        for (int i = 0; i < sentences.length; i++) {
            root.insert(sentences[i], times[i]);
        }
    }

    public List<String> input(char c) {
        if (c == '#') {
            root.insert(prefix, 1);
            prefix = "";
            return new ArrayList<String>();
        }
        prefix = prefix + c;
        List<String> res = root.autoComplete(prefix);
        System.out.println(res.toString());
        return res;
    }

    class AutoCompleteTrie implements Comparable<AutoCompleteTrie>{
        protected final Map<Character, AutoCompleteTrie> children;
        protected String value;
        protected boolean isWord = false;
        protected int count = 0;

        @Override
        public int compareTo(AutoCompleteTrie that) {
            if (this.count != that.count) {
                return this.count - that.count;
            } else {
                return this.value.compareTo(that.value);
            }
        }
        /**
         * constructor, initialize a new ACT with empty string as the root
         * @param value
         */
        private AutoCompleteTrie(String value) {
            this.value = value;
            children = new HashMap<Character, AutoCompleteTrie> ();
        }
        public AutoCompleteTrie() {
            this("");
        }
        /**
         * insert a word, this will construct a root to leave path
         * with the key of each node a character in the word,
         * value the prefix of the word till the key character
         * @param word
         */
        public void insert (String word, int count) {
            if (word == null)
                throw new IllegalArgumentException("Null string!");
            //this is a reference to the current object:
            //the object whose method or constructor is being called
            AutoCompleteTrie node = this;
            for (char c : word.toCharArray()) {
                //System.out.println(c + ": " + node.value);
                if (!node.children.containsKey(c))
                    node.add(c);
                node = node.children.get(c);

            }
            node.isWord = true;
            node.count += count;
            node.value = word;
        }

        /**
         * add a child of the node
         * the child will have the key the input character
         * and the value the value of the node + key character
         * @param c
         */
        private void add(char c) {
            String val;
            val = this.value + c;
            children.put(c, new AutoCompleteTrie(val));
        }

        /**
         * search if a word exists in the trie
         * @param word
         * @return
         */
        public boolean find(String word) {
            AutoCompleteTrie node = this;
            for (char c : word.toCharArray()) {
                if (!node.children.containsKey(c))
                    return false;
                node = node.children.get(c);
            }
            return node.value.equals(word);
        }

        /**
         * input prefix return all possible strings
         * with the same prefix in the trie
         * find the node of the prefix in the trie
         * call allChildren method and return the list
         * @param prefix
         * @return
         */
        public List<String> autoComplete(String prefix) {
            AutoCompleteTrie node = this;
            for (char c : prefix.toCharArray()) {
                if (!node.children.containsKey(c))
                    return Collections.emptyList();
                node = node.children.get(c);
            }
            List<AutoCompleteTrie> allChildren = node.allChildren();
            Collections.sort(allChildren);
            List<String> rst = new ArrayList<String> ();
            for (int i = 0; i < FREQ; i++) {
                //System.out.println(allChildren.get(i).value);
                rst.add(allChildren.get(i).value);
            }
            return rst;
        }
        /**
         * generate the list of all children of the current node/object
         * @return
         */
        private List<AutoCompleteTrie> allChildren() {
            List<AutoCompleteTrie> rst = new ArrayList<AutoCompleteTrie> ();

            //if the prefix is also a previous input word, add it to the list
            if (this.isWord) {
                rst.add(this);
            }
            //add all children
            for (Entry<Character, AutoCompleteTrie> entry : children.entrySet()) {
                AutoCompleteTrie child = entry.getValue();
                List<AutoCompleteTrie> childPrefixes = child.allChildren();
                rst.addAll(childPrefixes);
            }
            return rst;
        }
    }
}

/**
 * Your AutocompleteSystem object will be instantiated and called as such:
 * AutocompleteSystem obj = new AutocompleteSystem(sentences, times);
 * List<String> param_1 = obj.input(c);
 */
'''