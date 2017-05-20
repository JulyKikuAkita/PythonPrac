__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/reverse-bits.py
# Time : O(n)
# Space: O(1)
# Bit Manipulation
#
# Reverse bits of a given 32 bits unsigned integer.
#
# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).
#
# Follow up:
# If this function is called many times, how would you optimize it?
#
# Related problem: Reverse Integer
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
#

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

if __name__ == '__main__':
  print Solution().reverseBits(1)

#java
js = '''
public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int ret = 0;
        for (int i = 0; i < 32; i++) {
            if ((n & 1) != 0) {
                ret |= 1;
            }
            n >>>= 1;  // padding 0 on the left side
            if (i < 31) {
                ret <<= 1;
            }
        }
        return ret;
    }
}

public class Solution2 {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int ret = 0;
        for (int i = 0; i < 32; i++) {
            ret <<= 1;
            if ((n & 1) != 0) {
                ret |= 1;
            }
            n >>>= 1;  // padding 0 on the left side

        }
        return ret;
    }
}
'''