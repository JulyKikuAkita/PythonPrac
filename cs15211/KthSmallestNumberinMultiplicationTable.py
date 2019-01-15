__source__ = 'https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 668. Kth Smallest Number in Multiplication Table
#
# Nearly every one have used the Multiplication Table.
# But could you find out the k-th smallest number quickly from the multiplication table?
#
# Given the height m and the length n of a m * n Multiplication Table,
# and a positive integer k, you need to return the k-th smallest number in this table.
#
# Example 1:
# Input: m = 3, n = 3, k = 5
# Output:
# Explanation:
# The Multiplication Table:
# 1	2	3
# 2	4	6
# 3	6	9
#
# The 5-th smallest number is 3 (1, 2, 2, 3, 3).
# Example 2:
# Input: m = 2, n = 3, k = 6
# Output:
# Explanation:
# The Multiplication Table:
# 1	2	3
# 2	4	6
#
# The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
# Note:
# The m and n will be in the range [1, 30000].
# The k will be in the range [1, m * n]
#
import unittest
# 532ms 78.12%
class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def enough(x):
            count = 0
            for i in xrange(1, m+1):
                count += min(x // i, n)
            return count >= k

        lo, hi = 1, m * n
        while lo < hi:
            mi = (lo + hi) / 2
            if not enough(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/solution/

Approach #1: Brute Force [Memory Limit Exceeded]
Complexity Analysis
Time Complexity: O(m*n) to create the table, and O(m*nlog(m*n)) to sort it.
Space Complexity: O(m*n) to store the table.
# Memory Limit Exceeded
# Last executed input:
# 9895
# 28405
# 100787757
class Solution {
    public int findKthNumber(int m, int n, int k) {
        int[] table = new int[m*n];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                table[(i - 1) * n + j - 1] = i * j;
            }
        }
        Arrays.sort(table);
        return table[k-1];
    }
}

Approach #2: Next Heap [Time Limit Exceeded]
Complexity Analysis
Time Complexity: O(k*mlogm)=O(m^2 nlogm).
Our initial heapify operation is O(m).
Afterwards, each pop and push is O(mlogm), and our outer loop is O(k) = O(m*n)O(k)=O(m*n)
Space Complexity: O(m). Our heap is implemented as an array with mm elements.
# TLE
# 9895
# 28405
# 100787757
class Solution {
    public int findKthNumber(int m, int n, int k) {
        PriorityQueue<Node> heap = new PriorityQueue<Node>(m,
            Comparator.<Node> comparingInt(node -> node.val));

        for (int i = 1; i <= m; i++) {
            heap.offer(new Node(i, i));
        }

        Node node = null;
        for (int i = 0; i < k; i++) {
            node = heap.poll();
            int nxt = node.val + node.root;
            if (nxt <= node.root * n) {
                heap.offer(new Node(nxt, node.root));
            }
        }
        return node.val;
    }
}

class Node {
    int val;
    int root;
    public Node(int v, int r) {
        val = v;
        root = r;
    }
}

Approach #3: Binary Search [Accepted]
Complexity Analysis
Time Complexity: O(m*log(m*n)). Our binary search divides the interval [lo, hi] into half at each step.
At each step, we call enough which requires O(m)O(m) time.
Space Complexity: O(1). We only keep integers in memory during our intermediate calculations
# 19ms 34.94%
class Solution {
    public boolean enough(int x, int m, int n, int k) {
        int count = 0;
        for (int i = 1; i <= m; i++) {
            count += Math.min(x / i, n);
        }
        return count >= k;
    }

    public int findKthNumber(int m, int n, int k) {
        int lo = 1, hi = m * n;
        while (lo < hi) {
            int mi = lo + (hi - lo) / 2;
            if (!enough(mi, m, n, k)) lo = mi + 1;
            else hi = mi;
        }
        return lo;
    }
}

# 10ms 99.60%
class Solution {
    public int findKthNumber(int m, int n, int k) {
        int l = 1, r = m * n;
        while (l < r) {
            int mid = l + (r - l) / 2;
            int c = count(m, n ,mid);
            if (c < k) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return l;
    }

    private int count (int m, int n, int target) {
        int i = 1, j = n, count = 0;
        while (j >= 1 && i <= m) {
            if (target >= i * j) {
                count += j;
                i++;
            } else {
                j--;
            }
        }
        return count;
    }
}
'''