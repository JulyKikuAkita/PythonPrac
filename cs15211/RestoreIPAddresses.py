__source__ = 'https://leetcode.com/problems/restore-ip-addresses/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/restore-ip-addresses.py
# Time:  O(n^m) = O(3^4)
# Space: O(n * m) = O(3 * 4)
# DFS
#
# Description: Leetcode # 93. Restore IP Addresses
#
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# For example:
# Given "25525511135",
#
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
#
# Related Topics
# Backtracking String
#
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
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        test = SolutionOther()
        #print test.restoreIpAddresses("25525511135")
        #print Solution().restoreIpAddresses("0000")
        print Solution().restoreIpAddresses("25525511135")

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
3-loop divides the string s into 4 substring: s1, s2, s3, s4. Check if each substring is valid.
In isValid, strings whose length greater than 3 or equals to 0 is not valid;
or if the string's length is longer than 1 and the first letter is '0' then it's invalid;
or the string whose integer representation greater than 255 is invalid.

# 4ms 33.49%
class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> solutions = new ArrayList<String>();
        restoreIp(s, solutions, 0, "", 0);
        return solutions;
    }

    private void restoreIp(String ip, List<String> solutions, int idx, String restored, int count) {
        if (count > 4) return;
        if (count == 4 && idx == ip.length()) solutions.add(restored);

        for (int i=1; i<4; i++) {
            if (idx+i > ip.length()) break;
            String s = ip.substring(idx,idx+i);
            if ((s.startsWith("0") && s.length()>1) || (i==3 && Integer.parseInt(s) >= 256)) continue;
            restoreIp(ip, solutions, idx+i, restored+s+(count==3?"" : "."), count+1);
        }
    }
}

# 1ms 99.64%
class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> result = new ArrayList<>();
        if (s.length() < 4 || s.length() > 12) {
            return result;
        }
        restoreIp(s.toCharArray(), 1, result, new ArrayList<>(), s.charAt(0) - '0');
        return result;
    }

    private void restoreIp(char[] s, int index, List<String> result, List<Integer> cur, int num) {
        if (index == s.length) {
            if (cur.size() == 3) {
                cur.add(num);
                result.add(convertIp(cur));
                cur.remove(cur.size() - 1);
            }
            return;
        }
        int curNum = s[index] - '0';
        int next = num * 10 + curNum;
        if (num != 0 && next < 256) {
            restoreIp(s, index + 1, result, cur, next);
        }
        if (s.length - index <= (4 - cur.size() - 1) * 3) {
            cur.add(num);
            restoreIp(s, index + 1, result, cur, curNum);
            cur.remove(cur.size() - 1);
        }
    }

    private String convertIp(List<Integer> nums) {
        StringBuilder sb = new StringBuilder();
        sb.append(nums.get(0));
        for (int i = 1; i < 4; i++) {
            sb.append('.').append(nums.get(i));
        }
        return sb.toString();
    }
}

# 1ms 99.64%
class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> result = new ArrayList<String>();
        List<String> temp = new ArrayList<String>();
        dfs(s,temp,result,0);
        return result;
    }
    public void dfs(String s, List<String> tmp, List<String> res, int start){
        if (tmp.size() == 4 && start == s.length()) {
            res.add(tmp.get(0) + '.' + tmp.get(1) + '.' + tmp.get(2) + '.' + tmp.get(3));
            return;
        }
        int num = 0;
        if (s.length() - start > (4 - tmp.size()) * 3 ) return;
        if (s.length() - start < (4 - tmp.size())) return;
        for (int i = start; i < 3 + start && i < s.length(); i++) {
            num = num * 10 + (s.charAt(i) - '0');
            if (num > 255 || num < 0) break;
            tmp.add(s.substring(start, i + 1));
            dfs(s, tmp, res, i + 1);
            tmp.remove(tmp.size() - 1);
            if (num == 0) break;
        }
    }
}
'''
