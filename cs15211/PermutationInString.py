__source__ = 'https://leetcode.com/problems/permutation-in-string/'
# Time:  O(n!) //brute force
# Space: O(n2)
#
# Description: 567. Permutation in String
#
# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
# In other words, one of the first string's permutations is the substring of the second string.
#
# Example 1:
# Input:s1 = "ab" s2 = "eidbaooo"
# Output:True
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
# Note:
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].
# Hide Company Tags Microsoft
# Hide Tags Two Pointers
# Hide Similar Problems (H) Minimum Window Substring (E) Find All Anagrams in a String
#
import unittest


# For each window representing a substring of s2 of length len(s1),
# we want to check if the count of the window is equal to the count of s1.
# Here, the count of a string is the list of: [the number of a's it has,
# the number of b's,... , the number of z's.]
#
# We can maintain the window by deleting the value of s2[i - len(s1)]
# when it gets larger than len(s1). After, we only need to check if
# it is equal to the target. Working with list values of [0, 1,..., 25]
# instead of 'a'-'z' makes it easier to count later.
#
# 52ms 76.04%
class Solution(object):
    def checkInclusion(self, s1, s2):
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]

        target = [0] * 26
        for x in A:
            target[x] += 1

        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            if i >= len(A):
                window[B[i - len(A)]] -= 1
            if window == target:
                return True
        return False

# your function here

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/permutation-in-string/solution/
#
https://leetcode.com/articles/short-permutation-in-a-long-string/
Java Solution, Sliding Window
How do we know string p is a permutation of string s? Easy,
each character in p is in s too. So we can abstract all permutation strings of s to a map (Character -> Count).
i.e. abba -> {a:2, b:2}. Since there are only 26 lower case letters in this problem,
we can just use an array to represent the map.
How do we know string s2 contains a permutation of s1? We just need to create a sliding window with length of s1,
move from beginning to the end of s2. When a character moves in from right of the window,
we subtract 1 to that character count from the map. When a character moves out from left of the window,
we add 1 to that character count. So once we see all zeros in the map,
meaning equal numbers of every characters between s1 and the substring in the sliding window,
we know the answer is true.

# 8ms 98.88%
class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int len1 = s1.length(), len2 = s2.length();
        if (len1 > len2) return false;

        int[] count = new int[26];
        for (int i = 0; i < len1; i++) {
            count[s1.charAt(i) - 'a']++;
            count[s2.charAt(i) - 'a']--;
        }
        if (allZero(count)) return true;

        for (int i = len1; i < len2; i++) {
            count[s2.charAt(i) - 'a']--;
            count[s2.charAt(i - len1) - 'a']++;
            if (allZero(count)) return true;
        }

        return false;
    }

    private boolean allZero(int[] count) {
        for (int i = 0; i < 26; i++) {
            if (count[i] != 0) return false;
        }
        return true;
    }
}
'''