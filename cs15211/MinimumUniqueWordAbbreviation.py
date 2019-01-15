__source__ = 'https://leetcode.com/problems/minimum-unique-word-abbreviation/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/minimum-unique-word-abbreviation.py
# Time:  O(2^n)
# Space: O(n)
#
# Description: 411. Minimum Unique Word Abbreviation
#
# A string such as "word" contains the following abbreviations:
#
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# Given a target string and a set of strings in a dictionary,
# find an abbreviation of this target string with the smallest possible length such that
# it does not conflict with abbreviations of the strings in the dictionary.
#
# Each number or letter in the abbreviation is considered length = 1.
# For example, the abbreviation "a32bc" has length = 4.
#
# Note:
# In the case of multiple answers as shown in the second example below, you may return any one of them.
# Assume length of target string = m, and dictionary size = n.
# You may assume that m <= 21, n <= 1000, and log2(n) + m <= 20.
#
# Examples:
# "apple", ["blade"] -> "a4" (because "5" or "4e" conflicts with "blade")
#
# "apple", ["plain", "amber", "blade"] -> "1p3" (other valid answers include "ap3", "a3e", "2p2", "3le", "3l1").
# Hide Company Tags Google
# Hide Tags Backtracking Bit Manipulation
# Hide Similar Problems (M) Generalized Abbreviation (E) Valid Word Abbreviation (H) Word Abbreviation

import re
import unittest
# 47.83%
# https://discuss.leetcode.com/topic/61457/c-bit-manipulation-dfs-solution
# The key idea of my solution is to preprocess the dictionary to transfer all the words to bit sequences (int):
# Pick the words with same length as target string from the dictionary and compare the characters with target.
# If the characters are different, set the corresponding bit to 1, otherwise, set to 0.
# Ex: "abcde", ["abxdx", "xbcdx"] => [00101, 10001]
#
# The problem is now converted to find a bit mask that can represent the shortest abbreviation,
# so that for all the bit sequences in dictionary, mask & bit sequence > 0.
# Ex: for [00101, 10001], the mask should be [00001]. if we mask the target string with it,
# we get "****e" ("4e"), which is the abbreviation we are looking for.
#
# To find the bit mask, we need to perform DFS with some optimizations. But which bits should be checked?
# We can perform "or" operation for all the bit sequences in the dictionary and do DFS for the "1" bits in the result.
# Ex: 00101 | 10001 = 10101, so we only need to take care of the 1st, 3rd, and 5th bit.
#
# Please refer @topcoder007's post about the basic idea of bit manipulation.
#
# The idea is to find all valid masks with minimum bits set first, and then find the minimum abbreviation recursively.
# For each bit in a key built from diff of target and word, there could be below cases:
#
# If a bit is 0, which means the char in word is same as the corresponding char in target,
# the bit has no effect to the final result on this word
# If a bit is 1 and it is the only bit set, i.e. the only difference from target,
# then that char is required, i.e. the bit must be set in final result
# If there are 2 or more bits set, all the bits are optional,
# i.e. as long as one of them is set in final result,
# it will make the abbreviation distinct between target and this word.
# If a bit is optional for word1 but required for word2,
# we can ignore word1 because it is already covered by word2.
# For example "apple" ["xpple", "xpplx"] => [10000, 10001] => [10000] => "a4
# if a bit is optional for both word1 and word2, we can take that bit to cover both words and at same time,
# minimize the number of set bits. For example "apple" ["xppze", "xpplx"] => [10010, 10001] => [10000] => "a4
# Therefore, a valid abbreviation key will be [required bits] | [ a mask with minimum number of '1' which ensure
# at least one optional bit set for each word], steps as below:
#
# Generate keys for each word dictionary, if required (only 1 bit set), put it to required mask.
# If optional, put to the distinct list.
# Check all keys in distinct list, if covered by required , remove from the list
# Make all keys distinct, i.e. distinct[i] & distinct[j] == 0 if i != j
# For remaining keys in distinct, take required as base mask and then pick up 1 optional bit from each key recursively,
# and check the length of the abbreviation.
#
# 192ms 11.11%
class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        def bits_len(target, bits):
            return sum(((bits >> i) & 3) == 0 for i in xrange(len(target)-1))

        diffs = []
        for word in dictionary:
            if len(word) != len(target):
                continue
            diffs.append(sum(2**i for i, c in enumerate(word) if target[i] != c))

        if not diffs:
            return str(len(target))

        bits = 2**len(target) - 1
        for i in xrange(2**len(target)):
            if all(d & i for d in diffs) and bits_len(target, i) > bits_len(target, bits):
                bits = i

        abbr = []
        pre = 0
        for i in xrange(len(target)):
            if bits & 1:
                if i - pre > 0:
                    abbr.append(str(i - pre))
                pre = i + 1
                abbr.append(str(target[i]))
            elif i == len(target) - 1:
                abbr.append(str(i - pre + 1))
            bits >>= 1

        return "".join(abbr)

