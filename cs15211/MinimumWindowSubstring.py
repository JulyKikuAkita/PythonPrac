__source__ = 'https://leetcode.com/problems/minimum-window-substring/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/minimum-window-substring.py
# Time:  O(n)
# Space: O(k), k is the number of different characters
# Hashtable
#
# Description: Leetcode # 76. Minimum Window Substring
#
# Given a string S and a string T, find the minimum window in S
# which will contain all the characters in T in complexity O(n).
#
# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".
#
# Note:
# If there is no such window in S that covers all characters in T, return the emtpy string "".
#
# If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
# Companies
# LinkedIn Snapchat Uber Facebook
# Related Topics
# Hash Table Two Pointers String
# Similar Questions
# Substring with Concatenation of All Words Minimum Size Subarray Sum
# Sliding Window Maximum Permutation in String Smallest Range
#
import unittest
import collections
class Solution:
    # @return a string
    def minWindow(self, S, T):
        current_count = [0 for i in xrange(52)] #Radix a-zA-Z -> 52
        expected_count = [0 for i in xrange(52)]

        for char in T:
            expected_count[ord(char) - ord('a')] += 1

        i, count, start, min_width, min_start = 0, 0, 0, float("inf"), 0
        while i < len(S):
            current_count[ord(S[i]) - ord('a')] += 1
            if current_count[ord(S[i]) - ord('a')] <= expected_count[ord(S[i]) - ord('a')]:
                count += 1

            if count == len(T):
                while expected_count[ord(S[start]) - ord('a')] == 0 or \
                      current_count[ord(S[start]) - ord('a')] > expected_count[ord(S[start]) - ord('a')]:
                    current_count[ord(S[start]) - ord('a')] -= 1
                    start += 1

                if min_width > i - start + 1:
                    min_width = i - start + 1
                    min_start = start
            i += 1

        if min_width == float("inf"):
            return ""

        return S[min_start:min_width+min_start]

class Solution2:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = ""
        len_s = len(s)
        len_t = len(t)
        dict = collections.defaultdict(int)
        cnt = 0
        minLen = float("inf")

        for i in xrange(len_t):
            dict[t[i]] += 1

        s_idx = 0
        for i in xrange(len_s):
            if s[i] in dict:
                dict[s[i]] -= 1

                if dict[s[i]] >= 0:
                    cnt += 1

            while cnt == len(t):
                if s[s_idx] in dict:
                    dict[s[s_idx]]  += 1

                    if dict[s[s_idx]] > 0:
                        if minLen > i - s_idx + 1:
                            minLen = i - s_idx + 1
                            res = s[s_idx: i+1]
                        cnt -= 1
                s_idx += 1
        return res

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        self.assertEqual("BANC", Solution2().minWindow("ADOBECODEBANC", "ABC"))
        self.assertEqual("BANC", Solution().minWindow("ADOBECODEBANC", "ABC"))

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/minimum-window-substring/solution/
# 25ms 52.80%
class Solution {
    public String minWindow(String s, String t) {
        String res = "";
        if(s == null || t == null || s.length() == 0 || t.length() == 0) return res;
        int minLen = Integer.MAX_VALUE;
        Map<Character, Integer> map = new HashMap<>();
        for( int i = 0; i < t.length(); i++){
            if(!map.containsKey(t.charAt(i))){
                map.put(t.charAt(i), 0);
            }
            map.put(t.charAt(i), map.get(t.charAt(i)) + 1);
        }
        int cnt = 0;
        int prev = 0;

        for(int i = 0 ; i < s.length(); i++){
            char c = s.charAt(i);
            if(map.containsKey(c)){
                map.put(c, map.get(c) - 1);
                if(map.get(c) >= 0){
                    cnt += 1;
                }
                while(cnt == t.length()){
                    char p = s.charAt(prev);
                    if(map.containsKey(p)){
                        map.put(p, map.get(p) + 1);

                        if(map.get(p) > 0){
                            if(minLen > i - prev + 1){
                                minLen = i - prev + 1;
                                res = s.substring(prev, i + 1);
                            }
                            cnt --;
                        }
                    }
                    prev ++;
                }
            }
        }
        return res;
    }
}

#76.01% 7ms
class Solution {
    public String minWindow(String s, String t) {
        int lenS = s.length();
        int lenT = t.length();
        if (lenS == 0 || lenT == 0) {
            return "";
        }
        int[] sCount = new int[128];
        int[] tCount = new int[128];
        int count = lenT;
        int[] result = new int[] {-1, -1};
        int start = 0;
        for (int i = 0; i < lenT; i++) {
            tCount[t.charAt(i)]++;
        }
        for (int i = 0; i < lenS; i++) {
            char c = s.charAt(i);
            sCount[c]++;
            if (sCount[c] <= tCount[c]) {
                count--;
            }
            if (count == 0) {
                while (true) {
                    char remove = s.charAt(start);
                    if (sCount[remove] <= tCount[remove]) {
                        break;
                    }
                    sCount[remove]--;
                    start++;
                }
                if (result[0] < 0 || result[1] - result[0] > i + 1 - start) {
                    result[0] = start;
                    result[1] = i + 1;
                }
                sCount[s.charAt(start++)]--;
                count++;
            }
        }
        return result[0] < 0 ? "" : s.substring(result[0], result[1]);
    }
}

# 4ms 96.63%
class Solution {
    public String minWindow(String s, String t) {
        if (s == null || t == null || s.length() == 0 || t.length() == 0) {
            return null;
        }
        int start = -1;
        int end = s.length() + 1;
        int left = 0;
        int windowSize = 0;
        int[] count = new int[256];
        for (char c : t.toCharArray()) {
            count[c]++;
        }
        for (int i = 0; i < s.length(); ++i) {
            if(--count[s.charAt(i)] >= 0) {
                windowSize++;
            }
            if (windowSize == t.length()) {
                while (++count[s.charAt(left)] <= 0) {
                    left++;
                }
                if (i - left < end - start) {
                    start = left;
                    end = i;
                }
                left++;
                windowSize--;
            }
        }
        return start == -1 ? "" : s.substring(start, end + 1);
    }
}
'''
