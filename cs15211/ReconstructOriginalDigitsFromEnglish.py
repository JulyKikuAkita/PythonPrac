__source__ = 'https://leetcode.com/problems/reconstruct-original-digits-from-english/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/reconstruct-original-digits-from-english.py
# Time:  O(n)
# Space: O(1)
#
# Description: 423. Reconstruct Original Digits from English
#
# Given a non-empty string containing an out-of-order English representation
# of digits 0-9, output the digits in ascending order.
#
# Note:
# Input contains only lowercase English letters.
# Input is guaranteed to be valid and can be transformed to its original digits.
# That means invalid inputs such as "abc" or "zerone" are not permitted.
# Input length is less than 50,000.
# Example 1:
# Input: "owoztneoer"
#
# Output: "012"
# Example 2:
# Input: "fviefuro"
#
# Output: "45"
#
# Fun fact:
# zero: Only digit with z
# two: Only digit with w
# four: Only digit with u
# six: Only digit with x
# eight: Only digit with g
#
# The odd ones for easy looking, each one's letters all also appear in other digit words:
# one, three, five, seven, nine
#
import unittest
from collections import Counter
# 1052ms 1.94%
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        # The count of each char in each number string.
        cnts = [Counter(_) for _ in ["zero", "one", "two", "three", \
                                     "four", "five", "six", "seven", \
                                     "eight", "nine"]]

        # The order for greedy method.
        order = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]

        # The unique char in the order.
        unique_chars = ['z', 'o', 'w', 't', 'u', \
                        'f', 'x', 's', 'g', 'n']

        cnt = Counter(list(s))
        res = []
        for i in order:
            while cnt[unique_chars[i]] > 0:
                cnt -= cnts[i]
                res.append(i)
        res.sort()
        return "".join(map(str, res))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
The idea is:
for zero, it's the only word has letter 'z',
for two, it's the only word has letter 'w',
......
so we only need to count the unique letter of each word, Coz the input is always valid.
#
# 24ms 32.02%
class Solution {
    public String originalDigits(String s) {
        int[] count = new int[10];
        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if (c == 'z') count[0]++;
            if (c == 'w') count[2]++;
            if (c == 'x') count[6]++;
            if (c == 's') count[7]++; //7-6
            if (c == 'g') count[8]++;
            if (c == 'u') count[4]++;
            if (c == 'f') count[5]++; //5-4
            if (c == 'h') count[3]++; //3-8
            if (c == 'i') count[9]++; //9-8-5-6
            if (c == 'o') count[1]++; //1-0-2-4
        }
        count[7] -= count[6];
        count[5] -= count[4];
        count[3] -= count[8];
        count[9] = count[9] - count[8] - count[5] - count[6];
        count[1] = count[1] - count[0] - count[2] - count[4];

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i <= 9; i++){
            for (int j = 0; j < count[i]; j++){
                sb.append(i);
            }
        }
        return sb.toString();
    }
}
'''
