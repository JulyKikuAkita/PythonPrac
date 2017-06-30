__source__ = 'https://github.com/kamyu104/LeetCode/blob/master/Python/sentence-screen-fitting.py'
# Time:  O(r + n * c)
# Space: O(n)
#
# Description:
# Given a rows x cols screen and a sentence represented by a list of non-empty words,
# find how many times the given sentence can be fitted on the screen.
#
# Note:
#
# A word cannot be split into two lines.
# The order of words in the sentence must remain unchanged.
# Two consecutive words in a line must be separated by a single space.
# Total words in the sentence won't exceed 100.
# Length of each word is greater than 0 and won't exceed 10.
# 1 <= rows, cols <= 20,000.
# Example 1:
#
# Input:
# rows = 2, cols = 8, sentence = ["hello", "world"]
#
# Output:
# 1
#
# Explanation:
# hello---
# world---
#
# The character '-' signifies an empty space on the screen.
# Example 2:
#
# Input:
# rows = 3, cols = 6, sentence = ["a", "bcd", "e"]
#
# Output:
# 2
#
# Explanation:
# a-bcd-
# e-a---
# bcd-e-
#
# The character '-' signifies an empty space on the screen.
# Example 3:
#
# Input:
# rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]
#
# Output:
# 1
#
# Explanation:
# I-had
# apple
# pie-I
# had--
#
# The character '-' signifies an empty space on the screen.
# Hide Company Tags Google
# Hide Tags Dynamic Programming

import unittest

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        def words_fit(sentence, start, cols):
            if len(sentence[start]) > cols:
                return 0

            s, count = len(sentence[start]), 1
            i = (start + 1) % len(sentence)
            while s + 1 + len(sentence[i]) <= cols:
                s += 1 + len(sentence[i])
                count += 1
                i = (i + 1) % len(sentence)
            return count

        wc = [0] * len(sentence)
        for i in xrange(len(sentence)):
            wc[i] = words_fit(sentence, i, cols)

        words, start = 0, 0
        for i in xrange(rows):
            words += wc[start]
            start = (start + wc[start]) % len(sentence)
        return words / len(sentence)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
Say sentence=["abc", "de", "f], rows=4, and cols=6.
The screen should look like

"abc de"
"f abc "
"de f  "
"abc de"
Consider the following repeating sentence string, with positions of the start character of each row on the screen.

"abc de f abc de f abc de f ..."
 ^      ^     ^    ^      ^
 0      7     13   18     25
Our goal is to find the start position of the row next to the last row on the screen, which is 25 here.
Since actually it's the length of everything earlier,
we can get the answer by dividing this number by the length of (non-repeated) sentence string.
Note that the non-repeated sentence string has a space at the end; it is "abc de f " in this example.

Here is how we find that position. In each iteration, we need to adjust start based on spaces either added or removed.

"abc de f abc de f abc de f ..." // start=0
 012345                          // start=start+cols+adjustment=0+6+1=7 (1 space removed in screen string)
        012345                   // start=7+6+0=13
              012345             // start=13+6-1=18 (1 space added)
                   012345        // start=18+6+1=25 (1 space added)
                          012345



public class Solution {
    public int wordsTyping(String[] sentence, int rows, int cols) {
        String s = String.join(" ", sentence) + " ";
        int start = 0, l = s.length();
        for (int i = 0; i < rows; i++) {
            start += cols;
            if (s.charAt(start % l) == ' ') {
                start++;
            } else {
                while (start > 0 && s.charAt((start-1) % l) != ' ') {
                    start--;
                }
            }
        }

        return start / s.length();
    }
}











'''