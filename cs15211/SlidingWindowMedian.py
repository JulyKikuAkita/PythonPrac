__source__ = 'https://leetcode.com/problems/sliding-window-median/'
# Time:  O(n*logk)
# Space: O()
#
# Description: 480. Sliding Window Median
#
# Median is the middle value in an ordered integer list.
# If the size of the list is even, there is no middle value.
# So the median is the mean of the two middle value.
#
# Examples:
# [2,3,4] , the median is 3
#
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Given an array nums, there is a sliding window of size k which is moving from the very left of the array
# to the very right. You can only see the k numbers in the window.
# Each time the sliding window moves right by one position.
# Your job is to output the median array for each window in the original array.
#
# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
#
# Window position                Median
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       1
#  1 [3  -1  -3] 5  3  6  7       -1
#  1  3 [-1  -3  5] 3  6  7       -1
#  1  3  -1 [-3  5  3] 6  7       3
#  1  3  -1  -3 [5  3  6] 7       5
#  1  3  -1  -3  5 [3  6  7]      6
# Therefore, return the median sliding window as [1,-1,-1,3,5,6].
#
# Note:
# You may assume k is always valid, ie: 1 <= k <= input array's size for non-empty array.
#
# Hide Company Tags Google
# Hide Similar Problems (H) Find Median from Data Stream
#
import unittest

class Solution(object):
    pass  # your function here

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/sliding-window-median/solution/

TreeMap is used to implement an ordered MultiSet.

Almost the same idea of Find Median from Data Stream 
https://leetcode.com/problems/find-median-from-data-stream/

Use two Heaps to store numbers. maxHeap for numbers smaller than current median,
minHeap for numbers bigger than and equal to current median.
A small trick I used is always make size of minHeap equal (when there are even numbers)
or 1 element more (when there are odd numbers) than the size of maxHeap.
Then it will become very easy to calculate current median.
Keep adding number from the right side of the sliding window and 
remove number from left side of the sliding window.
And keep adding current median to the result.

# 82ms 22.97%
class Solution {
    public double[] medianSlidingWindow(int[] nums, int k) {
        double[] res = new double[nums.length-k+1];
        TreeMap<Integer, Integer> minHeap = new TreeMap<Integer, Integer>();
        TreeMap<Integer, Integer> maxHeap = new TreeMap<Integer, Integer>(Collections.reverseOrder());
        
        int minHeapCap = k/2; //smaller heap when k is odd.
        int maxHeapCap = k - minHeapCap; 
        
        for(int i=0; i< k; i++){
            maxHeap.put(nums[i], maxHeap.getOrDefault(nums[i], 0) + 1);
        }
        int[] minHeapSize = new int[]{0};
        int[] maxHeapSize = new int[]{k};
        for(int i=0; i< minHeapCap; i++){
            move1Over(maxHeap, minHeap, maxHeapSize, minHeapSize);
        }
        
        res[0] = getMedian(maxHeap, minHeap, maxHeapSize, minHeapSize);
        int resIdx = 1;
        
        for(int i=0; i< nums.length-k; i++){
            int addee = nums[i+k];
            if(addee <= maxHeap.keySet().iterator().next()){
                add(addee, maxHeap, maxHeapSize);
            } else {
                add(addee, minHeap, minHeapSize);
            }
            
            int removee = nums[i];
            if(removee <= maxHeap.keySet().iterator().next()){
                remove(removee, maxHeap, maxHeapSize);
            } else {
                remove(removee, minHeap, minHeapSize);
            }

            //rebalance
            if(minHeapSize[0] > minHeapCap){
                move1Over(minHeap, maxHeap, minHeapSize, maxHeapSize);
            } else if(minHeapSize[0] < minHeapCap){
                move1Over(maxHeap, minHeap, maxHeapSize, minHeapSize);
            }
            
            res[resIdx] = getMedian(maxHeap, minHeap, maxHeapSize, minHeapSize);
            resIdx++;
        }
        return res;
    }

    public double getMedian(TreeMap<Integer, Integer> bigHeap, TreeMap<Integer, Integer> smallHeap, int[] bigHeapSize, int[] smallHeapSize){
        return bigHeapSize[0] > smallHeapSize[0] ? (double) bigHeap.keySet().iterator().next() : ((double) bigHeap.keySet().iterator().next() + (double) smallHeap.keySet().iterator().next()) / 2.0;
    }
    
    //move the top element of heap1 to heap2
    public void move1Over(TreeMap<Integer, Integer> heap1, TreeMap<Integer, Integer> heap2, int[] heap1Size, int[] heap2Size){
        int peek = heap1.keySet().iterator().next();
        add(peek, heap2, heap2Size);
        remove(peek, heap1, heap1Size);
    }
    
    public void add(int val, TreeMap<Integer, Integer> heap, int[] heapSize){
        heap.put(val, heap.getOrDefault(val,0) + 1);
        heapSize[0]++;
    }
    
    public void remove(int val, TreeMap<Integer, Integer> heap, int[] heapSize){
        if(heap.put(val, heap.get(val) - 1) == 1) heap.remove(val);
        heapSize[0]--;
    }
}
'''
