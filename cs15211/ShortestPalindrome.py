__source__ = 'https://leetcode.com/problems/shortest-palindrome/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/shortest-palindrome.py
# Time:  O(n)
# Space: O(n)
# Description: Leetcode # 214. Shortest Palindrome
#
# Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it.
# Find and return the shortest palindrome you can find by performing this transformation.
#
# For example:
#
# Given "aacecaaa", return "aaacecaaa".
#
# Given "abcd", return "dcbabcd".
#
# Companies
# Pocket Gems Google
# Related Topics
# String
# Similar Questions
# Longest Palindromic Substring Implement strStr() Palindrome Pairs
#

# KMP Algorithm
import unittest
class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        if not s :
            return s
        A = s + s[::-1]
        prefix = self.getPrefix(A)

        return s[prefix[-1]+1:][::-1] + s

    def getPrefix(self, pattern):
        prefix = [-1] * len(pattern)
        j = -1
        for i in xrange(1, len(pattern)):
            while j > -1 and pattern[j + 1] != pattern[i]:
                j = prefix[j]
            if pattern[j+1] == pattern[i]:
                j += 1
            prefix[i] = j
        return prefix


class Solution2(unittest.TestCase):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #KMP prefix table
        ttl_s = s + "#" + s[::-1]
        prefix = [ 0 for _ in xrange(len(ttl_s))]

        for i in xrange(1, len(ttl_s)):
            j = prefix[i-1]
            while j > 0 and ttl_s[i] != ttl_s[j]:
                j = prefix[j-1]
            prefix[i] = j + 1 if ttl_s[i] == ttl_s[j] else j
        res = s[::-1][:len(s)-prefix[-1]:]
        #print res, ttl_s
        return res + s

    def test(self):
        self.assertEqual("bbabb", self.shortestPalindrome("abb"))

# Manacher's Algorithm
class Solution_TLE:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        string = self.preProcess(s)
        palindrome = [0] * len(string)
        center, right = 0, 0
        for i in xrange(1, len(string) - 1):
            i_mirror = 2 * center - i
            if right > i:
                palindrome[i] = min(right - i, palindrome[i_mirror])
            else:
                palindrome[i] = 0

            while string[i + 1 + palindrome[i]] == string[i - 1 - palindrome[i]]:
                palindrome[i] += 1

            if i + palindrome[i] > right:
                center, right = i, i + palindrome[i]

        max_len = 0
        for i in xrange(1, len(string) - 1):
            if i - palindrome[i] == 1:
                max_len = palindrome[i]
        return s[len(s) - 1: max_len-1: -1] + s


    def preProcess(selfs, s):
        if not s:
            return "^$"
        string = "^"
        for i in s:
            string += "#" + i
        string += "#$"
        return string

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

        print Solution().shortestPalindrome("baaabc")
        print Solution().shortestPalindrome("aba")

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/shortest-palindrome/solution/
# 1.  The idea is to use two anchors j and i to compare the String from beginning and end.
If j can reach the end, the String itself is Palindrome.
Otherwise, we divide the String by j, and get mid = s.substring(0, j) and suffix.

We reverse suffix as beginning of result and recursively
call shortestPalindrome to get result of mid then append suffix to get result.

#71.76% 5ms
public class Solution {
    public String shortestPalindrome(String s) {
        if ( s == null || s.length() == 0 ) return s;
        int i = 0, j = s.length() - 1;
        while (j >= 0) {
            if (s.charAt(i) == s.charAt(j)) i++;
            j--;
        }
        if (i == s.length()) return s;
        String suffix = s.substring(i); // i to s.length()
        String prefix = new StringBuilder(suffix).reverse().toString();
        String mid = shortestPalindrome(s.substring(0, i));
        return prefix + mid + suffix;
    }
}

