__source__ = 'https://leetcode.com/problems/power-of-three/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/power-of-three.py
# Time:  O(1)
# Space: O(1)
#
# Description: Leetcode # 326. Power of Three
#
# Given an integer, write a function to determine if it is a power of three.
# Follow up:
# Could you do it without using any loop / recursion?
#
# Companies
# Google
# Related Topics
# Math
# Similar Questions
# Power of Two Power of Four
#
import unittest
import math
class Solution(object):
    def __init__(self):
        self.__max_log3 = int(math.log(0x7fffffff) / math.log(3))
        self.__max_pow3 = 3 ** self.__max_log3  # 1162261467

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and self.__max_pow3 % n == 0

#185ms
class Solution2(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 1:
            if n % 3 != 0:
                break
            else:
                n = n / 3

        return n == 1


class Solution3(object):
    powerOfThree = {1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683,
                     59049, 177147, 531441, 1594323, 4782969, 14348907,
                     43046721, 129140163, 387420489, 1162261467}
    def isPowerOfThree(self, n):
        return n in self.powerOfThree

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/power-of-three/
#91.65% 17ms # recursion
public class Solution {
    public boolean isPowerOfThree(int n) {
        if(n <= 0) return false;
        if(n == 1) return true;
        else if(n % 3 ==0) return isPowerOfThree(n/3);
        else return false;
    }
}

#70.06%  18ms # iteration
public class Solution {
    public boolean isPowerOfThree(int n) {
        if (n > 1) {
            while( n % 3 == 0) n /= 3;
        }
        return n == 1;
    }
}

#29.23% 21ms
public class Solution {
    public boolean isPowerOfThree(int n) {
        if (n == 0) {
            return false;
        }
        return Math.pow(3, Math.round(Math.log(n) / Math.log(3))) == n;
    }
}

# http://algobox.org/power-of-three/
#91.65% 17ms
public class Solution {
    public boolean isPowerOfThree(int n) {
        // 1162261467 is 3^19,  3^20 is bigger than int Integer_MAX_VALUE = 2,147,483,647
        return (n > 0) && 1162261467 % n == 0;
    }
}

#70.06% 18ms
public class Solution {
    public boolean isPowerOfThree(int n) {
        return (n > 0 && Math.pow(3, 19) % n == 0);
    }
}

#5.04% 57ms
public class Solution {
    public boolean isPowerOfThree(int n) {
        HashSet<Integer> set = new HashSet<>(
        Arrays.asList(1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467));
        return set.contains(n);
    }
}
'''