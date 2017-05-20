__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/remove-duplicate-letters.py
# Time:  O(n)
# Space: O(k), k is size of the alphabet

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
# Hide Company Tags Google
# Hide Tags Stack Greedy


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


# java
js = '''
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
'''