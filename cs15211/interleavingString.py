__source_ = 'https://leetcode.com/problems/interleaving-string/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/interleaving-string.py
# Time:  O(m * n)
# Space: O(m + n)
# DP
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
#
# For example,
# Given:
# s1 = "aabcc",
# s2 = "dbbca",
#
# When s3 = "aadbbcbcac", return true.
# When s3 = "aadbbbaccc", return false.
# Related Topics
# Dynamic Programming String
#
#
import unittest
# Time:  O(m * n)
# Space: O(m + n)
# Dynamic Programming + Sliding Window
class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) > len(s2):  # if s1 > s2. index out of range at match[i][0]
            return self.isInterleave(s2,s1,s3)
        match = [False for i in xrange(len(s1) + 1)]
        match[0] = True
        for i in xrange(1, len(s1) + 1):
            match[i] = match[i - 1] and s1[i -1] == s3[i - 1]

        for j in xrange(1, len(s2) + 1):
            match[0] = match[0] and s2[j - 1] == s3[j - 1]
            for i in xrange(1, len(s1) + 1):
                match[i] = (match[i - 1] and s1[i - 1] == s3[i + j -1]) or (match[i] and s2[j -1] == s3[i + j - 1])

        return match[-1]

# Time:  O(m * n)
# Space: O(m * n)
# Dynamic Programming
class Solution2:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False

        match = [[False for i in xrange(len(s2) + 1)]for j in xrange(len(s1) + 1)]
        match[0][0] = True

        for i in xrange(1, len(s1) + 1):
            match[i][0] = match[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in xrange(1, len(s2) + 1):
            match[0][j] = match[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in xrange(1, len(s1) + 1):
            for j in xrange(1, len(s2) + 1):
                match[i][j] = (match[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                              (match[i][j - 1] and s2[j - 1] == s3[i + j - 1])

        return match[-1][-1]

# Time:  O(m * n)
# Space: O(m * n)
# Recursive + Hash
class Solution3:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        self.match = {}
        if len(s1) + len(s2) != len(s3):
            return False
        return self.isInterleaveRecursive(s1, s2, s3, 0, 0, 0)

    def isInterleaveRecursive(self, s1, s2, s3, a, b, c ):
        if ([a, b]) in self.match.keys():
            return self.match[repr([a,b])]

        if c == len(s3):
            return True

        result = False
        if a < len(s1) and s1[a] == s3[c]:
            result = result or self.isInterleaveRecursive(s1, s2, s3, a + 1, b, c + 1)
        if b < len(s2) and s2[b] == s3[c]:
            result = result or self.isInterleaveRecursive(s1, s2, s3, a, b + 1, c + 1)

        #self.match[repr([a,b])] = result
        self.match[str([a,b])] = result

        return result

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        my_test = Solution3()
        #print my_test.isInterleave("aabcc","dbbca","aadbbcbcac")
        #print my_test.isInterleave("aabcc","dbbca","aadbbbaccc")
        print Solution3().isInterleave("a", "", "a")
        print Solution2().isInterleave("aabcc", "dbbca", "aadbbcbcac")
        print Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc")

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/interleaving-string/solution/
Thought: https://leetcode.com/problems/interleaving-string/tabs/solution#approach-2-recursion-with-memoization-accepted
#68%  4ms
public class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        int l1 = s1.length();
        int l2 = s2.length();
        int l3 = s3.length();

        if( l1 + l2 != l3) return false;

        Map<String, Boolean> map = new HashMap<String, Boolean>();
        return dfs(s1, s2, s3, 0, 0, 0, map);
    }

    private boolean dfs(String s1, String s2, String s3, int l1, int l2, int l3, Map<String, Boolean> map){
        String key = Integer.toString(l1) + Integer.toString(l2);
        if(map.containsKey(key)){
            return map.get(key);
        }

        if(l3 == s3.length()) return true;

        boolean res = false;
        if(l1 < s1.length() && s1.charAt(l1) == s3.charAt(l3)){
            res = res | dfs( s1, s2, s3, l1 + 1, l2, l3 + 1, map);
        }
        if(l2 < s2.length() && s2.charAt(l2) == s3.charAt(l3)){
            res = res | dfs( s1, s2, s3, l1, l2 + 1, l3 + 1, map);
        }
        map.put(key, res);
        return res;
    }
}



#84.9% 3ms
public class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        int len1 = s1.length();
        int len2 = s2.length();
        int len3 = s3.length();
        if (len1 + len2 != len3) {
            return false;
        }
        boolean[] dp = new boolean[len2 + 1];
        dp[0] = true;
        for (int i = 0; i < len2; i++) {
            if (s2.charAt(i) == s3.charAt(i)) {
                dp[i + 1] = true;
            } else {
                break;
            }
        }
        for (int i = 0; i < len1; i++) {
            dp[0] &= s1.charAt(i) == s3.charAt(i);
            for (int j = 0; j < len2; j++) {
                dp[j + 1] = (dp[j + 1] && s1.charAt(i) == s3.charAt(i + j + 1)) || (dp[j] && s2.charAt(j) == s3.charAt(i + j + 1));
            }
        }
        return dp[len2];
    }
}

#84.9% 3ms
public class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        int len1 = s1.length();
        int len2 = s2.length();
        int len3 = s3.length();
        if (len1 + len2 != len3) {
            return false;
        }
        boolean[] dp = new boolean[len1 + 1];
        dp[0] = true;
        for (int i = 0; i < len1; i++) {
            if (s1.charAt(i) == s3.charAt(i)) {
                dp[i + 1] = true;
            } else {
                break;
            }
        }
        for (int i = 0; i < len2; i++) {
            dp[0] &= s2.charAt(i) == s3.charAt(i);
            for (int j = 0; j < len1; j++) {
                dp[j + 1] = (dp[j] && s1.charAt(j) == s3.charAt(i + j + 1)) || (dp[j + 1] && s2.charAt(i) == s3.charAt(i + j + 1));
            }
        }
        return dp[len1];
    }
}

#68.5% 4ms
public class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        int l1 = s1.length();
        int l2 = s2.length();
        int l3 = s3.length();

        if ( l1 + l2 != l3) return false;

        boolean[][] dp = new boolean[l1 + 1][l2 + 1];
        dp[0][0] = true;

        for (int i = 1; i <= l1; i++){
            dp[i][0] = dp[i-1][0] & (s1.charAt(i - 1) == s3.charAt(i -1));
        }

        for (int i = 1; i <= l2; i++){
            dp[0][i] = dp[0][i-1] & (s2.charAt(i - 1) == s3.charAt(i -1));
        }

        for (int i = 1; i <= l1; i++){
            for (int j = 1; j <= l2; j++){
                dp[i][j] = (dp[i-1][j] && (s1.charAt(i - 1) == s3.charAt(i + j - 1) )) ||
                (dp[i][j-1] && ( s2.charAt(j-1) == s3.charAt( i + j - 1)  ));
            }
        }
        return dp[l1][l2];
    }
}
'''