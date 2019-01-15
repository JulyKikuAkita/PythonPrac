__source__ = 'https://leetcode.com/problems/maximum-distance-in-arrays/'
# Time:  O(n)
# Space: O(1)
#
# Description: 624. Maximum Distance in Arrays
#
# Given m arrays, and each array is sorted in ascending order.
# Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance.
# We define the distance between two integers a and b to be their absolute difference |a-b|.
# Your task is to find the maximum distance.
#
# Example 1:
# Input:
# [[1,2,3],
#  [4,5],
#  [1,2,3]]
# Output: 4
# Explanation:
# One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
# Note:
# Each given array will have at least 1 number. There will be at least two non-empty arrays.
# The total number of the integers in all the m arrays will be in the range of [2, 10000].
# The integers in the m arrays will be in the range of [-10000, 10000].
# Hide Company Tags Yahoo
# Hide Tags Array Hash Table
#
import unittest


class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/maximum-distance-in-arrays/solution/

public class Solution {
    public int maxDistance(int[][] arrays) {
		if (arrays == null || arrays.length == 0) return 0;

		int diff = Integer.MIN_VALUE;
		int m = arrays.length;

		int min =  arrays[0][0], max = arrays[0][arrays[0].length-1];
		for (int i = 1; i < m; i++) {
			int head = arrays[i][0];
			int tail = arrays[i][arrays[i].length-1];
			diff = Math.max(Math.abs(max-head), diff);
                        diff = Math.max(Math.abs(tail-min), diff);
			max = Math.max(tail, max);
			min = Math.min(head, min);
		}

		return diff;
    }
}

# update input to List
# 16ms 20.10%
class Solution {
    public int maxDistance(List<List<Integer>> arrays) {
        int result = Integer.MIN_VALUE;
        int max = arrays.get(0).get(arrays.get(0).size() - 1);
        int min = arrays.get(0).get(0);
        
        for (int i = 1; i < arrays.size(); i++) {
            result = Math.max(result, Math.abs(arrays.get(i).get(0) - max));
            result = Math.max(result, Math.abs(arrays.get(i).get(arrays.get(i).size() - 1) - min));
            max = Math.max(max, arrays.get(i).get(arrays.get(i).size() - 1));
            min = Math.min(min, arrays.get(i).get(0));
        }
        
        return result;
    }
}

'''
