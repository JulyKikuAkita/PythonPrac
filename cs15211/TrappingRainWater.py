__source__ = 'https://leetcode.com/problems/trapping-rain-water/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/trapping-rain-water.py
# Time:  O(n)
# Space: O(1)
# Greedy
#
# Description: Leetcode # 42. Trapping Rain Water
#
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
#  compute how much water it is able to trap after raining.
#
# For example,
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped.
#
# Companies
# Google Twitter Zenefits Amazon Apple Bloomberg
# Related Topics
# Array Stack Two Pointers
# Similar Questions
# Container With Most Water Product of Array Except Self Trapping Rain Water II
#
import unittest
class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        result = 0
        top = 0
        # first highest top
        for i in xrange(len(A)):
            if A[top] < A[i]:
                top = i
        # second highest top
        second_top = 0
        for i in xrange(top):
            if A[second_top] < A[i]:
                second_top = i
            result += A[second_top] - A[i]
        second_top = len(A) - 1
        for i in reversed(xrange(top, len(A))):
            if A[second_top] < A[i]:
                second_top = i
            result += A[second_top] - A[i]
        return result

# Time:  O(n)
# Space: O(n)
class Solution2_github:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        result = 0
        stack = []
        for i in xrange(len(A)):
            mid_height = 0
            while stack:
                [pos, height] = stack.pop()
                result += ( min(height, A[i]) - mid_height) * (i - pos - 1)
                mid_height = height

                if A[i] < height:
                    stack.append([pos, height])
                    break
            stack.append([i, A[i]])
        return result

# http://www.cnblogs.com/zuoyuan/p/3781453.html
class Solution2:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        leftmosthigh = [ 0 for i in range(len(A))]
        leftmax = 0

        for i in range(len(A)):
            if A[i] > leftmax:
                leftmax = A[i]
            leftmosthigh[i] = leftmax

        sum = 0
        rightmax = 0
        for i in reversed(range(len(A))):
            if A[i] > rightmax:
                rightmax = A[i]
            if min(rightmax, leftmosthigh[i]) > A[i]:
                sum += min(rightmax, leftmosthigh[i]) - A[i]
        return sum

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        #test = Solution2()
        A= [0,1,0,2,1,0,1,3,2,1,2,1]
        A2 = [1,2,3,2,2,1]
        #print test.trap(A)
        print Solution().trap(A2)
        #print Solution2_github().trap(A)

if __name__ == '__main__':
    unittest.main()

Java = '''
Thought: https://leetcode.com/problems/trapping-rain-water/solution/

# Two pointers
# 14ms 39.58%
class Solution {
    public int trap(int[] height) {
        if (height == null || height.length == 0) return 0;
        int left = 0, right = height.length - 1;
        int leftMax = 0, rightMax = 0, res = 0;
        while (left < right) {
            leftMax = Math.max(leftMax, height[left]);
            rightMax = Math.max(rightMax, height[right]);
            if (leftMax > rightMax) {
                res += rightMax - height[right];
                right--;
            } else {
                res += leftMax - height[left];
                left++;
            }
        }
        return res;
    }
}

# better naive
# 14ms 39.58%
class Solution {
    public int trap(int[] height) {
        int len = height.length;
        int[] leftMax = new int[len];
        int[] rightMax = new int[len];
        int result = 0;
        for (int i = 1; i < len; i++) {
            leftMax[i] = Math.max(leftMax[i - 1], height[i - 1]);
        }
        for (int i = len - 2; i >= 0; i--) {
            rightMax[i] = Math.max(rightMax[i + 1], height[i + 1]);
        }
        for (int i = 1; i < len - 1; i ++) {
            result += Math.max(0, Math.min(leftMax[i], rightMax[i]) - height[i]);
        }
        return result;
    }
}

# Stack based, important technique
A stack based solution for reference, inspired by Histogram
Indeed this question can be solved in one pass and O(1) space,
but it's probably hard to come up with in a short interview.
If you have read the stack O(n) solution for Largest Rectangle in Histogram,
you will find this solution is very very similar.

The main idea is : if we want to find out how much water on a bar(bot),
we need to find out the left larger bar's index (il), and right larger bar's index(ir),
so that the water is (min(A[il],A[ir])-A[bot])*(ir-il-1), use min since only the lower boundary can hold water,
and we also need to handle the edge case that there is no il.

To implement this we use a stack that store the indices with decreasing bar height,
once we find a bar who's height is larger, then let the top of the stack be bot,
the cur bar is ir, and the previous bar is il.

# 22ms 12.13%
class Solution {
    public int trap(int[] height) {
        if (height == null) return 0;
        Stack<Integer> s = new Stack<Integer>();
        int i = 0, res = 0, maxBotWater = 0;
        while (i < height.length) {
            if (s.isEmpty() || height[i] <= height[s.peek()]) {
                s.push(i++);
            } else {
                int bot = s.pop();
                maxBotWater = s.isEmpty() ? 0 : (Math.min(height[s.peek()], height[i]) - height[bot]) * ( i - s.peek() - 1);
                res += maxBotWater;
            }
        }
        return res;
    }
}

'''