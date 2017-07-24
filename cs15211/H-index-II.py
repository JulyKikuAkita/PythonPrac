__source__ = 'https://leetcode.com/problems/h-index-ii/tabs/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/h-index-ii.py
# Time:  O(logn)
# Space: O(1)
#
# Follow up for H-Index: What if the citations array is sorted in
# ascending order? Could you optimize your algorithm?
#
# Hint:
#
# Expected runtime complexity is in O(log n) and the input is sorted.
# Companies
# Facebook
# Related Topics
# Binary Search
# Similar Questions
# H-Index

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        n = len(citations)
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) / 2
            if citations[mid] >= n - mid:
                right = mid - 1
            else:
                left = mid + 1
        return n - left



#Java
Java = '''
citations[index] >= length(citations) - index

Thought: https://leetcode.com/problems/h-index/tabs/solution

Just binary search, each time check citations[mid]
case 1: citations[mid] == len-mid, then it means there are citations[mid] papers

that have at least citations[mid] citations.
case 2: citations[mid] > len-mid, then it means there are citations[mid] papers
that have moret than citations[mid] citations, so we should continue searching in the left half
case 3: citations[mid] < len-mid, we should continue searching in the right side
After iteration, it is guaranteed that right+1 is the one we need to find (i.e. len-(right+1) papars have at least len-(righ+1) citations)

1. 75%
public class Solution {
    public int hIndex(int[] citations) {
        if (citations.length == 0) {
            return 0;
        }
        int start = 0;
        int end = citations.length - 1;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (citations[mid] < citations.length - mid - 1) {
                start = mid;
            } else if (citations[mid] > citations.length - mid - 1) {
                end = mid;
            } else {
                return citations.length - mid - 1;
            }
        }
        if (citations[end] <= citations.length - end - 1) {
            return citations.length - end - 1;
        } else if (citations[start] <= citations.length - start - 1) {
            return citations.length - start - 1;
        } else {
            return citations.length;
        }
    }
}


#57%
public class Solution {
    public int hIndex(int[] citations) {
        // sanity check
        if (citations == null || citations.length == 0) return 0;
        int n = citations.length;

        int lo = 0, hi = n-1;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int h = n - mid;
            if (citations[mid] == h) return h;
            else if (citations[mid] < h) lo = mid + 1;
            else hi = mid -1;
        }

        return n - lo;
    }
}

3. 46%
I am very sure that two-branch binary search is more efficient than three branch binary search.
and (low + high) is not good idea since it may rely on the overflow behavior.
In fact, using count step first mid is the standard implement way of C++,
so I do not think there are better ways to implement the binary search.

public class Solution {
    public int hIndex(int[] citations) {
        int len = citations.length;

        int first = 0;
        int mid;
        int count = len;
        int step;

        while (count > 0) {
            step = count / 2;
            mid = first + step;
            if (citations[mid] < len - mid) {
                first = mid + 1;
                count -= (step + 1);
            }
            else {
                count = step;
            }
        }

        return len - first;
    }
}
'''