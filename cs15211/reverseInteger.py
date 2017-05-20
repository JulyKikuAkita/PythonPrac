__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/reverse-integer.py
# Time: O(logn)
# Space: O(1)
#
# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321
#
# click to show spoilers.
#
# Have you thought about this?
# Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!
#
# If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.
#
# Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer,
# then the reverse of 1000000003 overflows. How should you handle such cases?
#
# Throw an exception? Good, but what if throwing an exception is not an option?
# You would then have to re-design the function (ie, add an extra parameter).
#

class Solution:
    # @return an integer
    def reverse(self, x):
        ans = 0
        if x >= 0:
            while x:
                ans = ans * 10 + x % 10
                x /= 10
            return ans if ans <= 2147483647 else 0  # Handle overflow.
        else:
            return -self.reverse(-x)

class Solution2(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        overflow = (1 << 31) # unsigned int 2^31 -1
        neg = False
        if x < 0:
            neg = True
            x *= -1

        if x>0xFFFFFFFF:
            return 0

        ans = 0
        while x:
            ans *= 10
            if ans + (x % 10) > overflow:
                return 0

            ans += x % 10
            x /= 10

        if neg:
            ans *= -1
        return ans


# test case
if __name__ == "__main__":
    print Solution().reverse(123)
    print Solution().reverse(-321)

#java
js = '''
public class Solution {
    public int reverse(int x) {
        long origin = Math.abs((long) x);
        long result = 0;
        while (origin > 0) {
            result *= 10;
            result += origin % 10;
            origin /= 10;
        }
        int ret = (int) result;
        if ((long) ret != result) {
            return 0;
        }
        return x < 0 ? -ret : ret;
    }
}
'''