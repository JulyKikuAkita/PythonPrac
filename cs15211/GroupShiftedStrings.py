__author__ = 'July'
'''
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd".
We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets,
group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Return:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
Note: For the return value, each inner list's elements must follow the lexicographic order.

Show Company Tags: google, uber
'''
# https://github.com/kamyu104/LeetCode/blob/master/Python/group-shifted-strings.py
# Time:  O(nlogn)
# Space: O(n)
import collections
class Solution:
    # @param {string[]} strings
    # @return {string[][]}
    def groupStrings(self, strings):
        groups = {};
        for s in strings: #Grouping
            if self.hashStr(s) not in groups:
                groups[self.hashStr(s)] = [s]
            else:
                groups[self.hashStr(s)].append(s)
        result = []
        for key, val in groups.iteritems():
            result.append(sorted(val))
        return result



    def hashStr(self, s):
        base = ord(s[0])
        hashcode = ""
        for i in xrange(len(s)):
            #if ord(s[i]) - base >= 0:
            #    hashcode += unichr(ord('a') + ord(s[i]) - base)
            #else:
            hashcode += unichr(ord('a') + ((ord(s[i]) - base + 26) % 26))
        return hashcode

class Solution2(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        d = collections.defaultdict(list)
        for s in strings:
            shift = tuple([(ord(c) - ord(s[0])) % 26 for c in s])
            d[shift].append(s)

        return map(sorted, d.values())


#TEST
in1 = \
["abc", "txb", "def" , "i", \
"d", "nw", "e", "g", "h"]
print Solution().groupStrings(in1)

# java:
# http://blog.csdn.net/pointbreak1/article/details/48780345