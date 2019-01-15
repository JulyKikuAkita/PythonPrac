__source__ = 'https://leetcode.com/problems/pancake-sorting/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 969. Pancake Sorting
#
# Given an array A, we can perform a pancake flip:
# We choose some positive integer k <= A.length,
# then reverse the order of the first k elements of A.
# We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.
#
# Return the k-values corresponding to a sequence of pancake flips that sort A.
# Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.
#
# Example 1:
#
# Input: [3,2,4,1]
# Output: [4,2,4,3]
# Explanation:
# We perform 4 pancake flips, with k values 4, 2, 4, and 3.
# Starting state: A = [3, 2, 4, 1]
# After 1st flip (k=4): A = [1, 4, 2, 3]
# After 2nd flip (k=2): A = [4, 1, 2, 3]
# After 3rd flip (k=4): A = [3, 2, 1, 4]
# After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted.
# Example 2:
#
# Input: [1,2,3]
# Output: []
# Explanation: The input is already sorted, so there is no need to flip anything.
# Note that other answers, such as [3, 3], would also be accepted.
# Note:
#
# 1 <= A.length <= 100
# A[i] is a permutation of [1, 2, ..., A.length]
#
import unittest

class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans = []

        N = len(A)
        B = sorted(range(1, N+1), key = lambda i: -A[i-1])
        for i in B:
            for f in ans:
                if i <= f:
                    i = f+1 - i
            ans.extend([i, N])
            N -= 1
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/pancake-sorting/solution/
Approach 1: Sort Largest to Smallest
Complexity Analysis
Time Complexity: O(N), where N is the length of A.
Space Complexity: O(N). 
We can place the largest element (in location i, 1-indexed) by flipping i to move the element to the first position, 
then A.length to move it to the last position. 
Afterwards, the largest element is in the correct position, 
so we no longer need to pancake-flip by A.length or more.
# 80ms
class Solution {
    public List<Integer> pancakeSort(int[] A) {
        List<Integer> ans = new ArrayList();
        int N = A.length;

        Integer[] B = new Integer[N];
        for (int i = 0; i < N; ++i)
            B[i] = i+1;
        Arrays.sort(B, (i, j) -> A[j-1] - A[i-1]);

        for (int i: B) {
            for (int f: ans)
                if (i <= f)
                    i = f+1 - i;
            ans.add(i);
            ans.add(N--);
        }

        return ans;
    }
}

# The basic idea is simple: use 2 flip to move the current max number to tail.
# Time Complexity: O(N ^2), where N is the length of A.
# Space Complexity: O(N). 
# 14ms 
class Solution {
    public List<Integer> pancakeSort(int[] A) {
         List<Integer> res = new ArrayList<>();
        for (int i = A.length; i > 1; i--) {
            int idx = findLargest(A, i);
            if (idx == i - 1) continue;
            flip(A, idx + 1); // idx at tail
            flip(A, i);
            res.add(idx + 1);
            res.add(i);
        }
        return res;
    }
    
   private  int findLargest(int[] a, int len) {
        int idx = 0;
        for (int i = 0; i < len ; i++) {
            if (a[i] > a[idx]) idx = i;
        }
        return idx;
    }
    
    private void flip(int[] a, int len) {
        int left = 0, right = len - 1;
        while (left < right) {
            int tmp = a[left];
            a[left] = a[right];
            a[right] = tmp;
            left++;
            right--;
        }
    }
}

# https://leetcode.com/problems/pancake-sorting/discuss/214213/JavaC%2B%2BPython-Straight-Forward
# Time Complexity: O(N ^2), where N is the length of A.
# 13ms
class Solution {
    public List<Integer> pancakeSort(int[] A) {
        List<Integer> res = new ArrayList<>();
        for (int x = A.length, i; x > 0; x--) {
            for (i = 0; A[i] != x; i++);
            reverse(A, i + 1);
            res.add(i + 1);
            reverse(A, x);
            res.add(x);
        }
        return res;
    }
    
    private void reverse(int[] A, int k) {
        for (int i = 0, j = k - 1; i < j; i++, j--) {
            int tmp = A[i];
            A[i] = A[j];
            A[j] = tmp;
        }
    }
}
'''
