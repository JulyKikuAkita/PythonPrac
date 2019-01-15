__source__ = 'https://leetcode.com/problems/compare-version-numbers/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/compare-version-numbers.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 165. Compare Version Numbers
#
# Compare two version numbers version1 and version1.
# If version1 > version2 return 1, if version1 < version2
# return -1, otherwise return 0.
#
# You may assume that the version strings are non-empty and
# contain only digits and the . character.
# The . character does not represent a decimal point and
# is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to
# version three", it is the fifth second-level revision of
# the second first-level revision.
#
# Here is an example of version numbers ordering:
#
# 0.1 < 1.1 < 1.2 < 13.37
#
# Companies
# Microsoft Apple
# Related Topics
# String
#
import itertools
import unittest
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        n1, n2 = len(version1), len(version2)
        i, j = 0, 0
        while i < n1 or j < n2:
            v1, v2 = 0, 0
            while i < n1 and version1[i] != '.':
                v1 = v1 * 10 + int(version1[i])
                i += 1
            while j < n2 and version2[j] != '.':
                v2 = v2 * 10 + int(version2[j])
                j += 1
            if v1 != v2:
                return 1 if v1 > v2 else -1
            i += 1
            j += 1
        return 0

# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1, v2 = version1.split("."), version2.split(".")

        if len(v1) > len(v2):
            v2 += ['0' for _ in xrange(len(v1) - len(v2))]
        elif len(v1) < len(v2):
            v1 += ['0' for _ in xrange(len(v2) - len(v1))]

        i = 0
        while i < len(v1):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
            else:
                i += 1

        return 0

    def compareVersion2(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]
        while len(v1) != len(v2):
            if len(v1) > len(v2):
                v2.append(0)
            else:
                v1.append(0)
        return cmp(v1, v2)

    def compareVersion3(self, version1, version2):
        splits = (map(int, v.split('.')) for v in (version1, version2))
        return cmp(*zip(*itertools.izip_longest(*splits, fillvalue=0)))

    def compareVersion4(self, version1, version2):
        main1, _, rest1 = ('0' + version1).partition('.')
        main2, _, rest2 = ('0' + version2).partition('.')
        return cmp(int(main1), int(main2)) or len(rest1 + rest2) and self.compareVersion4(rest1, rest2)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().compareVersion("21.0", "121.1.0")
        print Solution().compareVersion("01", "1")
        print Solution().compareVersion("1", "1.0")

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
# 1ms 89.56%
class Solution {
    public int compareVersion(String version1, String version2) {
        String[] tokens1 = version1.split("\\.");
        String[] tokens2 = version2.split("\\.");
        for (int i = 0; i < Math.max(tokens1.length, tokens2.length); i++) {
            int v1 = i >= tokens1.length ? 0 : Integer.parseInt(tokens1[i]);
            int v2 = i >= tokens2.length ? 0 : Integer.parseInt(tokens2[i]);
            if (v1 != v2) {
                return Integer.compare(v1, v2);
            }
        }
        return 0;
    }
}

# 0ms 100%
class Solution {
    public int compareVersion(String version1, String version2) {
        if(version1 == null && version2 == null) return 0;
        if(version1 == null) return -1;
        if(version2 == null) return 1;
        int i=0, j=0;
        while (i < version1.length() || j < version2.length()){
            int tmp1 = 0;
            int tmp2 = 0;
            while(i < version1.length() && version1.charAt(i) != '.'){
                tmp1 = tmp1 * 10 + version1.charAt(i) - '0';
                i++;
            }
            i++;
            while (j < version2.length() && version2.charAt(j) != '.'){
                tmp2 = tmp2 *10 + version2.charAt(j) - '0';
                j++;
            }
            j++;
            if(tmp1 > tmp2) return 1;
            if (tmp1 < tmp2) return -1;

        }
        return 0;
    }
}

# 0ms 100%
class Solution {
    public int compareVersion(String version1, String version2) {
        int len1 = version1.length();
        int len2 = version2.length();
        int index1 = 0;
        int index2 = 0;
        while (index1 < len1 || index2 < len2) {
            int cur1 = 0;
            int cur2 = 0;
            while (index1 < len1) {
                char c = version1.charAt(index1++);
                if (c == '.') {
                    break;
                }
                cur1 = cur1 * 10 + c - '0';
            }
            while (index2 < len2) {
                char c = version2.charAt(index2++);
                if (c == '.') {
                    break;
                }
                cur2 = cur2 * 10 + c - '0';
            }
            if (cur1 > cur2) {
                return 1;
            } else if (cur1 < cur2) {
                return -1;
            }
        }
        return 0;
    }
}
'''
