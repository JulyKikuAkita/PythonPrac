__source__ = 'https://leetcode.com/problems/reverse-bits/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/reverse-bits.py
# Time : O(n)
# Space: O(1)
# Bit Manipulation
#
# Description: Leetcode # 190. Reverse Bits
# Reverse bits of a given 32 bits unsigned integer.
#
# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
# return 964176192 (represented in binary as 00111001011110000010100101000000).
#
# Follow up:
# If this function is called many times, how would you optimize it?
#
# Companies
# Apple Airbnb
# Related Topics
# Bit Manipulation
# Similar Questions
# Number of 1 Bits
#
import unittest
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in xrange(32):
            result <<= 1
            result |= n & 1
            n >>= 1
        return result

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().reverseBits(1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
#32.35% 2ms
public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int ret = 0;
        for (int i = 0; i < 32; i++) {
            if ((n & 1) != 0) {
                ret |= 1; //same as // res += n & 1
            }
            n >>>= 1;  // padding 0 on the left side
            if (i < 31) {  // CATCH: for last digit, don't shift!
                ret <<= 1;
            }
        }
        return ret;
    }
}

# Thought :
We first intitialize result to 0. We then iterate from 0 to 31 (an integer has 32 bits).
In each iteration: We first shift result to the left by 1 bit.
Then, if the last digit of input n is 1, we add 1 to result. To find the last digit of n, we just do: (n & 1)
Example, if n=5 (101), n&1 = 101 & 001 = 001 = 1; however, if n = 2 (10), n&1 = 10 & 01 = 0).
Finally, we update n by shifting it to the right by 1 (n >>= 1) At the end of the iteration, we return result.

Example, if input n = 13 (represented in binary as
0000_0000_0000_0000_0000_0000_0000_1101, the "_" is for readability),
calling reverseBits(13) should return:
1011_0000_0000_0000_0000_0000_0000_0000

Here is how our algorithm would work for input n = 13:

Initially, result = 0 = 0000_0000_0000_0000_0000_0000_0000_0000,
n = 13 = 0000_0000_0000_0000_0000_0000_0000_1101

Starting for loop:
i = 0:
result = result << 1 = 0000_0000_0000_0000_0000_0000_0000_0000.
n&1 = 0000_0000_0000_0000_0000_0000_0000_1101 &
0000_0000_0000_0000_0000_0000_0000_0001 =
0000_0000_0000_0000_0000_0000_0000_0001 = 1
therefore result = result + 1 =
0000_0000_0000_0000_0000_0000_0000_0000 +
0000_0000_0000_0000_0000_0000_0000_0001 =
0000_0000_0000_0000_0000_0000_0000_0001 = 1
We right shift n by 1 (n >>= 1) to get:
n = 0000_0000_0000_0000_0000_0000_0000_0110.
We then go to the next iteration.

i = 1:
result = result << 1 = 0000_0000_0000_0000_0000_0000_0000_0010;
n&1 = 0000_0000_0000_0000_0000_0000_0000_0110 &
0000_0000_0000_0000_0000_0000_0000_0001
= 0000_0000_0000_0000_0000_0000_0000_0000 = 0;
therefore we don't increment result.
We right shift n by 1 (n >>= 1) to get:
n = 0000_0000_0000_0000_0000_0000_0000_0011.
We then go to the next iteration.

i = 2:
result = result << 1 = 0000_0000_0000_0000_0000_0000_0000_0100.
n&1 = 0000_0000_0000_0000_0000_0000_0000_0011 &
0000_0000_0000_0000_0000_0000_0000_0001 =
0000_0000_0000_0000_0000_0000_0000_0001 = 1
therefore result = result + 1 =
0000_0000_0000_0000_0000_0000_0000_0100 +
0000_0000_0000_0000_0000_0000_0000_0001 =
result = 0000_0000_0000_0000_0000_0000_0000_0101
We right shift n by 1 to get:
n = 0000_0000_0000_0000_0000_0000_0000_0001.
We then go to the next iteration.

i = 3:
result = result << 1 = 0000_0000_0000_0000_0000_0000_0000_1010.
n&1 = 0000_0000_0000_0000_0000_0000_0000_0001 &
0000_0000_0000_0000_0000_0000_0000_0001 =
0000_0000_0000_0000_0000_0000_0000_0001 = 1
therefore result = result + 1 =
= 0000_0000_0000_0000_0000_0000_0000_1011
We right shift n by 1 to get:
n = 0000_0000_0000_0000_0000_0000_0000_0000 = 0.

Now, from here to the end of the iteration, n is 0, so (n&1) will always be 0 and n >>=1 will not change n.
The only change will be for result <<=1, i.e. shifting result to the left by 1 digit.
Since there we have i=4 to i = 31 iterations left, this will result
in padding 28 0's to the right of result. i.e at the end, we get result = 1011_0000_0000_0000_0000_0000_0000_0000
This is exactly what we expected to get

#32.35% 2ms
public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        if (n == 0) return 0;

        int result = 0;
        for (int i = 0; i < 32; i++) {
            result <<= 1;
            if ((n & 1) == 1) result++;
            n >>= 1;
        }
        return result;
    }
}

#32.35% 2ms
public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        n = ((n & 0x55555555) << 1) | ((n & 0xAAAAAAAA) >>> 1);
        n = ((n & 0x33333333) << 2) | ((n & 0xCCCCCCCC) >>> 2);
        n = ((n & 0x0F0F0F0F) << 4) | ((n & 0xF0F0F0F0) >>> 4);
        n = ((n & 0x00FF00FF) << 8) | ((n & 0xFF00FF00) >>> 8);
        return (n >>> 16) | (n << 16);
    }
}
'''