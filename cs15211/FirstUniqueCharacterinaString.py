__source__ = 'https://leetcode.com/problems/first-unique-character-in-a-string/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/first-unique-character-in-a-string.py
# Time:  O(n)
# Space: O(n)
#
# Description: Leetcode # 387. First Unique Character in a String
#
# Given a string, find the first non-repeating character in it and
# return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.
#
# Companies
# Microsoft Amazon Bloomberg
#
from collections import defaultdict
import unittest
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = defaultdict(int)
        candidtates = set()
        for i, c in enumerate(s):
            if lookup[c]:
                candidtates.discard(lookup[c])
            else:
                lookup[c] = i+1
                candidtates.add(i+1)
        return min(candidtates)-1 if candidtates else -1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/first-unique-character-in-a-string/solution/

# 8ms 97.47%
class Solution {
    public int firstUniqChar(String s) {
        int[] count = new int[26];
        char[] arr = s.toCharArray();
        for (char c : arr) {
            count[c - 'a']++;
        }
        for (int i = 0; i < arr.length; i++) {
            if (count[arr[i] - 'a'] == 1) {
                return i;
            }
        }
        return -1;
    }
}

# 4ms 100%
class Solution {
    public int firstUniqChar(String s) {
        int res = s.length();
        for(char i = 'a' ;i <= 'z';i++) {
            int idx = s.indexOf(i);
            if(idx != -1 && idx == s.lastIndexOf(i)) {
                res = Math.min(res, idx);
            }
        }
        return res == s.length() ? -1 : res;
    }
}
'''
