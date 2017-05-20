__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/longest-palindromic-substring.py
# Time:  O(n)
# Space: O(n)
# String
#
# Given a string S, find the longest palindromic substring in S.
# You may assume that the maximum length of S is 1000,
#  and there exists one unique longest palindromic substring.
#
#  Amazon Microsoft Bloomberg

# Manacher's Algorithm
# Manacher (1975) found a linear time algorithm for listing all the palindromes that appear at the start of a given string.
#  However, as observed e.g., by Apostolico, Breslauer & Galil (1995), the same algorithm can also be used to find all maximal palindromic substrings anywhere within the input string,
# again in linear time. Therefore, it provides a linear time solution to the longest palindromic substring problem. Alternative linear time solutions were provided by Jeuring (1994),
# and by Gusfield (1997), who described a solution based on suffix trees. Efficient parallel algorithms are also known for the problem.[1]
# http://en.wikipedia.org/wiki/Longest_palindromic_substring
class Solution:
    def longestPalindrome(self, s):
        string = self.preProcess(s)
        palindrome = [0] * len(string)
        center, right = 0, 0
        print string, palindrome, len(string)

        for i in xrange(1, len(string) - 1):
            i_mirror = 2 * center - i
            if right > i:
                palindrome[i] = min(right - i, palindrome[i_mirror])
            else:
                palindrome[i] = 0

            print i, right, string[i + 1 + palindrome[i]], string[i - 1 - palindrome[i]], palindrome[i]
            while string[i + 1 + palindrome[i]] == string[i - 1 - palindrome[i]]:
                palindrome[i] += 1

            if i + palindrome[i] > right:
                center, right = i, i + palindrome[i]

        max_len, max_center = 0, 0
        for i in xrange(1, len(string) - 1):
            print i, palindrome, max_len
            if palindrome[i] > max_len:
                max_len = palindrome[i]
                max_center = i
        start = (max_center - 1 - max_len) / 2
        return s[start:start + max_len]

    def preProcess(self, s):
        if not s:
            return "^s"
        string = "^$"
        for i in s:
            string += "#" + i
        string += "#$"

        return string

# Time:  O(n^2)
# Space: O(1)
# http://www.programcreek.com/2013/12/leetcode-solution-of-longest-palindromic-substring-java/
# 3. A Simple Algorithm
class Solution2:
    def longestPalindrome(self, s):
        start, end = 0 , 0
        for i in xrange(len(s)):
            # get longest palindrome with center of i
            len1 = self.expandAroundCenter(s, i, i)
            # get longest palindrome with center of i, i+1
            len2 = self.expandAroundCenter(s, i , i + 1)
            finallen = max(len1, len2)

            if finallen > end - start:
                start = i - (finallen - 1) / 2
                end = i + finallen / 2
            #print "i = ",i, len1, len2, start, end
        return s[start:end+1]


    def expandAroundCenter(self, s, left, right):
        L, R = left, right
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L  - 1

# Time:  O(n^3)
# Space: O(1)
class naive:
    def longestPalindrome(self, s):
        maxPalinLen = 0
        longestPal = ""

        # check all possible sub strings
        for i in xrange(len(s)):
            for j in xrange(i+1, len(s)):
                cur_len = j - i
                curr = s[i:j+1]
                if self.isPalindrome(curr):
                    if cur_len > maxPalinLen:
                        longestPal = curr
                        maxPalinLen = cur_len
        return longestPal

    def isPalindrome(self, s):
        for i in xrange(len(s) / 2):
            if s[i] != s[-(i+1)]:
                return False
        return True

# Time:  O(n^2)
# Space: O(n^2)
# http://www.programcreek.com/2013/12/leetcode-solution-of-longest-palindromic-substring-java/
# 3. DP (OT)
class DP:
    def longestPalindrome(self, s):
        if not s or len(s) <=1:
            return s
        longestStr = ""
        dptable = [[0 for i in xrange(len(s))]for j in xrange(len(s))]

        # every single letter is palindrome
        for i in xrange(len(s)):
            dptable[i][i] = 1

        # e.g. bb
	    # two consecutive same letters are palindrome
        for i in xrange(len(s) - 2 + 1):
            if s[i] == s[i +1]:
                dptable[i][i+1] = 1
                longestStr = s[i:i+2]

        # condition for calculate whole table
        for i in xrange(3, len(s) + 1):
            for j in xrange(len(s) - i + 1):
                k = i + j - 1
                if s[j] == s[k]:
                    dptable[j][k] = dptable[j+1][k-1]
                    if dptable[j][k] == 1 :
                        longestStr = s[j:k+1]
                else:
                    dptable[j][k] = 0
                self.printtab(dptable)
        return longestStr

    def printtab(self, table):
        for i in xrange(len(table)):
            print table[i]
        print "----------------"



