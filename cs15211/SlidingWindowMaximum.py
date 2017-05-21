__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/sliding-window-maximum.py
# Time:  O(n)
# Space: O(k)
#
# Given an array nums, there is a sliding window of size k
# which is moving from the very left of the array to the
# very right. You can only see the k numbers in the window.
# Each time the sliding window moves right by one position.
#
# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Therefore, return the max sliding window as [3,3,5,5,6,7].
#
# Note:
# You may assume k is always valid, ie: 1 <= k <= input array's size for non-empty array.
#
# Follow up:
# Could you solve it in linear time?
#
# Amazon Google Zenefits
# Hide Tags Heap
# Hide Similar Problems (H) Minimum Window Substring (E) Min Stack (H) Longest Substring with At Most Two Distinct Characters (H) Paint House II

from collections import deque

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        q = deque()
        max_numbers = []

        for i in xrange(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        for i in xrange(k, len(nums)):
            max_numbers.append(nums[q[0]])

            while q and nums[i] >= nums[q[-1]]:
                q.pop()

            while q and q[0] <= i - k:
                q.popleft()

            q.append(i)

        if q:
            max_numbers.append(nums[q[0]])

        return max_numbers


#java
js = '''
public class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if(nums == null || nums.length == 0){
            return new int[0];
        }

        int[] res = new int[nums.length - k  + 1];
        Deque<Integer> deque = new ArrayDeque<>();

        for(int i = 0; i < nums.length; i++){
            int cur = nums[i];
            // remove numbers out of range k
            while(!deque.isEmpty() && deque.peekFirst() <= i - k){
                deque.pollFirst();
            }
            // remove numbers out of range k
            while(!deque.isEmpty() && nums[deque.peekLast()] <= cur){
                deque.pollLast();
            }
            // q contains index... r contains content
            deque.offer(i);

            if ( i >= k - 1){
                res[i-k+1] = nums[deque.getFirst()];
            }
        }
        return res;
    }
}

public class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int len = nums.length;
        if (len == 0) {
            return new int[0];
        }
        int[] result = new int[len - k + 1];
        LinkedList<Integer> list = new LinkedList<>();
        for (int i = 0; i < len; i++) {
            while (!list.isEmpty() && nums[list.getLast()] <= nums[i]) {
                list.removeLast();
            }
            list.add(i);
            if (i >= k - 1) {
                result[i - k + 1] = nums[list.getFirst()];
                if (list.getFirst() == i - k + 1) {
                    list.removeFirst();
                }
            }
        }
        return result;
    }
}

#https://discuss.leetcode.com/topic/26480/o-n-solution-in-java-with-two-simple-pass-in-the-array
O(n) solution in Java with two simple pass in the array
public class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums == null || nums.length == 0) return new int[0];
        final int[] max_left = new int[nums.length];
        final int[] max_right = new int[nums.length];

        max_left[0] = nums[0];
        max_right[nums.length - 1] = nums[nums.length - 1];

        for (int i = 1 ;i < nums.length; i++)  {
            max_left[i] = (i % k == 0) ? nums[i] : Math.max(nums[i], max_left[i-1]);
            int j = nums.length - i - 1;
            max_right[j] = (j %  k == 0) ? nums[j] : Math.max(max_right[j + 1], nums[j]);
        }

        int[] res = new int[nums.length - k + 1];
        for (int i = 0, j = 0; i + k <= nums.length; i++, j++) {
            res[j] = Math.max(max_left[i + k - 1], max_right[i]);
        }
        return res;
    }
}

# monotonic queue problem
https://discuss.leetcode.com/topic/19297/this-is-a-typical-monotonic-queue-problem
Sliding window minimum/maximum = monotonic queue. I smelled the solution just when I read the title.
This is essentially same idea as others' deque solution, but this is much more standardized and modulized.
If you ever need to use it in your real product, this code is definitely more preferable.

What does Monoqueue do here:

It has three basic options:

push: push an element into the queue; O (1) (amortized)

pop: pop an element out of the queue; O(1) (pop = remove, it can't report this element)

max: report the max element in queue;O(1)

It takes only O(n) time to process a N-size sliding window minimum/maximum problem.

Note: different from a priority queue (which takes O(nlogk) to solve this problem), it doesn't pop the max element:
It pops the first element (in original order) in queue.


'''