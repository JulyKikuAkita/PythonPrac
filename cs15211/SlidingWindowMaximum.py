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
#  Heap

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

            while(!deque.isEmpty() && deque.peekFirst() <= i - k){
                deque.pollFirst();
            }

            while(!deque.isEmpty() && nums[deque.peekLast()] <= cur){
                deque.pollLast();
            }

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
'''