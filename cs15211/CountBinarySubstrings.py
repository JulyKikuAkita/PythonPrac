__source__ = 'https://leetcode.com/problems/count-binary-substrings/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 696. Count Binary Substrings
#
# Give a string s, count the number of non-empty (contiguous) substrings
# that have the same number of 0's and 1's, and all the 0's and
# all the 1's in these substrings are grouped consecutively.
#
# Substrings that occur multiple times are counted the number of times they occur.
#
# Example 1:
# Input: "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's:
#  "0011", "01", "1100", "10", "0011", and "01".
#
# Notice that some of these substrings repeat and are counted the number of times they occur.
#
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
# Example 2:
# Input: "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
# Note:
#
# s.length will be between 1 and 50,000.
# s will only consist of "0" or "1" characters.
#
import unittest

# 120ms 87.36%
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = map(len, s.replace('01', '0 1').replace('10', '1 0').split())
        return sum(min(a, b) for a, b in zip(s, s[1:]))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/count-binary-substrings/solution/
Approach #1: Group By Character [Accepted]
Complexity Analysis
Time Complexity: O(N), where N is the length of s.
Every loop is through O(N) items with O(1) work inside the for-block.
Space Complexity: O(N), the space used by groups.



Approach #2: Linear Scan [Accepted]
Complexity Analysis
Time Complexity: O(N), where N is the length of s. Every loop is through O(N) items with O(1) work inside the for-block.
Space Complexity: O(1), the space used by prev, cur, and ans.

# 11ms 100%
class Solution {
    public int countBinarySubstrings(String s) {
        int total = 0;
        int count1=0;
        int count2=0;
        char[] chars = s.toCharArray();
        char prev = chars[0];
        for(int i=0;i<chars.length;++i) {
            if (chars[i]!=prev) {
                total++;
                count1 = count2;
                count2 = 1;
                prev = chars[i];
            } else {
                count2++;
                if (count2<=count1) {
                    total++;
                }
            }
        }
        return total;
    }
}
'''