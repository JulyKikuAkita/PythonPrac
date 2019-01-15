__source__ = 'https://leetcode.com/problems/minimum-increment-to-make-array-unique/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 945. Minimum Increment to Make Array Unique
#
# Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.
#
# Return the least number of moves to make every value in A unique.
#
# Example 1:
#
# Input: [1,2,2]
# Output: 1
# Explanation:  After 1 move, the array could be [1, 2, 3].
#
# Example 2:
#
# Input: [3,2,1,2,1,7]
# Output: 6
# Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
# It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
#
# Note:
#
#     0 <= A.length <= 40000
#     0 <= A[i] < 40000
#
import unittest
# 224ms 23.83%
class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        A.append(100000)
        ans = taken = 0

        for i in xrange(1, len(A)):
            if A[i-1] == A[i]:
                taken += 1
                ans -= A[i]
            else:
                give = min(taken, A[i] - A[i-1] - 1)
                ans += give * (give + 1) / 2 + give * A[i-1]
                taken -= give
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/minimum-increment-to-make-array-unique/solution/
#
Approach 1: Counting
Complexity Analysis
Time Complexity: O(N), where N is the length of A.
Space Complexity: O(N)
# 15ms 82.08%
class Solution {
    public int minIncrementForUnique(int[] A) {
        int[] count = new int[100000];
        for (int x: A) count[x]++;

        int ans = 0, taken = 0;

        for (int x = 0; x < 100000; ++x) {
            if (count[x] >= 2) {
                taken += count[x] - 1;
                ans -= x * (count[x] - 1);
            }
            else if (taken > 0 && count[x] == 0) {
                taken--;
                ans += x;
            }
        }

        return ans;
    }
}

Approach 2: Maintain Duplicate Info
Complexity Analysis
Time Complexity: O(NLogN), where N is the length of A.
Space Complexity: O(N) in additional space complexity, 
depending on the specific implementation of the built in sort.

# 39ms 32.21%
class Solution {
    public int minIncrementForUnique(int[] A) {
        Arrays.sort(A);
        int ans = 0, taken = 0;

        for (int i = 1; i < A.length; ++i) {
            if (A[i-1] == A[i]) {
                taken++;
                ans -= A[i];
            } else {
                int give = Math.min(taken, A[i] - A[i-1] - 1);
                ans += give * (give + 1) / 2 + give * A[i-1];
                taken -= give;
            }
        }

        if (A.length > 0)
            ans += taken * (taken + 1) / 2 + taken * A[A.length - 1];

        return ans;
    }
}

# 12s 85.84%
class Solution {
    public int minIncrementForUnique(int[] A) {
        int[] count = new int[40002];
        int result = 0;
        int max = 0;
        for (int a : A) {
            count[a]++;
            max = Math.max(max, a);
        }
        
        for (int i = 0; i < max; i++) {
            if (count[i] <= 1) continue;
            int diff = count[i] - 1;
            result += diff;
            count[i+1] += diff;
            count[i] = 1;
        }
        int diff = count[max] - 1;
        result += (1 + diff) * diff / 2;
        return result;
    }
}
'''
