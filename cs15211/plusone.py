__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/plus-one.py
# Time:  O(n)
# Space: O(1)
# Array
#
# Given a non-negative number represented as an array of digits, plus one to the number.
#
# The digits are stored such that the most significant digit is at the head of the list.
#

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

if __name__ == "__main__":
    print Solution().plusOne([9,9,9,9])

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

t1=SolutionOther()
#print t1.plusOne([2,0,1,4])
#print t1.plusOne([1,0])
print t1.plusOne([199])