if __name__ == "__main__":
    #print Solution().longestPalindrome("abac")
    #print Solution2().longestPalindrome("abac")
    #print naive().longestPalindrome("abac")
    print DP().longestPalindrome("dabcba")


class SolutionOther:
    #dp solution :http://leetcode.com/2011/11/longest-palindromic-substring-part-i.html
    # You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
    # @return a string
    def longestPalindrome(self, s):
        arr = ['$' , '#']
        for i in range(len(s)):
            arr.append(s[i])
            arr.append('#')
        p = [0] * len(arr)
        print p
        print arr

        mx, pos, ansp = 0 , 0, 0
        for i in range(1, len(arr)):
            p[i] = min(mx - i ,p[2 * pos -i]) if mx > i else 1
            print "i= ", i, p[i], ansp, mx,pos
            while p[i] + i < len(arr) and arr[i + p[i]] == arr[i - p[i]]:
                print i, p[i], arr[i+p[i]]
                p[i] += 1
            if p[i] + i > mx:
                mx, pos = p[i] + i, i
            if p[i] > p[ansp]:
                ansp = i
        st = (ansp - p[ansp] + 1 ) //2
        print st
        return s[st:st+p[ansp] - 1]

#test
test = SolutionOther()
#print test.longestPalindrome("amorrroma")
#print test.longestPalindrome("ccd")

#str = "abcd"
#print str[0:2]

#java
js = '''
public class Solution {
    public String longestPalindrome(String s) {
        if (s.length() < 2) {
            return s;
        }
        int start = 0;
        int end = 0;
        for (int i = 1; i < s.length(); i++) {
            if (i - end + start - 1 >= 0 && isPalindrome(s, i - end + start - 1, i)) {
                start = i - end + start - 1;
                end = i;
            } else if (i - end + start - 2 >= 0 && isPalindrome(s, i - end + start - 2, i)) {
                start = i - end + start - 2;
                end = i;
            }
        }
        return s.substring(start, end + 1);
    }

    private boolean isPalindrome(String s, int start, int end) {
        while (start < end) {
            if (s.charAt(start++) != s.charAt(end--)) {
                return false;
            }
        }
        return true;
    }
}


public class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.length() == 0) {
            return s;
        }
        char[] strArr = generateExpandedCharArray(s);
        int[] manArr = new int[strArr.length];

        int center = 0;
        int right = 0;
        for (int i = 1; i < manArr.length - 1; i++) {
            if (i < right) {
                manArr[i] = Math.min(right - i, manArr[2 * center - i]);
            } else {
                manArr[i] = 0;
            }
            while (strArr[i + 1 + manArr[i]] == strArr[i - 1 - manArr[i]]) {
                manArr[i]++;
            }
            if (i + manArr[i] > right) {
                center = i;
                right = i + manArr[i];
            }
        }
        int len = 0;
        int mid = 0;
        for (int i = 1; i < manArr.length - 1; i++) {
            if (manArr[i] > len) {
                len = manArr[i];
                mid = i;
            }
        }
        int start = (mid - 1 - len) / 2;
        return s.substring(start, start + len);
    }

    private char[] generateExpandedCharArray(String s) {
        char[] origin = s.toCharArray();
        char[] result = new char[origin.length * 2 + 3];
        result[0] = '$';
        result[result.length - 1] = '%';
        for (int i = 1; i < result.length - 1; i++) {
            if ((i & 1) == 0) {
                result[i] = origin[(i >> 1) - 1];
            } else {
                result[i] = '#';
            }
        }
        return result;
    }
}


#dp
public class Solution {
    public String longestPalindrome(String s) {
        if(s.length() < 2) return s;

        boolean[][] dp = new boolean [s.length()][s.length()];
        String res = s.substring(0,1);
        for(int i = 1; i < s.length() ; i++){
            dp[i-1][i-1] = true;
            if(s.charAt(i-1) == s.charAt(i)){
                dp[i-1][i] = true;
                res = s.substring(i-1, i+1);
            }
        }
        dp[s.length()-1][s.length()-1] = true;

        for(int len = 3; len <= s.length(); len++){
            for(int i = 0; i + len <= s.length() ; i++){
                int j = i + len - 1;

                if(s.charAt(i) == s.charAt(j) && dp[i+1][j-1]){
                    dp[i][j] = true;
                    if(len > res.length()){
                        res = s.substring(i, j+1);
                    }
                }
            }
        }
        return res;
    }
}
'''