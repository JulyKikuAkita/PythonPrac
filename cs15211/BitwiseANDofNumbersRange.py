__source__ = 'https://leetcode.com/problems/bitwise-and-of-numbers-range/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/bitwise-and-of-numbers-range.py
# Time:  O(1)
# Space: O(1)
#
# Description: Leetcode # 201. Bitwise AND of Numbers Range
#
# Given a range [m, n] where 0 <= m <= n <= 2147483647,
# return the bitwise AND of all numbers in this range, inclusive.
#
# For example, given the range [5, 7], you should return 4.
#
# [26, 30]
# [11 010,   11 011,  11 100,  11 101,  11 110]
#
# Related Topics
# Bit Manipulation
#
import unittest
class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        i, diff = 0, n-m
        while diff:
            diff >>= 1
            i += 1
        return n&m >> i << i


    def rangeBitwiseAndVanilla(self, m, n):
        ans = m
        for i in xrange(m+1,n+1):
            ans &= i
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().rangeBitwiseAnd(5, 7)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
The idea is very simple:
last bit of (odd number & even number) is 0.
when m != n, There is at least an odd number and an even number, so the last bit position result is 0.
Move m and n rigth a position.
Keep doing step 1,2,3 until m equal to n, use a factor to record the iteration time.

#12.43% 10ms
public class Solution {
    public int rangeBitwiseAnd(int m, int n) {
        if(m == 0){
            return 0;
        }
        int moveFactor = 1;
        while(m != n){
            m >>= 1;
            n >>= 1;
            moveFactor <<= 1;
        }
        return m * moveFactor;
    }
}

#22.51% 9ms
public class Solution {
    public int rangeBitwiseAnd(int m, int n) {
        if (m == n) {
            return m;
        }
        int highestDiffBit = 0;
        int base = 1 << 31;
        while (base != 0) {
            if ((m & base) != (n & base)) {
                highestDiffBit = base;
                break;
            }
            base >>>= 1;
        }
        return m & ~((highestDiffBit << 1) - 1);
    }
}

Thought:
The idea is to use a mask to find the leftmost common digits of m and n.
Example: m=1110001, n=1110111, and you just need to find 1110000 and it will be the answer.

#51.82% 8ms
public class Solution {
    public int rangeBitwiseAnd(int m, int n) {
        if(m==n) return m;
        int nHigh=Integer.highestOneBit(n);
        if(Integer.highestOneBit(m)!=nHigh) return 0;
        int xor=m^n;
        return (nHigh-Integer.highestOneBit(xor)*2+nHigh)&n;
    }
}

#22.51% 9ms
class Solution {
    public int rangeBitwiseAnd(int m, int n) {
        int r=Integer.MAX_VALUE;
        while((m&r)!=(n&r))  r=r<<1;
        return n&r;
    }
}

Thought:
The key point: reduce n by removing the rightest '1' bit until n<=m;

(1)if n>m,suppose m = yyyzzz, n = xxx100, because m is less than n, m can be equal to three cases:

(a) xxx011 (if yyy==xxx)
(b) less than xxx011 (if yyy==xxx)
(c) yyyzzz (if yyy<xxx)
for case (a), and (b), xxx011 will always be ANDed to the result,
which results in xxx011 & xxx100 = uuu000(uuu == yyy&xxx == xxx);

for case (c), xxx000/xxx011 will always be ANDed to the result,
which results in yyyzzz & xxx000 & xxx011 & xxx100 = uuu000 (uuu <= yyy & xxx)

=> for any case, you will notice that: rangBitWiseAnd(vvvzzz,xxx100) == uuu000 == rangBitWiseAnd(vvvzzz,xxx000),
(not matter what the value of"uuu" will be, the last three digits will be all zero)

=> This is why the rightest '1' bit can be removed by : n = n & (n-1);

(2)when n==m, obviously n is the result.

(3)when n < m, suppose we reduce n from rangBitWiseAnd(yyyzzz,xxx100) to rangBitWiseAnd(yyyzzz,xxx000);

i) xxx100 >yyyzzz => xxx >= yyy;

ii) xxx000 < yyyzzz => xxx <= yyy;

=> xxx == yyy;

=> rangBitWiseAnd(yyyzzz,xxx000) == rangeBitWiseAnd(xxxzzz,xxx000);

=>result is xxx000, which is also n;

# 51.82% 8ms
class Solution {
     public int rangeBitwiseAnd(int m, int n) {
        while(m<n) n = n & (n-1);
        return n;
    }
}
'''