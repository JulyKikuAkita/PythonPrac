__source__ = 'https://leetcode.com/problems/maximum-sum-circular-subarray/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 918. Maximum Sum Circular Subarray
#
# Given a circular array C of integers represented by A,
# find the maximum possible sum of a non-empty subarray of C.
#
# Here, a circular array means the end of the array connects to the beginning of the array.
# (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)
#
# Also, a subarray may only include each element of the fixed buffer A at most once.
# (Formally, for a subarray C[i], C[i+1], ..., C[j],
# there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)
#
#
#
# Example 1:
#
# Input: [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3
#
# Example 2:
#
# Input: [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
#
# Example 3:
#
# Input: [3,-1,2,-1]
# Output: 4
# Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
#
# Example 4:
#
# Input: [3,-2,2,-3]
# Output: 3
# Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
#
# Example 5:
#
# Input: [-2,-3,-1]
# Output: -1
# Explanation: Subarray [-1] has maximum sum -1
#
# Note:
#     -30000 <= A[i] <= 30000
#     1 <= A.length <= 30000
#
import unittest

# 224ms 29.94%
class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def kadane(gen):
            # Maximum non-empty subarray sum
            ans = cur = None
            for x in gen:
                cur = x + max(cur, 0)
                ans = max(ans, cur)
            return ans

        S = sum(A)
        ans1 = kadane(iter(A))
        ans2 = S + kadane(-A[i] for i in xrange(1, len(A)))
        ans3 = S + kadane(-A[i] for i in xrange(len(A) - 1))
        return max(ans1, ans2, ans3)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/maximum-sum-circular-subarray/solution/
#
Kadane's algorithm is given by the following psuedocode:
# Kadane's algorithm
# ans = cur = None
# for x in A:
#     cur = x + max(cur, 0)
#     ans = max(ans, cur)
# return ans

# 11ms 85.21%
Approach 1: Next Array
Complexity Analysis
Time Complexity: O(N), where N is the length of A.
Space Complexity: O(N)

class Solution {
    public int maxSubarraySumCircular(int[] A) {
        int N = A.length;
        int ans = A[0], cur = A[0];
        for (int i = 1; i < N; i++) {
            cur = A[i] + Math.max(cur, 0);
            ans = Math.max(ans, cur);
            
        }
        
        // ans is the answer for 1-interval subarrays.
        // Now, let's consider all 2-interval subarrays.
        // For each i, we want to know
        // the maximum of sum(A[j:]) with j >= i+2

        // rightsums[i] = A[i] + A[i+1] + ... + A[N-1]
        int[] rightsums = new int[N];
        rightsums[N-1] = A[N-1];
        for (int i = N - 2; i >= 0; i--) {
            rightsums[i] = rightsums[i + 1] + A[i];
        }
        
        // maxright[i] = max_{j >= i} rightsums[j]
        int[] maxright = new int[N];
        maxright[N-1] = A[N-1];
        for (int i = N - 2; i >= 0; i--) {
            maxright[i] = Math.max(maxright[i + 1], rightsums[i]);
        }
        
        int leftsum = 0;
        for (int i = 0; i < N-2; ++i) {
            leftsum += A[i];
            ans = Math.max(ans, leftsum + maxright[i+2]);
        }

        return ans;
    }
}

Approach 2: Prefix Sums + Monoqueue
Complexity Analysis
Time Complexity: O(N), where N is the length of A.
Space Complexity: O(N)

# 59ms 6.81%
class Solution {
    public int maxSubarraySumCircular(int[] A) {
        int N = A.length;
        
        // Compute P[j] = B[0] + B[1] + ... + B[j-1]
        // for fixed array B = A+A
        int[] P = new int[2*N+1];
        for (int i = 0; i < 2*N; ++i)
            P[i + 1] = P[i] + A[i % N];
        
        // Want largest P[j] - P[i] with 1 <= j-i <= N
        // For each j, want smallest P[i] with i >= j-N
        int ans = A[0];
        // deque: i's, increasing by P[i]
        Deque<Integer> deque = new ArrayDeque();
        deque.offer(0);
        
        for (int j = 1; j <= 2 *N; ++j) {
            // If the smallest i is too small, remove it.
            if (deque.peekFirst() < j-N) deque.pollFirst();
            
            // The optimal i is deque[0], for cand. answer P[j] - P[i].
            ans = Math.max(ans, P[j] - P[deque.peekFirst()]);
            
            // Remove any i1's with P[i2] <= P[i1].
            while (!deque.isEmpty() && P[j] <= P[deque.peekLast()])
                deque.pollLast();
            
            deque.offerLast(j);
        }
        return ans;           
    }
}

