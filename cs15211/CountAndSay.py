__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/count-and-say.py
# Time:  O(n * 2^n)
# Space: O(2^n)
# String
#
# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.
#
# Note: The sequence of integers will be represented as a string.
# Facebook



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

if __name__ == "__main__":
    for i in xrange(1,4):
        print Solution().countAndSay(i)




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

#test
test = SolutionOther()
print test.countAndSay(4)

#java
js = '''
public class Solution {
    public String countAndSay(int n) {
        if (n <= 0) {
            return "";
        }
        String result = "1";
        while (--n > 0) {
            result = countNext(result);
        }
        return result;
    }

    private String countNext(String str) {
        if (str.length() == 0) {
            return "";
        }
        StringBuilder sb = new StringBuilder();
        char c = str.charAt(0);
        int count = 1;
        for (int i = 1; i < str.length(); i++) {
            char curr = str.charAt(i);
            if (curr == c) {
                count++;
            } else {
                sb.append(count);
                sb.append(c);
                c = curr;
                count = 1;
            }
        }
        sb.append(count);
        sb.append(c);
        return sb.toString();
    }
}
'''