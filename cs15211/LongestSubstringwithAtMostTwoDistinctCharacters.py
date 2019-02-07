__source__ = 'https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/longest-substring-with-at-most-two-distinct-characters.py
# Time:  O(n^2)
# Space: O(1)
# Hashtable
#
# Description: Leetcode # 159. Longest Substring with At Most Two Distinct Characters
#
# Given a string, find the length of the longest substring T
# that contains at most 2 distinct characters.
#
# For example, Given s = "eceba",
#
# T is "ece" which its length is 3.
#
# Companies
# Google
# Related Topics
# Hash Table Two Pointers String
# Similar Questions
# Longest Substring Without Repeating Characters
# Sliding Window Maximum
# Longest Substring with At Most K Distinct Characters
#
import unittest
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLongestSubstringTwoDistinct(self, s):
        longest, start, distinct_count = 0,0,0
        visited = [0 for _ in xrange(256)]

        for i, char in enumerate(s):
            #print i, char, "longest = ", longest
            if visited[ord(char)] == 0:
                distinct_count += 1
            visited[ord(char)] += 1

            while distinct_count > 2:
                #print i, char, distinct_count, start, ord(s[i]), visited[ord(s[start])]
                visited[ord(s[start])] -= 1
                if visited[ord(s[start])] == 0:
                    distinct_count -= 1
                start += 1

            longest = max(longest, i - start + 1)

        return longest
    # considering "aaabbc"
    # i: at the position of 2nd distinct char
    # j: at the last occurrence of 1st distinct char
    # lastStart : same as j if only 2 different char, or at the first occurrence of
    #            2nd distinct char if there's 3 distinct char
    def lengthOfLongestSubstringTwoDistinctleetcode(self, s):
        longest, lastStart =  0, 0
        j = -1

        for i in xrange(1, len(s)):
            if s[i] == s[i-1]:
                continue
            if j >= 0 and s[j] != s[i]:
                longest = max(longest, i - lastStart)
                lastStart = j + 1
            j = i - 1
        return max(longest, len(s) - lastStart)

# Test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().lengthOfLongestSubstringTwoDistinct("eceba")
        print Solution().lengthOfLongestSubstringTwoDistinctleetcode("eceba")

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
# Sliding window with arr template
# 2ms 93.49%%
class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        if (s == null || s.length() == 0) return 0;
        int[] counts = new int[256];
        int start = 0, end = 0, k = 0, maxLen = 0;
        while(end < s.length()) {
            if (counts[s.charAt(end)]++ == 0) k++;
            end++;
            while (k > 2) {
                if(counts[s.charAt(start)]-- == 1) {
                  k--;
                }
                start++;
            }
            maxLen = Math.max(maxLen, end - start);
        }
        return maxLen;
    }
}

# Sliding window with arr template [bad coding style]
# 1ms 100%
class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        int[] map =  new int[256];
        int max = 0, cnt = 0;
        for (int l = 0, r = 0; r < s.length(); r++) {
            if (map[s.charAt(r)]++ == 0) cnt++;
            while (cnt > 2) {
                if (--map[s.charAt(l)] == 0) cnt--;
                l++;
            }
            max = Math.max(max, r - l + 1);
        }
        return max;
    }
}

# https://discuss.leetcode.com/topic/71662/sliding-window-algorithm-template-to-solve-all-the-leetcode-substring-search-problem
# Sliding window with map template
# 14ms 28.72%
class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        if (s.length() < 1) return 0;
        HashMap<Character,Integer> map = new HashMap();
        int start = 0, end = 0;
        int ans = 0;
        while (end < s.length()) {
            map.put(s.charAt(end), map.getOrDefault(s.charAt(end), 0) + 1);
            end++;
            while (map.size() > 2) {
                map.put(s.charAt(start), map.get(s.charAt(start)) - 1);
                if (map.get(s.charAt(start)) == 0) map.remove(s.charAt(start));
                start++;
            }
            ans = Math.max(ans, end - start);
        }
        return ans;
    }
}

# 4ms improvement
# 10ms 63.04%
class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        if (s.length() < 1) return 0;
        HashMap<Character,Integer> map = new HashMap();
        int lo = 0, hi = 0;
        int maxLength = 0;
        while (hi < s.length()) {
            if (map.size() <= 2) {
                map.put(s.charAt(hi), hi);
                hi++;
            }
            if (map.size() > 2) {
                int leftMost = s.length();
                for (int i : map.values()) {
                    leftMost = Math.min(leftMost, i);
                }
                char c = s.charAt(leftMost);
                map.remove(c);
                lo = leftMost + 1;
            }
            maxLength = Math.max(maxLength, hi - lo);
        }
        return maxLength;
    }
}
# 4ms 74.10%
class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        int i = 0, j = -1;
        int maxLen = 0;
        for (int k = 1; k < s.length(); k++) {
            if (s.charAt(k) == s.charAt(k-1)) continue;
            if (j > -1 && s.charAt(k) != s.charAt(j)) {
                maxLen = Math.max(maxLen, k - i);
                i = j + 1;
            }
            j = k - 1;
        }
        return maxLen > (s.length() - i) ? maxLen : s.length() - i;
    }
}
'''
