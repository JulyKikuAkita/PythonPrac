__source__ = 'https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 862. Shortest Subarray with Sum at Least K
#
# Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.
#
# If there is no non-empty subarray with sum at least K, return -1.
#
# Example 1:
#
# Input: A = [1], K = 1
# Output: 1
# Example 2:
#
# Input: A = [1,2], K = 4
# Output: -1
# Example 3:
#
# Input: A = [2,-1,2], K = 3
# Output: 3
#
#
# Note:
#
# 1 <= A.length <= 50000
# -10 ^ 5 <= A[i] <= 10 ^ 5
# 1 <= K <= 10 ^ 9
#
import unittest

#228ms 98.26%
class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: Approach 1: Sliding Window
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/solution/
#
# 50 ms, 32.32%
class Solution {
    public int shortestSubarray(int[] A, int K) {
        int N = A.length;
        long[] P = new long[N + 1];
        for (int i = 0; i < N; ++i) {
            P[i+1] = P[i] + (long) A[i];
        }

        // Want smallest y-x with P[y] - P[x] >= K
        int ans = N+1; // N+1 is impossible
        Deque<Integer> monoq = new LinkedList(); //opt(y) candidates, as indices of P

        for (int y = 0; y < P.length; y++) {
            // Want opt(y) = largest x with P[x] <= P[y] - K;
            while (!monoq.isEmpty() && P[y] <= P[monoq.getLast()]) monoq.removeLast();
            while (!monoq.isEmpty() && P[y] >= P[monoq.getFirst()] + K) {
                ans = Math.min(ans, y - monoq.removeFirst());
            }
            monoq.addLast(y);
        }
        return ans < N + 1? ans : -1;
    }
}

# Detail with deque:
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/143726/C++JavaPython-O(N)-Using-Deque
# 27ms 94.12%
class Solution {
    public int shortestSubarray(int[] A, int K) {
        int N = A.length, res = N + 1;
        int[] B = new int[N + 1];
        for (int i = 0; i < N; i++) B[i + 1] = B[i] + A[i];
        Deque<Integer> d = new ArrayDeque();
        for (int i = 0; i < N + 1; i++) {
            while (d.size() > 0 && B[i] - B[d.getFirst()] >= K) {
                res = Math.min(res, i - d.pollFirst());
            }
            while (d.size() > 0 && B[i] <= B[d.getLast()]) {
                d.pollLast();
            }
            d.addLast(i);
        }
        return res <= N ? res : -1;
    }
}

# TreeMap
#7.68% 150ms
class Solution {
    public int shortestSubarray(int[] A, int K) {
        if (A.length == 0) return -1;
        TreeMap<Long, Integer> tree = new TreeMap<>();
        long total = 0;
        int minLen = Integer.MAX_VALUE;
        for (int i = 0; i < A.length; i++) {
            total += A[i];
            Long num = tree.floorKey(total-K);
            if (total >= K) {
                if (i+1 < minLen) {
                    minLen = i+1;
                }
            }
            while (num != null) {
                if (i-tree.get(num) < minLen) {
                    minLen = i-tree.get(num);
                }
                tree.remove(num);
                num = tree.lowerKey(num);
            }
            tree.put(total, i);
        }
        return minLen == Integer.MAX_VALUE ? -1 : minLen;
    }
}
'''