__source__ = 'https://leetcode.com/problems/best-meeting-point/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/best-meeting-point.py
# Time:  O(m * n)
# Space: O(m + n)
#
# Description: Leetcode # 296. Best Meeting Point
#
# A group of two or more people wants to meet and minimize the total travel distance.
# You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group.
# The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
#
# For example, given three people living at (0,0), (0,4), and (2,2):
#
# 1 - 0 - 0 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
#
# The point (0,2) is an ideal meeting point, as the total travel distance of 2+2+2=6 is minimal. So return 6.
#
# Companies
# Twitter
# Related Topics
# Math Sort
# Similar Questions
# Shortest Distance from All Buildings Minimum Moves to Equal Array Elements II
#

from random import randint
import unittest
class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x = [i for i, row in enumerate(grid) for v in row if v == 1]
        y = [j for row in grid for j, v in enumerate(row) if v == 1]

        print x, y
        for p, q in enumerate(grid):
            print p,q
        for s in grid:
            for n, k in enumerate(s) :
                print "( n= %s , k = %s)" %(n, k)
                if k == 1:
                    print n, k

        mid_x = self.findKthLargest(x, len(x) / 2 + 1)
        mid_y = self.findKthLargest(y, len(y) / 2 + 1)

        return sum([abs(mid_x-i) + abs(mid_y-j) \
                   for i, row in enumerate(grid) for j, v in enumerate(row) if v == 1])

    def findKthLargest(self, nums, k):
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot_idx = randint(left, right)
            new_pivot_idx = self.PartitionAroundPivot(left, right, pivot_idx, nums)
            if new_pivot_idx == k - 1:
                return nums[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:  # new_pivot_idx < k - 1.
                left = new_pivot_idx + 1

    def PartitionAroundPivot(self, left, right, pivot_idx, nums):
        pivot_value = nums[pivot_idx]
        new_pivot_idx = left
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        for i in xrange(left, right):
            if nums[i] > pivot_value:
                nums[i], nums[new_pivot_idx] =  nums[new_pivot_idx], nums[i]
                new_pivot_idx += 1

        nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
        return new_pivot_idx

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
        print Solution().minTotalDistance(grid)

if __name__ == '__main__':
    unittest.main()

Java = '''
Thought: https://leetcode.com/articles/best-meeting-point/
# 11.59% 20ms
public class Solution {
    public int minTotalDistance(int[][] grid) {
        List<Integer> ipos = new ArrayList<>();
        List<Integer> jpos = new ArrayList<>();

        for(int i = 0; i < grid.length; i++){
            for( int j = 0; j < grid[0].length ; j++){
                if(grid[i][j] == 1){
                    ipos.add(i);
                    jpos.add(j);
                }
            }
        }

        int sum = 0;
        for(Integer pos: ipos) {
            sum += Math.abs(pos - ipos.get(ipos.size() / 2 ) );
        }

        Collections.sort(jpos);
        for(Integer pos:jpos){
            sum += Math.abs(pos - jpos.get(jpos.size() / 2 ));
        }
        return sum;
    }
}

Solution 1
#89.78% 2ms
No need to sort the coordinates if we collect them in sorted order.

public class Solution {
    public int minTotalDistance(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int total = 0, Z[] = new int[m*n];
        for (int dim=0; dim<2; ++dim) {
            int i = 0, j = 0;
            if (dim == 0) {
                for (int x=0; x<n; ++x)
                    for (int y=0; y<m; ++y)
                        if (grid[y][x] == 1)
                            Z[j++] = x;
            } else {
                for (int y=0; y<m; ++y)
                    for (int g : grid[y])
                        if (g == 1)
                            Z[j++] = y;
            }
            while (i < --j)
                total += Z[j] - Z[i++];
        }
        return total;
    }
}

Solution 2
#89.78% 2ms
BucketSort-ish. Count how many people live in each row and each column. Only O(m+n) space.

public class Solution {
    public int minTotalDistance(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[] I = new int[m], J = new int[n];
        for (int i=0; i<m; ++i)
            for (int j=0; j<n; ++j)
                if (grid[i][j] == 1) {
                    ++I[i];
                    ++J[j];
                }
        int total = 0;
        for (int[] K : new int[][]{ I, J }) {
            int i = 0, j = K.length - 1;
            while (i < j) {
                int k = Math.min(K[i], K[j]);
                total += k * (j - i);
                if ((K[i] -= k) == 0) ++i;
                if ((K[j] -= k) == 0) --j;
            }
        }
        return total;
    }
}

#89.78% 2ms
public class Solution {
    public int minTotalDistance(int[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) return 0;
        int m = grid.length, n = grid[0].length;
        int[] row = new int[m];
        int[] col = new int[n];
        int all = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    row[i]++;
                    col[j]++;
                    all++;
                }
            }
        }
        return cal(row, all) + cal(col, all);
    }

    private int cal(int[] nums, int all) {
        int half = (all + 1) / 2;
        int mid = 0, cnt = 0;
        for (; mid < nums.length; mid++) {
            cnt += nums[mid];
            if (cnt >= half) break;
        }
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            res += nums[i] * Math.abs(mid - i);
        }
        return res;
    }
}
'''