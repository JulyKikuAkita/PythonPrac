__source__ = 'https://leetcode.com/problems/find-k-th-smallest-pair-distance/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 719. Find K-th Smallest Pair Distance
#
# Given an integer array, return the k-th smallest distance among all the pairs.
# The distance of a pair (A, B) is defined as the absolute difference between A and B.
#
# Example 1:
# Input:
# nums = [1,3,1]
# k = 1
# Output: 0
# Explanation:
# Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.
# Note:
# 2 <= len(nums) <= 10000.
# 0 <= nums[i] < 1000000.
# 1 <= k <= len(nums) * (len(nums) - 1) / 2.
#
import unittest

# 52ms 100%
class Solution(object):
    def smallestDistancePair(self, nums, k):
        def possible(guess):
            #Is there k or more pairs with distance <= guess?
            count = left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k

        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi) / 2
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1

        return lo

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/find-k-th-smallest-pair-distance/solution/

Approach #1: Heap [Time Limit Exceeded]
Complexity Analysis
Time Complexity: O((k+N)logN), where N is the length of nums. As k = O(N^2), this is
O(N^2logN) in the worst case.
The complexity added by our heap operations is either O((k+N)logN) in the Java solution,
or O(klogN+N) in the Python solution because the heapq.heapify operation is linear time.
Additionally, we add O(NlogN) complexity due to sorting.
Space Complexity: O(N), the space used to store our heap of at most N-1 elements.

# TLE
class Solution {
    public int smallestDistancePair(int[] nums, int k) {
        Arrays.sort(nums);
        PriorityQueue<Node> heap = new PriorityQueue<Node>(nums.length,
            Comparator.<Node> comparingInt(node -> nums[node.nei] - nums[node.root]));
        for (int i = 0; i + 1 < nums.length; ++i) {
            heap.offer(new Node(i, i+1));
        }

        Node node = null;
        for (; k > 0; --k) {
            node = heap.poll();
            if (node.nei + 1 < nums.length) {
                heap.offer(new Node(node.root, node.nei + 1));
            }
        }
        return nums[node.nei] - nums[node.root];
    }
}

class Node {
    int root;
    int nei;
    Node(int r, int n) {
        root = r;
        nei = n;
    }
}

Approach #2: Binary Search + Prefix Sum [Accepted]
Complexity Analysis
Time Complexity: O(W+NlogW+NlogN), where N is the length of nums,
and W is equal to nums[nums.length - 1] - nums[0].
We do O(W) work to calculate prefix initially.
The logW factor comes from our binary search,
and we do O(N) work inside our call to possible (or to calculate count in Java).
The final O(NlogN) factor comes from sorting.
Space Complexity: (N+W), the space used to store multiplicity and prefix.

# 17ms 39.53%
class Solution {
    public int smallestDistancePair(int[] nums, int k) {
        Arrays.sort(nums);
        int WIDTH = 2 * nums[nums.length - 1];

        //multiplicity[i] = number of nums[j] == nums[i] (j < i)
        int[] multiplicity = new int[nums.length];
        for (int i = 1; i < nums.length; ++i) {
            if (nums[i] == nums[i-1]) {
                multiplicity[i] = 1 + multiplicity[i - 1];
            }
        }

        //prefix[v] = number of values <= v
        int[] prefix = new int[WIDTH];
        int left = 0;
        for (int i = 0; i < WIDTH; ++i) {
            while (left < nums.length && nums[left] == i) left++;
            prefix[i] = left;
        }

        int lo = 0;
        int hi = nums[nums.length - 1] - nums[0];
        while (lo < hi) {
            int mi = (lo + hi) / 2;
            int count = 0;
            for (int i = 0; i < nums.length; ++i) {
                count += prefix[nums[i] + mi] - prefix[nums[i]] + multiplicity[i];
            }
            //count = number of pairs with distance <= mi
            if (count >= k) hi = mi;
            else lo = mi + 1;
        }
        return lo;
    }
}

Approach #3: Binary Search + Sliding Window [Accepted]
Complexity Analysis
Time Complexity: O(NlogW+NlogN), where N is the length of nums,
and W is equal to nums[nums.length - 1] - nums[0].
The logW factor comes from our binary search,
and we do O(N) work inside our call to possible
(or to calculate count in Java).
The final O(NlogN) factor comes from sorting.
Space Complexity: O(1). No additional space is used except for integer variables.

# 6ms 99.27%
# Note: unable to apply the easy low +1 < high strategy
class Solution {
    public int smallestDistancePair(int[] nums, int k) {
        Arrays.sort(nums);
        int lo = 0, hi = nums[nums.length - 1] - nums[0];
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            int count = 0, left = 0;
            for (int right = 0; right < nums.length; right++) {
                while (nums[right] - nums[left] > mid) {
                    left++;
                }
                count += right - left;
            }
            //count = number of pairs with distance <= mid
            if (count >= k) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
'''