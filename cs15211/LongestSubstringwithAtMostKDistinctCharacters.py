__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/longest-substring-with-at-most-k-distinct-characters.py
# Given a string, find the length of the longest substring T
# that contains at most k distinct characters.
#
# For example, Given s = "eceba", k = 2,
#
# T is "ece" which its length is 3.

# Google
# hashtable, String

#  Time:  O(n)
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

#java
js = '''
public class Solution {
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