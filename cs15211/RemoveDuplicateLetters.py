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
    public String removeDuplicateLetters(String s){
        if(s.length() == 0) return s;

        //We use 128 is to avoid substraction
        //if we use 26, we have to substract 'a' from a char
        int[] count = new int[128];
        char[] result = new char[26];
        boolean[] assigned = new boolean[128];
        char c;
        int end = -1;

        for(int i=0; i<s.length(); i++){
            count[s.charAt(i)]++;
        }

        for(int i=0; i<s.length(); i++){
            c = s.charAt(i);
            count[c]--;
            if(assigned[c])
                continue;

            while(end >= 0 && result[end] > c && count[result[end]]>0){
                assigned[result[end]] = false;
                end--;
            }

            end++;
            result[end] = c;
            assigned[c] = true;
        }

        StringBuilder bd = new StringBuilder();
        for(int i=0; i<=end; i++){
            bd.append(result[i]);
        }
        return bd.toString();
    }
}
'''