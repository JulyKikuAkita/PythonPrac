__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/palindrome-permutation.py
# Time:  O(n)
# Space: O(1)
'''Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

Hint:

Consider the palindromes of odd vs even length. What difference do you notice?
Count the frequency of each character.
If each character occurs even number of times, then it must be a palindrome. How about character which occurs odd number of times?

#count of  odd number char < 2

'''


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
# http://blog.csdn.net/pointbreak1/article/details/48766113

