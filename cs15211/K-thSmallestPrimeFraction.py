__source__ = 'https://leetcode.com/problems/k-th-smallest-prime-fraction/'
# Time:  O(KlogN)
# Space: O(N)
#
# Description: Leetcode # 786. K-th Smallest Prime Fraction
#
# A sorted list A contains 1, plus some number of primes.
# Then, for every p < q in the list, we consider the fraction p/q.
#
# What is the K-th smallest fraction considered?
# Return your answer as an array of ints, where answer[0] = p and answer[1] = q.
#
# Examples:
# Input: A = [1, 2, 3, 5], K = 3
# Output: [2, 5]
# Explanation:
# The fractions to be considered in sorted order are:
# 1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
# The third fraction is 2/5.
#
# Input: A = [1, 7], K = 1
# Output: [1, 7]
# Note:
#
# A will have length between 2 and 2000.
# Each A[i] will be between 1 and 30000.
# K will be between 1 and A.length * (A.length - 1) / 2.
#
import unittest
import heapq
# 7504ms 28.85%, may TLE
class Solution(object):
    #Note - this solution may TLE.
    def kthSmallestPrimeFraction(self, A, K):
        pq = [(A[0] / float(A[i]), 0, i) for i in xrange(len(A) - 1, 0, -1)]

        for _ in xrange(K-1):
            frac, i, j = heapq.heappop(pq)
            i += 1
            if i < j:
                heapq.heappush(pq, (A[i] / float(A[j]), i, j))

        return A[pq[0][1]], A[pq[0][2]]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/k-th-smallest-prime-fraction/solution/
Approach #1: Binary Search [Accepted]
Complexity Analysis
Time Complexity: O(NlogW), where N is the length of primes,
and W is the width (in quantized units) of our binary search,
(hi - lo) / 1e-9 which is 10^9
Space Complexity: O(1)

# 6ms 100%
class Solution {
    public int[] kthSmallestPrimeFraction(int[] primes, int K) {
        double lo = 0, hi = 1;
        int[] ans = new int[]{0, 1};

        while (hi - lo > 1e-9) {
            double mi = lo + (hi - lo) / 2.0;
            int[] res = under(mi, primes);
            if (res[0] < K) {
                lo = mi;
            } else {
                ans[0] = res[1];
                ans[1] = res[2];
                hi = mi;
            }
        }
        return ans;
    }

    public int[] under(double x, int[] primes) {
        // Returns {count, numerator, denominator}
        int numer = 0, denom = 1, count = 0, i = -1;
        for (int j = 1; j < primes.length; ++j) {
            // For each j, find the largest i so that primes[i] / primes[j] < x
            // It has to be at least as big as the previous i, so reuse it ("two pointer")
            while (primes[i+1] < primes[j] * x) ++i;

            // There are i+1 fractions: (primes[0], primes[j]),
            // (primes[1], primes[j]), ..., (primes[i], primes[j])
            count += i+1;
            if (i >= 0 && numer * primes[j] < denom * primes[i]) {
                numer = primes[i];
                denom = primes[j];
            }
        }
        return new int[]{count, numer, denom};
    }
}
Approach #2: Heap [Accepted]
Complexity Analysis
Time Complexity: O(KlogN), where N is the length of A.
The heap has up to N elements, which uses O(logN) work to perform a pop operation on the heap.
We perform O(K)O such operations.
Space Complexity: O(N), the size of the heap.

# 805ms 28.87%
class Solution {
    public int[] kthSmallestPrimeFraction(int[] A, int K) {
         PriorityQueue<int[]> pq = new PriorityQueue<int[]>((a, b) ->
            A[a[0]] * A[b[1]] - A[a[1]] * A[b[0]]);

        for (int i = 1; i < A.length; i++) {
            pq.add(new int[]{0, i});
        }

        while(--K > 0) {
            int[] frac = pq.poll();
            if (frac[0]++ < frac[1] ) pq.offer(frac);
        }

        int[] ans = pq.poll();
        return new int[]{A[ans[0]], A[ans[1]]};
    }
}

Approach #3: Divide and Conquer [Accepted]
One approach outside the scope of this article is to perform a divide and conquer,
leading to a marvelous O(N)O(N) time complexity.
https://leetcode.com/problems/k-th-smallest-prime-fraction/discuss/115545/O(n)

# 8ms 93.58%
class Solution {
    public int[] kthSmallestPrimeFraction(int[] A, int K) {
        int n = A.length;
        double l = 0.0, r = 1.0;
        while (l < r) {
            double mid = (l + r) / 2;
            int total = 0, p = 0, q = 0;
            double max = 0.0;
            int j = 1;
            for (int i = 0; i < n - 1; i++) {
                while (j < n && A[i] > mid * A[j]) j++;
                total += (n - j);
                if (j == n) break;

                double f = (A[i] * 1.0) / A[j];
                if ( f > max) {
                    max = f;
                    p = i;
                    q = j;
                }
            }
            if (total == K) return new int[]{A[p],A[q]};
            else if (total > K) r = mid;
            else l = mid;
        }
        return new int[0];
    }
}
'''