__source__ = 'https://leetcode.com/problems/find-all-anagrams-in-a-string/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/find-all-anagrams-in-a-string.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 438. Find All Anagrams in a String
#
# Given a string s and a non-empty string p, find all the start indices
# of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of
# both strings s and p will not be larger than 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:
#
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# Companies
# Amazon
# Related Topics
# Hash Table
# Similar Questions
# Valid Anagram Permutation in String
#
# 116ms 68.85%
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []

        cnts = [0] * 26
        for c in p:
            cnts[ord(c) - ord('a')] += 1

        left, right = 0, 0
        while right < len(s):
            cnts[ord(s[right]) - ord('a')] -= 1
            while left <= right and cnts[ord(s[right]) - ord('a')] < 0:
                cnts[ord(s[left]) - ord('a')] += 1
                left += 1
            if right - left + 1 == len(p):
                result.append(left)
            right += 1

        return result

Java = '''
Thought:
Same idea from a fantastic sliding window template, please refer:
https://discuss.leetcode.com/topic/30941/here-is-a-10-line-template-that-can-solve-most-substring-problems

Time Complexity will be O(n) because the "start" and "end" points will only move from left to right once.

# 10ms 89.31%
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> list = new ArrayList<>();
        if (s == null || s.length() == 0 || p == null || p.length() == 0) return list;
        int[] hash = new int[256]; //character hash
        //record each character in p to hash
        for (char c : p.toCharArray()) {
            hash[c]++;
        }
        //two points, initialize count to p's length
        int left = 0, right = 0, count = p.length();
        while (right < s.length()) {
            //move right everytime, if the character exists in p's hash, decrease the count
            //current hash value >= 1 means the character is existing in p
            if (hash[s.charAt(right++)]-- >= 1) count--;

            //when the count is down to 0, means we found the right anagram
            //then add window's left to result list
            if (count == 0) list.add(left);

            //if we find the window's size equals to p, then we have to move left
            // (narrow the window) to find the new match window
            //++ to reset the hash because we kicked out the left
            //only increase the count if the character is in p
            //the count >= 0 indicate it was original in the hash, cuz it won't go below 0
            if (right - left == p.length() && hash[s.charAt(left++)]++ >= 0) count++;
        }
        return list;
    }
}

# get rid of auto increment and decrement
# 24ms 50.64%
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> ans = new ArrayList<>();
        if (s == null || s.length() == 0 || p == null || p.length() == 0) return ans;
        int[] counts = new int[256];
        for (char c : p.toCharArray()) counts[c]++;
        int len = p.length(), left = 0, right = 0;
        while (right < s.length()) {
            if (counts[s.charAt(right)] >= 1) len--;
            counts[s.charAt(right)]--;
            right++;
            
            if (len == 0) ans.add(left);
            if (right - left == p.length()){
                if(counts[s.charAt(left)] >= 0) len++;
                counts[s.charAt(left)]++;
                left++;
            } 
        }
        return ans;
    }
}

template:
https://discuss.leetcode.com/topic/68976/sliding-window-algorithm-template-to-solve-all-the-leetcode-substring-search-problem

2. HashTable + sliding window
# 15ms 66.83%
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> ans = new ArrayList<>();
        if (s == null || s.length() == 0 || p == null || p.length() == 0) return ans;
        int[] counts = new int[256];
        for (char c : p.toCharArray()) counts[c]++;
        int len = p.length(), left = 0, right = 0;
        while (right < s.length()) {
            char c = s.charAt(right);
            right++;
            if (counts[c] >= 1) len--;
            counts[c]--;
           
            while (right - left > p.length()) {
                char prev = s.charAt(left);
                if (counts[prev] >= 0) len++;
                counts[prev]++;
                left++;
            }
            if (len == 0) ans.add(left);
        }
        return ans;
    }
}

'''
