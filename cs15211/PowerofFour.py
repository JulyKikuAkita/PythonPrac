__source__ = 'https://leetcode.com/problems/power-of-four/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/power-of-four.py
# Time:  O(1)
# Space: O(1)

# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
#
# Example:
# Given num = 16, return true. Given num = 5, return false.
#
# Follow up: Could you solve it without loops/recursion?
# Companies
# Two Sigma
# Related Topics
# Bit Manipulation
# Similar Questions
# Power of Two Power of Three
#
import unittest
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # print 0b01010101010101010101010101010101  =1431655765 in 31 digits
        return num > 0 and (num & (num - 1)) == 0 and \
               ((num & 0b01010101010101010101010101010101) == num)


# Time:  O(1)
# Space: O(1)
class Solution2(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        print 0b11
        while num and not (num & 0b11):
            num >>= 2
        return (num == 1)

    #38ms
    def isPowerOfFourIF(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num > 1:
            if num % 4 == 0:
                num /= 4
            else :
                return False
        return num == 1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        s1 = Solution().isPowerOfFour(16)
        s2 = Solution2().isPowerOfFour(16)
        s3 = Solution2().isPowerOfFourIF(16)

        self.assertTrue(s1)
        self.assertTrue(s2)
        self.assertTrue(s3)


if __name__ == '__main__':
    unittest.main()
#Java
Java = '''
#18.58% 2ms
public class Solution {
    public boolean isPowerOfFour(int num) {
        return num > 0 && Math.pow(4, Math.round((Math.log(num) / Math.log(4)))) == num;
    }
}

#18.58% 2ms
public class Solution {
    public boolean isPowerOfFour(int num) {
        while(num > 0 && ((num & 0b11) == 0) ){
            num >>= 2;
        }
        return num == 1;
    }
}

#Iteration:
#18.58% 2ms
public class Solution {
    public boolean isPowerOfFour(int num) {
        if (num < 1) return false;
        while (num > 1) {
            if (num % 4 == 0) num /= 4;
            else return false;
        }
        return num == 1;
    }
}

#Recursion:
#18.58% 2ms
public class Solution {
    public boolean isPowerOfFour(int num) {
        if (num < 1) return false;
        else if (num == 1) return true;
        else if (num % 4 == 0 ) return isPowerOfFour(num / 4);
        else return false;
    }
}
'''