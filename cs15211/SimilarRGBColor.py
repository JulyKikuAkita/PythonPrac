__source__ = 'https://leetcode.com/problems/similar-rgb-color/'
# Time:  O(1)
# Space: O(1)
#
# Description: Leetcode # 800. Similar RGB Color
#
# In the following, every capital letter represents some hexadecimal digit from 0 to f.
#
# The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand.
# For example, "#15c" is shorthand for the color "#1155cc".
#
# Now, say the similarity between two colors "#ABCDEF"
# and "#UVWXYZ" is -(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2.
#
# Given the color "#ABCDEF", return a 7 character color that is most similar to #ABCDEF,
# and has a shorthand (that is, it can be represented as some "#XYZ"
#
# Example 1:
# Input: color = "#09f166"
# Output: "#11ee66"
# Explanation:
# The similarity is -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -73.
# This is the highest among any shorthand color.
# Note:
#
# color is a string of length 7.
# color is a valid RGB color: for i > 0, color[i] is a hexadecimal digit from 0 to f
# Any answer which has the same (highest) similarity as the best answer will be accepted.
# All inputs and outputs should use lowercase letters, and the output is 7 characters.
#
import unittest

# 20ms 100%
class Solution:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        return '#' + self.helper(color[1:3]) + self.helper(color[3:5]) + self.helper(color[5:7])

    def helper(self, color):
        maps = '0123456789abcdef'

        if int(color, 16) % 17 > 8:
            index = int(color, 16) // 17 + 1
        else:
            index = int(color, 16) // 17

        return str(maps[index]) * 2

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/similar-rgb-color/solution/
#
# For a color like hex1,
# it has 3 colored components r1 = (hex1 >> 16) % 256, g1 = (hex1 >> 8) % 256, b1 = (hex1 >> 0) % 256.
# Then, the first addend in the similarity is -(r1 - r2) * (r1 - r2), etc.
#
# 6ms 100%
class Solution {
    public String similarRGB(String color) {
        StringBuilder sb = new StringBuilder(color.length());
        sb.append("#");
        for (int i = 1; i < color.length(); i += 2) {
            sb.append(getHexDigits(color.charAt(i), color.charAt(i + 1)));
        }
        return sb.toString();
    }

    private String  getHexDigits(char c1, char c2) {
        int d1 = Character.isDigit(c1) ? c1 - '0': 10 + c1 - 'a';
        int d2 = Character.isDigit(c2) ? c2 - '0': 10 + c2 - 'a';
        int sum = d1 * 16 + d2;
        int index = sum / 17; //[ 0x00(0) , 0x11(17), 0x22(34),  0x33(51), ........., 0xff(255) ]
        int remainder = sum % 17;
        if (remainder > 17 / 2) index++;
        char c = 0 <= index && index <= 9 ? (char)('0' + index) : (char)('a' + index - 10);
        return String.valueOf(c) + String.valueOf(c);
    }
}
'''
