__source__ = 'https://leetcode.com/problems/strobogrammatic-number-iii/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/strobogrammatic-number-iii.py
# Time:  O(5^(n/2))
# Space: O(n)
#
# Description: Leetcode # 248. Strobogrammatic Number III
#
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
#
# Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.
#
# For example,
# Given low = "50", high = "100", return 3. Because 69, 88, and 96 are three strobogrammatic numbers.
#
# Note:
# Because the range might be a large number, the low and high numbers are represented as string.
#
# Related Topics
# Math Recursion
# Similar Questions
# Strobogrammatic Number Strobogrammatic Number II
#

# Time:  O(5^(n/2))
# Space: O(n)
import unittest
# 28ms 93.99%
class Solution:
    lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    cache = {}

    # @param {string} low
    # @param {string} high
    # @return {integer}
    def strobogrammaticInRange3(self, low, high):
        count = self.countStrobogrammaticUntil(high, False) - \
                self.countStrobogrammaticUntil(low, False) + \
                self.isStrobogrammatic(low)
        return count if count >= 0 else 0

    def countStrobogrammaticUntil(self, num,  can_start_with_0):
        if can_start_with_0 and num in self.cache:
            return self.cache[num]

        count = 0
        if len(num) == 1:
            for c in ['0', '1', '8']:
                if num[0] >= c:
                    count += 1
            self.cache[num] = count
            return count

        for key, val in self.lookup.iteritems():
            if can_start_with_0 or key != '0':
                if num[0] > key:
                    if len(num) == 2:  # num is like "21"
                        count += 1
                    else:  # num is like "201"
                        count += self.countStrobogrammaticUntil('9' * (len(num) - 2), True)
                elif num[0] == key:
                    if len(num) == 2:  # num is like 12".
                        if num[-1] >= val:
                            count += 1
                    else:
                        if num[-1] >= val:  # num is like "102".
                            count += self.countStrobogrammaticUntil(self.getMid(num), True);
                        elif (self.getMid(num) != '0' * (len(num) - 2)):  # num is like "110".
                            count += self.countStrobogrammaticUntil(self.getMid(num), True) - \
                                     self.isStrobogrammatic(self.getMid(num))

        if not can_start_with_0: # Sum up each length.
            for i in xrange(len(num) - 1, 0, -1):
                count += self.countStrobogrammaticByLength(i)
        else:
            self.cache[num] = count

        return count

    def getMid(self, num):
        return num[1:len(num) - 1]

    def countStrobogrammaticByLength(self, n):
        if n == 1:
            return 3
        elif n == 2:
            return 4
        elif n == 3:
            return 4 * 3
        else:
            return 5 * self.countStrobogrammaticByLength(n - 2)

    def isStrobogrammatic(self, num):
        n = len(num)
        for i in xrange((n+1) / 2):
            if num[n-1-i] not in self.lookup or \
               num[i] != self.lookup[num[n-1-i]]:
                return False
        return True

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().strobogrammaticInRange3("50","100")

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 5ms 96.73%
class Solution {
    private static char[] SINGLE_NUM = new char[] {'0', '1', '8'};
    private static char[][] DOUBLE_NUM = new char[][] {{'0', '0'}, {'1', '1'}, {'6', '9'}, {'8', '8'}, {'9', '6'}};

    public int strobogrammaticInRange(String low, String high) {
        int result = 0;
        char[] lowArr = low.toCharArray();
        char[] highArr = high.toCharArray();
        for (int i = lowArr.length; i <= highArr.length; i++) {
            result += strobogrammaticInRange(lowArr, highArr, new char[i], 0, i - 1);
        }
        return result;
    }

    private int strobogrammaticInRange(char[] low, char[] high, char[] cur, int start, int end) {
        int result = 0;
        if (start > end) {
            return compare(low, cur) <= 0 && compare(cur, high) <= 0 ? 1 : 0;
        } else if (start == end) {
            for (char c : SINGLE_NUM) {
                cur[start] = c;
                if (compare(low, cur) <= 0 && compare(cur, high) <= 0) {
                    result++;
                }
            }
        } else {
            for (char[] c : DOUBLE_NUM) {
                if (start > 0 || c[0] != '0') {
                    cur[start] = c[0];
                    cur[end] = c[1];
                    result += strobogrammaticInRange(low, high, cur, start + 1, end - 1);
                }
            }
        }
        return result;
    }

    private int compare(char[] num1, char[] num2) {
        if (num1.length != num2.length) {
            return Integer.compare(num1.length, num2.length);
        }
        for (int i = 0; i < num1.length; i++) {
            if (num1[i] != num2[i]) {
                return Character.compare(num1[i], num2[i]);
            }
        }
        return 0;
    }
}

# DP
# 0ms 100%
class Solution {
    char[] one={'0','1','6','8','9'},two={'0','1','9','8','6'};
    int count=0;
    public int strobogrammaticInRange(String low, String high) {
        if(low.length()>high.length()) return 0;
        int[][] dp=new int[high.length()+1][2];
        dp[0][0]=0;
        dp[0][1]=1;
        dp[1][0]=3;
        dp[1][1]=3;
        for(int i=2;i<=high.length();i++){
            dp[i][0]=dp[i-2][1]*4;
            dp[i][1]=dp[i-2][1]*5;
        }
        recurse(low.length(),0,low.length()-1,low.toCharArray(),dp);
        int tmp=count,total=0;
        count=0;
        if(!recurse(high.length(),0,high.length()-1,high.toCharArray(),dp)) count++;
        for(int i=low.length();i<high.length();i++){
            total+=dp[i][0];
        }
        return (total-tmp+count>=0)?total-tmp+count:0;
    }
    public boolean recurse(int lvl,int start,int end,char[] arr,int[][] dp){
        if(start>end) return false;
        else if(start==end){
            if(arr[start]>'0') count++;
            if(arr[start]>'1') count++;
            if(arr[start]>'8') count++;
            if(arr[start]=='0'||arr[start]=='1'||arr[start]=='8') return false;
            return true;
        }
        else{
            for(int i=((lvl==arr.length)?1:0);i<one.length;i++){
                if(arr[start]==one[i]){
                    if(!recurse(lvl-2,start+1,end-1,arr,dp)){
                        if(arr[end]==two[i]) return false;
                        if(arr[end]>two[i]) count++;
                    }
                    return true;
                }
                if(arr[start]>one[i]) count+=(dp[lvl][0]/4);
                else break;
            }
            return true;
        }
    }
}

'''
