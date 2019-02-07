__source__ = 'https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/longest-substring-with-at-most-k-distinct-characters.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 340. Longest Substring with At Most K Distinct Characters
#
# Given a string, find the length of the longest substring T that contains at most k distinct characters.
#
# For example, Given s = "eceba", k = 2,
#
# T is "ece" which its length is 3.
#
# Companies
# Google
# Related Topics
# Hash Table String
# Similar Questions
# Longest Substring with At Most Two Distinct Characters
# Longest Repeating Character Replacement
#
import unittest
# Time:  O(n)
# Space: O(1)
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        longest, start, distinct_count, visited = 0, 0, 0, [0 for _ in xrange(256)]
        for i, char in enumerate(s):
            if visited[ord(char)] == 0:
                distinct_count += 1
            visited[ord(char)] += 1

            while distinct_count > k:
                visited[ord(s[start])] -= 1
                if visited[ord(s[start])] == 0:
                    distinct_count -= 1
                start += 1

            longest = max(longest, i - start + 1)
        return longest

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: 
#
# Sliding window with array
# 2ms 99.83%
class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        if (s == null || s.length() == 0) return 0;
        int[] counts = new int[256];
        int distinct = 0;
        int start = 0, end = 0;
        int maxLen = 0;
        while (end < s.length()) {
            if (counts[s.charAt(end)]++ == 0) {
                distinct++;
            }
            end++;

            while (distinct > k) {
                if (counts[s.charAt(start)]-- == 1) {
                    distinct--;
                }
                start++;
            }

            maxLen = Math.max(maxLen, end - start);
        }
        return maxLen;
    }
}

# Sliding window with array
# 2ms 99.83%
class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        int[] count = new int[256];
        int num = 0, i = 0, res = 0;
        for (int j = 0; j < s.length(); j++) {
            if (count[s.charAt(j)]++ == 0) num++;
            if (num > k) {
                while (--count[s.charAt(i++)] > 0); // move i to unseen char
                num--;
            }
            res = Math.max(res, j - i + 1);
        }
        return res;
    }
}

# Sliding Window with map template
# 45ms 8.62%
class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        int start = 0, end = 0, max = 0;
        Map<Character, Integer> map = new HashMap();
        while (end < s.length()) {
            map.put(s.charAt(end), map.getOrDefault(s.charAt(end), 0) + 1);
            end++;
            while (map.size() > k) {
                map.put(s.charAt(start), map.get(s.charAt(start)) - 1);
                if (map.get(s.charAt(start)) == 0) map.remove(s.charAt(start));
                start++;
            }
            max = Math.max(max, end - start);
        }
        return max;
    }
}

# Java O(nlogk) using TreeMap to keep last occurrence Interview "follow-up" question!
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/discuss/80044/Java-O(nlogk)-using-TreeMap-to-keep-last-occurrence-Interview-%22follow-up%22-question!
# Solving the problem with O(n) time is not enough, 
# some interviewer may require this solution as a followup. Instead of recording each char's count, 
# we keep track of char's last occurrence. If you consider k as constant, it is also a O(n) algorithm.
# inWindow keeps track of each char in window and its last occurrence position
# lastOccurrence is used to find the char in window with left most last occurrence. 
# A better idea is to use a PriorityQueue, as it takes O(1) to getMin, 
# However Java's PQ does not support O(logn) update a internal node, it takes O(n). 
# TreeMap takes O(logn) to do both getMin and update.
# Every time when the window is full of k distinct chars, 
# we lookup TreeMap to find the one with leftmost last occurrence and 
# set left bound j to be 1 + first to exclude the char to allow new char coming into window.
# Some imporvement with treeMap
# 17ms 46.12%
class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        int len = s.length();
        if (len <= k) {
            return len;
        } else if (k == 0) {
            return 0;
        }
        int[] lastIndex = new int[128];
        TreeSet<Integer> indices = new TreeSet<>();
        int start = 0;
        int result = 0;
        for (int i = 0; i < len; i++) {
            char c = s.charAt(i);
            if (lastIndex[c] == 0) {
                if (k == 0) {
                    result = Math.max(result, i - start);
                    int removeIndex = indices.pollFirst() - 1;
                    start = removeIndex + 1;
                    lastIndex[s.charAt(removeIndex)] = 0;
                    k++;
                }
                k--;
            } else {
                indices.remove(lastIndex[c]);
            }
            lastIndex[c] = i + 1;
            indices.add(i + 1);
        }
        result = Math.max(result, len - start);
        return result;
    }
}


'''
