__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/compare-version-numbers.py
# Time:  O(n)
# Space: O(1)
#
# Compare two version numbers version1 and version1.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
#
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
#
# Here is an example of version numbers ordering:
#
# 0.1 < 1.1 < 1.2 < 13.37
#

# Time:  O(n)
# Space: O(n), this could be enhanced to O(1) by better but trivial string parsing
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a boolean
    def compareVersion(self, version1, version2):
        v1, v2 = version1.split("."), version2.split(".")

        if len(v1) > len(v2):
            v2 += ['0' for _ in xrange(len(v1) - len(v2)) ]
        elif len(v1) < len(v2):
            v1 += ['0' for _ in xrange(len(v2) - len(v1))]

        #'''
        i = 0
        while i < len(v1):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
            else:
                i += 1
        return 0
        #'''


        '''
        for i in xrange(len(v1)):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
        return 0
        '''


if __name__ == "__main__":
    print Solution().compareVersion("21.0", "121.1.0")
    print Solution().compareVersion("01", "1")
    print Solution().compareVersion("1", "1.0")



# http://bookshadow.com/weblog/2014/12/17/leetcode-compare-version-numbers/
class SolutionOther:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        #in case of "01"
        nv1 = version1
        nv2 = version2
        if len(version1) > 1 and version1[0] == '0' and version1[1] != '.' :
            nv1 = version1[1:]
        if len(version2) > 1 and version2[0] == '0' and version2[1] != '.' :
            nv2 = version2[1:]

        v1Array = nv1.split(".")
        v2Array = nv2.split(".")
        lenv1 = len(v1Array)
        lenv2 = len(v2Array)
        lenMax = max(lenv1, lenv2)

        #print lenv1, lenv2, nv1, nv2, v1Array
        for x in range(lenMax):
            v1Token = 0
            if x < lenv1:
                v1Token = int(v1Array[x])
                #print x, lenv1, v1Token, int(v1Array[x])
            v2Token = 0
            if x < lenv2:
                v2Token = int(v2Array[x])

            if v1Token < v2Token:
                return -1
            if v1Token > v2Token:
                return 1
        return 0

# not working: runtime err:
# Line 6: ValueError: invalid literal for int() with base 10: '1.0'
    def compareVersion2(self, version1, version2):

        v1 = int(version1)
        v2 = int(version2)

        if v1 - v2 > 0:
            return 1
        elif v1-v2 <0:
            return -1
        else:
            return 0

#test
test = SolutionOther()
print test.compareVersion("0.1", "1.0")