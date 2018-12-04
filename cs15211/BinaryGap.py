__source__ = 'https://leetcode.com/problems/binary-gap/description/'
# Time:  O(logN) Note that logN is the number of digits in the binary representation of N
# Space: O(1)
#
# Description: Leetcode # 868. Binary Gap
#
# Given a positive integer N,
# find and return the longest distance between two consecutive 1's
# in the binary representation of N.
#
# If there aren't two consecutive 1's, return 0.
# Example 1:
#
# Input: 22
# Output: 2
# Explanation:
# 22 in binary is 0b10110.
# In the binary representation of 22, there are three ones,
# and two consecutive pairs of 1's.
# The first consecutive pair of 1's have distance 2.
# The second consecutive pair of 1's have distance 1.
# The answer is the largest of these two distances, which is 2.
# Example 2:
#
# Input: 5
# Output: 2
# Explanation:
# 5 in binary is 0b101.
# Example 3:
#
# Input: 6
# Output: 1
# Explanation:
# 6 in binary is 0b110.
# Example 4:
#
# Input: 8
# Output: 0
# Explanation:
# 8 in binary is 0b1000.
# There aren't any consecutive pairs of 1's in the binary representation of 8,
# so we return 0.
#
# Note:
#
# 1 <= N <= 10^9
#
import unittest


class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/binary-gap/solution/
# Approach 1: Store Indexes

# 8ms 88.70%
class Solution {
    public int binaryGap(int N) {
        int[] A = new int[32];
        int t = 0;
        for (int i = 0; i < 32; i++) {
            if ((( N >> i) & 1) != 0) A[t++] = i;
        }

        int ans = 0;
        for (int i = 0; i < t - 1; i++) {
            ans = Math.max(ans, A[i+1] - A[i]);
        }
        return ans;
    }
}

# Approach 2: One Pass
# 11ms 58.34%
class Solution {
    public int binaryGap(int N) {
        int last = -1, ans = 0;
        for (int i = 0; i < 32; i++) {
            if (((N >> i) & 1) > 0) {
                if (last >= 0) ans = Math.max(ans, i - last);
                last = i;
            }
        }
        return ans;
    }
}

# 7ms 99.48%
class Solution {
    public int binaryGap(int N) {
        int pre = -1, pos = 0, res = 0 ;
        while(N != 0){

            if((N & 1) == 1){
                if(pre!=-1)res = Math.max(res, pos-pre);
                pre = pos;
            }
            pos++;
            N = N/2;

        }
        return res;
    }
}
'''