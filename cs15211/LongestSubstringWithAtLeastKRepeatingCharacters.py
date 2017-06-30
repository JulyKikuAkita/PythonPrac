__source__ = 'https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/#/description'
# Time:  O(26 * n) = O(n)
# Space: O(26) = O(1)

#
# Description:
# Find the length of the longest substring T of a given string
# (consists of lowercase letters only) such that every character in T
# appears no less than k times.
#
# Example 1:
#
# Input:
# s = "aaabb", k = 3
#
# Output:
# 3
#
# The longest substring is "aaa", as 'a' is repeated 3 times.
# Example 2:
#
# Input:
# s = "ababbc", k = 2
#
# Output:
# 5
#
# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
#  Baidu

# Recursive solution.
import unittest

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def longestSubstringHelper(s, k, start, end):
            count = [0] * 26
            for i in xrange(start, end):
                count[ord(s[i]) - ord('a')] += 1
            max_len = 0
            i = start
            while i < end:
                while i < end and count[ord(s[i]) - ord('a')] < k:
                    i += 1
                j = i
                while j < end and count[ord(s[j]) - ord('a')] >= k:
                    j += 1

                if i == start and j == end:
                    return end - start

                max_len = max(max_len, longestSubstringHelper(s, k, i, j))
                i = j
            return max_len

        return longestSubstringHelper(s, k, 0, len(s))
# If every character appears at least k times, the whole string is ok.
# Otherwise split by a least frequent character
# (because it will always be too infrequent and thus can't be part of any ok substring)
# and make the most out of the splits.

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
Java divide and conquer(recursion) solution
100%
public class Solution {
   //395. Longest Substring with At Least K Repeating Characters

   private int findLongestSub(String s, int k, int start, int end) {
       //count frequency of char over [start, end]
	   if (end < start) {
		   return 0;
	   }
	   int[] countArray = new int[26];
	   for (int i = start; i <= end; i++) {
		   char c = s.charAt(i);
		   int index = c- 'a';
		   countArray[index]++;
	   }

	   //define a valid array isValid, isValid[i] = true if character c(i=c-'a')
	   //has at least k occurences

	   boolean[] isValid = new boolean[26];

	   //boolean fullValid to flag whether all characters over [start, end]
	   //have frequency >= k
	   boolean fullValid = true;
	   for (int i = 0; i < 26; i++) {
		   if (countArray[i] > 0 && countArray[i] < k) {
			   //find a character with freq < k
			   isValid[i] = false;
			   fullValid = false;
		   }
		   else {
			   //the freq >= k
			   isValid[i] = true;
		   }

	   }

	   if (fullValid) {
		   return end-start+1;
	   }

	   //start to check from start to end
	   //if at index i, we find a character that has freq less than k
	   // we treat it as a separator and check the left substring
	   //from start up to
	   //this character(exclusive)
	   //and the right substring at i+1(i is the chr

	   //define last start that will be the starting point

	   int lastStart = start;
	   int length = 0;
	   for (int i = start; i <= end; i++) {
		   char c = s.charAt(i);
		   int index = c-'a';
		   if (isValid[index] == false) {
			   /*System.out.println("char is " + c);
			   System.out.println("last start is " + lastStart);
			   System.out.println("end is " + (i-1));*/
			   length = Math.max(length, findLongestSub(s, k, lastStart, i-1));
			   //update lastStart to be i+1 (start checking the right substring
			   lastStart = i+1;
		   }
	   }

	   //at the end if there is no invalid character
	   //we get the length of the qualified string
	   //note this step is important otherwise we will miss a qualified substring
	   length = Math.max(length,  findLongestSub(s,k, lastStart, end));

	   return length;
   }
   public int longestSubstring(String s, int k) {
	   //store the frequency of each character in s
	   //if a character has frequency that is less than k
	   //we cannot include that character in our candidate substring
	   //it must be excluded, treat that character as the separator and search within
	   //the left substring[start, i) and right substring [i+1, end]
	   //where i is the index of that separator
	   //and compare the result length
	   //a candidate string cannot contain characters with overall frequency < k


	   return findLongestSub(s, k, 0, s.length()-1);
   }
}

36%
public class Solution {
    public int longestSubstring(String s, int k) {
        char[] str = s.toCharArray();
        return dfs(str, 0, s.length(), k);
    }

    public int dfs(char[] str, int start, int end, int k) {
        if (end - start < k) return 0;

        int[] count = new int[26];
        for (int i = start; i < end; i++) {
            int idx = str[i] - 'a';
            count[idx]++;
        }

        for (int i = 0; i < 26; i++) {
            if (count[i] < k  && count[i] > 0) {
                for (int j = start; j < end; j++) {
                    if (str[j] == i + 'a') {
                        int left = dfs(str, start, j, k);
                        int right = dfs(str, j + 1, end, k);
                        return Math.max(left, right);
                    }
                }
            }
        }
        return end - start;
    }
}
'''