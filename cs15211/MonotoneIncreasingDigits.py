# coding=utf-8
__source__ = 'https://leetcode.com/problems/monotone-increasing-digits/'
# Time:  O(logN)
# Space: O(N)
#
# Description: Leetcode # 738. Monotone Increasing Digits
#
#  Given a non-negative integer N,
# find the largest number that is less than or equal to N with monotone increasing digits.
#
# (Recall that an integer has monotone increasing digits
# if and only if each pair of adjacent digits x and y satisfy x <= y.)
#
# Example 1:
#
# Input: N = 10
# Output: 9
#
# Example 2:
#
# Input: N = 1234
# Output: 1234
#
# Example 3:
#
# Input: N = 332
# Output: 299
#
# Note: N is an integer in the range [0, 10^9].
#
import unittest

# 24ms 86.23%
class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        S = list(str(N))
        i = 1
        while i < len(S) and S[i-1] <= S[i]:
            i += 1
        while 0 < i < len(S) and S[i-1] > S[i]:
            S[i-1] = str(int(S[i-1]) - 1)
            i -= 1
        S[i+1:] = '9' * (len(S) - i-1)
        return int("".join(S))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/monotone-increasing-digits/solution/
#
Approach #1: Greedy [Accepted]
Complexity Analysis
Time Complexity: O(D^2), where D≈logN is the number of digits in N. 
We do O(D) work building and comparing each candidate, and we do this O(D) times.
Space Complexity: O(D), the size of the answer and the temporary string we are comparing.

# 12ms 54.26%
class Solution {
    public int monotoneIncreasingDigits(int N) {
        String S = String.valueOf(N);
        String ans = "";
        search: for (int i = 0; i < S.length(); ++i) {
            for (char d = '1'; d <= '9'; ++d) {
                if (S.compareTo(ans + repeat(d, S.length() - i)) < 0) {
                    ans += (char) (d - 1);
                    continue search;
                }
            }
            ans += '9';
        }
        return Integer.parseInt(ans);
    }

    public String repeat(char c, int count) {
        StringBuilder sb = new StringBuilder(count);
        for (int i = 0; i < count; ++i) sb.append(c);
        return sb.toString();
    }
}

Approach #2: Truncate After Cliff [Accepted]
Complexity Analysis
Time Complexity: O(D), where D≈logN is the number of digits in N. 
Each step in the algorithm is a linear scan of the digits.
Space Complexity: O(D), the size of the answer.

# 12ms 54.26%
class Solution {
    public int monotoneIncreasingDigits(int N) {
        char[] S = String.valueOf(N).toCharArray();
        int i = 1;
        while (i < S.length && S[i - 1] <= S[i]) i++;
        while (0 < i && i < S.length && S[i - 1] > S[i]) S[--i]--;
        for (int j = i + 1; j < S.length; j++) S[j] = '9';
        return Integer.parseInt(String.valueOf(S));
    }
}

# 7ms 100%
class Solution {
    // from right to left, if zero based ith digit is larger than previous, 
    // then need to change the number to 10^i - 1 + (previous digit) * 10^i.
    public int monotoneIncreasingDigits(int N) {
        int res = 0;
        for (int i = 1, previous = 9; N > 0; i *= 10, N /= 10) {
            int cur = N % 10;
            if (cur > previous) {
                previous = cur - 1;
                res = i * previous + i - 1;
            } else { // cur <= previous
                previous = cur;
                res += i * previous;
            }
        }
        return res;
    }
}

# 7ms 100%
class Solution {
    public int monotoneIncreasingDigits(int N) {
        if (N < 10) return N;
        char[] digits = String.valueOf(N).toCharArray();
        int index = 1;
        while (index < digits.length && digits[index - 1] <= digits[index]) index++;
        if (index == digits.length) return N;
        while (index > 1 && digits[index - 2] == digits[index - 1]) index--;
        char[] res;
        int start = 0;
        if (index > 0 && digits[index - 1] == '1') {
            res = new char[digits.length - index];
        } else {
            res = new char[digits.length];
            while (start < index) {
                res[start] = digits[start];
                start++;
            }
            res[start - 1]--;
        }
        
        while (start < res.length) res[start++] = '9';
        return Integer.valueOf(new String(res));
    }
}
'''
