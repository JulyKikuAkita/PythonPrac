__source__ = 'https://leetcode.com/problems/longest-repeating-character-replacement/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/longest-repeating-character-replacement.py
# Time:  O(n)
# Space: O(1)
#
# Description: 424. Longest Repeating Character Replacement
#
# Given a string that consists of only uppercase English letters,
# you can replace any letter in the string with another letter at most k times.
# Find the length of a longest substring containing all repeating letters
# you can get after performing the above operations.
#
# Note:
# Both the string's length and k will not exceed 104.
#
# Example 1:
#
# Input:
# s = "ABAB", k = 2
#
# Output:
# 4
#
# Explanation:
# Replace the two 'A's with two 'B's or vice versa.
# Example 2:
#
# Input:
# s = "AABABBA", k = 1
#
# Output:
# 4
#
# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
#
# Pocket Gems
# Hide Similar Problems (H) Longest Substring with At Most K Distinct Characters
#
import unittest
import collections
# 396ms 23.64%
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = lo = hi = 0
        counts = collections.Counter()
        for hi in range(1, len(s)+1):
            counts[s[hi-1]] += 1
            max_char_n = counts.most_common(1)[0][1]
            if hi - lo - max_char_n > k:
                counts[s[lo]] -= 1
                lo += 1
        return hi - lo

    def characterReplacement2(self, s, k):
        res = 0

        cnts = [0] * 26
        times, i, j = k, 0, 0
        while j < len(s):
            cnts[ord(s[j]) - ord('A')] += 1
            if s[j] != s[i]:
                times -= 1
                if times < 0:
                    res = max(res, j - i)
                    while i < j and times < 0:
                        cnts[ord(s[i]) - ord('A')] -= 1
                        i += 1
                        times = k - (j - i + 1 - cnts[ord(s[i]) - ord('A')])
            j += 1

        return max(res, j - i + min(i, times))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

There's no edge case for this question.
The initial step is to extend the window to its limit,
that is, the longest we can get to with maximum number of modifications.
Until then the variable start will remain at 0.

Then as end increase, the whole substring from 0 to end will violate the rule,
so we need to update start accordingly (slide the window).
We move start to the right until the whole string satisfy the constraint again.
Then each time we reach such situation, we update our max length.

The problem says that we can make at most k changes to the string
(any character can be replaced with any other character).
So, let's say there were no constraints like the k.
Given a string convert it to a string with all same characters with minimal changes. The answer to this is

length of the entire string - number of times of the maximum occurring character in the string

Given this, we can apply the at most k changes constraint and maintain a sliding window such that
(length of substring - number of times of the maximum occurring character in the substring) <= k

# 7ms 79.95%
class Solution {
    public int characterReplacement(String s, int k) {
        int len = s.length();
        int[] count = new int[26];
        int start = 0, maxCount = 0, maxLength = 0;
        for (int end = 0; end < len; end++) {
            maxCount = Math.max(maxCount, ++count[s.charAt(end) - 'A']);
            while (end - start + 1 - maxCount > k) {
                count[s.charAt(start) - 'A']--;
                start++;
            }
            maxLength = Math.max(maxLength, end - start + 1);
        }
        return maxLength;
    }
}

'''
