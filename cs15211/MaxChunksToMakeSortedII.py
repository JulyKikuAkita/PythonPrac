__source__ = 'https://leetcode.com/problems/max-chunks-to-make-sorted-ii/'
# Time:  O(NlogN)
# Space: O(N)
#
# Description: Leetcode # 768. Max Chunks To Make Sorted II
#
# This question is the same as "Max Chunks to Make Sorted"
# except the integers of the given array are not necessarily distinct,
# the input array could be up to length 2000,
# and the elements could be up to 10**8.
#
# Given an array arr of integers (not necessarily distinct),
# we split the array into some number of "chunks" (partitions),
# and individually sort each chunk.
# After concatenating them, the result equals the sorted array.
#
# What is the most number of chunks we could have made?
#
# Example 1:
#
# Input: arr = [5,4,3,2,1]
# Output: 1
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3],
# which isn't sorted.
#
# Example 2:
#
# Input: arr = [2,1,3,4,4]
# Output: 4
# Explanation:
# We can split into two chunks, such as [2, 1], [3, 4, 4].
# However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
#
# Note:
#
#     arr will have length in range [1, 2000].
#     arr[i] will be an integer in range [0, 10**8].
#
import unittest
import collections
# 52ms 52.94%
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = collections.Counter()
        counted = []
        for x in arr:
            count[x] += 1
            counted.append((x, count[x]))

        ans, cur = 0, None
        for X, Y in zip(counted, sorted(counted)):
            cur = max(cur, X)
            if cur == Y:
                ans += 1
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/max-chunks-to-make-sorted-ii/solution/
#
Approach #1: Sliding Window [Accepted]
Complexity Analysis
Time Complexity: O(NLogN), where N is the length of arr
Space Complexity: O(N)

# 24ms 14.65%
class Solution {
    public int maxChunksToSorted(int[] arr) {
        Map<Integer, Integer> count = new HashMap();
        int ans = 0, nonzero = 0;

        int[] expect = arr.clone();
        Arrays.sort(expect);
        
        for (int i = 0; i < arr.length; ++i) {
            int x = arr[i], y = expect[i];
            
            count.put(x, count.getOrDefault(x, 0) + 1);
            if (count.get(x) == 0) nonzero--;
            if (count.get(x) == 1) nonzero++;
            
            count.put(y, count.getOrDefault(y, 0) - 1);
            if (count.get(y) == -1) nonzero++;
            if (count.get(y) == 0) nonzero--;

            if (nonzero == 0) ans++;
        }
        return ans;
    }
}

Approach #2: Sorted Count Pairs [Accepted]
Complexity Analysis
Time Complexity: O(NLogN), where N is the length of arr
Space Complexity: O(N)
# 61ms 4.46%
class Solution {
    public int maxChunksToSorted(int[] arr) {
        Map<Integer, Integer> count = new HashMap();
        List<Pair> counted = new ArrayList();
        for (int x : arr) {
            count.put(x, count.getOrDefault(x, 0) + 1);
            counted.add(new Pair(x, count.get(x)));
        }
        List<Pair> expect = new ArrayList(counted);
        Collections.sort(expect, (a, b) -> a.compare(b));
        
        Pair cur = counted.get(0);
        int ans = 0;
        for (int i = 0; i < arr.length; ++i) {
            Pair X = counted.get(i), Y = expect.get(i);
            if (X.compare(cur) > 0) cur = X;
            if (cur.compare(Y) == 0) ans++;
        }

        return ans;
    }
}

class Pair {
    int val, count;
    Pair(int v, int c) {
        val = v; count = c;
    }
    int compare(Pair that) {
        return this.val != that.val ? this.val - that.val : this.count - that.count;
    }
}


# 6ms 91.40%
class Solution {
    public int maxChunksToSorted(int[] arr) {
        if (arr.length == 0) return 0;
        int[] minArr = new int[arr.length];
        int min = arr[arr.length - 1];
        for (int i = arr.length - 1; i >= 0; i--) {
            min = Math.min(min, arr[i]);
            minArr[i] = min;
        }
        int res = 0;
        int max = arr[0];
        for (int i = 0; i < arr.length; i++) {
            max = Math.max(max, arr[i]);
            if (i == arr.length - 1 || max <= minArr[i + 1]) res++;
        }
        return res;
    }
}
'''
