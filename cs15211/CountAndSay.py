__source__ = 'https://leetcode.com/problems/count-and-say/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/count-and-say.py
# Time:  O(n * 2^n)
# Space: O(2^n)
# String
#
# Description: Leetcode # 38. Count and Say
#
# The count-and-say sequence is the sequence of integers with the first five terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth term of the count-and-say sequence.
#
# Note: Each term of the sequence of integers will be represented as a string.
#
# Example 1:
#
# Input: 1
# Output: "1"
# Example 2:
#
# Input: 4
# Output: "1211"
#
# Companies
# Facebook
# Related Topics
# String
# Similar Questions
# Encode and Decode Strings
#

import unittest
class Solution:
    # @return a string
    def countAndSay(self, n):
        seq = "1"
        for i in xrange(n-1):
            seq = self.getNext(seq)
        return seq

    def getNext(self, seq):
        i, next_seq = 0, ""
        while i < len(seq):
            cnt = 1
            while i < len(seq) - 1 and  seq[i] == seq[i+1]:
                cnt += 1
                i += 1
            next_seq += "{}{}".format(cnt,seq[i])
            i += 1
        return next_seq

class SolutionOther:
    # @return a string
    def countAndSay(self, n):
        ans, now = [str(1), ''], 0
        for i in range(1,n):
            #^1 = XOR 1

            now, pre, ans[now] = now^1 , now, ""
            dupscount, j = 0, 0
            #print i, "i val:", now, pre, ans

            while j < len(ans[pre]):
                #print ans[pre], ans[now]
                dupscount, actChar, j = 1, ans[pre][j], j+1

                #print j, "j val:", dupscount, actChar

                while j < len(ans[pre]) and actChar == ans[pre][j]:
                    #print j, "j val:", dupscount, actChar
                    j += 1
                    dupscount += 1
                ans[now] += str(dupscount) + actChar

        return ans[now]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        for i in xrange(1,4):
            print Solution().countAndSay(i)
        test = SolutionOther()
        print test.countAndSay(4)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
 1.     1
 2.     11
 3.     21
 4.     1211
 5.     111221
 6.     312211
 7.     13112221
 8.     1113213211
 9.     31131211131221
 10.   13211311123113112211

# 2ms 97.14%
class Solution {
    public String countAndSay(int n) {
        if (n <= 0) {
            return "";
        }
        String cur = "1";
        for (int i = 1; i < n; i++) {
            cur = countNext(cur);
        }
        return cur;
    }

    private String countNext(String str) {
        StringBuilder sb = new StringBuilder();
        char prev = str.charAt(0);
        int count = 1;
        for (int i = 1; i < str.length(); i++) {
            char cur = str.charAt(i);
            if (cur == prev) {
                count++;
            } else {
                sb.append(count).append(prev);
                prev = cur;
                count = 1;
            }
        }
        sb.append(count).append(prev);
        return sb.toString();
    }
}

# 2ms 97.14%
class Solution {
    public String countAndSay(int n) {
       String s = "1";
        for (int i = 1; i < n ; i ++){
            s = iterate(s);
        }
        return s;
    }
    public String iterate(String s){
        StringBuilder res = new StringBuilder();
        int count = 1;
        for( int i = 1; i < s.length(); i++){
            if (s.charAt(i) == s.charAt(i - 1)){
                count++;
            }
            else{
               res.append(count);
                res.append(s.charAt(i-1));
                count = 1;
            }
        }
        res.append(count);
        res.append(s.charAt(s.length()-1));
        return res.toString();
    }
}

# 2ms 97.14%
class Solution {
    public String countAndSay(int n) {
        if (n < 1) {
            return "";
        }
        StringBuilder sb = new StringBuilder();
        String num = "1";
        for (int i = 1; i < n; i++) {
            char c = num.charAt(0);
            int count = 1;
            for (int j = 1; j < num.length(); j++) {
                if (num.charAt(j) == c) {
                    count++;
                } else {
                    sb.append(count).append(c);
                    c = num.charAt(j);
                    count = 1;
                }
            }
            sb.append(count).append(c);
            num = sb.toString();
            sb.setLength(0);
        }
        return num;
    }
}
'''