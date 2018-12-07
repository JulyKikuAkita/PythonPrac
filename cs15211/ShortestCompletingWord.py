__source__ = 'https://leetcode.com/problems/shortest-completing-word/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 748. Shortest Completing Word
#
# Find the minimum length word from a given dictionary words,
# which has all the letters from the string licensePlate.
# Such a word is said to complete the given string licensePlate
#
# Here, for letters we ignore case.
# For example, "P" on the licensePlate still matches "p" on the word.
#
# It is guaranteed an answer exists.
# If there are multiple answers, return the one that occurs first in the array.
#
# The license plate might have the same letter occurring multiple times.
# For example, given a licensePlate of "PP", the word "pair" does not complete the licensePlate,
# but the word "supper" does.
#
# Example 1:
# Input: licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
# Output: "steps"
# Explanation: The smallest length word that contains the letters "S", "P", "S", and "T".
# Note that the answer is not "step", because the letter "s" must occur in the word twice.
# Also note that we ignored case for the purposes of comparing whether a letter exists in the word.
# Example 2:
# Input: licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
# Output: "pest"
# Explanation: There are 3 smallest length words that contains the letters "s".
# We return the one that occurred first.
# Note:
# licensePlate will be a string with length in range [1, 7].
# licensePlate will contain digits, spaces, or letters (uppercase or lowercase).
# words will have a length in the range [10, 1000].
# Every words[i] will consist of lowercase letters, and have length in range [1, 15].
#
import unittest

# 48ms 96.76%
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        plate = [c.lower() for c in licensePlate if c.isalpha()]
        s= set(plate)
        words.sort(key = lambda x : len(x))
        for item in words:
            if all( plate.count(l) <= item.count(l) for l in s):
                return item

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/shortest-completing-word/solution/
Approach #1: Compare Counts [Accepted]
Complexity Analysis
Time Complexity: O(N) where N is the length of words,
and assuming the lengths of licensePlate and words[i] are bounded by O(1)
Space Complexity: O(1) in additional space.

#7ms 95.64%
class Solution {
    public String shortestCompletingWord(String licensePlate, String[] words) {
        int[] target = count(licensePlate);
        String ans = "";
        for (String word: words) {
            if ((word.length() < ans.length() || ans.length() == 0) &&
                dominates(count(word.toLowerCase()), target)) {
                ans = word;
            }
        }
        return ans;
    }

    private boolean dominates(int[] count1, int[] count2) {
        for (int i = 0; i < 26; i++) {
            if (count1[i] < count2[i]) return false;
        }
        return true;
    }

    private int[] count(String word) {
        int[] ans = new int[26];
        for (char c: word.toCharArray()) {
            int index = Character.toLowerCase(c) - 'a';
            if (0 <= index && index < 26) {
                ans[index]++;
            }
        }
        return ans;
    }
}

# 5ms 100%
class Solution {
    private static final int[] primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103};

    public String shortestCompletingWord(String licensePlate, String[] words) {
        long charProduct = getCharProduct(licensePlate.toLowerCase());
        String shortest = "aaaaaaaaaaaaaaaaaaaa"; // 16 a's
        for(String word : words)
            if (word.length() < shortest.length() && getCharProduct(word) % charProduct == 0)
                    shortest = word;
        return shortest;
    }

    private long getCharProduct(String plate) {
        long product = 1L;
        for(char c : plate.toCharArray()) {
            int index = c - 'a';
            if (0 <= index && index <= 25)
                product *= primes[index];
        }
        return product;
    }
}
'''