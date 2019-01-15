__source__ = 'https://leetcode.com/problems/sum-of-subarray-minimums/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 907. Sum of Subarray Minimums
#
# Given an array of integers A, find the sum of min(B),
# where B ranges over every (contiguous) subarray of A.
#
# Since the answer may be large, return the answer modulo 10^9 + 7.
#
# Example 1:
#
# Input: [3,1,2,4]
# Output: 17
# Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
#
#
# Note:
#
# 1 <= A.length <= 30000
# 1 <= A[i] <= 30000
#
import unittest

# 132ms 91.43%
class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7

        stack = []
        ans = dot = 0
        for j, y in enumerate(A):
            # Add all answers for subarrays [i, j], i <= j
            count = 1
            while stack and stack[-1][0] >= y:
                x, c = stack.pop()
                count += c
                dot -= x * c

            stack.append((y, count))
            dot += y * count
            ans += dot
        return ans % MOD

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/sum-of-subarray-minimums/solution/
#
Approach 1: Prev/Next Array
Complexity Analysis
Time Complexity: O(N), where N is the length of A.
Space Complexity: O(N) 

# 157ms 18.99%
class Solution {
    public int sumSubarrayMins(int[] A) {
        int MOD = 1_000_000_007;
        int N = A.length;

        // prev has i* - 1 in increasing order of A[i* - 1]
        // where i* is the answer to query j
         Stack<Integer> stack = new Stack();
        int[] prev = new int[N];
        for (int i = 0; i < N; ++i) {
            while (!stack.isEmpty() && A[i] <= A[stack.peek()]) stack.pop();
            prev[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(i);
        }
        
         // next has k* + 1 in increasing order of A[k* + 1]
        // where k* is the answer to query j
        stack = new Stack();
        int[] next = new int[N];
        for (int k = N - 1; k >= 0; k--) {
            while (!stack.isEmpty() && A[k] < A[stack.peek()]) stack.pop();
            next[k] = stack.isEmpty() ? N : stack.peek();
            stack.push(k);
        }
        
        // Use prev/next array to count answer
        long ans = 0;
        for (int i = 0; i < N; ++i) {
            ans += (i - prev[i]) * (next[i] - i) % MOD * A[i] % MOD;
            ans %= MOD;
        }
        return (int) ans;
    }
}

Approach 2: Maintain Stack of Minimums
Complexity Analysis
Time Complexity: O(N), where N is the length of A.
Space Complexity: O(N)
    
# 77ms 75.98%
class Solution {
    public int sumSubarrayMins(int[] A) {
        int MOD = 1_000_000_007;

        Stack<RepInteger> stack = new Stack();
        int ans = 0, dot = 0;
        for (int j = 0; j < A.length; ++j) {
            // Add all answers for subarrays [i, j], i <= j
            int count = 1;
            while (!stack.isEmpty() && stack.peek().val >= A[j]) {
                RepInteger node = stack.pop();
                count += node.count;
                dot -= node.val * node.count;
            }
            stack.push(new RepInteger(A[j], count));
            dot += A[j] * count;
            ans += dot;
            ans %= MOD;
        }
        return ans;
    }
}

class RepInteger {
    int val, count;
    RepInteger(int v, int c) {
        val = v;
        count = c;
    }
}    
    
# 22ms 92.43%
class Solution {
    public int sumSubarrayMins(int[] A) {
        int MOD = 1_000_000_007;
        int N = A.length;
        long res = 0;
        
        int[] front = new int[N];
        for (int i = 0; i < N; i++) {
            int last = i - 1;
            while (last >= 0 && A[last] >= A[i])
                last = front[last];
            front[i] = last;
        }
        
        int[] tail = new int[A.length];
        for (int i = N - 1; i >= 0; i--) {
            int last = i + 1;
            while (last < N && A[last] > A[i])
                last = tail[last];
            tail[i] = last;
        }
    
        
        for (int i = 0; i < N; i++) {
            res = (res + A[i] * (tail[i] - i) * (i - front[i])) % MOD;
        }
        
        return (int) res;
    }
}
'''
