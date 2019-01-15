__source__ = 'https://leetcode.com/problems/range-addition/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/range-addition.py
# Time:  O(k + n)
# Space: O(1)
#
# Description: Leetcode # 370. Range Addition
#
# Assume you have an array of length n initialized with all 0's and are given k update operations.
#
# Each operation is represented as a triplet: [startIndex, endIndex, inc]
# which increments each element of subarray A[startIndex ... endIndex]
# (startIndex and endIndex inclusive) with inc.
#
# Return the modified array after all k operations were executed.
#
# Example:
#
# Given:
#
#     length = 5,
#     updates = [
#         [1,  3,  2],
#         [2,  4,  3],
#         [0,  2, -2]
#     ]
#
# Output:
#
#     [-2, 0, 3, 5, 3]
# Explanation:
#
# Initial state:
# [ 0, 0, 0, 0, 0 ]
#
# After applying operation [1, 3, 2]:
# [ 0, 2, 2, 2, 0 ]
#
# After applying operation [2, 4, 3]:
# [ 0, 2, 5, 5, 3 ]
#
# After applying operation [0, 2, -2]:
# [-2, 0, 3, 5, 3 ]
#
# Companies
# Google
# Related Topics
# Array
# Similar Questions
# Range Addition II
#
import unittest
class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        result = [0] * length
        for update in updates:
            result[update[0]] += update[2]
            if update[1]+1 < length:
                result[update[1]+1] -= update[2]

        for i in xrange(1, length):
            result[i] += result[i-1]
        return result

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/range-addition/solution/

# 2ms 59/22%
class Solution {
    public int[] getModifiedArray(int length, int[][] updates) {
        int[] result = new int[length];
        for (int[] update : updates) {
            result[update[0]] += update[2];
            if (update[1] < length - 1) {
                result[update[1] + 1] -= update[2];
            }
        }
        for (int i = 1; i < length; i++) {
            result[i] += result[i - 1];
        }
        return result;
    }
}

# 1ms 100%
class Solution {
     public int[] getModifiedArray(int length, int[][] updates) {
        int[] res = new int[length];
         for(int[] update : updates) {
            int value = update[2];
            int start = update[0];
            int end = update[1];
            res[start] += value;
            if (end < length - 1)
                res[end + 1] -= value;
        }

        int sum = 0;
        for(int i = 0; i < length; i++) {
            sum += res[i]; //use sum faster than user res[i] += res[i-1]
            res[i] = sum;
        }

        return res;
    }
}
'''
