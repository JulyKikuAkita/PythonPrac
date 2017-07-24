__source__ = 'https://leetcode.com/problems/largest-rectangle-in-histogram/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/largest-rectangle-in-histogram.py
# Time:  O(n)
# Space: O(n)
#
# Description: Leetcode # 84. Largest Rectangle in Histogram
#
# Given n non-negative integers representing the histogram's bar
# height where the width of each bar is 1,
# find the area of largest rectangle in the histogram.
#
# For example,
# Given height = [2,1,5,6,2,3],
# return 10.
#
# Related Topics
# Array Stack
# Similar Questions
# Maximal Rectangle
#
import unittest
class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        increasing, area, i = [], 0, 0
        while i <= len(height):
            if not increasing or ( i < len(height) and height[i] > height[increasing[-1]]):
                increasing.append(i)
                i += 1
            else:
                last = increasing.pop()
                if not increasing: # if increasing is empty
                    area = max(area, i * height[last])
                    #print "at if: ",i, height[last], area
                else:
                    area = max(area, height[last] * (i - increasing[-1] - 1))
                    #print "at else :" ,area
        return area

# http://www.cnblogs.com/zuoyuan/p/3783993.html
class Solution2:
    # @param height, a list of integer
    # @return an integer
    # http://chaoren.is-programmer.com/posts/42674.html
    def largestRectangleArea(self, height):
        stack = []
        i = 0
        maxArea = 0
        h = height + [0]
        h_length = len(h)

        while i < h_length:
            # if stack is empty or h[stack[-1]] <= h[i]
            if (not stack) or h[stack[-1]] <= h[i]:
                stack.append(i)
                i += 1
            else:
                t = stack.pop()
                maxArea = max(maxArea, h[t] * (i if not stack else i - stack[-1] -1))
        return maxArea

    # O(n^2)
    def largestRectangleAreaNSquare(self, height):
        maxArea = 0
        for i in range(len(height)):
            min = height[i]
            for j in range(i, len(height)):
                if height[j] < min:
                    min = height[j]
                if min * (j-i+1) > maxArea:
                    maxArea = min * (j-i+1)
        return maxArea

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        rec1 = [2, 0, 2]
        rec2 = [2, 1, 5, 6, 2, 3]
        rec3 = [1, 2, 3, 1]
        #print Solution().largestRectangleArea(rec1)
        #print Solution().largestRectangleArea(rec2)
        print Solution().largestRectangleArea(rec3)

if __name__ == '__main__':
    unittest.main()

Java = '''
Thought: http://www.geeksforgeeks.org/largest-rectangle-under-histogram/
https://leetcode.com/problems/largest-rectangle-in-histogram/#/solution
# with segment tree: http://www.geeksforgeeks.org/largest-rectangular-area-in-a-histogram-set-1/

# 65.83% 22ms
# O(n)
public class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack<Integer> stack = new Stack<>();
        int len = heights.length;
        int result = 0;
        for (int i = 0; i < len; i++) {
            while (!stack.isEmpty() && heights[stack.peek()] > heights[i]) {
                int peak = stack.pop();
                result = Math.max(result, heights[peak] * (stack.isEmpty() ? i : i - stack.peek() - 1));
            }
            stack.push(i);
        }
        while (!stack.isEmpty()) {
            int peak = stack.pop();
            result = Math.max(result, heights[peak] * (stack.isEmpty() ? len : len - stack.peek() - 1));
        }
        return result;
    }
}

#16.69% 29ms
public class Solution {
    public int largestRectangleArea(int[] height) {
        int len = height.length;
        Stack<Integer> s = new Stack<Integer>();
        int maxArea = 0;
        for(int i = 0; i <= len; i++){
            int h = (i == len ? 0 : height[i]);
            if(s.isEmpty() || h >= height[s.peek()]){
                s.push(i);
            }else{
                int tp = s.pop();
                maxArea = Math.max(maxArea, height[tp] * (s.isEmpty() ? i : i - 1 - s.peek()));
                i--;
            }
        }
        return maxArea;
    }
}

# Thought: https://discuss.leetcode.com/topic/39151/5ms-o-n-java-solution-explained-beats-96
# 90.38% 4ms
public static int largestRectangleArea(int[] height) {
    if (height == null || height.length == 0) {
        return 0;
    }
    int[] lessFromLeft = new int[height.length]; // idx of the first bar the left that is lower than current
    int[] lessFromRight = new int[height.length]; // idx of the first bar the right that is lower than current
    lessFromRight[height.length - 1] = height.length;
    lessFromLeft[0] = -1;

    for (int i = 1; i < height.length; i++) {
        int p = i - 1;

        while (p >= 0 && height[p] >= height[i]) {
            p = lessFromLeft[p];
        }
        lessFromLeft[i] = p;
    }

    for (int i = height.length - 2; i >= 0; i--) {
        int p = i + 1;

        while (p < height.length && height[p] >= height[i]) {
            p = lessFromRight[p];
        }
        lessFromRight[i] = p;
    }

    int maxArea = 0;
    for (int i = 0; i < height.length; i++) {
        maxArea = Math.max(maxArea, height[i] * (lessFromRight[i] - lessFromLeft[i] - 1));
    }

    return maxArea;
}

//divide and conquer
# 98.88% 2ms
public class Solution {
    //int max=0;
    public int largestRectangleArea(int[] heights) {
        if(heights==null|heights.length==0) return 0;
        return divide(heights,0,heights.length-1);
        //return max;
    }
    public int divide(int[] heights,int start,int end){
        if(start>end) return 0;
        if(start==end) return heights[start];
        boolean sorted=true;
        int min=start;
        //int max=0;
        for(int i=start+1;i<=end;i++){
            if(heights[i]<heights[i-1]) sorted=false;
            if(heights[i]<heights[min]) min=i;
        }
        if(sorted){
            int max=0;
            for(int i=start;i<=end;i++){
                max=Math.max(max,heights[i]*(end-i+1));
            }
            return max;
        }
        int l=divide(heights,start,min-1);
        int r=divide(heights,min+1,end);
        int res=Math.max(l,r);
        res=Math.max(res,heights[min]*(end-start+1));
        return res;
    }
}
'''