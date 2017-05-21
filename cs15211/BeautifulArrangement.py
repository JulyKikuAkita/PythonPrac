__source__ = 'https://leetcode.com/problems/beautiful-arrangement/#/description'
# Time complexity : O(k). k refers to the number of valid permutations.
# Space complexity : O(n). visited array of size nn is used.
#
# Description:
# Suppose you have N integers from 1 to N.
# We define a beautiful arrangement as an array that is constructed by these N numbers successfully
# if one of the following is true for the ith position (1 <= i <= N) in this array:
#
# The number at the ith position is divisible by i.
# i is divisible by the number at the ith position.
# Now given N, how many beautiful arrangements can you construct?
#
# Example 1:
# Input: 2
# Output: 2
# Explanation:
#
# The first beautiful arrangement is [1, 2]:
#
# Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
#
# Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
#
# The second beautiful arrangement is [2, 1]:
#
# Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
#
# Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
# Note:
# N is a positive integer and will not exceed 15.
# Hide Company Tags Google
# Hide Tags Backtracking
#
import unittest

class Solution(object):
    cache= {}
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        def helper(i, x):
            if i == 1:
                return 1
            key = (i, x)
            if key in self.cache:
                return self.cache[key]
            total = 0
            for j in xrange(len(x)):
                if x[j] % i == 0 or i % x[j] == 0:
                    total += helper(i - 1, x[:j] + x[j+1:])
            self.cache[key] = total
            return total
        return helper(N, tuple(range(1, N + 1)))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
https://leetcode.com/articles/beautiful-arrangement/
#Thought: Just try every possible number at each position...
1. backtracking template(same as permutation) 35.77%
Time complexity : O(k). k refers to the number of valid permutations.
Space complexity : O(n). visited array of size nn is used.
The depth of recursion tree will also go upto n. Here, nn refers to the given integer n.

public class Solution {
    int count = 0;
    public int countArrangement(int N) {
        if ( N <= 0) return 0;
        backtracking(N, 1, new boolean[N+1]);
        return count;
    }

    public void backtracking(int N, int start, boolean[] used) {
        if (start > N) {
            count++;
            return;
        }

        for (int i = 1; i <= N; i++) {
            if (!used[i] && (i % start == 0 || start % i == 0)) {
                used[i] = true;
                backtracking(N, start + 1, used);
                used[i] = false;
            }
        }
    }
}

2. optimized
Java 6ms beats 98% back tracking (swap) starting from the back
The back tracking start from the back so that each search won't go too deep before it fails
because smaller numbers have higher chance to be divisible among themselves.
Also I don't use "visited" boolean array but use swap of an array of 1~N to avoid duplication.

public class Solution {
    int count = 0;
    public int countArrangement(int N) {
        if ( N <= 0) return 0;
        int[] nums = new int[N+1];
        for (int i = 0; i<= N; i++) {
            nums[i] = i;
        }
        backtracking(N, nums);
        return count;
    }

    public void backtracking(int N, int[] nums) {
        if (N == 0) {
            count++;
            return;
        }

        for (int i = N; i > 0; i--) {
            swap(nums, i, N);
            if (nums[N] % N == 0 || N % nums[N] == 0) {
                backtracking(N - 1, nums);
            }
            swap(nums, i, N);
        }
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
'''