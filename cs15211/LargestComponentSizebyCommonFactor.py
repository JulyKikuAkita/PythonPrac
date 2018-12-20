__source__ = 'https://leetcode.com/problems/largest-component-size-by-common-factor/'
# Time:  O(N sqrt{W}) where N is the length of A, and W=max(A[i]).
# Space: O(N)
#
# Description: Leetcode # 952. Largest Component Size by Common Factor
#
# Given a non-empty array of unique positive integers A, consider the following graph:
#
#     There are A.length nodes, labelled A[0] to A[A.length - 1];
#     There is an edge between A[i] and A[j] if and only if A[i] and A[j]
# share a common factor greater than 1.
#
# Return the size of the largest connected component in the graph.
#
#
#
# Example 1:
#
# Input: [4,6,15,35]
# Output: 4
#
# Example 2:
#
# Input: [20,50,9,63]
# Output: 2
#
# Example 3:
#
# Input: [2,3,6,7,4,12,21,39]
# Output: 8
#
# Note:
#
#     1 <= A.length <= 20000
#     1 <= A[i] <= 100000
#

import unittest
import collections
# 2880ms 6.81%
class DSU:
    def __init__(self, N):
        self.p = range(N)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution(object):
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        B = []
        for x in A:
            facs = []
            d = 2
            while d * d <= x:
                if x % d == 0:
                    while x % d == 0:
                        x /= d
                    facs.append(d)
                d += 1

            if x > 1 or not facs:
                facs.append(x)
            B.append(facs)

        primes = list({p for facs in B for p in facs})
        prime_to_index = {p: i for i, p in enumerate(primes)}

        dsu = DSU(len(primes))
        for facs in B:
            for x in facs:
                dsu.union(prime_to_index[facs[0]], prime_to_index[x])

        count = collections.Counter(dsu.find(prime_to_index[facs[0]]) for facs in B)
        return max(count.values())

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/largest-component-size-by-common-factor/solution/
#
Approach 1: Union-Find
Complexity Analysis
Time Complexity: O(N sqrt{W}) where N is the length of A, and W=max(A[i]).
Space Complexity: O(N)

3 285ms 29.68%
class Solution {
    public int largestComponentSize(int[] A) {
        int N = A.length;

        // factored[i] = a list of unique prime factors of A[i]
        ArrayList<Integer>[] factored = new ArrayList[N];
        for (int i = 0; i < N; ++i) {
            factored[i] = new ArrayList<Integer>();
            int d = 2, x = A[i];
            while (d * d <= x) {
                if (x % d == 0) {
                    while (x % d == 0)
                        x /= d;
                    factored[i].add(d);
                }

                d++;
            }

            if (x > 1 || factored[i].isEmpty())
                factored[i].add(x);
        }

        // primesL : a list of all primes that occur in factored
        Set<Integer> primes = new HashSet();
        for (List<Integer> facs: factored)
            for (int x: facs)
                primes.add(x);

        int[] primesL = new int[primes.size()];
        int t = 0;
        for (int x: primes)
            primesL[t++] = x;

        // primeToIndex.get(v) == i  iff  primes[i] = v
        Map<Integer, Integer> primeToIndex = new HashMap();
        for (int i = 0; i < primesL.length; ++i)
            primeToIndex.put(primesL[i], i);

        DSU dsu = new DSU(primesL.length);
        for (List<Integer> facs: factored)
            for (int x: facs)
                dsu.union(primeToIndex.get(facs.get(0)), primeToIndex.get(x));

        int[] count = new int[primesL.length];
        for (List<Integer> facs: factored)
            count[dsu.find(primeToIndex.get(facs.get(0)))]++;

        int ans = 0;
        for (int x: count)
            if (x > ans)
                ans = x;
        return ans;
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
# 124ms 90.54%
class Solution {
    int[] size, rank, root;
    int res = 0;
    
    public int largestComponentSize(int[] A) {
        int[] map = new int[100001];
        size = new int[A.length];
        rank = new int[A.length];
        root = new int[A.length];
        Arrays.fill(size, 1);
        for (int i = 0; i < root.length; i++) root[i] = i;
        
        for (int i = 0; i < A.length; i++) {
            int f = 2, n = A[i], a = A[i];
            while ( f * f <= a && a != 1) {
                if (a % f == 0) {
                    while (a % f == 0) a /= f;
                    if (map[f] == 0) map[f] = i + 1;
                    else {
                        int m = map[f] - 1;
                        union(i, m);
                    }
                }
                f++;
            }
            if (a != 1) {
                if (map[a] == 0) map[a] = i + 1;
                else {
                    int m = map[a] - 1;
                    union(i, m); 
                }
            }
        }
        return res;   
    }
    
    public void union(int n, int m) {
        int root1 = find(n), root2 = find(m);
        if (root1 != root2) {
            if (rank[root1] > rank[root2]) {
                root[root2] = root1;
                size[root1] += size[root2];
            } else if (rank[root1] < rank[root2]) {
                root[root1] = root2;
                size[root2] += size[root1];
            } else {
                root[root2] = root1;
                size[root1] += size[root2];
                rank[root1]++;
            }
        }
        res = Math.max(res, Math.max(size[root1], size[root2]));
    }
    
    public int find(int n) {
        while (root[n] != n) n = root[n];
        return root[n];
    }
    
}

# not understand...
# 45ms 99.44%
class Solution {
    public int largestComponentSize(int[] A) {
        if(A.length <= 1) return A.length;
		int max = 0;
        for (int v : A) {
            if (v > max) max = v;
        }
		int[] pfs = initPF(max);
		int[] cs = new int[max+1];
		max = 0;
        for (int v : A) {
            if (v > 1) {
                int k = pfs[v];
                int root = rootof(cs, k);
				max = Math.max(max, ++cs[root]);
                for(;;) {
                    int k1 = pfs[v];
					if(k1 != k) {
						k = k1;
						int rk = rootof(cs, k);
						if(rk != root) {
							max = Math.max(max, merge(cs, root, rk));
						}
					}
                    if(v <= k) break;
					v /= k;
                }
            }
        }
		return max;
    }
    
    private int[] initPF(int N) {
        int[] pfs = new int[N + 1];
        for (int v = 2; v <= N; v += 2) pfs[v] = 2;
        for (int p = 3; p <= N; p += 2) {
            for (;p <= N && pfs[p] != 0; p += 2); 
            if (p > N) break;
                pfs[p] = p;
                int p2 = p + p;
                for (int v = p + p2; v <= N; v += p2) {
                    if (pfs[v] == 0) pfs[v] = p;
            }
        }
        return pfs;
    }
    
    private int rootof(int[] cs, int v) {
        int r = cs[v];
		if (r >= 0) return v;
        r = -r;
        int r1 = rootof(cs, r);
        if (r != -r) cs[v] = -r1;
		return r1;
    }
    
    private int merge(int[] cs, int r1, int r2) {
        int v = cs[r1] + cs[r2];
        cs[r1] = v;
        cs[r2] = -r1;
        return v;
    }
        
}
'''
