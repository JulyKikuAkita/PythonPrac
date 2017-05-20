__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/power-of-two.py

# Time:  O(1)
# Space: O(1)
#
# Given an integer, write a function to determine if it is a power of two.
#
# Google

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n-1)) == 0
    def isPowerOfTwo2IF(self, n):
        return n > 0 and pow(2, int(math.log(n) / math.log(2))) == n
# java
# http://algobox.org/power-of-two/
js = '''
public class Solution {
    public boolean isPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }
}
'''