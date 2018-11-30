# coding=utf-8
__source__ = 'https://leetcode.com/problems/ip-to-cidr/'
# Time:  O(N) where N is the length of nums.
# Space: O(1)
#
# Description: Leetcode # 751. IP to CIDR
# Given a start IP address ip and a number of ips we need to cover n,
# return a representation of the range as a list (of smallest possible length) of CIDR blocks.
#
# A CIDR block is a string consisting of an IP,
# followed by a slash, and then the prefix length.
# For example: "123.45.67.89/20".
# That prefix length "20" represents the number of common prefix bits in the specified range.
#
# Example 1:
# Input: ip = "255.0.0.7", n = 10
# Output: ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]
# Explanation:
# The initial ip address, when converted to binary, looks like this (spaces added for clarity):
# 255.0.0.7 -> 11111111 00000000 00000000 00000111
# The address "255.0.0.7/32" specifies all addresses with a common prefix of 32 bits to the given address,
# ie. just this one address.
#
# The address "255.0.0.8/29" specifies all addresses with a common prefix of 29 bits to the given address:
# 255.0.0.8 -> 11111111 00000000 00000000 00001000
# Addresses with common prefix of 29 bits are:
# 11111111 00000000 00000000 00001000
# 11111111 00000000 00000000 00001001
# 11111111 00000000 00000000 00001010
# 11111111 00000000 00000000 00001011
# 11111111 00000000 00000000 00001100
# 11111111 00000000 00000000 00001101
# 11111111 00000000 00000000 00001110
# 11111111 00000000 00000000 00001111
#
# The address "255.0.0.16/32" specifies all addresses with a common prefix of 32 bits to the given address,
# ie. just 11111111 00000000 00000000 00010000.
#
# In total, the answer specifies the range of 10 ips starting with the address 255.0.0.7 .
#
# There were other representations, such as:
# ["255.0.0.7/32","255.0.0.8/30", "255.0.0.12/30", "255.0.0.16/32"],
# but our answer was the shortest possible.
#
# Also note that a representation beginning with say, "255.0.0.7/30" would be incorrect,
# because it includes addresses like 255.0.0.4 = 11111111 00000000 00000000 00000100
# that are outside the specified range.
# Note:
# ip will be a valid IPv4 address.
# Every implied address ip + x (for x < n) will be a valid IPv4 address.
# n will be an integer in the range [1, 1000].
#
import unittest

# 24ms 100%
class Solution(object):
    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        start = self.ipToInt(ip)
        ans = []
        while n:
            mask = max(33 - (start & -start).bit_length(), 33 - n.bit_length())
            ans.append(self.intToIp(start) + '/' + str(mask))
            start += 1 << (32 - mask)
            n -= 1 << (32 - mask)
        return ans

    def ipToInt(self, ip):
        ans = 0
        for x in ip.split('.'):
            ans = 256 * ans + int(x)
        return ans

    def intToIp(self, x):
        return ".".join(str((x >> i) % 256) for i in (24,16, 8, 0))


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/ip-to-cidr/solution/
#23ms, 15.42%
class Solution {
    public List<String> ipToCIDR(String ip, int n) {
        long start = ipToLong(ip);
        List<String> ans = new ArrayList();
        while (n > 0) {
            int mask = Math.max(33 - bitLength(Long.lowestOneBit(start)),
                               33 - bitLength(n));
            ans.add(longToIp(start) + "/" + mask);
            start += 1 << (32 - mask);
            n -= 1 << (32 -mask);
        }
        return ans;
    }

    private long ipToLong(String ip) {
        long ans = 0;
        for (String x: ip.split("\\.")) {
            ans = 256 * ans + Integer.valueOf(x);
        }
        return ans;
    }

    private String longToIp(long x) {
        return String.format("%s.%s.%s.%s", x >> 24, (x >> 16) % 256, (x >>8) % 256, x % 256);
    }

    private int bitLength(long x) {
        if (x == 0) return 1;
        int ans = 0;
        while (x > 0) {
            x >>= 1;
            ans++;
        }
        return ans;
    }
}

#6ms 100%
class Solution {

    public List<String> ipToCIDR(String ip, int n) {
		//思路，找到这些IPs中从右往左第一位相同的二进制位
		// x & -x ;-x是x的补码，返回x与2^64的最大公约数，
		//即x最多能被n个2整除就返回2^n,如果x是奇数返回1;返回值为0 ，说明x=0;为其他数，表示x为x与2^64的最大公约数
		//一言以蔽之就是获取32位二进制表示中从右往左首次出现1的位置
		long x = 0;
		//以"."划分每个IP
		String[] ipsegment = ip.split("\\.");
		for(int i=0;i<ipsegment .length;i++){
			x = Integer.parseInt(ipsegment [i])+x*256;
		}
		List<String> res = new ArrayList<>();
		while(n>0){
			long temp = x & -x;//求得该IP用32位二进制表示中从右往左首次出现1的位置
			//-x才是x的补码，~x为反码
			//temp如果为奇数，则该IP为第一个CIDR块
			//如果偶数，则该IP用二进制表示下的最低有效位的位数能表示的地址的数量
			while(temp>n) {
				temp = temp/2;
			}
                        //到这里temp肯定是小于n的，这告诉我们包括此IP在内的temp个IPs可以用一个ICDR来表示
			//接下来求出这些IPs所处的CIDR
			res.add(longToIP(x, (int)temp));
			//x加上temp;
			x+=temp;//temp个ips考虑好了，接下来考虑从x+temp考虑
			n-=temp;//还有几个IPs要求ICDR的
		}
		return res;
	}

	public String longToIP(long x,int temp){
		int netID = 32;
		while(temp>0){
			temp/=2;
			netID--;
		}

		int[] ans = new int[4];
		for(int i=0;i<ans.length-1;i++){
			ans[i] = (int)(x & 255);
		         x>>=8;
		}
		ans[ans.length-1] = (int)x;
		netID++; //加1：比如说某些IPs有m位相同，是指0-m-1位相同
		return ans[3]+"."+ans[2]+"."+ans[1]+"."+ans[0]+"/"+netID;
	}
}
'''