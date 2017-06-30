__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/jump-game.py
# Time:  O(n)
# Space: O(1)
# Greedy
#
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
# For example:
# A = [2,3,1,1,4], return true.
#
# A = [3,2,1,0,4], return false.
#  Microsoft, Amazon
#  Array Greedy

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        reachable = 0
        for i, length in enumerate(A):
            if i > reachable:
                break
            reachable = max(reachable, i + length)
        return reachable >= len(A) - 1

class Solution2:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if len(A) == 0 :
            return False
        jumpdis = A[0]
        for i in range(1, len(A)):
            jumpdis -= 1
            if jumpdis < 0:
                return False
            jumpdis = max(jumpdis, A[i])
        return True

#test
test = Solution2()
A1 = [2,3,1,1,4]
A2 = [3,2,1,0,4]
#print test.canJump(A1)
#print test.canJump(A2)

if __name__ == "__main__":
    print Solution().canJump([2,3,1,1,4])
    print Solution().canJump([3,2,1,0,4])

#java
java = '''
# We can track the maximum length a position can reach.
# The key to solve this problem is to find 2 conditions:
# 1) the position can not reach next step (return false) , and
# 2) the maximum reach the end (return true).

public class Solution {
    public boolean canJump(int[] nums) {
        int end = 0;
        int cur = 0;
        while (cur <= end && end < nums.length) {
            end = Math.max(end, cur + nums[cur]);
            cur++;
        }
        return end >= nums.length - 1;
    }
}

public class Solution {
    public boolean canJump(int[] nums) {
        if (nums.length < 2) return true;

        for(int i = 0, max = 0; i < nums.length && i <= max; i++) {
            max = Math.max(max, i + nums[i]);
            if (max >= nums.length - 1) return true;
        }
        return false;
    }
}
'''