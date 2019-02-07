__source__ = 'https://leetcode.com/problems/k-similar-strings/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 854. K-Similar Strings
#
# Strings A and B are K-similar (for some non-negative integer K) if we can swap the positions of two letters in A exactly K times so that the resulting string equals B.
#
# Given two anagrams A and B, return the smallest K for which A and B are K-similar.
#
# Example 1:
#
# Input: A = "ab", B = "ba"
# Output: 1
# Example 2:
#
# Input: A = "abc", B = "bca"
# Output: 2
# Example 3:
#
# Input: A = "abac", B = "baca"
# Output: 2
# Example 4:
#
# Input: A = "aabc", B = "abca"
# Output: 2
# Note:
#
# 1 <= A.length == B.length <= 20
# A and B contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}
#
import unittest
import itertools
import collections
# 4904ms 0%
class Solution(object):
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if A == B: return 0

        N = len(A)
        alphabet = 'abcdef'
        pairs = [(a, b) for a in alphabet for b in alphabet if a != b]
        index = {p: i for i, p in enumerate(pairs)}

        count = [0] * len(index)
        for a, b in itertools.izip(A, B):
            if a != b:
                count[index[a, b]] += 1

        seen = set()
        for size in xrange(2, len(alphabet) + 1):
            for cand in itertools.permutations(alphabet, size):
                i = cand.index(min(cand))
                seen.add(cand[i:] + cand[:i])

        possibles = []
        for cand in seen:
            row = [0] * len(alphabet) * (len(alphabet) - 1)
            for a, b in itertools.izip(cand, cand[1:] + cand[:1]):
                row[index[a, b]] += 1
            possibles.append(row)

        ZERO = tuple([0] * len(row))
        memo = {ZERO: 0}
        def solve(count):
            if count in memo: return memo[count]

            ans = float('-inf')
            for row in possibles:
                count2 = list(count)
                for i, x in enumerate(row):
                    if count2[i] >= x:
                        count2[i] -= x
                    else: break
                else:
                    ans = max(ans, 1 + solve(tuple(count2)))

            memo[count] = ans
            return ans

        return sum(count) - solve(tuple(count))

# 472ms 39.78%
class Solution2(object):
    def kSimilarity(self, A, B):
        def neighbors(S):
            for i, c in enumerate(S):
                if c != B[i]:
                    break

            T = list(S)
            for j in xrange(i+1, len(S)):
                if S[j] == B[i]:
                    T[i], T[j] = T[j], T[i]
                    yield "".join(T)
                    T[j], T[i] = T[i], T[j]

        queue = collections.deque([A])
        seen = {A: 0}
        while queue:
            S = queue.popleft()
            if S == B: return seen[S]
            for T in neighbors(S):
                if T not in seen:
                    seen[T] = seen[S] + 1
                    queue.append(T)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/k-similar-strings/solution/
Approach 1: Brute Force with Dynamic Programming
Complexity Analysis
Time Complexity: O(2^(N+W)), where N is the length of the string, and W is the length of the alphabet.
Space Complexity: O(2^(N+W))

class Solution {
    String[] alphabet = new String[]{"a", "b", "c", "d", "e", "f"};
    Map<String, Integer> memo;

    public int kSimilarity(String A, String B) {
        if (A.equals(B)) return 0;
        int N = A.length();
        memo = new HashMap();
        int ans = 0;

        int[] count = new int[alphabet.length * alphabet.length];
        for (int i = 0; i < N; ++i)
            if (A.charAt(i) != B.charAt(i)) {
                count[alphabet.length * (A.charAt(i) - 'a') + (B.charAt(i) - 'a')]++;
                ans++;
            }

        List<int[]> possibles = new ArrayList();
        // Enumerate over every cycle
        for (int size = 2; size <= alphabet.length; ++size)
            search: for (String cycle: permutations(alphabet, 0, size)) {
                // Check if cycle is canonical
                for (int i = 1; i < size; ++i)
                    if (cycle.charAt(i) < cycle.charAt(0))
                        continue search;

                // Add count to possibles
                int[] row = new int[count.length];
                for (int i = 0; i < size; ++i) {
                    int u = cycle.charAt(i) - 'a';
                    int v = cycle.charAt((i+1) % size) - 'a';
                    row[alphabet.length * u + v]++;
                }
                possibles.add(row);
            }

        int[] ZERO = new int[count.length];
        memo.put(Arrays.toString(ZERO), 0);
        return ans - numCycles(possibles, count);
    }

    public int numCycles(List<int[]> possibles, int[] count) {
        String countS = Arrays.toString(count);
        if (memo.containsKey(countS)) return memo.get(countS);

        int ans = Integer.MIN_VALUE;
        search: for (int[] row: possibles) {
            int[] count2 = count.clone();
            for (int i = 0; i < row.length; ++i) {
                if (count2[i] >= row[i])
                    count2[i] -= row[i];
                else
                    continue search;
            }
            ans = Math.max(ans, 1 + numCycles(possibles, count2));
        }

        memo.put(countS, ans);
        return ans;
    }

    public List<String> permutations(String[] alphabet, int used, int size) {
        List<String> ans = new ArrayList();
        if (size == 0) {
            ans.add(new String(""));
            return ans;
        }

        for (int b = 0; b < alphabet.length; ++b)
            if (((used >> b) & 1) == 0)
                for (String rest: permutations(alphabet, used | (1 << b), size - 1))
                    ans.add(alphabet[b] + rest);
        return ans;
    }
}

