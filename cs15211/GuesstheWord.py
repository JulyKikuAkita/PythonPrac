import collections

__source__ = 'https://leetcode.com/problems/guess-the-word/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 843. Guess the Word
#
# This problem is an interactive problem new to the LeetCode platform.
#
# We are given a word list of unique words,
# each word is 6 letters long, and one word in this list is chosen as secret.
#
# You may call master.guess(word) to guess a word.
# The guessed word should have type string and must be from the original list with 6 lowercase letters.
#
# This function returns an integer type,
# representing the number of exact matches (value and position) of your guess to the secret word.
# Also, if your guess is not in the given wordlist, it will return -1 instead.
#
# For each test case, you have 10 guesses to guess the word.
# At the end of any number of calls,
# if you have made 10 or less calls to master.guess and at least one of these guesses was the secret,
# you pass the testcase.
#
# Besides the example test case below,
# there will be 5 additional test cases,
# each with 100 words in the word list.
# The letters of each word in those testcases were chosen independently at random from 'a' to 'z',
# such that every word in the given word lists is unique.
#
# Example 1:
# Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]
#
# Explanation:
#
# master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
# master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
# master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
# master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
# master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
#
# We made 5 calls to master.guess and one of them was the secret, so we pass the test case.
# Note:  Any solutions that attempt to circumvent the judge will result in disqualification.
#

import unittest

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

#20ms 100%
class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        for i in range(10):
            l = len(wordlist)
            word = wordlist[random.randint(0, l - 1)]
            n = master.guess(word)
            wordlist = [w for w in wordlist if sum(a == b for a, b in zip(w, word)) == n]

#24ms 70.57%
class Solution2(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        def same_match(w,i):
            return sum(m==n for m,n in zip(w,i))
        def most_match():
            count = [collections.defaultdict(int) for _ in range(6)]
            for word in candidates:
                for i,c in enumerate(word):
                    count[i][c]+=1
            return max(candidates, key = lambda x: sum(count[i][c] for i,c in enumerate(x)))
        candidates = wordlist[:]
        while candidates:
            w = most_match()
            s = master.guess(w)
            if s==6:
                return
            candidates = [i for i in candidates if same_match(w,i)==s]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/guess-the-word/solution/
Approach #1: Minimax with Heuristic [Accepted]
Complexity Analysis

Time Complexity: O(N^2 log N), where N is the number of words,
and assuming their length is O(1). Each call to solve is O(N^2),
and the number of calls is bounded by O(logN).
Space Complexity: O(N^2)


/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface Master {
 *     public int guess(String word) {}
 * }
 */

#2ms 92.21%
class Solution {
    public void findSecretWord(String[] wordlist, Master master) {
        Random rand = new Random();
        int x = 0, i = 0;
        while (i < 10 && x < 6) {
            int idx = rand.nextInt(wordlist.length);
            String cand = wordlist[idx];
            x = master.guess(cand);
            if (x == -1) continue;
            List<String> next = new ArrayList<>();
            for (String w: wordlist) {
                if (match(w, cand) == x) next.add(w);
            }
            i++;
            wordlist = next.toArray(new String[next.size()]);
        }
    }

    private int match(String s, String t) {
        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == t.charAt(i)) res++;
        }
        return res;
    }
}
'''