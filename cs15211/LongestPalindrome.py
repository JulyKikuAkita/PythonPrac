__source__ = 'https://leetcode.com/problems/longest-palindrome/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/longest-palindrome.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 409. Longest Palindrome
#
# Given a string which consists of lowercase or uppercase letters,
# find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
# Example:
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# Google
# Hide Tags Hash Table
# Hide Similar Problems (E) Palindrome Permutation
#
import collections
import unittest
class Solution(object):
    # 24ms 97.31%
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odds = 0
        for k, v in collections.Counter(s).iteritems():
            odds += v & 1
        return len(s) - odds + int(odds > 0)

    # 44ms 13.74%
    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: int
        """
        odd = sum(map(lambda x: x & 1, collections.Counter(s).values()))
        return len(s) - odd + int(odd > 0)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/longest-palindrome/solution/

# Count duplicates in the pass, then check if we have an extra character to fix in the middle.

# 6ms 83.22%
class Solution {
    public int longestPalindrome(String s) {
        if ( s == null || s.length() ==0 ) return 0;
        char[] map = new char[256];
        int count = 0;
        for (char c: s.toCharArray()) {
            if (map[c] - 1 == 0) {
                count += 2;
                map[c]--;
            } else {
                map[c]++;
            }
        }
        if (count < s.length()) count++;
        return count;
    }
}

# 4ms 100%
class Solution {
    public int longestPalindrome(String s) {
        boolean[] map = new boolean[128];
        int len = 0;
        for (char c : s.toCharArray()) {
            map[c] = !map[c];         // flip on each occurrence, false when seen n*2 times
            if (!map[c]) len+=2;
        }
        if (len < s.length()) len++; // if more than len, atleast one single is present
        return len;
    }
}

# 5ms 93.71%
class Solution {
    public int longestPalindrome(String s) {
        int[] count = new int[256];
        for (char c : s.toCharArray()){
            count[c]++;
        }
        int res = 0;
        for (int i = 0; i < count.length; i++){
            if (count[i] % 2 == 0){
                res += count[i];
            } else {
                res += count[i]-1 ;
            }
        }
        if (res < s.length()){
            res++;
        }
        return res;
    }
}

# 14ms 27.34%
class Solution {
    public int longestPalindrome(String s) {
        if ( s == null || s.length() == 0 ) return 0;
        HashSet<Character> hs = new HashSet<Character>();
        int count = 0;
        for ( int i = 0; i < s.length(); i++) {
            if (hs.contains(s.charAt(i))) {
                hs.remove(s.charAt(i));
                count++;
            }else {
                hs.add(s.charAt(i));
            }
        }
        if(!hs.isEmpty()) return count * 2 + 1;
        return count * 2;
    }
}

'''
