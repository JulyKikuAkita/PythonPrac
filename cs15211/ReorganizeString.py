import heapq

__source__ = 'https://leetcode.com/problems/reorganize-string/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 767. Reorganize String
#
# Given a string S, check if the letters can be rearranged
# so that two characters that are adjacent to each other are not the same.
#
# If possible, output any possible result.  If not possible, return the empty string.
#
# Example 1:
#
# Input: S = "aab"
# Output: "aba"
# Example 2:
#
# Input: S = "aaab"
# Output: ""
# Note:
#
# S will consist of lowercase letters and have length in range [1, 500].
#
import unittest

class Solution1(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        N = len(S)
        A = []
        for c, x in sorted ((S.count(x), x) for x in set(S)):
            if c > (N + 1) / 2: return ""
            A.extend(c * x)
        ans = [None] * N
        ans[::2], ans[1::2] = A[N/2:], A[:N/2]
        return "".join(ans)

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        pq = [(-S.count(x), x) for x in set(S)]
        heapq.heapify(pq)
        if any(-nc > (len(S) + 1) /2 for nc, x in pq):
            return ""
        ans = []
        while len(pq) >= 2:
            nct1, ch1 = heapq.heappop(pq)
            nct2, ch2 = heapq.heappop(pq)
            #This code turns out to be superfluous, but explains what is happening
            #if not ans or ch1 != ans[-1]:
            #    ans.extend([ch1, ch2])
            #else:
            #    ans.extend([ch2, ch1])
            ans.extend([ch1,ch2])
            if nct1 + 1:
                heapq.heappush(pq, (nct1 + 1, ch1))
            if nct2 + 1:
                heapq.heappush(pq, (nct2 + 1, ch2))
        return "".join(ans) + (pq[0][1] if pq else '')


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/reorganize-string/solution/
# 3ms, 100%
# If N is the length of the string,
# and the count of some letter is greater than (N+1) / 2, the task is impossible.
# Approach #1: Sort by Count [Accepted]
# Time Complexity: O(A(N+logA)), where N is the length of S, and A is the size of the alphabet.
# In Java, our implementation is O(N+AlogA). If A is fixed, this complexity is O(N).
# Space Complexity: O(N). In Java, our implementation is O(N+A).

class Solution {
    public String reorganizeString(String S) {
        int N = S.length();
        int[] counts = new int[26];
        //Encoded counts[i] = 100*(actual count) + (i)
        for (char c : S.toCharArray()) counts[c - 'a'] += 100;
        for (int i = 0; i < 26; i++) counts[i] += i;
        Arrays.sort(counts);

        char[] res = new char[N];
        int t = 1;
        for (int code: counts) {
            int ct = code / 100;
            char ch = (char) ('a' + (code % 100));
            if (ct > (N + 1) / 2) return "";
            for (int i = 0; i < ct; i++) {
                if (t >= N) t = 0;
                res[t] = ch;
                t += 2;
            }
        }
        return String.valueOf(res);
    }
}

# Approach #2: Greedy with Heap [Accepted]

# Time Complexity: O(NlogA)), where N is the length of S,
# and A is the size of the alphabet. If A is fixed, this complexity is O(N).
# Space Complexity: O(A). If A is fixed, this complexity is O(1).

class MultiChar{
    int count;
    char letter;
    MultiChar(int ct, char ch) {
        count = ct;
        letter = ch;
    }
}

class Solution {
    public String reorganizeString(String S) {
        int N = S.length();
        int[] count = new int[26];
        for (char c : S.toCharArray()) count[c - 'a']++;
        PriorityQueue<MultiChar> pq = new PriorityQueue<MultiChar>((a, b) -> a.count == b.count ? a.letter - b.letter : b.count - a.count);

        for (int i = 0; i < 26; i++) {
            if (count[i] > 0) {
                if (count[i] > (N + 1) / 2) return "";
                pq.add(new MultiChar(count[i], (char) ('a' + i)));
            }
        }

        StringBuilder sb = new StringBuilder();
        while (pq.size() >= 2) {
            MultiChar mc1 = pq.poll();
            MultiChar mc2 = pq.poll();
            /*This code turns out to be superfluous, but explains what is happening
            if (ans.length() == 0 || mc1.letter != ans.charAt(ans.length() - 1)) {
                ans.append(mc1.letter);
                ans.append(mc2.letter);
            } else {
                ans.append(mc2.letter);
                ans.append(mc1.letter);
            }*/
            sb.append(mc1.letter);
            sb.append(mc2.letter);
            if (--mc1.count > 0) pq.add(mc1);
            if (--mc2.count > 0) pq.add(mc2);
        }
        if (pq.size() > 0) sb.append(pq.poll().letter);
        return sb.toString();

    }
}

'''