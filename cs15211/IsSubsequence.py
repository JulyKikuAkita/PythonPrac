__source__ = 'https://leetcode.com/problems/is-subsequence/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/is-subsequence.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 392. Is Subsequence
#
# Given a string s and a string t, check if s is subsequence of t.
#
# You may assume that there is only lower case English letters in both s and t.
# t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
#
# A subsequence of a string is a new string which is formed from
# the original string by deleting some (can be none) of the characters
# without disturbing the relative positions of the remaining characters.
# (ie, "ace" is a subsequence of "abcde" while "aec" is not).
#
# Example 1:
# s = "abc", t = "ahbgdc"
#
# Return true.
#
# Example 2:
# s = "axc", t = "ahbgdc"
#
# Return false.
#
# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B,
# and you want to check one by one to see if T has its subsequence.
# In this scenario, how would you change your code?
#
# Companies
# Pinterest
# Related Topics
# Binary Search Dynamic Programming Greedy
#
import unittest

# Greedy solution.
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True

        i = 0
        for c in t:
            if c == s[i]:
                i += 1
            if i == len(s):
                break
        return i == len(s)

    def isSubsequence2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t = iter(t)
        return all(c in t for c in s)


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
# two pointers:
#59.60% 37ms
public class Solution {
    public boolean isSubsequence(String s, String t) {
        if (s.length() == 0) return true;
        int indexS = 0, indexT = 0;
        while (indexT < t.length()) {
            if (t.charAt(indexT) == s.charAt(indexS)) {
                indexS++;
                if (indexS == s.length()) return true;
            }
            indexT++;
        }
        return false;
    }
}

#94.93% 3ms
public class Solution {
    public boolean isSubsequence(String s, String t) {
        if (s.length() == 0) return true;

        int prev = t.indexOf(s.charAt(0));
        if (prev == -1) return false;

        for (int i = 1; i < s.length(); i++) {
            prev = t.indexOf(s.charAt(i), prev + 1);
            if (prev == -1) return false;
        }
        return true;
    }
}

#96.90% 2ms
class Solution {
    public boolean isSubsequence(String s, String t) {
        int[] a = new int[s.length() + 1];
		a[0] = -1;
		for (int i = 0; i < s.length(); i++) {
			int index = t.indexOf(s.charAt(i), a[i] + 1);
			if (index == -1) {
				return false;
			}
			a[i + 1] = index;
		}
        return true;
    }
}

# quick examples fro java Collections.binarySearch(list, key)
# http://www.geeksforgeeks.org/collections-binarysearch-java-examples/
// Returns index of key in sorted list sorted in
// ascending order
public static int binarySearch(List slist, T key)

// Returns index of key in sorted list sorted in
// order defined by Comparator c.
public static int binarySearch(List slist, T key, Comparator c)

If key is not present, the it returns "(-(insertion point) - 1)".
The insertion point is defined as the point at which the key
would be inserted into the list.

public static void main(String[] args)
    {
        List al = new ArrayList();
        al.add(1);
        al.add(2);
        al.add(3);
        al.add(10);
        al.add(20);

        // 10 is present at index 3.
        int index = Collections.binarySearch(al, 10);
        System.out.println(index);

        // 13 is not present. 13 would have been inserted
        // at position 4. So the function returns (-4-1)
        // which is -5.
        index = Collections.binarySearch(al, 15);
        System.out.println(index);
    }

# 16.12% 60ms
Binary search solution for follow-up with detailed comments
Re: Java binary search using TreeSet got TLE

I think the Map and TreeSet could be simplified by Array and binarySearch.
Since we scan T from beginning to the end (index itself is in increasing order),
List will be sufficient. Then we can use binarySearch to replace with TreeSet
ability which is a little overkill for this problem. Here is my solution.

    // Follow-up: O(N) time for pre-processing, O(Mlog?) for each S.
    // Eg-1. s="abc", t="bahbgdca"
    // idx=[a={1,7}, b={0,3}, c={6}]
    //  i=0 ('a'): prev=1
    //  i=1 ('b'): prev=3
    //  i=2 ('c'): prev=6 (return true)
    // Eg-2. s="abc", t="bahgdcb"
    // idx=[a={1}, b={0,6}, c={5}]
    //  i=0 ('a'): prev=1
    //  i=1 ('b'): prev=6
    //  i=2 ('c'): prev=? (return false)

    public boolean isSubsequence(String s, String t) {
        List<Integer>[] idx = new List[256]; // Just for clarity
        for (int i = 0; i < t.length(); i++) {
            if (idx[t.charAt(i)] == null)
                idx[t.charAt(i)] = new ArrayList<>();
            idx[t.charAt(i)].add(i);
        }

        int prev = 0;
        for (int i = 0; i < s.length(); i++) {
            if (idx[s.charAt(i)] == null) return false; // Note: char of S does NOT exist in T causing NPE
            int j = Collections.binarySearch(idx[s.charAt(i)], prev);
            if (j < 0) j = -j - 1;
            if (j == idx[s.charAt(i)].size()) return false;
            prev = idx[s.charAt(i)].get(j) + 1;
        }
        return true;
    }
'''