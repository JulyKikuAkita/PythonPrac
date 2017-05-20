__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/largest-rectangle-in-histogram.py
# Time:  O(n)
# Space: O(n)
#
# Given n non-negative integers representing the histogram's bar
# height where the width of each bar is 1,
# find the area of largest rectangle in the histogram.
#
# For example,
# Given height = [2,1,5,6,2,3],
# return 10.
#
# Array Stack
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
if __name__ == '__main__':
    rec1 = [2, 0, 2]
    rec2 = [2, 1, 5, 6, 2, 3]
    rec3 = [1, 2, 3, 1]
    #print Solution().largestRectangleArea(rec1)
    #print Solution().largestRectangleArea(rec2)
    print Solution().largestRectangleArea(rec3)


#java
js = '''
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

public class Solution {
    public int largestRectangleArea(int[] heights) {
        if( heights == null ||heights.length == 0) return 0;
        int res = 0;

        int[] record = new int[heights.length + 1];
        for(int i = 0; i < heights.length;i++){
            record[i] = heights[i];
        }
        record[heights.length] = 0;

        Stack<Integer> stack = new Stack<>();
        for(int i = 0; i <record.length; i++){
            if(stack.isEmpty() || record[stack.peek()] <= record[i]){
                stack.push(i);
            }else{
                int h = record[stack.pop()];
                int curArea;
                if(stack.isEmpty()){
                    curArea = h * i;
                }else{
                    curArea = h * (i - stack.peek() - 1);
                }
                res = Math.max(res, curArea);
                i--;
            }
        }
        return res;
    }
}
'''