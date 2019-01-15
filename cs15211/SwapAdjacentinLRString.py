__source__ = 'https://leetcode.com/problems/swap-adjacent-in-lr-string/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 777. Swap Adjacent in LR String
#
# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL",
# a move consists of either replacing one occurrence of "XL" with "LX",
# or replacing one occurrence of "RX" with "XR".
# Given the starting string start and the ending string end,
# return True if and only if there exists a sequence of moves to transform one string to the other.
#
# Example:
#
# Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
# Output: True
# Explanation:
# We can transform start to end following these steps:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
#
# Note:
#     1 <= len(start) = len(end) <= 10000.
#     Both start and end will only consist of characters in {'L', 'R', 'X'}.
#
import unittest
import itertools
# 40ms 96.45%
class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        # For (i, x) and (j, y) in enumerate(start), enumerate(end)
        # where x != 'X' and y != 'X',
        # and where if one exhausts early, it's elements are (None, None),...
        for (i, x), (j, y) in itertools.izip_longest(
                ((i, x) for i, x in enumerate(start) if x != 'X'),
                ((j, y) for j, y in enumerate(end) if y != 'X'),
                fillvalue = (None, None)):

            # If not solid or accessible, return False
            if x != y or (x == 'L' and i < j) or (x == 'R' and i > j):
                return False
        return True

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/swap-adjacent-in-lr-string/solution/
#
Approach #1: Invariant [Accepted]
Complexity Analysis
Time Complexity: O(N), where N is the length of start and end.
Space Complexity: O(N). The replacement operation is O(N), 
while the remaining operations use O(1) additional space. 
We could amend the replace part of our algorithm to use pointers so as to reduce the total complexity to O(1)

# 24ms 35.91%
class Solution {
    public boolean canTransform(String start, String end) {
        if (!start.replace("X", "").equals(end.replace("X", ""))) return false;
        int t = 0;
        for (int i = 0; i < start.length(); i++) {
            if (start.charAt(i) == 'L') {
                while(end.charAt(t) != 'L') t++;
                if (i < t++) return false;
            }
        }
        
        t = 0;
        for (int i = 0; i < start.length(); i++) {
            if (start.charAt(i) == 'R') {
                while (end.charAt(t) != 'R') t++;
                if (i > t++) return false;
            }
        }
        return true;
    }
}

Approach #2: Two Pointers [Accepted]
Complexity Analysis
Time Complexity: O(N), where N is the length of start and end.
Space Complexity: O(1)

# 5ms 98.26%
class Solution {
    public boolean canTransform(String start, String end) {
        int N = start.length();
        char[] S = start.toCharArray(), T = end.toCharArray();
        int i = -1, j = -1;
        while (++i < N && ++j < N) {
            while (i < N && S[i] == 'X') i++;
            while (j < N && T[j] == 'X') j++;
            /* At this point, i == N or S[i] != 'X',
               and j == N or T[j] != 'X'.  i and j
               are the indices representing the next
               occurrences of non-X characters in S and T.
            */

            // If only one of i < N and j < N, then it isn't solid-
            // there's more people in one of the strings.
            if ((i < N) ^ (j < N)) return false;
            if (i < N && j < N) {
                // If the person isn't the same, it isn't solid.
                // Or, if the person moved backwards, it isn't accessible.
                if (S[i] != T[j] || (S[i] == 'L' && i < j) ||
                        (S[i] == 'R' && i > j) )
                    return false;
            }
        }
        return true;
    }
}

# 7ms 77,80%
class Solution {
    public boolean canTransform(String start, String end) {
        // the Two string should be the same after removing all the 'X'
        
        // XL to LX --> L will only move the the left
        // RX to XR --> R will only move the the right
        
        // so, the position of R in the end String should >= that in the start String
        // the position of L in the end String should <= that in the start String
        
        char[] s = start.toCharArray();
        char[] e = end.toCharArray();
        int n = s.length;
        int i = 0;
        int j = 0;
        while (i < n && j < n) {
            // (1) ignore 'X'
            while (i < n && s[i] == 'X') {
                i++;
            }
            while (j < n && e[j] == 'X') {
                j++;
            }
            
            // (2) check end of the string or not
            if (i == n && j == n) {
                return true;
            }
            if (i == n || j == n) {
                return false;
            }
            
            // (3) check character is the same or not
            if (s[i] != e[j]) {     // s[i] and e[i] should all be 'L' or all be 'R'
                return false;
            }
            
            // (4) check character index support the rule or not.
            if (s[i] == 'L' && i < j) {
                return false;
            }
            if (s[i] == 'R' && i > j) {
                return false;
            }
            
            i++;
            j++;
        }
        return true;
    
    }
}


'''
