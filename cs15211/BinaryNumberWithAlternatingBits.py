__source__ = 'https://leetcode.com/problems/binary-number-with-alternating-bits/description/'
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 693. Binary Number with Alternating Bits
#
# Given a positive integer, check whether it has alternating bits: namely,
# if two adjacent bits will always have different values.
#
# Example 1:
# Input: 5
# Output: True
# Explanation:
# The binary representation of 5 is: 101
# Example 2:
# Input: 7
# Output: False
# Explanation:
# The binary representation of 7 is: 111.
# Example 3:
# Input: 11
# Output: False
# Explanation:
# The binary representation of 11 is: 1011.
# Example 4:
# Input: 10
# Output: True
# Explanation:
# The binary representation of 10 is: 1010.
#
# Companies
# Yahoo
# Related Topics
# Bit Manipulation
# Similar Questions
# Number of 1 Bits
#
import unittest
class Solution(object):
    def hasAlternatingBits(self, n):
        bits = bin(n)
        return all(bits[i] != bits[i+1]
                   for i in xrange(len(bits) - 1))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/binary-number-with-alternating-bits/

#3.06% 23ms
class Solution {
    public boolean hasAlternatingBits(int n) {
        return Integer.toBinaryString(n).matches("(10)*1?");
    }
}

#50.75% 14ms
class Solution {
    public boolean hasAlternatingBits(int n) {
        String bits = Integer.toBinaryString(n);
        for (int i = 0; i < bits.length() - 1; i++) {
            if (bits.charAt(i) == bits.charAt(i+1)) {
                return false;
            }
        }
        return true;
    }
}

#75.95% 13ms
class Solution {
    public boolean hasAlternatingBits(int n) {
            int previous =0;
            while (n>0){
                previous = n%2;
                n = n/2;
                if(previous == n%2) return false;
            }
            return true;
        }
}
'''