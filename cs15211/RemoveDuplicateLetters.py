__source__ = 'https://leetcode.com/problems/remove-duplicate-letters/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/remove-duplicate-letters.py
# Time:  O(n)
# Space: O(k), k is size of the alphabet
#
# Description: Leetcode # 316. Remove Duplicate Letters
#
# Given a string which contains only lowercase letters,
# remove duplicate letters so that every letter appear
# once and only once. You must make sure your result is
# the smallest in lexicographical order among all
# possible results.
#
# Example:
# Given "bcabc"
# Return "abc"
#
# Given "cbacdcbc"
# Return "acdb"
#
# Companies
# Google
# Related Topics
# Stack Greedy
#
import unittest
import collections
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        remaining = collections.defaultdict(int)
        for c in s:
            remaining[c] += 1

        in_stack, stk = set(), []
        for c in s:
            if c not in in_stack:
                while stk and stk[-1] > c and remaining[stk[-1]]:
                    in_stack.remove(stk.pop())
                stk += c
                in_stack.add(c)
            remaining[c] -= 1
        return "".join(stk)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
#13.02% 36ms

Given the string s, the greedy choice (i.e., the leftmost letter in the answer) is the smallest s[i], s.t.
the suffix s[i .. ] contains all the unique letters.
(Note that, when there are more than one smallest s[i]'s, we choose the leftmost one.
Why? Simply consider the example: "abcacb".)

After determining the greedy choice s[i], we get a new string s' from s by

removing all letters to the left of s[i],
removing all s[i]'s from s.
We then recursively solve the problem w.r.t. s'.

The runtime is O(26 * n) = O(n).

public class Solution {
    public String removeDuplicateLetters(String s) {
        int[] cnt = new int[26];
        int pos = 0; // the position for the smallest s[i]
        for (int i = 0; i < s.length(); i++) cnt[s.charAt(i) - 'a']++;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) < s.charAt(pos)) pos = i;
            if (--cnt[s.charAt(i) - 'a'] == 0) break;
        }
        return s.length() == 0 ? ""
        : s.charAt(pos) + removeDuplicateLetters(s.substring(pos + 1).replaceAll("" + s.charAt(pos), ""));
    }
}

#96.97% 3ms
public class Solution {
    public String removeDuplicateLetters(String s) {
        int[] arr = new int[26];
        int end = -1;
        int[] count = countCharacters(s);
        boolean[] added = new boolean[26];
        for (int i = 0; i < s.length(); i++) {
            int cur = s.charAt(i) - 'a';
            count[cur]--;
            if (added[cur]) {
                continue;
            }
            while (end >= 0 && arr[end] > cur && count[arr[end]] > 0) {
                added[arr[end]] = false;
                end--;
            }
            arr[++end] = cur;
            added[cur] = true;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i <= end; i++) {
            sb.append((char) (arr[i] + 'a'));
        }
        return sb.toString();
    }

    private int[] countCharacters(String s) {
        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
        }
        return count;
    }
}

# 93.87% 4ms
class Solution {
    public String removeDuplicateLetters(String s) {
        if ( s.length() == 0) return s;
        int[] count = new int[128];
        char[] res = new char[26];
        boolean[] assigned = new boolean[128];

        char c ;
        int end = -1;

        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i)]++;
        }

        for (int i = 0; i < s.length(); i++) {
            c = s.charAt(i);
            count[c]--;
            if (assigned[c]) continue;
            while (end >= 0 && res[end] > c && count[res[end]] > 0) {
                assigned[res[end]] = false;
                end--;
            }
            end++;
            res[end] = c;
            assigned[c] = true;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i <= end; i++) {
            sb.append(res[i]);
        }
        return sb.toString();
    }
}
'''