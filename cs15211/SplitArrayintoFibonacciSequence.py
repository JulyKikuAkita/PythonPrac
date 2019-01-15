__source__ = 'https://leetcode.com/problems/split-array-into-fibonacci-sequence/'
# Time:  O(N^2)
# Space: O(N)
#
# Description: Leetcode # 842. Split Array into Fibonacci Sequence
#
# Given a string S of digits, such as S = "123456579",
# we can split it into a Fibonacci-like sequence [123, 456, 579].
#
# Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:
#
# 0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
# F.length >= 3;
# and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
# Also, note that when splitting the string into pieces,
# each piece must not have extra leading zeroes, except if the piece is the number 0 itself.
#
# Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.
#
# Example 1:
#
# Input: "123456579"
# Output: [123,456,579]
# Example 2:
#
# Input: "11235813"
# Output: [1,1,2,3,5,8,13]
# Example 3:
#
# Input: "112358130"
# Output: []
# Explanation: The task is impossible.
# Example 4:
#
# Input: "0123"
# Output: []
# Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
# Example 5:
#
# Input: "1101111"
# Output: [110, 1, 111]
# Explanation: The output [11, 0, 11, 11] would also be accepted.
# Note:
#
# 1 <= S.length <= 200
# S contains only digits.
#
import unittest

# 24ms 100%
class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        for i in xrange(min(10, len(S))):
            x = S[:i+1]
            if x != '0' and x.startswith('0'): break
            a = int(x)
            for j in xrange(i+1, min(i+10, len(S))):
                y = S[i+1: j+1]
                if y != '0' and y.startswith('0'): break
                b = int(y)
                fib = [a, b]
                k = j + 1
                while k < len(S):
                    nxt = fib[-1] + fib[-2]
                    nxtS = str(nxt)
                    if nxt <= 2**31 - 1 and S[k:].startswith(nxtS):
                        k += len(nxtS)
                        fib.append(nxt)
                    else :
                        break
                else:
                    if len(fib) >= 3:
                        return fib
        return []

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/split-array-into-fibonacci-sequence/solution/

The first two elements of the array uniquely determine the rest of the sequence.

Approach #1: Brute Force [Accepted]
Complexity Analysis
Time Complexity: O(N^2), where N is the length of S,
and with the requirement that the values of the answer are O(1) in length.
Space Complexity: O(N).

# 4ms 100%
class Solution {
    public List<Integer> splitIntoFibonacci(String S) {
        int N = S.length();
        for (int i = 0; i < Math.min(10, N); ++i) {
            if (S.charAt(0) == '0' && i > 0) break;
            long a = Long.valueOf(S.substring(0, i+1));
            if (a >= Integer.MAX_VALUE) break;

            search: for (int j = i+1; j < Math.min(i+10, N); ++j) {
                if (S.charAt(i+1) == '0' && j > i+1) break;
                long b = Long.valueOf(S.substring(i+1, j+1));
                if (b >= Integer.MAX_VALUE) break;

                List<Integer> fib = new ArrayList();
                fib .add((int) a);
                fib .add((int) b);

                int k = j + 1;

                while (k < N) {
                    long next = fib.get(fib.size() - 2) + fib.get(fib.size() - 1);
                    String nextS = String.valueOf(next);

                    if (next <= Integer.MAX_VALUE && S.substring(k).startsWith(nextS)) {
                        k += nextS.length();
                        fib.add((int) next);
                    }
                    else continue search;
                }
                if (fib.size() >= 3) return fib;
            }
        }
        return new ArrayList<Integer>();
    }
}


# 4ms 100%
class Solution {
    public List<Integer> splitIntoFibonacci(String S) {
        List<Integer>result = new ArrayList<>();
        helper(S,result,0);
        return result;
    }

    private boolean helper(String S,List<Integer>result,int index){
        if (index == S.length() && result.size() >= 3) return true;
        long num = 0;
        for (int i = index; i < S.length(); i++) {
            if (S.charAt(index) == '0' &&  i > index) break;
            num = num * 10 + (S.charAt(i) - '0');
            if (num > Integer.MAX_VALUE) break;
            //not !=num then break but < num then break,
            // cuz if the sum of last >= num, then there are still possibility as we increase num by one digit
            if (result.size() > 2 && result.get(result.size() - 2) + result.get(result.size() - 1) < num) break;
            if (result.size() <= 1 || num == result.get(result.size() - 2) + result.get(result.size() - 1)) {
                result.add((int) num);
                if (helper(S, result, i + 1)) return true;
                result.remove(result.size() - 1);
            }
        }
        return false;
    }
}
'''
