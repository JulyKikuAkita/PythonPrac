__source__ = 'https://leetcode.com/problems/h-index/tabs/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/h-index.py
# Time:  O(n)
# Space: O(n)
#
# Description: Leetcode # 274. H-Index
#
# Given an array of citations (each citation is a non-negative integer)
# of a researcher, write a function to compute the researcher's h-index.
#
# According to the definition of h-index on Wikipedia:
# "A scientist has index h if h of his/her N papers have
# at least h citations each, and the other N - h papers have
# no more than h citations each."
#
# For example, given citations = [3, 0, 6, 1, 5],
# which means the researcher has 5 papers in total
# and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and
# the remaining two with no more than 3 citations each, his h-index is 3.
#
# Note: If there are several possible values for h, the maximum one is taken as the h-index.
#
# Companies
# Bloomberg Google Facebook
# Related Topics
# Hash Table Sort
# Similar Questions
# H-Index II
#
import unittest
# Counting sort.
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        count = [0] * (n + 1)
        for x in citations:
            # put all x >= n in the same bucket
            if x >= n:
                count[n] += 1
            else:
                count[x] += 1
        h = 0
        for i in reversed(xrange(0, n + 1)):
            h += count[i]
            if h >= i:
                return i
            return h

# Time:  O(nlogn)
# Space: O(1)
class Solution2(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse = True)
        h = 0
        for x in citations:
            if x >= h + 1:
                h += 1
            else:
                break
        return h

# Time:  O(nlogn)
# Space: O(n)
class Solution3(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        return sum(x >= i + 1 for i, x  in enumerate(sorted(citations, reverse=True)))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/h-index/tabs/solution
citations[index] >= length(citations) - index

1. Comparison sort based
# Time:  O(n log n)
# Space: O(1)
#10.43% 3ms
public class Solution {
    public int hIndex(int[] citations) {
        // sorting the citations in ascending order
        Arrays.sort(citations);
        // finding h-index by linear search
        int i = 0;
        while (i < citations.length && citations[citations.length - 1 - i] > i) {
            i++;
        }
        return i; // after the while loop, i = i' + 1
    }
}

2. counting sort
# 50.50% 1ms
public class Solution {
    public int hIndex(int[] citations) {
        int n = citations.length;
        int[] papers = new int[n + 1];
        // counting papers for each citation number
        for (int c: citations)
            papers[Math.min(n, c)]++;
        // finding the h-index
        int k = n;
        for (int s = papers[n]; k > s; s += papers[k])
            k--;
        return k;
    }
}

3. bucket sort: 94 % - 50%
# 50.50% 1ms
public class Solution {
    public int hIndex(int[] citations) {
        int n = citations.length;
        int[] bucket = new int[n + 1];
        for(int c : citations) {
            if(c >= n) bucket[n]++;
            else bucket[c]++;
        }
        int count = 0;
        for(int i=n; i>= 0; i--) {
            count += bucket[i];
            if(count >= i) return i;
        }
        return 0;
    }
}
'''