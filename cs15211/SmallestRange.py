__source__ = 'https://leetcode.com/problems/smallest-range/'
# Time:  O(nlogn)
# Space: O(nlogn)
#
# Description: 632. Smallest Range
#
# You have k lists of sorted integers in ascending order.
# Find the smallest range that includes at least one number from each of the k lists.
#
# We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.
#
# Example 1:
# Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# Output: [20,24]
# Explanation:
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
# Note:
# The given list may contain duplicates, so ascending order means >= here.
# 1 <= k <= 3500
# -105 <= value of elements <= 105.
# For Java users, please note that the input type has been changed to List<List<Integer>>.
# And after you reset the code template, you'll see this point.

import unittest
import heapq
# Thought:
# Keep a heap of the smallest elements. As we pop element A[i][j], we'll replace it with A[i][j+1].
# For each such element left, we want right,
# the maximum of the closest value in each row of the array that is >= left,
# which is also equal to the current maximum of our heap. We'll keep track of right as we proceed.
#
# 128ms 88.58%
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        pq = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(pq)

        ans = -1e9, 1e9
        right = max(row[0] for row in nums)
        while pq:
            left, i, j = heapq.heappop(pq)
            if right - left < ans[1] - ans[0]:
                ans = left, right
            if j + 1 == len(nums[i]):
                return ans
            v = nums[i][j+1]
            right = max(right, v)
            heapq.heappush(pq, (v, i, j+1))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/smallest-range/solution/

1. Java Code using PriorityQueue.  
similar to merge k array
Image you are merging k sorted array using a heap. Then everytime you pop the smallest element out
and add the next element of that array to the heap. By keep doing this, you will have the smallest range.

# 73ms 70.26%
class Solution {
    public int[] smallestRange(List<List<Integer>> nums) {
        if (nums == null || nums.size() == 0 || nums.get(0).size() == 0) return new int[0];
        PriorityQueue<Element> pq = new PriorityQueue<>((a, b) -> a.mVal - b.mVal);
        int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
        int m = nums.size();
        for (int i = 0; i < m ; i++) {
            Element e = new Element(i, 0, nums.get(i).get(0));
            pq.offer(e);
            max = Math.max(max, nums.get(i).get(0));
        }

        int range = Integer.MAX_VALUE;
        int start = -1, end = -1;
        while (pq.size() == m) {
            Element cur = pq.poll();
            if ( max - cur.mVal < range) {
                range = max - cur.mVal;
                start  = cur.mVal;
                end = max;
            }
            if (cur.mIdx + 1 < nums.get(cur.mRow).size()){
                cur.mIdx = cur.mIdx + 1;
                cur.mVal = nums.get(cur.mRow).get(cur.mIdx);
                pq.offer(cur);
                if (cur.mVal > max) max = cur.mVal;
            }
        }
        return new int[]{start, end};
    }

    public class Element {
        int mVal;
        int mIdx;
        int mRow;

        public Element(int r, int i, int v) {
			mVal = v;
			mIdx = i;
			mRow = r;
		}
    }
}
'''
