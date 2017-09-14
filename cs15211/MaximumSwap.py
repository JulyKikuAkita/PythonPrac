__source__ = 'https://leetcode.com/problems/maximum-swap/description/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 670. Maximum Swap
#
# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number.
# Return the maximum valued number you could get.
#
# Example 1:
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:
# Input: 9973
# Output: 9973
# Explanation: No swap.
# Note:
# The given number is in the range [0, 10^8]
#
# Companies
# Facebook
# Related Topics
# Array Math
# Similar Questions
# Create Maximum Number
#
import unittest

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        A = map(int, str(num))
        last = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for d in xrange(9, x, -1):
                if last.get(d, None) > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(map(str, A)))
        return num

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/maximum-swap/solution/

Use buckets to record the last position of digit 0 ~ 9 in this num.

Loop through the num array from left to right.
For each position, we check whether there exists a larger digit in this num (start from 9 to current digit).
We also need to make sure the position of this larger digit is behind the current one.
If we find it, simply swap these two digits and return the result.

#30.55% 10ms
class Solution {
    public int maximumSwap(int num) {
        char[] digits = Integer.toString(num).toCharArray();

        int[] buckets = new int[10];
        for (int i = 0; i < digits.length; i++) {
            buckets[digits[i] - '0'] = i;
        }

        for (int i = 0; i < digits.length; i++) {
            for (int k = 9; k > digits[i] - '0'; k--) {
                if (buckets[k] > i) {
                    char tmp = digits[i];
                    digits[i] = digits[buckets[k]];
                    digits[buckets[k]] = tmp;
                    return Integer.valueOf(new String(digits));
                }
            }
        }
        return num;
    }
}

# 56.39% 9ms
class Solution {
    public int maximumSwap(int num) {
        String numCopy = String.valueOf(num);
        int len = numCopy.length();
        int[] largestSeen = new int[len];
        largestSeen[len - 1] = numCopy.charAt(len - 1) - '0';
        for (int i = len - 2; i >= 0; i--) {
            largestSeen[i] = Math.max(numCopy.charAt(i) - '0', largestSeen[i + 1]);
        }
        for (int i = 0; i < numCopy.length(); i++) {
            if (numCopy.charAt(i) - '0' < largestSeen[i]) {
                int swapPoint = findNumIndex(numCopy, largestSeen[i]);
                String r = numCopy.substring(0, i) + largestSeen[i] + numCopy.substring(i + 1, swapPoint) + numCopy.charAt(i);
                if (swapPoint < numCopy.length() - 1) {
                    r += numCopy.substring(swapPoint + 1);
                }
                return Integer.parseInt(r);
            }
        }
        return num;
    }

    private int findNumIndex(String num, int target) {
        for (int i = num.length() - 1; i >= 0; i--) {
            if (num.charAt(i) - '0' == target) {
                return i;
            }
        }
        return -1;
    }
}
'''