__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/trapping-rain-water.py
# Time:  O(n)
# Space: O(1)
# Greedy
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
#  Google Twitter Zenefits Amazon Apple Bloomberg
# Hide Tags Array Stack Two Pointers

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
#test = Solution2()
A= [0,1,0,2,1,0,1,3,2,1,2,1]
A2 = [1,2,3,2,2,1]
#print test.trap(A)
if __name__ == '__main__':
    print Solution().trap(A2)
    #print Solution2_github().trap(A)

#java
js = '''
public class Solution {
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
'''