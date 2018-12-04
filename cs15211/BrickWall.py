__source__ = 'https://leetcode.com/problems/brick-wall/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/brick-wall.py
# Time:  O(n), n is the total number of the bricks
# Space: O(m), m is the total number different widths
#
# Description: Leetcode # 554. Brick Wall
#
# There is a brick wall in front of you. The wall is rectangular and has several rows of bricks.
# The bricks have the same height but different width. You want to draw a vertical line from
# the top to the bottom and cross the least bricks.
#
# The brick wall is represented by a list of rows. Each row is a list of integers representing the
# width of each brick in this row from left to right.
#
# If your line go through the edge of a brick, then the brick is not considered as crossed.
# You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.
#
# You cannot draw a line just along one of the two vertical edges of the wall,
# in which case the line will obviously cross no bricks.
#
# Example:
# Input:
# [[1,2,2,1],
#  [3,1,2],
#  [1,3,2],
#  [2,4],
#  [3,1,2],
#  [1,3,1,1]]
# Output: 2
#
# Note:
# The width sum of bricks in different rows are the same and won't exceed INT_MAX.
# The number of bricks in each row is in range [1,10,000].
# The height of wall is in range [1,10,000].
# Total number of bricks of the wall won't exceed 20,000.
#
# Companies
# Facebook
# Related Topics
# Hash Table
#
import unittest
import collections

# 52ms 54.86%
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        widths = collections.defaultdict(int)
        result = len(wall)
        for row in wall:
            width = 0
            for i in xrange(len(row)-1):
                width += row[i]
                widths[width] += 1
                result = min(result, len(wall) - widths[width]);
        return result

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/brick-wall/solution/

# 28ms 37.38%
public class Solution {
    public int leastBricks(List<List<Integer>> wall) {
        if(wall.size() == 0) return 0;
        int count = 0;
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(List<Integer> list : wall){
            int length = 0;
            for(int i = 0; i < list.size() - 1; i++){
                length += list.get(i);
                map.put(length, map.getOrDefault(length, 0) + 1);
                count = Math.max(count, map.get(length));
            }
        }
        return wall.size() - count;
    }
}

#16ms 97.98%
public class Solution {
    public int leastBricks(List<List<Integer>> wall) {
        if (wall == null || wall.size() == 0 || wall.get(0).size() == 0) {
            return 0;
        }

        HashMap<Integer, Integer> map = new HashMap<>();
        int max = 0;
        for (List<Integer> row: wall) {
            int pos = 0;
            for (int i = 0; i < row.size() - 1; i++) {
                pos += row.get(i);
                if (!map.containsKey(pos)) {
                    map.put(pos, 1);
                    if (max == 0) {
                        max = 1;
                    }
                } else {
                    int val = map.get(pos);
                    map.put(pos, val + 1);
                    max = Math.max(val + 1, max);
                }
            }
        }

      //  System.out.println(max);
        return wall.size() - max;
    }
}
'''