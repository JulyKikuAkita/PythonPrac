# coding=utf-8
__source__ = 'https://leetcode.com/problems/sentence-similarity-ii/'
# Time:  O()
# Space: O()
# Union-Find
#
# Description: Leetcode # 737. Sentence Similarity II
#
# Given two sentences words1, words2 (each represented as an array of strings),
# and a list of similar word pairs pairs, determine if two sentences are similar.
#
# For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar,
# if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].
#
# Note that the similarity relation is transitive.
# For example, if "great" and "good" are similar,
# and "fine" and "good" are similar, then "great" and "fine" are similar.
#
# Similarity is also symmetric.
# For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.
#
# Also, a word is always similar with itself.
# For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar,
# even though there are no specified similar word pairs.
#
# Finally, sentences can only be similar if they have the same number of words.
# So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].
#
# Note:
#
# The length of words1 and words2 will not exceed 1000.
# The length of pairs will not exceed 2000.
# The length of each pairs[i] will be 2.
# The length of each words[i] and pairs[i][j] will be in the range [1, 20].
#
import unittest
import itertools

# 160ms 64.69%
class DSU:
    def __init__(self, N):
        self.par = range(N)
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)

class SolutionDSU(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        if len(words1) != len(words2): return False

        index = {}
        count = itertools.count()
        dsu = DSU(2 * len(pairs))
        for pair in pairs:
            for p in pair:
                if p not in index:
                    index[p] = next(count)
            dsu.union(index[pair[0]], index[pair[1]])

        return all(w1 == w2 or
                   w1 in index and w2 in index and
                   dsu.find(index[w1]) == dsu.find(index[w2])
                   for w1, w2 in zip(words1, words2))

# 112ms 100%
class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False

        def find_parent(w1):
            while w1 in parent:
                w1 = parent[w1]
            return w1

        parent = dict()
        for w1, w2 in pairs:
            w1 = find_parent(w1)
            w2 = find_parent(w2)
            if w1 != w2:
                parent[w1] = w2

        for i in xrange(len(words1)):
            if words1[i] == words2[i]:
                continue
            if find_parent(words1[i]) != find_parent(words2[i]):
                return False
        return True

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/sentence-similarity-ii/solution/

Approach #1: Depth-First Search [Accepted]
Complexity Analysis
Time Complexity: O(NP), where N is the maximum length of words1 and words2,
and P is the length of pairs.
Each of N searches could search the entire graph.
Space Complexity: O(P), the size of pairs.

# 23ms 99.29%
class Solution {
    public boolean areSentencesSimilarTwo(String[] words1, String[] words2, String[][] pairs) {
        // input check
        if (words1.length != words2.length) return false;
        // construct graph adjacency list
        Map<String, List<String>> graph = new HashMap();
        for (String[] pair: pairs) {
            graph.computeIfAbsent(pair[0], k -> new ArrayList()).add(pair[1]);
            graph.computeIfAbsent(pair[1], k -> new ArrayList()).add(pair[0]);
        }
        // stack based iterative DFS
        for (int i = 0; i < words1.length; ++i) {
            if (!connected(graph, words1[i], words2[i])) return false;
        }
        return true;
    }

    private boolean connected(Map<String, List<String>> graph, String w1, String w2) {
        // use stack-based DFS for connectivity check
        Stack<String> stack = new Stack();
        Set<String> seen = new HashSet();
        stack.add(w1);
        seen.add(w1);
        while (!stack.isEmpty()) {
            String word = stack.pop();
            if (word.equals(w2)) return true;
            for (String nei: graph.getOrDefault(word, new ArrayList<String>())) {
                if (!seen.contains(nei)) {
                    stack.push(nei);
                    seen.add(nei);
                }
            }
        }
        return false;
    }
}

Approach #2: Union-Find [Accepted]

Complexity Analysis
Time Complexity: O(NlogP+P), where N is the maximum length of words1 and words2,
and P is the length of pairs.
If we used union-by-rank,
this complexity improves to O(N * α(P)+P)≈O(N+P), where α is the Inverse-Ackermann function.
Space Complexity: O(P), the size of pairs.

# 23ms 99.35%
class Solution {
    private class Node {
        String word;
        int rank;
        Node parent;
        public Node(String word) {
            this.word = word;
            this.rank = 0;
            this.parent = null;
        }
    }

    public Node findParent(Node n1) {
        if (n1.parent == null) return n1;
        return findParent(n1.parent);
    }

    public void union(Node word1, Node word2) {
        Node p1 = findParent(word1);
        Node p2 = findParent(word2);
        if ( p1 == p2) return;
        if (p1.rank > p2.rank) p2.parent = p1;
        else if (p1.rank < p2.rank) p1.parent = p2;
        else{
            p2.parent = p1;
            p1.rank++;
        }
    }

    public boolean areSentencesSimilarTwo(String[] words1, String[] words2, String[][] pairs) {
        if (words1.length != words2.length) return false;
        Map<String, Node> map = new HashMap<>();
        for (int i = 0; i < pairs.length; i++) {
            Node node1 = map.get(pairs[i][0]);
            Node node2 = map.get(pairs[i][1]);
            if (node1 == null) {
                node1 = new Node(pairs[i][0]);
                map.put(pairs[i][0], node1); //setting parent as itself
            }
            if (node2 == null) {
                node2 = new Node(pairs[i][1]);
                map.put(pairs[i][1], node2); //setting parent as itself
            }
            union(node1, node2); //union of two nodes
        }

        for (int i = 0; i < words1.length; i++) {
            if (words1[i].equals(words2[i])) continue;
            Node n1 = map.get(words1[i]);
            Node n2 = map.get(words2[i]);
            if (n1 == null || n2 == null) return false;
            if (findParent(n1) != findParent(n2)) return false;
        }
        return true;
    }
}

# Use Map
# 36ms 72.35%
class Solution {
    public boolean areSentencesSimilarTwo(String[] words1, String[] words2, String[][] pairs) {
        int m = words1.length;
        int n = words2.length;
        if (m != n)
            return false;
        HashMap<String, String> unionMap = new HashMap<>();
        for (String[] pair : pairs){
            String parent1 = find(unionMap, pair[0]);
            String parent2 = find(unionMap, pair[1]);
            if (!parent1.equals(parent2)){
                unionMap.put(parent1, parent2);
            }
        }
        for (int i = 0; i < m; i++){
            String parent1 = find(unionMap, words1[i]);
            String parent2 = find(unionMap, words2[i]);
            if (!parent1.equals(parent2))
                return false;
        }
        return true;
    }

    private String find(HashMap<String, String> unionMap, String child){
        if (!unionMap.containsKey(child))
            return child;
        return find(unionMap, unionMap.get(child));
    }
}
'''
