__source__ = 'https://leetcode.com/problems/jump-game-ii/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/jump-game-ii.py
# Time:  O(n^2)
# Space: O(1)
#
# Description: Leetcode # 217. Contains Duplicate
#
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# For example:
# Given array A = [2,3,1,1,4]
#
# The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
#
# Related Topics
# Array Greedy
#
import unittest
class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        jum_count = 0
        dis = 0
        cur_dis = 0
        for i, length in enumerate(A):
            if i > dis:
                return -1
            if i > cur_dis:
                cur_dis = dis
                jum_count += 1
            dis = max(dis, i+length)
        return jum_count

class Solution2:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        result, prev_reachable, reachable = 0, -1, 0
        while reachable > prev_reachable:
            if reachable >= len(A) - 1:
                return result
            result += 1
            prev_reachable = reachable
            for i, length in enumerate(A[:reachable + 1]):
                reachable = max(reachable, i + length)
        return -1

class Solution3:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        count = 0
        jumpdis, min_nextdis = 0, 0

        for i in range(0, len(A)-1):
            min_nextdis = max(min_nextdis, A[i] + i)
            if i == jumpdis:
                jumpdis, count = min_nextdis, count +1
        return count
#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        test = Solution2()
        A1 = [2,3,1,1,4]
        A2 = [3,2,1,0,4]
        #print test.jump(A1)
        #print test.jump(A2)

        print Solution().jump([2,3,1,1,4])
        print Solution().jump([3,2,1,0,4])

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:

The main idea is based on greedy. Let's say the range of the current jump is [curBegin, curEnd],
curFarthest is the farthest point that all points in [curBegin, curEnd] can reach.
Once the current point reaches curEnd, then trigger another jump,
and set the new curEnd with curFarthest,
then keep the above steps, as the following:

# 57.31% 10ms
public class Solution {
    public int jump(int[] nums) {
        if ( nums.length < 2 ) return 0;
        int count = 0;
        int current_max = 0;
        int cur_end = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            current_max = Math.max(current_max, i + nums[i]);
            if (i == cur_end) {
                count++;
                cur_end = current_max;
            }
        }
        return count;
    }
}

#88.27% 9ms
public class Solution {
    public int jump(int[] nums) {
        if (nums == null || nums.length == 0) { return -1;}
        int start = 0, end = 0, jumps = 0;
        while (end < nums.length - 1) {
            jumps ++;
            int farthest = end;
            for (int i = start; i <= end; i++) {
                if (nums[i] + i > farthest) {
                    farthest = nums[i] + i;
                }
            }
            start = end + 1;
            end = farthest;
        }
        return jumps;
    }
}
'''