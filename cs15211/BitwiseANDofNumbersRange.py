__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/bitwise-and-of-numbers-range.py
# Time:  O(1)
# Space: O(1)
#
# Given a range [m, n] where 0 <= m <= n <= 2147483647,
# return the bitwise AND of all numbers in this range, inclusive.
#
# For example, given the range [5, 7], you should return 4.
#
# [26, 30]
# [11 010,   11 011,  11 100,  11 101,  11 110]

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

if __name__ == '__main__':
    print Solution().rangeBitwiseAnd(5, 7)
#http://www.cnblogs.com/grandyang/p/4431646.html

#java
js = '''
public class Solution {
    public int rangeBitwiseAnd(int m, int n) {
        if (m == n) {
            return m;
        }
        int result = 0;
        int cur = Integer.highestOneBit(n);
        int last = (m & cur);
        while (cur != 0 && last == (n & cur)) {
            result |= last;
            cur >>>= 1;
            last = (m & cur);
        }
        return result;
    }
}

class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        int d = INT_MAX;
        while ((m & d) != (n & d)) {
            d <<= 1;
        }
        return m & d;
    }
};

class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        int i = 0;
        while (m != n) {
            m >>= 1;
            n >>= 1;
            ++i;
        }
        return (m << i);
    }
};
'''