__source__ = 'https://leetcode.com/problems/top-k-frequent-elements/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/top-k-frequent-elements.py
# Time:  O(n) ~ O(n^2), O(n) on average.
# Space: O(n)
#
# Description: Leetcode # 347. Top K Frequent Elements
#
# Given a non-empty array of integers,
# return the k most frequent elements.
#
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].
#
# Note:
# You may assume k is always valid,
# 1 <= k <= number of unique elements.
# Your algorithm's time complexity must be better
# than O(n log n), where n is the array's size.
#
# Companies
# Pocket Gems Yelp
# Related Topics
# Hash Table Heap
# Similar Questions
# Word Frequency Kth Largest Element in an Array Sort Characters By Frequency
#

from random import randint
import collections
import unittest
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = collections.defaultdict(int)
        for i in nums:
            counts[i] += 1

        p = []
        for key, val in counts.iteritems():
            p.append((val, key))
        self.kthElement(p, k);

        result = []
        for i in xrange(k):
            result.append(p[i][1])
        return result

    def kthElement(self, nums, k):
        def PartitionAroundPivot(left, right, pivot_idx, nums):
            pivot_value = nums[pivot_idx][0]
            new_pivot_idx = left
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            for i in xrange(left, right):
                if nums[i][0] > pivot_value:
                    nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                    new_pivot_idx += 1

            nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
            return new_pivot_idx

        left, right = 0, len(nums) - 1
        while left <= right:
            pivot_idx = randint(left, right)
            new_pivot_idx = PartitionAroundPivot(left, right, pivot_idx, nums)
            if new_pivot_idx == k - 1:
                return
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:  # new_pivot_idx < k - 1.
                left = new_pivot_idx + 1

# Time:  O(nlogk)
# Space: O(n)
class Solution2(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return [key for key, _ in collections.Counter(nums).most_common(k)]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
// use an array to save numbers into different bucket whose index is the frequency
#83.84% 25ms
public class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int n: nums){
            map.put(n, map.getOrDefault(n,0)+1);
        }

        // corner case: if there is only one number in nums, we need the bucket has index 1.
        List<Integer>[] bucket = new List[nums.length+1]; //compile err if declare as new ArrayList<>[nums.length + 1];
        for(int n:map.keySet()){
            int freq = map.get(n);
            if(bucket[freq]==null)
                bucket[freq] = new LinkedList<>();
            bucket[freq].add(n);
        }

        List<Integer> res = new LinkedList<>();
        for(int i=bucket.length-1; i>0 && k>0; --i){ //bucket.length = nums.length + 1
            if(bucket[i]!=null){
                res.addAll(bucket[i]);
                k-= bucket[i].size();
            }
        }
        return res;
    }
}

// use maxHeap. Put entry into maxHeap so we can always poll a number with largest frequency
#14.82% 101ms
public class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int n: nums){
            map.put(n, map.getOrDefault(n,0)+1);
        }

        PriorityQueue<Map.Entry<Integer, Integer>> maxHeap =
                         new PriorityQueue<>((a,b)->(b.getValue()-a.getValue()));
        for(Map.Entry<Integer,Integer> entry: map.entrySet()){
            maxHeap.add(entry);
        }

        List<Integer> res = new ArrayList<>();
        while(res.size()<k){
            Map.Entry<Integer, Integer> entry = maxHeap.poll();
            res.add(entry.getKey());
        }
        return res;
    }
}

// use treeMap. Use freqncy as the key so we can get all freqencies in order
#63.61% 29ms
public class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int n: nums){
            map.put(n, map.getOrDefault(n,0)+1);
        }

        TreeMap<Integer, List<Integer>> freqMap = new TreeMap<>();
        for(int num : map.keySet()){
           int freq = map.get(num);
           if(!freqMap.containsKey(freq)){
               freqMap.put(freq, new LinkedList<>());
           }
           freqMap.get(freq).add(num);
        }

        List<Integer> res = new ArrayList<>();
        while(res.size()<k){
            Map.Entry<Integer, List<Integer>> entry = freqMap.pollLastEntry();
            res.addAll(entry.getValue());
        }
        return res;
    }
}
'''