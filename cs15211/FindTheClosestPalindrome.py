__source__ = 'https://leetcode.com/problems/find-the-closest-palindrome/#/description'
# Time:  O()
# Space: O()
#
# Description:
# Given an integer n, find the closest integer (not including itself), which is a palindrome.
# The 'closest' is defined as absolute difference minimized between two integers.
#
# Example 1:
# Input: "123"
# Output: "121"
# Note:
# The input n is a positive integer represented by string, whose length will not exceed 18.
# If there is a tie, return the smaller one as answer.
# Hide Company Tags Yelp
# Hide Tags String
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
#Thought:
public class Solution {
    public String nearestPalindromic(String n) {
        if (n.length() >= 2 && allNine(n)) {
            String s = "1";
            for (int i = 0; i < n.length() - 1; i++) {
                s += "0";
            }
            s += "1";
            return s;
        }
        boolean isOdd = (n.length() % 2 != 0);
        String left = n.substring(0, (n.length() + 1) / 2);
        long[] increment = {-1, 0, +1};
        String ret = n;
        long minDiff = Long.MAX_VALUE;
        for (long i : increment) {
            String s = getPalindrom(Long.toString(Long.parseLong(left) + i), isOdd);
            if (n.length() >= 2 && (s.length() != n.length() || Long.parseLong(s) == 0)) {
                s = "";
                for (int j = 0; j < n.length() - 1; j++) {
                    s += "9";
                }
            }
            long diff = s.equals(n) ? Long.MAX_VALUE : Math.abs(Long.parseLong(s) - Long.parseLong(n));
            if (diff < minDiff) {
                minDiff = diff;
                ret = s;
            }
        }
        return ret;
    }
    private String getPalindrom(String s, boolean isOdd) {
        String right = new StringBuilder(s).reverse().toString();
        return isOdd ? s.substring(0, s.length() - 1) + right : s + right;
    }
    private boolean allNine(String s) {
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != '9') {
                return false;
            }
        }
        return true;
    }
}
'''