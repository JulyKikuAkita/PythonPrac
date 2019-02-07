__source__ = 'https://leetcode.com/problems/string-without-aaa-or-bbb/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 984. String Without AAA or BBB
#
# Given two integers A and B, return any string S such that:
#
# S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
# The substring 'aaa' does not occur in S;
# The substring 'bbb' does not occur in S.
#
#
# Example 1:
#
# Input: A = 1, B = 2
# Output: "abb"
# Explanation: "abb", "bab" and "bba" are all correct answers.
# Example 2:
#
# Input: A = 4, B = 1
# Output: "aabaa"
#
# Note:
#
# 0 <= A <= 100
# 0 <= B <= 100
# It is guaranteed such an S exists for the given A and B.
#
import unittest


class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/string-without-aaa-or-bbb/solution/
# Approach 1: Greedy
# Complexity Analysis
# Time Complexity: O(A+B)
# Space Complexity: O(A+B)
#
# 6ms 40% 
class Solution {
    public String strWithout3a3b(int A, int B) {
        StringBuilder sb = new StringBuilder();
        int size = A + B;
        int a = 0, b = 0;
        for (int i = 0; i < size; i++) {
            if ((A >= B && a != 2) || b == 2) {
                sb.append("a");
                A--;
                a++;
                b = 0;
            } else if ((B >= A && b != 2) || a == 2){
                sb.append("b");
                B--;
                b++;
                a = 0;
            }
        }
        return sb.toString();
    }
}
'''
