__source__ = 'https://leetcode.com/problems/bulls-and-cows/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/bulls-and-cow.py
# Time:  O(n)
# Space: O(10) = O(1)
#
# Description: Leetcode # 299. Bulls and Cows
#
# You are playing the following Bulls and Cows game with your friend:
# You write a 4-digit secret number and ask your friend to guess it,
# each time your friend guesses a number, you give a hint, the hint
# tells your friend how many digits are in the correct positions
# (called "bulls") and how many digits are in the wrong positions
# (called "cows"), your friend will use those hints to find out the
# secret number.
#
# For example:
#
# Secret number:  1807
# Friend's guess: 7810
#
# Hint: 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)
# According to Wikipedia: "Bulls and Cows (also known as Cows and Bulls
# or Pigs and Bulls or Bulls and Cleots) is an old code-breaking mind or
# paper and pencil game for two or more players, predating the similar
# commercially marketed board game Mastermind. The numerical version of
# the game is usually played with 4 digits, but can also be played with
# 3 or any other number of digits."
#
# Write a function to return a hint according to the secret number and
# friend's guess, use A to indicate the bulls and B to indicate the cows,
# in the above example, your function should return 1A3B.
#
# You may assume that the secret number and your friend's guess only contain
# digits, and their lengths are always equal.
#
# Related Topics
# Hash Table
#
# One pass solution.
from collections import defaultdict
from itertools import izip
import unittest
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A, B = 0, 0
        s_lookup, g_lookup = defaultdict(int), defaultdict(int)
        for s, g  in izip(secret, guess):
            if s == g:
                A += 1
            else:
                if s_lookup[g]:
                    s_lookup[g] -= 1
                    B += 1
                else:
                    g_lookup[g] += 1
                if g_lookup[s]:
                    g_lookup[s] -= 1
                    B += 1
                else:
                    s_lookup[s] += 1

        return "%dA%dB" % (A, B)

# Two pass solution.
# imap: https://pymotw.com/2/itertools/
# The imap() function returns an iterator that calls a function on the values in the input iterators,
# and returns the results. It works like the built-in map(), except that it stops when any input iterator
# is exhausted (instead of inserting None values to completely consume all of the inputs).
# Counter: https://pymotw.com/2/collections/counter.html
# A Counter is a container that keeps track of how many times equivalent values are added.
from collections import Counter
from itertools import imap
import operator

class Solution2(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = sum(imap(operator.eq, secret, guess))
        B = sum((Counter(secret) & Counter(guess)).values()) - A
        return "%dA%dB" % (A, B)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
#45.77% 4ms
public class Solution {
    public String getHint(String secret, String guess) {
        // assume not null and equal length
        int bull = 0;
        int cow = 0;
        int[] secretArr = new int[10];
        int[] guessArr = new int[10];
        for (int i = 0; i < secret.length(); i++) {
            if (secret.charAt(i) == guess.charAt(i)) {
                bull++;
            } else {
                int secretNum = (int) (secret.charAt(i) - '0');
                int guessNum = (int) (guess.charAt(i) - '0');
                secretArr[secretNum]++;
                guessArr[guessNum]++;
                if (guessArr[secretNum] > 0) {
                    guessArr[secretNum]--;
                    secretArr[secretNum]--;
                    cow++;
                }
                if (secretArr[guessNum] > 0) {
                    secretArr[guessNum]--;
                    guessArr[guessNum]--;
                    cow++;
                }
            }
        }

        return "" + bull + "A" + cow + "B";
    }
}

#67.08% 3ms
public class Solution {
    public String getHint(String secret, String guess) {
        char[] seChar = secret.toCharArray();
        char[] guChar = guess.toCharArray();
        int[] countOfNum = new int[10];
        int bulls = 0;
        for(int i = 0; i < secret.length(); i++){
            if(secret.charAt(i) == guess.charAt(i))
                bulls++;
            countOfNum[seChar[i]-'0']++;
            countOfNum[guChar[i]-'0']--;
        }

        int sum = 0;
        for(int x : countOfNum){
            if(x > 0) sum += x;
        }


        return bulls + "A" + (secret.length() - sum - bulls) + "B";
    }
}
'''