Approach 3: Kadane's (Sign Variant)
Complexity Analysis
Time Complexity: O(N), where N is the length of A.
Space Complexity: O(1) in additional space complexity. 

For two-interval subarrays, let B be the array A with each element multiplied by -1 
Then the answer for two-interval subarrays is sum(A) + kadane(B)
Except, this isn't quite true, as if the subarray of B we choose is the entire array,
the resulting two interval subarray [[0,i] + [j,N - 1] would be empty
We can remedy this problem by doing Kadane twice: 
once on B with the first element removed, and once on B with the last element removed.

# 10ms 94.94%
class Solution {
    public int maxSubarraySumCircular(int[] A) {
        int S = 0;  // S = sum(A)
        for (int x: A) S += x;
        
        int ans1 = kadane(A, 0, A.length - 1, 1);
        int ans2 = S + kadane(A, 1, A.length - 1, -1);
        int ans3 = S + kadane(A, 0, A.length - 2, -1);
        return Math.max(ans1, Math.max(ans2, ans3));
    }
    
    private int kadane(int[] A, int i, int j, int sign) {
         // The maximum non-empty subarray for array
        // [sign * A[i], sign * A[i+1], ..., sign * A[j]]
        int ans = Integer.MIN_VALUE;
        int cur = Integer.MIN_VALUE;
        for (int k = i; k <= j; k++) {
            cur = sign * A[k] + Math.max(cur, 0);
            ans = Math.max(ans, cur);
        }
        return ans;
    }
}

Approach 4: Kadane's (Min Variant)
Complexity Analysis
Time Complexity: O(N), where N is the length of A.
Space Complexity: O(1) in additional space complexity. 

# 19ms 25.29%
class Solution {
    public int maxSubarraySumCircular(int[] A) {
        // S: sum of A
        int S = 0;
        for (int x: A) S += x;
        
        // ans1: answer for one-interval subarray
        int ans1 = Integer.MIN_VALUE;
        int cur = Integer.MIN_VALUE;
        for (int x: A) {
            cur = x + Math.max(cur, 0);
            ans1 = Math.max(cur, ans1);
        }
        
        // ans2: answer for two-interval subarray, interior in A[1:]
        int ans2 = Integer.MAX_VALUE;
        cur = Integer.MAX_VALUE;
        for (int i = 1; i < A.length; i++) {
            cur = A[i] + Math.min(cur, 0);
            ans2 = Math.min(ans2, cur);
        }
        ans2 = S - ans2;
        
       // ans3: answer for two-interval subarray, interior in A[:-1]
        int ans3 = Integer.MAX_VALUE;
        cur = Integer.MAX_VALUE;
        for (int i = 0; i < A.length - 1; ++i) {
            cur = A[i] + Math.min(cur, 0);
            ans3 = Math.min(ans3, cur);
        }
        return Math.max(ans1, Math.max(ans2, ans3));
    }
}

# 8ms 99.61%
class Solution {
    public int maxSubarraySumCircular(int[] A) {
        if (A == null || A.length == 0) return 0;
        int n = A.length;
        int minSum = 0;
        int maxSum = 0;
        int sum = 0;
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        for (int i = 0; i< n ; i++) {
            sum += A[i];
            minSum += A[i];
            maxSum += A[i];
            if (minSum < min) min = minSum;
            if (maxSum > max) max = maxSum;
            if (minSum > 0) minSum = 0;
            if (maxSum < 0) maxSum = 0;
        }
        if (max < 0) return max;
        return Math.max(max, sum - min);  
    }
} 

'''
