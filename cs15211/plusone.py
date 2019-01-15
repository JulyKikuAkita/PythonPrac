__source__ = 'https://leetcode.com/problems/plus-one/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/plus-one.py
# Time:  O(n)
# Space: O(1)
# Array
#
# Description: Leetcode # 66. Plus One
#
# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
#
# You may assume the integer do not contain any leading zero, except the number 0 itself.
#
# The digits are stored such that the most significant digit is at the head of the list.
#
# Companies
# Google
# Related Topics
# Array Math
# Similar Questions
# Multiply Strings Add Binary Plus One Linked List
#
import unittest
class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        current, carry = 0, 1

        #for i in xrange(len(digits) -1, -1, -1):
        for i in reversed(xrange(len(digits))):
            current = digits[i] + carry # +1 for digits[0] ; and + carry for digits[i]
            digits[i] = current % 10
            carry = current / 10
        if carry > 0:
            #digits = [1] + digits
            digits.insert(0,carry)
        return digits

class SolutionOther:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        rans=[]
        sum=0
        for i in range(len(digits)):
            #print i,sum,digits[i]
            sum += digits[i]*(10**(len(digits)-i-1))
        sum+=1
        while sum >=10 :
            rans += [sum%10]
            sum = int(sum/10)
        rans += [sum]
        return rans[::-1]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        print Solution().plusOne([9,9,9,9])
        t1=SolutionOther()
        #print t1.plusOne([2,0,1,4])
        #print t1.plusOne([1,0])
        print t1.plusOne([199])

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 0ms 100%
class Solution {
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        for (int i = n - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }

        int[] newNumber = new int[n + 1];
        newNumber[0] = 1;
        return newNumber;
    }
}

# 0ms 100%
class Solution {
    public int[] plusOne(int[] digits) {
        int carry = 1;
        int index = digits.length - 1;
        while (carry > 0 && index >= 0) {
            int sum = digits[index] + carry;
            digits[index] = sum % 10;
            carry = sum / 10;
            index--;
        }
        if (carry > 0) {
            int[] result = new int[digits.length + 1];
            result[0] = 1;
            return result;
        } else {
            return digits;
        }
    }
}
'''