# If the target is apple and the dictionary contains apply, then the abbreviation must include the e as the letter e,
# not in a number. It's the only letter distinguishing these two words. Similarly, if the dictionary contains tuple,
# then the abbreviation must include the a or the first p as a letter.
#
# For each dictionary word (of correct size), I create a diff-number whose bits tell me
# which of the word's letters differ from the target. Then I go through the 2m possible abbreviations,
# represented as number from 0 to 2m-1, the bits representing which letters of target are in the abbreviation.
#  An abbreviation is ok if it doesn't match any dictionary word.
# To check whether an abbreviation doesn't match a dictionary word,
# I simply check whether the abbreviation number and the dictionary word's diff-number have a common 1-bit.
# Which means that the abbreviation contains a letter where the dictionary word differs from the target.
#
# Then from the ok abbreviations I find one that maximizes how much length it saves me.
# Two consecutive 0-bits in the abbreviation number mean
# that the two corresponding letters will be encoded as the number 2. It saves length 1.
# Three consecutive 0-bits save length 2, and so on. To compute the saved length,
# I just count how many pairs of adjacent bits are zero.
#
# Now that I have the number representing an optimal abbreviation,
# I just need to turn it into the actual abbreviation.
# First I turn it into a string
# where each 1-bit is turned into the corresponding letter of the target and each 0-bit is turned into #.
# Then I replace streaks of # into numbers.

# 100ms 11.11%
class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        m = len(target)
        diffs = {sum(2**i for i, c in enumerate(word) if target[i] != c)
            for word in dictionary if len(word) == m}

        if not diffs:
            return str(m)
        bits = max((i for i in range(2**m) if all(d & i for d in diffs)),
                key = lambda bits: sum((bits >> i) & 3 == 0 for i in range(m -1)))

        s = ''.join(target[i] if bits & 2**i else '#' for i in range(m))
        print s
        return re.sub('#+', lambda m : str(len(m.group())), s)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 5ms 100%
1. Bitmask + backtracking
class Solution {
    int n, cand, bn, minLen, minab;
    List<Integer> dict = new ArrayList<>();

    public String minAbbreviation(String target, String[] dictionary) {
        n = target.length(); bn = 1 << n; cand = 0; minLen = Integer.MAX_VALUE;
        StringBuilder res = new StringBuilder();
        for (String s : dictionary) {
            int word = 0;
            if (s.length() != n) continue;
            for (int i = 0; i < n; i++) {
                if (target.charAt(i) != s.charAt(i)) {
                    word |= 1 << i;
                }
            }
            dict.add(word);
            cand |= word;
        }
        dfs(1, 0);  // DFS : 1 -> 1010 -> 10101
                    //                 -> 10100
                    //         -> 1011 -> 10110

        for (int i = 0; i < n; ) {
            if ((minab & (1 << i)) != 0) {
                res.append(target.charAt(i++));
            }else {
               int j = i;
               while (i < n && (minab & (1 <<i)) == 0) i++;
               res.append(i-j);
            }
        }
        return res.toString();
    }

    // Abbreviation for one digit is meaningless, thus at least two digits are used for abbreviation.
    private int abbrLen(int mask){
        int count = n;
        for (int b = 3; b < bn; b <<= 1) {
            if ((mask & b) == 0) count--;
        }
        return count;
    }

    private void dfs(int bit, int mask){
        int len = abbrLen(mask);
        if ( len >= minLen) return;
        boolean match = true;
        for (Integer d : dict) {
            if ((mask & d) == 0) {
                match = false;
                break;
            }
        }
        if (match) {  // a mask which can cover all differences, no need to find more.
            minLen = len;
            minab = mask;
        } else {  // No ? Then has to add more masks to cover all differences.
            for (int b = bit; b < bn; b <<= 1) {
                if ((cand & b) != 0) {
                    dfs(b << 1, mask + b);
                }
            }
        }
    }
}


Abbreviation number is pretty like wild card and it can match all the characters appearing in the trie.
There's 3 functions:
addTrie: add string to the trie
search: search a string to determine if that's the one in the trie (wild card mode)
abbrGenerator: generate all the possible abbreviations given certain length (which is num parameter).

