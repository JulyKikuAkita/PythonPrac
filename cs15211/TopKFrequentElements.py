__author__ = 'July'
'''
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        res = []
        for num in nums:
            if num not in dict:
                dict[num] = 0
            dict[num] += 1
        i = 0
        for w in sorted(dict, key = dict.get,reverse = True):
            res.append(w)
            i += 1
            if i == k:
                break
        return res