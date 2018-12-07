__source__ = 'https://leetcode.com/problems/construct-the-rectangle/#/description'
# Time:  O()
# Space: O()
#
# Description: 492. Construct the Rectangle
#
# 1. The area of the rectangular web page you designed must equal to the given target area.
# 2. The width W should not be larger than the length L, which means L >= W.
#
# 3. The difference between length L and width W should be as small as possible.
# You need to output the length L and the width W of the web page you designed in sequence.
# Example:
# Input: 4
# Output: [2, 2]
# Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1].
# But according to requirement 2, [1,4] is illegal; according to requirement 3,
# [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.
# Note:
# The given area won't exceed 10,000,000 and is a positive integer
# The web page's width and length you designed must be positive integers.

import math
import unittest
# 20ms 100%
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        mid = int(math.sqrt(area))
        while mid > 0:
            if area % mid == 0:
                return [int(area / mid), int(mid)]
            mid -= 1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 2ms 100%
class Solution {
    public int[] constructRectangle(int area) {
        int w = (int)Math.sqrt(area);
	    while (area%w!=0) w--;
	    return new int[]{area/w, w};
    }
}

# 2ms 100%
class Solution {
    public int[] constructRectangle1(int area) {
        int w = (int)Math.sqrt(area);
	    while (area%w!=0) w--;
	    return new int[]{area/w, w};
    }

    public int[] constructRectangle(int area) {
        int[] result = new int[2];
        if(area == 0){
            return result;
        }
        int a = (int)Math.sqrt(area);
        while(area%a != 0){
            a--;
        }
        int b = area/a;
        result[0] = b;
        result[1] = a;
        return result;
    }
}
'''