#98.79% 3ms
public class Solution {
    public String shortestPalindrome(String s) {
        if (s == null || s.length() == 0) return s;

        int i = 0;
        char[] arr = s.toCharArray();
        for (int j = arr.length - 1;j >= 0;j--) {
            if (arr[i] == arr[j]) {
                i++;
            }
        }
        if (i == arr.length) {
            return s;
        }
        return reverse(s.substring(i)) + shortestPalindrome(s.substring(0,i))
            + s.substring(i);
    }
    private String reverse(String s) {
        char[] arr = s.toCharArray();
        int left = 0;
        int right = arr.length - 1;
        while (left < right) {
            char temp = arr[left];
            arr[left++] = arr[right];
            arr[right--] = temp;
        }
        return new String(arr);
    }
}

Thought:
we reserved the original string ss and stored it as rev.
We iterate over i from 0 to n-1 and check for s[0:n-i] == rev[i:]
Pondering over this statement, had the rev been concatenated to s,
this statement is just finding the longest prefix that is equal to the suffix. Voila!

#KMP
#62.18% 8ms
# KMP initialized as j = -1, i = 0, lps = int[needle.length() + 1]
public class Solution {
    public String shortestPalindrome(String s) {
        String temp = s + "#" + new StringBuilder(s).reverse().toString();
        int[] lps = getLps(temp);
        return new StringBuilder(s.substring(lps[lps.length - 1])).reverse().toString() + s;
    }

    //getLongest prefix suffix table
    private int[] getLps(String s) {
        int[] lps = new int[s.length() + 1];
        int i = 0, j = -1;
        lps[0] = j;
        while (i < s.length()) {
            while(j >=0 && s.charAt(i) != s.charAt(j)) j = lps[j];
            i++;
            j++;
            lps[i] = j;
        }
        return lps;
    }
}

#49.58% 11ms
# KMP:
# KMP initialized as j = 0, i = 1, lps = int[needle.length()]
public class Solution {
    public String shortestPalindrome(String s) {
        String temp = s + "#" + new StringBuilder(s).reverse().toString();
        int[] table = getTable(temp);

        //get the maximum palindrome part in s starts from 0
        return new StringBuilder(s.substring(table[table.length - 1])).reverse().toString() + s;
    }

    public int[] getTable(String s){
        int[] table = new int[s.length()];
        int index = 0;
        //skip index 0, we will not match a string with itself
        for(int i = 1; i < s.length(); i++){
            if ( s.charAt(index ) == s.charAt(i)) {
                table[i] = table[i-1] + 1;  //we can extend match in prefix and postfix
                index++;
            } else {
                //match failed, we try to match a shorter substring
                //by assigning index to table[i-1], we will shorten the match string length, and jump to the
                //prefix part that we used to match postfix ended at i - 1
                index = table[i-1];

                 //we will try to shorten the match string length until we revert to the beginning of match (index 1)
                while(index > 0 && s.charAt(index) != s.charAt(i)){
                    index = table[index-1];
                }

                //when we are here may either found a match char or we reach the boundary and still no luck
                //so we need check char match
                if(s.charAt(index) == s.charAt(i)){
                    index ++ ; //if match, then extend one char
                }
                table[i] = index;
            }

        }
        return table;
    }

}

# KMP
#49.58% 11ms
# KMP initialized as j = 0, i = 1, lps = int[needle.length()]
public class Solution {
    public String shortestPalindrome(String s) {
        String reversed = new StringBuilder(s).reverse().toString();
        char[] full = new StringBuilder().append(s).append('#').append(reversed).toString().toCharArray();
        int[] prefix = new int[full.length];
        for (int i = 1; i < full.length; i++) {
            int j = prefix[i - 1];
            while (j > 0 && full[i] != full[j]) {
                j = prefix[j - 1];
            }
            prefix[i] = j + (full[i] == full[j] ? 1 : 0);
        }
        return new StringBuilder(reversed.substring(0, reversed.length() - prefix[prefix.length - 1])).append(s).toString();
    }
}
'''