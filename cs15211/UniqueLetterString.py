__source__ = ''
# Time:  O()
# Space: O()
#
# Description: Leetcode # 828. Unique Letter String
#
# A character is unique in string S if it occurs exactly once in it.
#
# For example, in string S = "LETTER", the only unique characters are "L" and "R".
#
# Let's define UNIQ(S) as the number of unique characters in string S.
#
# For example, UNIQ("LETTER") =  2.
#
# Given a string S with only uppercases,
# calculate the sum of UNIQ(substring) over all non-empty substrings of S.
#
# If there are two or more equal substrings at different positions in S, we consider them different.
#
# Since the answer can be very large, return the answer modulo 10 ^ 9 + 7.
#
# Example 1:
#
# Input: "ABC"
# Output: 10
# Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
# Evey substring is composed with only unique letters.
# Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
# Example 2:
#
# Input: "ABA"
# Output: 8
# Explanation: The same as example 1, except uni("ABA") = 1.
#
# Note: 0 <= S.length <= 10000.
#
import unittest
import collections

# 112ms 33.33%
class Solution(object):
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        N = len(S)
        index = collections.defaultdict(list)
        peek = collections.defaultdict(int)
        for i, c in enumerate(S):
            index[c].append(i)
        for c in index:
            index[c].extend([N, N])

        def get(c):
            return index[c][peek[c] + 1] - index[c][peek[c]]

        ans = 0
        cur = sum(get(c) for c in index)
        for i, c in enumerate(S):
            ans += cur
            oldv = get(c)
            peek[c] += 1
            cur += get(c) - oldv
        return ans % (10**9 + 7)

# 52ms 100%
class Solution(object):
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        index = collections.defaultdict(list)
        for i, c in enumerate(S):
            index[c].append(i)

        ans = 0
        for A in index.values():
            A = [-1] + A + [len(S)]
            for i in xrange(1, len(A) - 1):
                ans += (A[i] - A[i-1]) * (A[i+1] - A[i])
        return ans % (10**9 + 7)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/unique-letter-string/solution/
Approach #1: Maintain Answer of Suffix [Accepted]
Complexity Analysis
Time Complexity: O(N), where N is the length of S.
Space Complexity: O(N).

# 64ms 23.21%
class Solution {
    Map<Character, List<Integer>> index;
    int[] peek;
    int N;

    public int uniqueLetterString(String S) {
        index = new HashMap();
        peek = new int[26];
        N = S.length();

        for (int i = 0; i < S.length(); i++) {
            char c = S.charAt(i);
            index.computeIfAbsent(c, x-> new ArrayList<Integer>()).add(i);
        }

        long cur = 0, ans = 0;
        for (char c : index.keySet()) {
            index.get(c).add(N);
            index.get(c).add(N);
            cur += get(c);
        }

        for (char c : S.toCharArray()) {
            ans += cur;
            long oldv = get(c);
            peek[c - 'A']++;
            cur += get(c) - oldv;
        }
        return (int) ans % 1_000_000_007;
    }

    public long get(char c) {
        List<Integer> indexes = index.get(c);
        int i = peek[c - 'A'];
        return indexes.get(i + 1) - indexes.get(i);
    }
}

Approach #2: Split by Character [Accepted]
Complexity Analysis
Time Complexity: O(N), where N is the length of S.
Space Complexity: O(N). We could reduce this to O(A)
if we do not store all the indices, but compute the answer on the fly.

# 62ms 26.19%
class Solution {
    public int uniqueLetterString(String S) {
        Map<Character, List<Integer>> index = new HashMap();
        for (int i = 0; i < S.length(); i++) {
            char c = S.charAt(i);
            index.computeIfAbsent(c, x-> new ArrayList<Integer>()).add(i);
        }

        long ans = 0;
        for (List<Integer> A : index.values()) {
            for (int i = 0; i < A.size(); i++) {
                long prev = i > 0 ? A.get(i - 1) : - 1;
                long next = i < A.size() - 1 ? A.get(i+1) : S.length();
                ans += (A.get(i) - prev) * (next - A.get(i));
            }
        }
        return (int) ans % 1_000_000_007;
    }
}

# 8ms 100%
class Solution {
    static int MOD = 1000000007;
    public int uniqueLetterString(String S) {
	//pre stores the prev position of current char, prer stores prev postion of current char before pre
        int[] pre = new int[126], prer = new int[126];
        Arrays.fill(pre, -1);
        Arrays.fill(prer, -1);


        int sum = 0, cur = 0;
        char[] chs = S.toCharArray();
        for(int i = 0; i < chs.length; i++) {
	    //cur stores sum of all UNIQ over substring ending at postion i
            cur += (i - pre[chs[i]] - 1) - (pre[chs[i]] - prer[chs[i]]) + 1;
            prer[chs[i]] = pre[chs[i]];
            pre[chs[i]] = i;
            sum += cur;
            sum %= MOD;
        }

        return sum;
    }
}
'''