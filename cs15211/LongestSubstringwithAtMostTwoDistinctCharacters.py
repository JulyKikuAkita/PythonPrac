__source__ = 'https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/longest-substring-with-at-most-two-distinct-characters.py
# Time:  O(n^2)
# Space: O(1)
# Hashtable
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
# Longest Substring Without Repeating Characters Sliding Window Maximum Longest Substring with At Most K Distinct Characters

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


#test

if __name__ =="__main__":
    print Solution().lengthOfLongestSubstringTwoDistinct("eceba")
    print Solution().lengthOfLongestSubstringTwoDistinctleetcode("eceba")

Java = '''

#sliding window
# 84.79% 7ms
public class Solution {
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

# 62.63% 10ms
public class Solution {
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

# https://discuss.leetcode.com/topic/71662/sliding-window-algorithm-template-to-solve-all-the-leetcode-substring-search-problem
# 28.71% 33ms
public class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        if(s.length() < 1) return 0;
        HashMap<Character,Integer> index = new HashMap<Character,Integer>();
        int lo = 0;
        int hi = 0;
        int maxLength = 0;
        while(hi < s.length()) {
            if(index.size() <= 2) {
                char c = s.charAt(hi);
                index.put(c, hi);
                hi++;
            }
            if(index.size() > 2) {
                int leftMost = s.length();
                for(int i : index.values()) {
                    leftMost = Math.min(leftMost,i);
                }
                char c = s.charAt(leftMost);
                index.remove(c);
                lo = leftMost+1;
            }
            maxLength = Math.max(maxLength, hi-lo);
        }
        return maxLength;
    }
}

# 97.12% 4ms
public class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        int len = s.length();
        if (len == 0) {
            return 0;
        }
        char[] arr = s.toCharArray();
        int start = 0;
        int end = 1;
        int result = 0;
        char[] chars = new char[2];
        int[] lastIndex = new int[2];
        chars[0] = arr[0];
        while (end < len && arr[end] == chars[0]) {
            end++;
        }
        if (end == len) {
            return len;
        }
        chars[1] = arr[end];
        lastIndex[0] = end - 1;
        lastIndex[1] = end;
        while (++end < len) {
            if (arr[end] == chars[0]) {
                lastIndex[0] = end;
            } else if (arr[end] == chars[1]) {
                lastIndex[1] = end;
            } else {
                result = Math.max(result, end - start);
                if (lastIndex[0] < lastIndex[1]) {
                    start = lastIndex[0] + 1;
                    chars[0] = arr[end];
                    lastIndex[0] = end;
                } else {
                    start = lastIndex[1] + 1;
                    chars[1] = arr[end];
                    lastIndex[1] = end;
                }
            }
        }
        return Math.max(result, len - start);
    }
}
'''