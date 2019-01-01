# coding=utf-8
__source__ = 'https://leetcode.com/problems/similar-string-groups/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 839. Similar String Groups
#
# Two strings X and Y are similar if we can swap two letters (in different positions) of X,
# so that it equals Y.
#
# For example, "tars" and "rats" are similar (swapping at positions 0 and 2),
# and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".
#
# Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.
# Notice that "tars" and "arts" are in the same group even though they are not similar.
# Formally, each group is such that a word is in the group if and only if it is similar
# to at least one other word in the group.
#
# We are given a list A of strings.  Every string in A is an anagram of every other string in A.
# How many groups are there?
#
# Example 1:
#
# Input: ["tars","rats","arts","star"]
# Output: 2
#
# Note:
#     A.length <= 2000
#     A[i].length <= 1000
#     A.length * A[i].length <= 20000
#     All words in A consist of lowercase letters only.
#     All words in A have the same length and are anagrams of each other.
#     The judging time limit has been increased for this question.
#
import unittest


class Solution:
    pass  # start coding


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/similar-string-groups/solution/
#
# if it is similar, the string can traverse to each other
Approach #1: Piecewise [Accepted]
Complexity Analysis
Time Complexity: O(NWmin⁡(N,W^2)), where N is the length of A, and W is the length of each given word.
Space Complexity: O(NW^3) If N < W^2, the space complexity is O(N).
Otherwise, the space complexity is O(NW^3): for each of NW^2 neighbors we store a word of length W. 
(Plus, we store O(NW^2) node indices ("buckets") which is dominated by the O(NW^3) term.) 
Because W^2 <= N in this case, we could also write the space complexity as O(N^2 W)

# 3604ms 1.11%
class Solution {
    public int numSimilarGroups(String[] A) {
        int N = A.length;
        int W = A[0].length();
        DSU dsu = new DSU(N);

        if (N < W*W) { // If few words, then check for pairwise similarity: O(N^2 W)
            for (int i = 0; i < N; ++i)
                for (int j = i+1; j < N; ++j)
                    if (similar(A[i], A[j]))
                        dsu.union(i, j);

        } else { // If short words, check all neighbors: O(N W^3)
            Map<String, List<Integer>> buckets = new HashMap();
            for (int i = 0; i < N; ++i) {
                char[] L = A[i].toCharArray();
                for (int j0 = 0; j0 < L.length; ++j0)
                    for (int j1 = j0 + 1; j1 < L.length; ++j1) {
                        swap(L, j0, j1);
                        StringBuilder sb = new StringBuilder();
                        for (char c: L) sb.append(c);
                        buckets.computeIfAbsent(sb.toString(),
                                x-> new ArrayList<Integer>()).add(i);
                        swap(L, j0, j1);
                    }
            }

            for (int i1 = 0; i1 < A.length; ++i1)
                if (buckets.containsKey(A[i1]))
                    for (int i2: buckets.get(A[i1]))
                        dsu.union(i1, i2);
        }

        int ans = 0;
        for (int i = 0; i < N; ++i)
            if (dsu.parent[i] == i) ans++;

        return ans;
    }

    public boolean similar(String word1, String word2) {
        int diff = 0;
        for (int i = 0; i < word1.length(); ++i)
            if (word1.charAt(i) != word2.charAt(i))
                diff++;
        return diff <= 2;
    }

    public void swap(char[] A, int i, int j) {
        char tmp = A[i];
        A[i] = A[j];
        A[j] = tmp;
    }
}

class DSU {
    int[] parent;
    public DSU(int N) {
        parent = new int[N];
        for (int i = 0; i < N; ++i)
            parent[i] = i;
    }
    public int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    public void union(int x, int y) {
        parent[find(x)] = find(y);
    }
}
# https://leetcode.com/problems/similar-string-groups/discuss/132374/Short-C%2B%2B-solution-at-220ms-using-disjoint-set
# Union Find
# 211ms 92.16%
class Solution {
    class UF {
        int count;
        int[] parent;
        public UF(int n) {
            count = n;
            parent = new int[n];
            for (int i = 0; i < n; i++) parent[i] = i;
        }
        
        public int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }
        
        public void union(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            if (rootX != rootY) {
                count--;
                parent[rootX] = rootY;
            }
        }
    }
    
    public int numSimilarGroups(String[] A) {
        UF uf = new UF(A.length);
        for (int i = 0; i < A.length; i++) {
            for (int j = i + 1; j < A.length; j++) {
                if (isSimilar(A[i], A[j])) uf.union(i, j);
            }
        }
        return uf.count;
    }
    
    private boolean isSimilar(String s1, String s2) {
        int diff = 0;
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i) && ++diff > 2) return false;
        }
        return true;
    }
}

# BFS
# 556ms 35.29%
class Solution {
    public int numSimilarGroups(String[] A) {
        int res = 0;
        boolean[] seen = new boolean[A.length];
        for (int i = 0; i < A.length; i++) {
            if (seen[i]) continue;
            res++;
            Queue<String> q = new LinkedList();
            q.offer(A[i]);
            while (!q.isEmpty()) {
                String cur = q.poll();
                for (int j = 0; j < A.length; j++) {
                    if (seen[j]) continue;
                    String next = A[j];
                    int diff = 0;
                    for (int k = 0; k < cur.length(); k++) {
                        if (cur.charAt(k) != next.charAt(k)) diff++;
                    }
                    //important here, "aaaaa", "aaaaa" should be grouped together
                    if (diff == 2 || (diff == 0 && cur.length() >= 2)) { 
                        seen[j] = true;
                        q.add(next);
                    }
                    
                }
            }
        }
        return res;
    }
}

# DFS
# 475ms 37.25%
class Solution {
    public int numSimilarGroups(String[] A) {
        int res = 0;
        Set<String> set = new HashSet();
        for (int i = 0; i < A.length; i++) {
            if (!set.contains(A[i])) {
                dfs(i, A, set);
                res++;
            }
        }
        return res;
    }
    
    private void dfs(int k, String[] A, Set<String> set) {
        String cur = A[k];
        set.add(cur);    
        for (int i = 0; i < A.length; i++) {
            if (!set.contains(A[i]) && has2Diff(A[i], cur)) dfs(i, A, set);
        }
    }
    
    private boolean has2Diff(String s1, String s2) {
        int diff = 0, i = 0;
        while(i < s1.length() && diff <= 2) {
            if (s1.charAt(i) != s2.charAt(i++)) diff++;
        }
        return diff == 2;
    }
}

# DFS without using set
# 188ms 100%
class Solution {
    public int numSimilarGroups(String[] A) {
        if (A.length < 2) return A.length;
        int rst = 0;
        for (int i = 0; i < A.length; i++) {
            if (A[i] == null) continue;
            String str = A[i];
            A[i] = null;
            rst++;
            dfs(A, str);
        }
        return rst;
    }
    
    private void dfs(String[]arr, String str){
        for( int i = 0; i < arr.length; i++) {
            if (arr[i] == null) continue;
            if (similar(str, arr[i])) {
                String s = arr[i];
                arr[i] = null;
                dfs(arr, s);
            }
        }
    }
    
    private boolean similar(String w1, String w2){
        int diff = 0;
        for (int i = 0; i < w1.length(); i++) {
            if (w1.charAt(i) != w2.charAt(i)) {
                diff++;
                if (diff > 2) break;
            }
        }
        return diff <= 2;
    }     
}

'''
