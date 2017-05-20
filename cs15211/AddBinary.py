__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/add-binary.py
# Time:  O(n)
# Space: O(1)
#
# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".
#

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        result, carry, val, len_a, len_b, i = "", 0,0, len(a), len(b), 0

        for i in xrange(max(len_a, len_b)):
            val = carry
            if i < len_a:
                val += int(a[-(i + 1)])
            if i < len_b:
                val += int(b[-(i + 1)])
            carry, val = val / 2, val % 2
            print carry, val, result
            # format example: https://docs.python.org/3/library/string.html#formatspec
            result = "{0}{1}".format(val, result)

        if carry == 1:
            result = "1" + result
        return result

if __name__ == '__main__':
    result = Solution().addBinary('11', '1')
    print result


class Solution2:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        a = [ord(c) - ord('0') for c in a][::-1]
        b = [ord(c) - ord('0') for c in b][::-1]
        print a,b
        if len(a) < len(b):
            a,b = b,a
        flag = 0
        for i in range(len(a)):
            if  i < len(b):
                a[i] += b[i]
            a[i] += flag
            flag = a[i]//2
            a[i] %= 2
            print "loop", flag, a[i], i

        if flag:
            a.append(1)
        return ''.join([chr(c + ord('0'))for c in a][::-1])

# Java solution
# http://www.programcreek.com/2014/05/leetcode-add-binary-java/

#test
test = Solution2()
print test.addBinary('11', '1')
#print [ord(c) - ord('0') for c in '10'][::-1]

