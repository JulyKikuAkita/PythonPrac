__source__ = 'https://leetcode.com/problems/1-bit-and-2-bit-characters/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 717. 1-bit and 2-bit Characters
#
# We have two special characters.
# The first character can be represented by one bit 0.
# The second character can be represented by two bits (10 or 11).
#
# Now given a string represented by several bits.
# Return whether the last character must be a one-bit character or not.
# The given string will always end with a zero.
#
# Example 1:
# Input:
# bits = [1, 0, 0]
# Output: True
# Explanation:
# The only way to decode it is two-bit character and one-bit character.
# So the last character is one-bit character.
#
# Example 2:
# Input:
# bits = [1, 1, 1, 0]
# Output: False
# Explanation:
# The only way to decode it is two-bit character and two-bit character.
# So the last character is NOT one-bit character.
# Note:
#
# 1 <= len(bits) <= 1000.
# bits[i] is always 0 or 1.
#
import unittest

#20ms 100%
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1


class Solution2(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        parity = bits.pop()
        while bits and bits.pop(): parity ^= 1
        return parity == 0
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/1-bit-and-2-bit-characters/solution/
Approach #1: Increment Pointer [Accepted]

Complexity Analysis
Time Complexity: O(N), where N is the length of bits.
Space Complexity: O(1), the space used by i.

Approach #2: Greedy [Accepted]
The second-last 0 must be the end of a character (or, the beginning of the array if it doesn't exist)
#3ms 100%
class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        int i = bits.length - 2;
        while (i >= 0 && bits[i] > 0) i--;
        return (bits.length - i) % 2 == 0;
    }
}

#3ms 100%
class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        int ptr = 0; //pointer to iterate the array
        while(ptr < bits.length){
            if(bits[ptr] == 1){ // if we encounter a 1, we need to jump 2 spots since it can only be decoded [10 , 11]
                ptr +=2;
                if(ptr == bits.length){ // if we reach the end after jumping, it gurantees that the given string ended with a 2bit code.
                    return false;
                }
            } else{ // if we encounter a 0, we need to only jump 1 spot since it can only be decoded [0]
                ptr += 1;
                if(ptr == bits.length){ //if we reach the end after jumping, it means given string ended with a 1 bit code.
                    return true;
                }
            }
        }
        return true;
    }
}
'''