__author__ = 'July'
'''
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

For example:

Given s = "aabb", return ["abba", "baab"].

Given s = "abc", return [].
Google Uber

'''

# https://github.com/kamyu104/LeetCode/blob/master/Python/palindromePermutationii.py
# Time:  O(n * n!)
# Space: O(n)
import collections
import itertools
class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cnt = collections.Counter(s)
        mid = ''.join(k for k, v in cnt.iteritems() if v % 2 )
        chars = ''.join(k * (v / 2) for k , v in cnt.iteritems())
        return self.permuteUnique(mid, chars) if len(mid) < 2 else []

    def permuteUnique(self, mid, nums):
        result = []
        used = [False] * len(nums)
        self.permuteUniqueRecu(mid, result, used, [], nums)
        return result

    def permuteUniqueRecu(self, mid, result, used, cur, nums):
        if len(cur) == len(nums):
            half_palindrome = ''.join(cur)
            result.append(half_palindrome + mid + half_palindrome[::-1])
            return
        for i in xrange(len(nums)):
            if not used[i] and not (i > 0 and nums[i - 1] == nums[i] and used[i - 1]):
                used[i] = True
                cur.append(nums[i])
                self.permuteUniqueRecu(mid, result, used, cur, nums)
                cur.pop()
                used[i] = False

class Solution2(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cnt = collections.Counter(s)
        mid = tuple(k for k, v  in cnt.iteritems() if v % 2)
        chars = ''.join(k * (v / 2) for k ,v in cnt.iteritems())

        return [''.join(half_palindrome + mid + half_palindrome[::-1]) \
                for half_palindrome in set(itertools.permutations(chars))] if len(mid) < 2 else []


class Solution(3object):
    def __init__(self):
        self.res = []
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s) == 0:
            return []
        elif len(s) == 1:
            return [s]

        dict = collections.defaultdict(int)
        can = ""
        single = ""
        for c in s:
            dict[c] += 1

        for key in dict:
            if dict[key] % 2 != 0:
                single += key
                if len(single) > 1:
                    return []

            num = dict[key] / 2
            for i in xrange(num):
                can += key

        if len(can) == 0 and len(single) == 1:
            return [single]


        for i in xrange(len(can)):
            if i > 0 and can[i] == can[i-1]:
                continue
            self.dfs(can[i], can[:i]+can[i+1:], len(can), single)
        return self.res

    def dfs(self, left, can, length, single):
        if len(left) == length:
            self.res.append(left + single+ left[::-1])
            return
        for i in xrange(len(can)):
            if i > 0 and can[i] == can[i-1]:
                continue
            self.dfs(left + can[i], can[:i]+can[i+1:], length, single)
        return self.res


#JAVA solution
# http://blog.csdn.net/pointbreak1/article/details/48779125
# diff way :http://buttercola.blogspot.com/2015/09/leetcode-palindrome-permutation-ii.html