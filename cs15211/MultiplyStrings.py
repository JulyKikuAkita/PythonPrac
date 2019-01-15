__source__ = 'https://leetcode.com/problems/multiply-strings/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/multiply-strings.py
# Time:  O(m * n)
# Space: O(m + n)
# String
#
# Description: Leetcode # 346. Moving Average from Data Stream
#
# Given two numbers represented as strings, return multiplication of the numbers as a string.
#
# Note: The numbers can be arbitrarily large and are non-negative.
#
# Companies
# Facebook Twitter
# Related Topics
# Math String
# Similar Questions
# Add Two Numbers Plus One Add Binary Add Strings
#
import unittest
class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        result = [0 for i in xrange(len(num1)+ len(num2))]
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                result[i + j] += int(num1[i]) * int(num2[j])

        carry, num3 = 0, []
        for digit in result:
            sum = carry + digit
            carry = sum / 10
            num3.insert(0, str(sum % 10))

        while len(num3) > 1 and num3[0] == "0":
            del num3[0]

        return ''.join(num3)

class SolutionOther:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        num1 = num1[::-1]
        num2 = num2[::-1]
        arr = [ 0 for i in range(len(num1)+len(num2)) ]

        for i in range(len(num1)):
            for j in range(len(num2)):
                arr[i+j] += int(num1[i]) * int(num2[j])

        ans = []

        for i in range(len(arr)):
            digit = arr[i] % 10
            carry  = arr[i] /10
            if i < len(arr) -1:
                arr[i+1] += carry
            ans.insert(0, str(digit))

        while ans[0] == '0' and len(ans) >1:
            del ans[0]

        return ''.join(ans)

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        print Solution().multiply("123", "1000")
        test = SolutionOther()
        print test.multiply("1", "200")

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: 
# https://discuss.leetcode.com/topic/30508/easiest-java-solution-with-graph-explanation with pic

# 13ms 93.57%
class Solution {
    public String multiply(String num1, String num2) {
        int len1 = num1.length();
        int len2 = num2.length();
        num1 = new StringBuilder(num1).reverse().toString();
        num2 = new StringBuilder(num2).reverse().toString();
        int[] result = new int[len1 + len2];
        for (int i = 0; i < len1; i++) {
            int carry = 0;
            for (int j = 0; j < len2; j++) {
                int sum = result[i + j] + (num1.charAt(i) - '0') * (num2.charAt(j) - '0') + carry;
                result[i + j] = sum % 10;
                carry = sum / 10;
            }
            result[i + len2] = carry;
        }
        int end = len1 + len2 - 1;
        while (end > 0 && result[end] == 0) {
            end--;
        }
        StringBuilder sb = new StringBuilder();
        while (end >= 0) {
            sb.append(result[end--]);
        }
        return sb.toString();
    }
}

# 16ms 68.27%
class Solution {
    public String multiply(String num1, String num2) {
        int n1 = num1.length();
        int n2 = num2.length();
        int[] res = new int[n1+n2];
        String s1 = new StringBuilder(num1).reverse().toString();
        String s2 = new StringBuilder(num2).reverse().toString();

        for(int i = 0; i < n1; i++){
            for(int j = 0; j < n2; j++){
                res[i + j] += (s1.charAt(i) - '0') * (s2.charAt(j) - '0');
            }
        }

        StringBuilder sb = new StringBuilder();
        int carry  = 0;
        for(int r : res){
            int sum = r + carry;
            sb.insert(0, sum % 10);
            carry = sum / 10;
        }

        while(sb.length() > 1 && sb.charAt(0) == '0'){
            sb.deleteCharAt(0);
        }
        return sb.toString();
    }
}
'''
