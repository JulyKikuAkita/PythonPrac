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

# No stack:
# 289ms 11.94%
class Solution {
    public int sumSubarrayMins(int[] A) {
        long modulo = (long) (Math.pow(10, 9) + 7);
        long sumOfMin = 0;
        for (int i = 0; i < A.length; i++) {
            int left = i - 1;
            int right = i + 1;
            while (left >= 0 && A[i] <= A[left]) left--;
            while (right < A.length && A[i] < A[right]) right++;
            sumOfMin += (i - left) * (right - i) * A[i]; 
        }
        return (int) (sumOfMin % modulo);
    }
}
# https://leetcode.com/problems/sum-of-subarray-minimums/discuss/178876/stack-solution-with-very-detailed-explanation-step-by-step
# monotone stack
# 43ms 89.36%
class Solution {
    public int sumSubarrayMins(int[] A) {
        Deque<Integer> stack = new LinkedList<>();
        int[] left = new int[A.length], right = new int[A.length];
        for (int i = 0; i < A.length; i++) left[i] = i + 1;
        for (int i = 0; i < A.length; i++) right[i] = A.length - i;
        for (int i = 0; i < A.length; i++) {
            while (!stack.isEmpty() && A[stack.peekFirst()] > A[i]) stack.pollFirst();
            left[i] = stack.isEmpty() ? i + 1: i - stack.peekFirst();
            stack.offerFirst(i);
        }
        stack = new LinkedList();
        for (int i = 0; i < A.length; i++) {
            while (!stack.isEmpty() && A[stack.peekFirst()] > A[i]) {
                right[stack.peekFirst()] = i - stack.peekFirst();
                stack.pollFirst();
            }
            stack.offerFirst(i);
        }
        
        int ans = 0;
        int mod = (int) 1e9 + 7;
        for (int i = 0; i < A.length; i++) {
            ans = (ans + left[i] * right[i] * A[i]) % mod;
        }
        return ans;
    }
}

# https://leetcode.com/problems/sum-of-subarray-minimums/discuss/170750/C%2B%2BJavaPython-Stack-Solution
class Solution {
    public int sumSubarrayMins(int[] A) {
        Stack<Integer> s = new Stack<>();
        int n = A.length, res = 0, mod = (int)1e9 + 7, j,k;
        for (int i = 0; i <= n; i++) {
            while (!s.isEmpty() && A[s.peek()] > (i == n ? 0: A[i])) {
                j = s.pop();
                k = s.isEmpty() ? -1 : s.peek();
                res = (res + A[j] * (i - j) * (j - k)) % mod;
            }
            s.push(i);
        }
        return res;
    }
}
'''
