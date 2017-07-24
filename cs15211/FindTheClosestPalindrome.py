__source__ = 'https://leetcode.com/problems/find-the-closest-palindrome/#/description'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 234. Palindrome Linked List
# Given an integer n, find the closest integer (not including itself), which is a palindrome.
# The 'closest' is defined as absolute difference minimized between two integers.
#
# Example 1:
# Input: "123"
# Output: "121"
# Note:
# The input n is a positive integer represented by string, whose length will not exceed 18.
# If there is a tie, return the smaller one as answer.
#   Hide Hint 1
# Will brute force work for this problem? Think of something else.
#    Hide Hint 2
# Take some examples like 1234, 999,1000, etc and check their closest palindromes. How many different cases are possible?
#    Hide Hint 3
# Do we have to consider only left half or right half of the string or both?
#    Hide Hint 4
# Try to find the closest palindrome of these numbers- 12932, 99800, 12120. Did you observe something?
#
# Companies
# Yelp
# Related Topics
# String
#
import unittest
#
# Let's build a list of candidate answers for which the final answer must be one of those candidates.
# Afterwards, choosing from these candidates is straightforward.
#
# If the final answer has the same number of digits as the input string S,
# then the answer must be the middle digits + (-1, 0, or 1) flipped into a palindrome.
# For example, 23456 had middle part 234, and 233, 234, 235 flipped into a palindrome
# yields 23332, 23432, 23532. Given that we know the number of digits,
# the prefix 235 (for example) uniquely determines the corresponding palindrome 23532,
# so all palindromes with larger prefix like 23732 are strictly farther away from S than 23532 >= S.
#
# If the final answer has a different number of digits, it must be of the form 999....999 or 1000...0001,
# as any palindrome smaller than 99....99 or bigger than 100....001 will be farther away from S.
# 62ms
class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        K = len(n)
        candidates = [str(10**k + d) for k in (K-1, K) for d in (-1, 1)]
        prefix = n[:(K+1)/2]
        P = int(prefix)
        for start in map(str, (P-1, P, P+1)):
            candidates.append(start + (start[:-1] if K%2 else start)[::-1])

        def delta(x):
            return abs(int(n) - int(x))

        ans = None
        for cand in candidates:
            if cand != n and not cand.startswith('00'):
                if (ans is None or delta(cand) < delta(ans) or
                        delta(cand) == delta(ans) and int(cand) < int(ans)):
                    ans = cand
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/find-the-closest-palindrome/solution/
Time: O(n^-1/2)
Space: O(1)
#Brute force - TLE
public class Solution {
    public String nearestPalindromic(String n) {
        long num = Long.parseLong(n);
        for (long i = 1;; i++) {
            if (isPalindrome(num - i))
                return "" + (num - i);
            if (isPalindrome(num + i))
                return "" + (num + i);
        }
    }
    boolean isPalindrome(long x) {
        long t = x, rev = 0;
        while (t > 0) {
            rev = 10 * rev + t % 10;
            t /= 10;
        }
        return rev == x;
    }
}

#Thought:
#
# case1: if n >= 99 and all digit 9, the nearest should be 101, 1001, etc
# case2: generate palindrome with left part of n+1, n, n-1, if
#  res not valid number or to the next level, return 999(...) based on n's length
#  or return min distance res
#86.28%  18ms
public class Solution {
    public String nearestPalindromic(String n) {
        if (n.length() >= 2 && allNine(n)) { //999, 9999, ...
            String s = "1";
            for (int i = 0; i < n.length() - 1; i++) {
                s += "0";
            }
            s += "1";
            return s;
        }

        boolean isOdd = (n.length() & 1) == 1;
        String left = n.substring(0, (n.length() + 1) / 2);
        long[] increment = {-1, 0, 1};
        String ret = n;
        long minDiff = Long.MAX_VALUE, nL = Long.parseLong(n);
        for (long l : increment) {
            String candidate = getPalindrom(Long.toString(Long.parseLong(left) + l), isOdd);
            //System.out.println(candidate +" " + left);
            long candL = Long.parseLong(candidate);
            if (n.length() >= 2 && (candidate.length() != n.length() || candL == 0)) {
                candidate = "";
                for (int j = 0; j < n.length() - 1; j++) candidate += "9";
                candL = Long.parseLong(candidate);
            }
            long diff = candidate.equals(n) ? Long.MAX_VALUE : Math.abs(candL - nL);
            if (diff < minDiff) {
                minDiff = diff;
                ret = candidate;
            }
        }
        return ret;
    }

    private String getPalindrom(String left, boolean isOdd) {
        String right = new StringBuilder(left).reverse().toString();
        return isOdd ? left.substring(0, left.length() - 1) + right : left + right;
    }

    private boolean allNine(String s) {
        for (char c : s.toCharArray()) {
            if ( c != '9') return false;
        }
        return true;
    }
}
'''