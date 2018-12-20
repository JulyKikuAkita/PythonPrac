__source__ = 'https://leetcode.com/problems/minimum-genetic-mutation/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 433. Minimum Genetic Mutation
#
# A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".
#
# Suppose we need to investigate about a mutation (mutation from "start" to "end"),
# where ONE mutation is defined as ONE single character changed in the gene string.
#
# For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.
#
# Also, there is a given gene "bank", which records all the valid gene mutations.
# A gene must be in the bank to make it a valid gene string.
#
# Now, given 3 things - start, end, bank,
# your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end".
# If there is no such a mutation, return -1.
#
# Note:
#
# Starting point is assumed to be valid, so it might not be included in the bank.
# If multiple mutations are needed, all mutations during in the sequence must be valid.
# You may assume start and end string is not the same.
#
#
# Example 1:
#
# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]
#
# return: 1
#
#
# Example 2:
#
# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
#
# return: 2
#
#
# Example 3:
#
# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
#
# return: 3

import unittest
from collections import deque

# BFS through possible 3*8 mutations in each loop instead of all 4^8 - 1 possible genes.
# 28ms 21.82%
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        NUCLEOTIDES = ['A', 'C', 'T', 'G']
        bankSet = set(bank)

        q = deque()
        q.append((start, 0))

        L = len(start)

        # while loop contract
        # top cannot be in "bankSet"
        while q:
            top, topDist = q.popleft()

            if top == end:
                return topDist
            else:
                for i in xrange(L):
                    for nucleotide in NUCLEOTIDES:
                        gene_possible = top[:i] + nucleotide + top[i + 1:]
                        if gene_possible in bankSet:
                            bankSet.remove(gene_possible)
                            q.append((gene_possible, topDist + 1))
        return -1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: 
https://leetcode.com/problems/minimum-genetic-mutation/discuss/187877/JAVA-BFS-(-147-Word-Ladder)
# JAVA BFS ( ==147 Word Ladder)

# 2ms 65.05%
class Solution {
    private Set<String> dict, seen;
    private char[] GENES = {'G','C','A','T'};

    public int minMutation(String start, String end, String[] bank) {
        dict = new HashSet();
        for (String str : bank) dict.add(str);
        seen = new HashSet();

        Queue<String> q = new LinkedList();
        q.offer(start);
        int step = 0;
        boolean found = false;

        while (!q.isEmpty() && !found) {
            step++;
            int cnt = q.size();
            for (int i = 0; i < cnt; i++) {
                String cur = q.poll();
                List<String> mut = getMut(cur);
                for (String str: mut) {
                    if (str.equals(end)) {
                        found = true;
                        break;
                    }
                    if (!seen.contains(str)) {
                        seen.add(str);
                        q.offer(str);
                    }
                    if (found) break;
                }
            }
        }
        return found? step : -1;
    }

    private List<String> getMut(String word) {
        List<String> res = new LinkedList();
        char[] chars = word.toCharArray();
        for (int i = 0; i < 8; i++) {
            char pre = chars[i];
            for (char c : GENES) {
                chars[i] = c;
                if (dict.contains(String.valueOf(chars))) {
                    res.add(String.valueOf(chars));
                }
            }
            chars[i] = pre;
        }
        return res;
    }
}

# 2ms 65.05%
class Solution {
    public int minMutation(String start, String end, String[] bank) {
        if (start == null && end == null) {
            return 0;
        }
        final char[] genes = {'A', 'C', 'G', 'T'};
        Set<String> set = new HashSet<>();
        for (String b : bank) {
            set.add(b);
        }
        Queue<String> queue = new ArrayDeque<>();
        queue.offer(start);
        int numMutation = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String curr = queue.poll();
                if (curr.equals(end)) {
                    return numMutation;
                }
                char[] charArray = curr.toCharArray();
                for (int j = 0; j < charArray.length; j++) {
                    char currChar = charArray[j];
                    for (char gene : genes) { // A, C, G, T
                        if (gene != currChar) {
                            charArray[j] = gene;
                            String next = new String(charArray);
                            if (set.contains(next)) {
                                set.remove(next);
                                queue.offer(next);
                            }
                        }
                    }
                    charArray[j] = currChar;
                }
            }
            numMutation++;
        }
        return -1;
    }
}
'''