# Java DFS+Trie+Binary Search
# 84ms 36.43%
class Solution {
    class Node{ // Trie Node
        Node[] nodes;
        boolean isWord;
        Node(){
            nodes = new Node[26];
            isWord = false;
        }
        void add(String str){ // add a word to Trie
            if (str.length() == 0) isWord=true; // end of a word
            else {
                int idx = str.charAt(0)-'a'; // insert a new node
                if (nodes[idx] == null) nodes[idx] = new Node();
                nodes[idx].add(str.substring(1));
            }
        }
        boolean isAbbr(String abbr, int num){
            if ( num > 0){ // number of '*'
                for (Node node : nodes){
                    if (node != null && node.isAbbr(abbr, num-1)) return true;
                }
                return false; // not exist in the dictionary
            } else {
                if (abbr.length()==0) return isWord; // at the end of the addr
                int idx=0; // get the number of '*' at the start of the abbr
                while (idx < abbr.length() && abbr.charAt(idx) >='0' && abbr.charAt(idx) <='9' ) {
                    num = (num*10) + (abbr.charAt(idx++)-'0');
                }
                if (num>0) return isAbbr(abbr.substring(idx),num); // start with number
                else { // start with non-number
                    if (nodes[abbr.charAt(0)-'a'] != null )
                        return nodes[abbr.charAt(0)-'a'].isAbbr(abbr.substring(1), 0);
                    else return false; // not exist in the dictionary
                }
            }
        }
    }

    void getAbbs(char[] cc, int s, int len, StringBuilder sb, List<String> abbs){ //DFS with backtracking
        boolean preNum = (sb.length() > 0 ) && (sb.charAt(sb.length()-1) >= '0') && (sb.charAt(sb.length()-1) <= '9');
        if (len == 1)  {
            if ( s  < cc.length) {
                if (s==cc.length-1) abbs.add(sb.toString() + cc[s]); // add one char
                if (! preNum ) abbs.add(sb.toString() + (cc.length-s) ); // add a number
            }
        } else if (len > 1 ) {
            int last = sb.length();
            for (int i=s+1; i < cc.length; i++ ){
                if (! preNum) { // add a number
                    sb.append(i-s);
                    getAbbs(cc, i, len-1, sb, abbs);
                    sb.delete(last, sb.length());
                }
                if (i==s+1) { // add one char
                    sb.append(cc[s]);
                    getAbbs(cc, i, len-1, sb, abbs);
                    sb.delete(last, sb.length());
                }
            }
        }
    }

    public String minAbbreviation(String target, String[] dictionary) {
        List<String> dict = new ArrayList();
        int len = target.length();
        for (String str : dictionary) if (str.length() == len ) dict.add(str);
        if (dict.isEmpty()) return ""+len;
        Node root = new Node();
        for (String str : dict) root.add(str);
        char[] cc = target.toCharArray();
        String ret = null;

        int min = 1, max = len;
        while (max >= min) {
            int mid = min+( (max-min)/2 );
            List<String> abbs = new ArrayList();
            getAbbs(cc, 0, mid, new StringBuilder(), abbs);
            boolean conflict = true;
            for (String abbr: abbs){
                if ( ! root.isAbbr(abbr,0) ) {
                    conflict = false;
                    ret = abbr;
                    break;
                }
            }
            if (conflict) {
                min = mid+1;
            } else {
                max = mid-1;
            }
        }
        return ret;
    }
}

# 5ms 100%
class Solution {
    int n, cand, bn, minLen, minab;
    List<Integer> dict = new ArrayList<>();
    
    public String minAbbreviation(String target, String[] dictionary) {
        n = target.length(); bn = 1 << n; cand = 0; minLen = Integer.MAX_VALUE;
        StringBuilder res = new StringBuilder();
        for (String s : dictionary) {
            int word = 0;
            if (s.length() != n) continue;
            for (int i = 0; i < n; i++) {
                if (target.charAt(i) != s.charAt(i)) {
                    word |= 1 << i;
                }
            }
            dict.add(word);
            cand |= word;
        }
        dfs(1, 0);  // DFS : 1 -> 1010 -> 10101
                    //                 -> 10100
                    //         -> 1011 -> 10110
        
        for (int i = 0; i < n; ) {
            if ((minab & (1 << i)) != 0) {
                res.append(target.charAt(i++));
            }else {
               int j = i;
               while (i < n && (minab & (1 <<i)) == 0) i++;
               res.append(i-j);
            }
        }
        return res.toString();
    }
    
    // Abbreviation for one digit is meaningless, thus at least two digits are used for abbreviation.
    private int abbrLen(int mask){
        int count = n;
        for (int b = 3; b < bn; b <<= 1) {
            if ((mask & b) == 0) count--;
        }
        return count;
    }

    private void dfs(int bit, int mask){
        int len = abbrLen(mask);
        if ( len >= minLen) return;
        boolean match = true;
        for (Integer d : dict) {
            if ((mask & d) == 0) {
                match = false;
                break;
            }
        }
        if (match) {  // a mask which can cover all differences, no need to find more.
            minLen = len;
            minab = mask;
        } else {  // No ? Then has to add more masks to cover all differences.
            for (int b = bit; b < bn; b <<= 1) {
                if ((cand & b) != 0) {
                    dfs(b << 1, mask + b);
                }
            }
        }
    }
}
'''
