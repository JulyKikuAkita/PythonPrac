# coding=utf-8
__source__ = 'https://leetcode.com/problems/scramble-string/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/scramble-string.py
# Time:  O(n^4)
# Space: O(n^3)
# DP
#
# Description: Leetcode # 87. Scramble String
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
# Related Topics
# Dynamic Programming String
#

# DP solution
# Time:  O(n^4)
# Space: O(n^3)
import unittest
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
                        if result[k][i][j] and result[n - k][i + k][j + k] or result[k][i][j + n - k] \
                                and result[n - k][i + k][j]:
                            result[n][i][j] = True
                            break
        #for n in xrange(len(s1)+1):
        #   print result[n]
        return result[n][0][0]

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
class TestMethods(unittest.TestCase):
    def test_Local(self):
        test = SolutionOther()
        #print test.isScramble("great", "rgeat")
        print test.isScramble("abc", "cab")
        #print test.isScrambleDP("great", "rgeat")
        #print test.isScrambleDP("abc", "cab")

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# DFS
# 2ms 99.21%
class Solution {
    public boolean isScramble(String s1, String s2) {
        if (s1.equals(s2)) return true;

        int[] letters = new int[26];
        for (int i = 0; i < s1.length(); i++) {
            letters[s1.charAt(i) - 'a']++;
            letters[s2.charAt(i) - 'a']--;
        }

        for (int i = 0; i < 26; i++) {
            if (letters[i] != 0) return false;
        }

        for (int i = 1; i < s1.length(); i++) {
            if (isScramble(s1.substring(0,i), s2.substring(0,i))
                && isScramble(s1.substring(i), s2.substring(i))) return true;
            if (isScramble(s1.substring(0,i), s2.substring(s2.length() - i))
                && isScramble(s1.substring(i), s2.substring(0, s2.length() - i))) return true;
        }
        return false;
    }
}

# 2ms 99.21%
class Solution {  
    public boolean isScramble(String s1, String s2) {  
        char[] t1 = s1.toCharArray();  
        char[] t2 = s2.toCharArray();  
        return scramble(t1, 0, t2, 0, t2.length);  
    }  
  
  
    //此方法做出来一下这几点的优化方案：  
    //用 字符数组和长度来替代字符串不用每次都切割子串  
    // 在判断字符的数组中的元素是否相同的时候少了一个对letter的循环遍历  
    private  boolean scramble(char[] s1, int i, char[] s2, int j, int n) {  
        //当 n == 1 的时候应该向上回溯  
        if (n == 1) return s1[i] == s2[j];  
  
        //判断字符是否相等  
        int[] letter = new int[26];  
        for (int k = i; k < i+n; k++) {  
            ++letter[s1[k]-'a'];  
        }  
        for (int k = j; k < j+n; k++) {  
            //存在不想等的字符  
            if (--letter[s2[k]-'a'] < 0)  
                return false;  
        }  
        for (int l = 1; l < n; l++) {  
            //将字符数组的前半部分和后半部分分别的进行对比 相当于s.substring()  
            if (scramble(s1,i,s2,j,l)  
                    && scramble(s1,i+l,s2,j+l,n-l)) return true;  
            //将s1前半部分和s2的后半部分对比，  
            if (scramble(s1,i,s2,n+j-l,l)  
                    && scramble(s1,i+l,s2,j,n-l)) return true;  
        }  
        return false;  
    }  
}  

# DP
# 12ms 27.34%
class Solution {
	public boolean isScramble(String s1, String s2) {
		if (s1.length() != s2.length()) return false;
		int len = s1.length();
		/**
		 * Let F(i, j, k) = whether the substring S1[i..i + k - 1] is a scramble of S2[j..j + k - 1] or not
		 * Since each of these substrings is a potential node in the tree, we need to check for all possible cuts.
		 * Let q be the length of a cut (hence, q < k), then we are in the following situation:
		 *
		 * S1 [   x1    |         x2         ]
		 *    i         i + q                i + k - 1
		 *
		 * here we have two possibilities:
		 *
		 * S2 [   y1    |         y2         ]
		 *    j         j + q                j + k - 1
		 *
		 * or
		 *
		 * S2 [       y1        |     y2     ]
		 *    j                 j + k - q    j + k - 1
		 *
		 * which in terms of F means:
		 *
		 * F(i, j, k) = for some 1 <= q < k we have:
		 *  (F(i, j, q) AND F(i + q, j + q, k - q)) OR (F(i, j + k - q, q) AND F(i + q, j, k - q))
		 *
		 * Base case is k = 1, where we simply need to check for S1[i] and S2[j] to be equal
		 * */
		boolean [][][] F = new boolean[len][len][len + 1];
		for (int k = 1; k <= len; ++k)
			for (int i = 0; i + k <= len; ++i)
				for (int j = 0; j + k <= len; ++j)
					if (k == 1)
						F[i][j][k] = s1.charAt(i) == s2.charAt(j);
					else for (int q = 1; q < k && !F[i][j][k]; ++q) {
						F[i][j][k] = (F[i][j][q] && F[i + q][j + q][k - q]) || (F[i][j + k - q][q] && F[i + q][j][k - q]);
					}
		return F[0][0][len];
	}
}

# 17ms 19.15%
class Solution {
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

# 4ms 59.58%
class Solution {
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