Approach 2: Pruned Breadth First Search
Complexity Analysis
Time Complexity: O(\sum_{k=0}^n \binom{N}{k} \frac{\min(2^k, (N-k)!)}{W * (\frac{N-k}{W})!}),
where N is the length of the string, and W is the length of the alphabet.
Space Complexity: O(N * t), where t is the time complexity given above.

# 11ms 18.64%
class Solution {
    public int kSimilarity(String A, String B) {
        Queue<String> queue = new ArrayDeque();
        queue.offer(A);
        Map<String, Integer> dist = new HashMap();
        dist.put(A, 0);

        while (!queue.isEmpty()) {
            String S = queue.poll();
            if (S.equals(B)) return dist.get(S);
            for (String T : neighbors(S, B)) {
                if (!dist.containsKey(T)) {
                    dist.put(T, dist.get(S) + 1);
                    queue.offer(T);
                }
            }
        }
        throw null;
    }

    private List<String> neighbors(String S, String target) {
        List<String> ans = new ArrayList();
        int i = 0;
        for (; i < S.length(); i++) {
            if (S.charAt(i) != target.charAt(i)) break;
        }

        char[] T = S.toCharArray();
        for (int j = i + 1; j < S.length(); j++) {
            if (S.charAt(j) == target.charAt(i)) {
                swap(T, i ,j);
                ans.add(new String(T));
                swap(T, i, j);
            }
        }
        return ans;

    }

    private void swap(char[] T, int i, int j) {
        char tmp = T[i];
        T[i] = T[j];
        T[j] = tmp;
    }
}

# 2ms 100%
class Solution {
    public int kSimilarity(String A, String B) {
        char[] chA = A.toCharArray();
        char[] chB = B.toCharArray();
        int cost = pre(chA, chB);
        return dfs(chA, chB, 0, cost);
    }

    private int dfs(char[] chA, char[] chB, int start, int cost) {
        int n = chA.length;
        while (start < n && chA[start] == chB[start]) {
            start++;
        }
        int min = cost + n - start;
        for (int j = start + 1; j < n; j++) {
            if (chA[j] == chB[start] && chA[j] != chB[j]) {
                swap(chA, start, j);
                min = Math.min(min, dfs(chA, chB, start + 1, cost + 1));
                swap(chA, start, j);
                if (chA[start] == chB[j]) break;
            }
        }
        return min;
    }

    private int pre(char[] chA, char[] chB) {
        int cost = 0;
        int n = chA.length;
        for (int i = 0; i < n; i++) {
            if (chA[i] != chB[i]) {
                for (int j = i + 1; j < n; j++) {
                    if (chA[i] == chB[j] && chA[j] == chB[i]) {
                        cost++;
                        swap(chA, i, j);
                        break;
                    }
                }
            }
        }
        return cost;
    }

    private void swap(char[] T, int i, int j) {
        char tmp = T[i];
        T[i] = T[j];
        T[j] = tmp;
    }
}

# https://leetcode.com/problems/k-similar-strings/discuss/139872/Java-Backtracking-with-Memorization
# backtracking
# 69ms 36.39%
class Solution {
    public int kSimilarity(String A, String B) {
        Map<String, Integer> map = new HashMap();
        return bs(A.toCharArray(), B, map, 0);
    }
    
    private int bs(char[] charA, String B, Map<String, Integer> map, int i) {
        String A = new String(charA);

        if (A.equals(B)) return 0;
        if (map.containsKey(A)) return map.get(A);
        int min = Integer.MAX_VALUE;
        while (i < charA.length && charA[i] == B.charAt(i)) {
            i++;
        }
        for (int j = i + 1; j < B.length(); j++) {
            if (charA[j] == B.charAt(i)) {
                swap(charA, j, i);
                int next = bs(charA, B, map, i + 1);
                if (next != Integer.MAX_VALUE) {
                    min = Math.min(min, next + 1);
                }
                swap(charA, j, i);
            }
        }
        map.put(A, min);
        return min;
    }
    
    public void swap(char[] cs, int i, int j) {
        char tmp = cs[i];
        cs[i] = cs[j];
        cs[j] = tmp;
    }
}

# https://leetcode.com/problems/k-similar-strings/discuss/140099/JAVA-BFS-32-ms-cleanconciseexplanationwhatever
# BFS
# 24ms 83.71%
class Solution {
    public int kSimilarity(String A, String B) {
        if (A.equals(B)) return 0;
        Set<String> set = new HashSet();
        Queue<String> q = new LinkedList();
        q.add(A);
        set.add(A);
        int res = 0;
        while (!q.isEmpty()) {
            res++;
            for (int sz = q.size() - 1; sz >= 0; sz--) {
                String s = q.poll();
                int p = 0;
                while (p < s.length() && s.charAt(p) == B.charAt(p)) p++;
                for (int j = p + 1; j < s.length(); j++) {
                    if (s.charAt(j) == B.charAt(j) || s.charAt(p) != B.charAt(j)) continue;
                    String tmp = swap(s, p, j);
                    if (tmp.equals(B)) return res;
                    if (set.add(tmp)) q.add(tmp);
                }
            }
        }
        return res;  
    }
    
    private String swap(String s, int i, int j) {
        char[] chs = s.toCharArray();
        char tmp = chs[i];
        chs[i] = chs[j];
        chs[j] = tmp;
        return new String(chs);
    }
}
'''
