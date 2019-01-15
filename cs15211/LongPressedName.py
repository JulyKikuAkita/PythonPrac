__source__ = 'https://leetcode.com/problems/long-pressed-name/'
# Time:  O(N + T)
# Space: O(1)
#
# Description: Leetcode # 925. Long Pressed Name
#
# Your friend is typing his name into a keyboard.
# Sometimes, when typing a character c, the key might get long pressed,
# and the character will be typed 1 or more times.
#
# You examine the typed characters of the keyboard.
# Return True if it is possible that it was your friends name, with some characters (possibly none)
# being long pressed.
#
# Example 1:
#
# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.
# Example 2:
#
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
# Example 3:
#
# Input: name = "leelee", typed = "lleeelee"
# Output: true
# Example 4:
#
# Input: name = "laiden", typed = "laiden"
# Output: true
# Explanation: It's not necessary to long press any character.
#
# Note:
#
# name.length <= 1000
# typed.length <= 1000
# The characters of name and typed are lowercase letters.
#
import unittest
import itertools

# identify by group counts
class Solution(object):
    def isLongPressedName(self, name, typed):
        g1 = [(k, len(list(grp))) for k, grp in itertools.groupby(name)]
        g2 = [(k, len(list(grp))) for k, grp in itertools.groupby(typed)]
        if len(g1) != len(g2):
            return False

        return all(k1 == k2 and v1 <= v2
                   for (k1,v1), (k2,v2) in zip(g1, g2))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/long-pressed-name/solution/
Complexity Analysis

Time Complexity: O(N+T), where N, T are the lengths of name and typed.
Space Complexity: O(1) in additional space complexity.
(In Java, .toCharArray makes this O(N), but this can be easily remedied.)


# 7ms 15.22%
class Solution {
    public boolean isLongPressedName(String name, String typed) {
        Group g1 = groupify(name);
        Group g2 = groupify(typed);
        if (!g1.key.equals(g2.key))
            return false;

        for (int i = 0; i < g1.count.size(); ++i)
            if (g1.count.get(i) > g2.count.get(i))
                return false;
        return true;
    }

    public Group groupify(String S) {
        StringBuilder key = new StringBuilder();
        List<Integer> count = new ArrayList();
        int anchor = 0;
        int N = S.length();
        for (int i = 0; i < N; ++i) {
            if (i == N-1 || S.charAt(i) != S.charAt(i+1)) { // end of group
                key.append(S.charAt(i));
                count.add(i - anchor + 1);
                anchor = i+1;
            }
        }

        return new Group(key.toString(), count);
    }
}

class Group {
    String key;
    List<Integer> count;
    Group(String k, List<Integer> c) {
        key = k;
        count = c;
    }
}


# 2 pointers
# 3ms 100%
class Solution {
    public boolean isLongPressedName(String name, String typed) {
        int i =0, j = 0;
        while(i < name.length() && j < typed.length()) {
            int count1 = 0;
            char c1 = name.charAt(i);
            while (name.charAt(i) == c1 && ++i < name.length()) count1++;
            int count2 = 0;
            char c2 = typed.charAt(j);
            while (typed.charAt(j) == c2 && ++j < typed.length()) count2++;
            if (c1 != c2 || count1  > count2) return false;
        }
        return i == name.length() && j == typed.length();
    }
}
'''
