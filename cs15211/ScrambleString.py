__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/scramble-string.py
# Time:  O(n^4)
# Space: O(n^3)
# DP
#
# Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
#
# Below is one possible representation of s1 = "great":
#
#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
# To scramble the string, we may choose any non-leaf node and swap its two children.
#
# For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".
#
#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
# We say that "rgeat" is a scrambled string of "great".
#
# Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".
#
#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
# We say that "rgtae" is a scrambled string of "great".
#
# Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
#

# DP solution
# Time:  O(n^4)
# Space: O(n^3)
class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if not s2 or len(s1) != len(s2):
            return False
        if not s1:
            return True

        result = [[[False for j in xrange(len(s2))] for i in xrange(len(s1))]for n in xrange(len(s1) + 1)]
        #for n in xrange(len(s1)+1):
        #    print result[n]

        for i in xrange(len(s1)):
            for j in xrange(len(s2)):
                if s1[i] == s2[j]:
                    result[1][i][j] = True

        for n in xrange(2, len(s1) + 1):
            for i in xrange(len(s1) - n + 1):
                for j in xrange(len(s2) -n + 1):
                    for k in xrange(1, n):
                        if result[k][i][j] and result[n - k][i + k][j + k] or result[k][i][j + n - k] and result[n - k][i + k][j]:
                            result[n][i][j] = True
                            break
        #for n in xrange(len(s1)+1):
        #   print result[n]


        return result[n][0][0]


#if __name__ == "__main__":
    #print Solution().isScramble("rgtae", "great")
    #print Solution().isScramble("abc", "cab")


class SolutionOther:
    # @return a boolean
    #recursion or 3 dimensional dp
    # http://www.cnblogs.com/zuoyuan/p/3777383.html
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        l1 = list(s1)
        l2 = list(s2)
        l1.sort()
        l2.sort()
        if l1 != l2:
            return False

        length = len(s1)
        for i in range(1, length):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[length-i:]) and self.isScramble(s1[i:], s2[:length-i]):
                return True
        return False

    # pass
    # http://c4fun.cn/blog/2014/03/20/leetcode-solution-02/
    def isScrambleDP(self, s1, s2):
        if len(s1) != len(s2): return False
        if len(s1) == 0: return True

        self.s1, self.s2= s1, s2
        lens = len(s1)
        self.dp = [[[-1] * lens for i in range(lens)] * lens for i in range(lens)]

        return self.dfs(0, 0, len(s1))

    def dfs(self, lp, rp, len):

        #print self.dp
        if self.dp[lp][rp][len -1] >= 0:
            print self.dp[lp][rp][len-1]
            return True if self.dp[lp][rp][len-1] == 1 else False
        if len == 1:
            return self.s1[lp] == self.s2[rp]
        for i in range(1, len):
            print self.dfs(lp, rp, i)
            if self.dfs(lp, rp, i) and self.dfs(lp+i, rp+i, len-i) or self.dfs(lp, rp+i, len-i) and self.dfs(lp +len -i, rp, i):
                self.dp[lp][rp][len -1] = 1
                return True
        self.dp[lp][rp][len-1] = 0

        return False






#test
test = SolutionOther()
#print test.isScramble("great", "rgeat")
print test.isScramble("abc", "cab")

#print test.isScrambleDP("great", "rgeat")
#print test.isScrambleDP("abc", "cab")

# java
js = '''
//dp
public class Solution {
    public boolean isScramble(String s1, String s2) {
        if ( s1.length() != s2.length()) return false;
        int len = s1.length();
        boolean[][][] dp =  new boolean[len][len][len+1];

        for( int i = 0; i < len; i++){
            for(int j = 0; j < len; j++){
                dp[i][j][0] = true;
                if (s1.charAt(i) == s2.charAt(j))
                    dp[i][j][1] = true;
            }
        }

        for (int k = 2; k <= len; k++){
            for (int i = 0; i + k <= len; i++){
                for ( int j = 0; j + k <= len; j++){
                    for(int m = 1; m < k; m++){
                        if((dp[i][j][m] && dp[i+m][j+m][k-m]) || (dp[i][j+k-m][m] && dp[i+m][j][k-m])){
                            dp[i][j][k] = true;
                            break;
                    }
                    }
                }
            }
        }
        return dp[0][0][len];

    }
}

public class Solution {
    public boolean isScramble(String s1, String s2) {
        int len1 = s1.length();
        int len2 = s2.length();
        if (len1 != len2) {
            return false;
        }
        return isScramble(s1.toCharArray(), s2.toCharArray(), 0, len1 - 1, 0, len2 - 1, new HashMap<Long, Boolean>());
    }

    private boolean isScramble(char[] s1, char[] s2, int start1, int end1, int start2, int end2, Map<Long, Boolean> cache) {
        long key = encode(new int[] {start1, end1, start2, end2}, s1.length + s2.length);
        if (cache.containsKey(key)) {
            return cache.get(key);
        }
        if (isEqual(s1, s2, start1, end1, start2, end2)) {
            cache.put(key, true);
            return true;
        } else if (!isAnagram(s1, s2, start1, end1, start2, end2)) {
            cache.put(key, false);
            return false;
        }
        for (int len = 0; len < end1 - start1; len++) {
            if ((isScramble(s1, s2, start1, start1 + len, start2, start2 + len, cache)
                    && (isScramble(s1, s2, start1 + len + 1, end1, start2 + len + 1, end2, cache)))
                || ((isScramble(s1, s2, start1, start1 + len, end2 - len, end2, cache))
                    && (isScramble(s1, s2, start1 + len + 1, end1, start2, end2 - len - 1, cache)))) {
                cache.put(key, true);
                return true;
            }
        }
        cache.put(key, false);
        return false;
    }

    private boolean isEqual(char[] s1, char[] s2, int start1, int end1, int start2, int end2) {
        while (start1 <= end1) {
            if (s1[start1++] != s2[start2++]) {
                return false;
            }
        }
        return true;
    }

    private boolean isAnagram(char[] s1, char[] s2, int start1, int end1, int start2, int end2) {
        int[] count = new int[128];
        while (start1 <= end1) {
            count[s1[start1++]]++;
        }
        while (start2 <= end2) {
            count[s2[start2++]]--;
        }
        for (int i = 0; i < 128; i++) {
            if (count[i] != 0) {
                return false;
            }
        }
        return true;
    }

    private long encode(int[] nums, int base) {
        long result = 0;
        for (int num : nums) {
            result = result * base + num;
        }
        return result;
    }
}
'''
