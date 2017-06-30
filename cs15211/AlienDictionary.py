__source__ = 'https://leetcode.com/problems/alien-dictionary/#/description'
# # https://github.com/kamyu104/LeetCode/blob/master/Python/alien-dictionary.py
# There is a new alien language which uses the latin alphabet.
# However, the order among letters are unknown to you.
# You receive a list of non-empty words from the dictionary,
# where words are sorted lexicographically by the rules of this new language.
# Derive the order of letters in this language.
#
# Example 1:
# Given the following words in dictionary,
#
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# The correct order is: "wertf".
#
# Example 2:
# Given the following words in dictionary,
#
# [
#   "z",
#   "x"
# ]
# The correct order is: "zx".
#
# Example 3:
# Given the following words in dictionary,
#
# [
#   "z",
#   "x",
#   "z"
# ]
# The order is invalid, so return "".
#
# Note:
# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.
# Hide Company Tags Google Airbnb Facebook Twitter Snapchat Pocket Gems
# Hide Tags Graph Topological Sort
# Hide Similar Problems (M) Course Schedule II
#

import sets
import collections

# Time:  O(n)
# Space: O(|V|+|E|) = O(26 + 26^2) = O(1)

# BFS solution.
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        result, zero_in_degree_queue, in_degree, out_degree = [], collections.deque(), {}, {}
        nodes = sets.Set()
        for word in words:
            for c in word:
                nodes.add(c)

        for i in xrange(1, len(words)):
            self.findEdges(words[i-1], words[i], in_degree, out_degree)

        for node in nodes:
            if node not in in_degree:
                zero_in_degree_queue.append(node)

        while zero_in_degree_queue:
            precedence = zero_in_degree_queue.popleft()
            result.append(precedence)

            if precedence in out_degree:
                for c in out_degree[precedence]:
                    in_degree[c].discard(precedence)
                    if not in_degree[c]:
                        zero_in_degree_queue.append(c)

                del out_degree[precedence]

        if out_degree:
            return ""
        return "".join(result)

    # Construct the graph.
    def findEdges(self, word1, word2, in_degree, out_degree):
        str_len = min(len(word1), len(word2))
        for i in xrange(str_len):
            if word1[i] != word2[i]:
                if word2[i] not in in_degree:
                    in_degree[word2[i]] = sets.Set()
                if word1[i] not in out_degree:
                    out_degree[word1[i]] = sets.Set()
                in_degree[word2[i]].add(word1[i])
                out_degree[word1[i]].add(word2[i])
                break

# DFS solution.
class Solution2(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # Find ancestors of each node by DFS.
        nodes, ancestors = sets.Set(), {}
        for i in xrange(len(words)):
            for c in words[i]:
                nodes.add(c)

        for node in nodes:
            ancestors[node] = []

        for i in xrange(1, len(words)):
            self.findEdges(words[i-1], words[i], ancestors)

        # Output topological order by DFS.
        result = []
        visited = {}
        for node in nodes:
            if self.topSortDFS(node, node, ancestors, visited, result):
                return ""
        return "".join(result)

    # Construct the graph.
    def findEdges(self, word1, word2, ancestors):
        min_len = min( len(word1), len(word2))
        for i in xrange(min_len):
            if word1[i] != word2[i]:
                ancestors[word2[i]].append(word1[i])
                break

    # Topological sort, return whether there is a cycle.
    def topSortDFS(self, root, node, ancestors, visited, result):
        if node not in visited:
            visited[node] = root
            for ancestor in ancestors[node]:
                if self.topSortDFS(root, ancestor, ancestors, visited, result):
                    return True
            result.append(node)
        elif visited[node] == root:
            # Visited from the same root in the DFS path.
            # So it is cyclic.
            return True
        return False


#java
js = '''
//dfs
public class Solution {
    public String alienOrder(String[] words) {
        if (words == null || words.length == 0) {
            return "";
        }
        Map<Character, Set<Character>> graph = new HashMap<>();
        Stack<Character> stack = new Stack<>();
        Set<Character> visited = new HashSet<Character>();
        Set<Character> loop = new HashSet<Character>();
        // Read to graph
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            for (int j = 0; j < word.length(); j++) {
                char c = word.charAt(j);
                if (!graph.containsKey(c)) {
                    graph.put(c, new HashSet<Character>());
                }
            }
            if (i > 0) {
                String prev = words[i - 1];
                for (int k = 0; k < prev.length() && k < word.length(); k++) {
                    if (prev.charAt(k) != word.charAt(k)) {
                        graph.get(prev.charAt(k)).add(word.charAt(k));
                        break;
                    }
                }
            }
        }
        // DFS
        for (char c : graph.keySet()) {
            if (!dfs(c, graph, stack, visited, loop)) {
                return "";
            }
        }
        // Print result
        StringBuilder sb = new StringBuilder();
        while (!stack.empty()) {
            sb.append(stack.pop());
        }
        return sb.toString();
    }

    private boolean dfs(char c, Map<Character, Set<Character>> graph, Stack<Character> stack, Set<Character> visited, Set<Character> loop) {
        if (visited.contains(c)) {
            return true;
        }
        if (loop.contains(c)) {
            return false;
        }
        loop.add(c);
        for (char next : graph.get(c)) {
            if (!dfs(next, graph, stack, visited, loop)) {
                return false;
            }
        }
        visited.add(c);
        stack.push(c);
        return true;
    }
}
//BFS
public class Solution {
    public String alienOrder(String[] words) {
        Map<Character, Set<Character>> map=new HashMap<Character, Set<Character>>();
        Map<Character, Integer> degree=new HashMap<Character, Integer>();
        String result="";
        if(words==null || words.length==0) return result;
        for(String s: words){
            for(char c: s.toCharArray()){
                degree.put(c,0);
            }
        }
        for(int i=0; i<words.length-1; i++){
            String cur=words[i];
            String next=words[i+1];
            int length=Math.min(cur.length(), next.length());
            for(int j=0; j<length; j++){
                char c1=cur.charAt(j);
                char c2=next.charAt(j);
                if(c1!=c2){
                    Set<Character> set=new HashSet<Character>();
                    if(map.containsKey(c1)) set=map.get(c1);
                    if(!set.contains(c2)){
                        set.add(c2);
                        map.put(c1, set);
                        degree.put(c2, degree.get(c2)+1);
                    }
                    break;
                }
            }
        }
        Queue<Character> q=new LinkedList<Character>();
        for(char c: degree.keySet()){
            if(degree.get(c)==0) q.add(c);
        }
        while(!q.isEmpty()){
            char c=q.remove();
            result+=c;
            if(map.containsKey(c)){
                for(char c2: map.get(c)){
                    degree.put(c2,degree.get(c2)-1);
                    if(degree.get(c2)==0) q.add(c2);
                }
            }
        }
        if(result.length()!=degree.size()) return "";
        return result;
    }
}
'''