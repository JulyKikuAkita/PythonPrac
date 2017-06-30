__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/palindrome-permutation.py
# Time:  O(n)
# Space: O(1)
#
# Given a string, determine if a permutation of the string could form a palindrome.
#
# For example,
# "code" -> False, "aab" -> True, "carerac" -> True.
#
# Hint:
#
# Consider the palindromes of odd vs even length. What difference do you notice?
# Count the frequency of each character.
# If each character occurs even number of times, then it must be a palindrome. How about character which occurs odd number of times?
#
# #count of  odd number char < 2
#  Google Uber Bloomberg
# Hide Tags Hash Table
# Hide Similar Problems (M) Longest Palindromic Substring (E) Valid Anagram (M) Palindrome Permutation II (E) Longest Palindrome
#

import collections
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #         print collections.Counter(s).values()
        return sum(v % 2 for v in collections.Counter(s).values()) < 2


from collections import defaultdict
class Solution2(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = defaultdict(int)
        for char in s:
            dict[char] = dict[char] + 1

        odd = 0
        for cnt in dict.values():
            if cnt % 2 == 1:
                odd += 1
            if odd > 1:
                return False

        return True

# Java solution
java = '''
https://leetcode.com/articles/palindrome-permutation/
Time complexity : O(n). We traverse over the string ss of length nn once only.
Space complexity : O(n). The setset can grow upto a maximum size of nn in case of all distinct elements.

The idea is to iterate over string, adding current character to set if set doesn't contain that character,
 or removing current character from set if set contains it.
When the iteration is finished, just return set.size()==0 || set.size()==1.

set.size()==0 corresponds to the situation when there are even number of any character in the string, and
set.size()==1 corresponsds to the fact that there are even number of any character except one.

public class Solution {
    public boolean canPermutePalindrome(String s) {
        Set<Character> set=new HashSet<Character>();
        for(int i=0; i<s.length(); ++i){
            if (!set.contains(s.charAt(i)))
                set.add(s.charAt(i));
            else
                set.remove(s.charAt(i));
        }
        return set.size()==0 || set.size()==1;
    }
}

public boolean canPermutePalindrome(String s) {
    BitSet bs = new BitSet();
    for (byte b : s.getBytes())
        bs.flip(b);
    return bs.cardinality() < 2;
}

#count char with boolean[128]
public class Solution {
    public boolean canPermutePalindrome(String s) {
        boolean[] arr = new boolean[128];
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            arr[c] = !arr[c];
        }
        boolean odd = false;
        for (int i = 0; i < 128; i++) {
            if (arr[i]) {
                if (odd) {
                    return false;
                } else {
                    odd = true;
                }
            }
        }
        return true;
    }
}

'''

