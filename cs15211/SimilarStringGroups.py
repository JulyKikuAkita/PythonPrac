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

# 240ms 81.69%
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
