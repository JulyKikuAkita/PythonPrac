__source__ = 'https://leetcode.com/problems/find-smallest-letter-greater-than-target/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 744. Find Smallest Letter Greater Than Target
#
# Given a list of sorted characters letters containing only lowercase letters,
# and given a target letter target,
# find the smallest element in the list that is larger than the given target.
#
# Letters also wrap around.
# For example,
# if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.
#
# Examples:
# Input:
# letters = ["c", "f", "j"]
# target = "a"
# Output: "c"
#
# Input:
# letters = ["c", "f", "j"]
# target = "c"
# Output: "f"
#
# Input:
# letters = ["c", "f", "j"]
# target = "d"
# Output: "f"
#
# Input:
# letters = ["c", "f", "j"]
# target = "g"
# Output: "j"
#
# Input:
# letters = ["c", "f", "j"]
# target = "j"
# Output: "c"
#
# Input:
# letters = ["c", "f", "j"]
# target = "k"
# Output: "c"
# Note:
# letters has a length in range [2, 10000].
# letters consists of lowercase letters, and contains at least 2 unique letters.
# target is a lowercase letter.
#
import unittest

# 56ms 18.71%
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        seen = set(letters)
        for i in xrange(1, 26):
            cand = chr((ord(target) - ord('a') + i) % 26 + ord('a'))
            if cand in seen:
                return cand

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/find-smallest-letter-greater-than-target/solution/
Approach #1: Record Letters Seen [Accepted]
Complexity Analysis
Time Complexity: O(N), where N is the length of letters. We scan every element of the array.
Space Complexity: O(1), the maximum size of seen.

# 9ms 32.72%
class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        boolean[] seen = new boolean[26];
        for (char c: letters) seen[c - 'a'] = true;
        while (true) {
            target++;
            if (target > 'z') target = 'a';
            if (seen[target - 'a']) return target;
        }

    }
}

Approach #2: Linear Scan [Accepted]
Complexity Analysis
Time Complexity: O(N), where N is the length of letters. We scan every element of the array.
Space Complexity: O(1), as we maintain only pointers.

# 8ms 42.86%
class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        for (char c : letters) {
            if (c > target) return c;
        }
        return letters[0];
    }
}

Approach #3: Binary Search [Accepted]
Complexity Analysis
Time Complexity: O(logN), where N is the length of letters.
We peek only at logN elements in the array.
Space Complexity: O(1), as we maintain only pointers.

# 5ms 99.63%
class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        int lo = 0, hi = letters.length;
        while (lo + 1 < hi) {
            int mid = lo + (hi - lo) / 2;
            if (letters[mid] <= target) lo = mid;
            else hi = mid;
        }
        return letters[(lo) % letters.length]  > target ? letters[(lo) % letters.length] : letters[(lo + 1) % letters.length];
    }
}

# 6ms 76.68%
class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        int lo = 0, hi = letters.length;
        while (lo < hi) {
            int mi = lo + (hi - lo) / 2;
            if (letters[mi] <= target) lo = mi + 1;
            else hi = mi;
        }
        return letters[lo % letters.length];
    }
}
'''