__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/jump-game-ii.py
# Time:  O(n^2)
# Space: O(1)
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
#  Array Greedy

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
test = Solution2()
A1 = [2,3,1,1,4]
A2 = [3,2,1,0,4]
#print test.jump(A1)
#print test.jump(A2)

if __name__ == '__main__':
    print Solution().jump([2,3,1,1,4])
    print Solution().jump([3,2,1,0,4])

#Java
js = '''
The main idea is based on greedy. Let's say the range of the current jump is [curBegin, curEnd],
curFarthest is the farthest point that all points in [curBegin, curEnd] can reach.
Once the current point reaches curEnd, then trigger another jump,
and set the new curEnd with curFarthest,
then keep the above steps, as the following:

public class Solution {
    public int jump(int[] nums) {
        if ( nums.length < 2 ) return 0;
        int count = 0;
        int current_max = 0;
        int cur_end = 0;
        for (int i = 0; i < nums.length -1; i++) { //note:  i < nums.length -1, notworking if set if( cur_end >= nums.length) return count;
            current_max = Math.max(current_max, i + nums[i]);
            if (i == cur_end) {
                count++;
                cur_end = current_max;
            }
        }
        return count;
    }
}

public class Solution {
    public int jump(int[] nums) {
        if ( nums.length < 2) return 0;
        int level = 0, currentMax = 0, moveSteps = 0, nextMax = 0;
        while (currentMax - moveSteps + 1 > 0) {
            level++;
            for (; moveSteps <= currentMax; moveSteps++) {
                nextMax = Math.max(nextMax, moveSteps + nums[moveSteps]);
                if (nextMax >= nums.length - 1) return level;
            }
            currentMax = nextMax;
        }
        return 0;
    }
}
'''