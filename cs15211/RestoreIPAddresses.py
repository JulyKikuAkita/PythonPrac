__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/restore-ip-addresses.py
# Time:  O(n^m) = O(3^4)
# Space: O(n * m) = O(3 * 4)
# DFS
#
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# For example:
# Given "25525511135",
#
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
#
# Backtracking String
import unittest
class Solution(unittest.TestCase):
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        result = []
        self.restoreIpAddressesRecur(result, s, 0, "", 0)
        return result

    def restoreIpAddressesRecur(self, result, s, start, current, dots):
        # pruning to improve performance
        if (4 - dots) * 3 < len(s) - start or (4 - dots) > len(s) - start: # break if 1) the # of rest numbers > 3 * dots
            return                                                         # 2) more dots than # rest numbers ( =>1 dots have no number is not valid )
        if start == len(s) and dots == 4:
            result.append(current[: -1]) # clone current[:lastword - 1] b.c last char will always be '.'
        else:
            for i in xrange(start, start + 3):
                if len(s) > i and self.isValid(s[start: i + 1]):
                    current += s[start : i + 1] + '.'
                    self.restoreIpAddressesRecur(result, s , i + 1, current, dots + 1)
                    current = current[:-(i - start + 2)]

    def isValid(self, s):
        if len(s) == 0 or (s[0] == "0" and s != "0"):
            return False
        return int(s) < 256

    def test(self):
        self.assertEqual(['0.0.0.0'], self.restoreIpAddresses("0000"))

class Solution2(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4:
            return []
        res = []
        self.dfs(s, res, 0, [], 0)
        return res

    def dfs(self, s, res, idx, cur, dot):
        if(4 - dot) * 3 < len(s) - idx  or (4 - dot) > len(s) - idx:
            return
        if idx == len(s) and dot == 4:
            res.append(''.join(cur)[:-1])
            return
        for i in xrange(idx, idx + 3):
            if len(s) > i and self.isValid(s[idx:i + 1]):
                cur.append(s[idx:i + 1] + '.')
                self.dfs(s, res, i + 1, cur, dot + 1)
                cur.pop()
    def isValid(self, s):
        if len(s) == 0 or (s[0] == "0" and s != "0"):
           return False
        return int(s) < 256

class SolutionOther:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        def dfs(s, sub, ips,ip):
            if sub == 4:
                if s == '':
                    #print "s =", s, "ip = ", ip[1:]
                    ips.append(ip[1:])
                return
            for i in range(1,4):
                if i <= len(s):
                    if int(s[:i]) <= 255:
                        #print ip
                        dfs(s[i:], sub+1, ips, ip+'.'+s[:i])
                    if s[0] == '0':
                        break
        self.ips = []
        self.ip = ''
        ips = []
        dfs(s, 0, ips, '')
        self.dfs_notworking(s, 0, self.ips, self.ip)
        print self.ips
        return ips

    def dfs_notworking(self, s, sub, ips, ip):
        if sub == 4:
            print s, ip
            if s == '':
                print self.ip
                self.ips.append(self.ip[1:])
            return
        for i in range(1, 4):
            if i <= len(s):
                if int(s[:i]) <= 255:
                    self.dfs_notworking(s[i:], sub+1, self.ips, self.ip+'.'+s[:i])
                if s[0] == '0':
                    break

#test
test = SolutionOther()
#print test.restoreIpAddresses("25525511135")

if __name__ == "__main__":
    #print Solution().restoreIpAddresses("0000")
    print Solution().restoreIpAddresses("25525511135")
#java
js = '''
public class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> result = new ArrayList<>();
        if (s.length() < 4) {
            return result;
        }
        restore(s, 1, result, new int[4], 0, s.charAt(0) - '0');
        return result;
    }

    private void restore(String s, int strIndex, List<String> result, int[] arr, int arrIndex, int cur) {
        if (strIndex == s.length()) {
            if (arrIndex == 3 && cur < 256) {
                arr[arrIndex] = cur;
                result.add(ipToString(arr));
            }
            return;
        } else if (arrIndex == arr.length || s.length() - strIndex > 3 * (arr.length - arrIndex)) {
            return;
        }
        int num = s.charAt(strIndex) - '0';
        int included = cur * 10 + num;
        if (cur > 0 && included < 256) {
            restore(s, strIndex + 1, result, arr, arrIndex, included);
        }
        arr[arrIndex] = cur;
        restore(s, strIndex + 1, result, arr, arrIndex + 1, num);
    }

    private String ipToString(int[] arr) {
        StringBuilder sb = new StringBuilder();
        sb.append(arr[0]);
        for (int i = 1; i < arr.length; i++) {
            sb.append('.').append(arr[i]);
        }
        return sb.toString();
    }
}
'''