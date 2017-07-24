__source__ = 'https://leetcode.com/problems/split-array-into-consecutive-subsequences/description/'
# Time:  O(n)
# Space: O(n)
#
# Description: Leetcode # 659. Split Array into Consecutive Subsequences
# You are given an integer array sorted in ascending order (may contain duplicates),
# you need to split them into several subsequences,
# where each subsequences consist of at least 3 consecutive integers.
# Return whether you can make such a split.
#
# Example 1:
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3
# 3, 4, 5
# Example 2:
# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3, 4, 5
# 3, 4, 5
# Example 3:
# Input: [1,2,3,4,4,5]
# Output: False
# Note:
# The length of the input is in range of [1, 10000]
#
# Companies
# Google
# Related Topics
# Heap Greedy
# Similar Questions
# Top K Frequent Elements
#
import unittest
import heapq

# Thought:
# I am using a kind of greedy method. runs build a map between tail number and the current run length.
# For example, for a consecutive seq 3,4,5, the key(tail number) is 5 and length is 3.
#
# The problem is there might be multiple sub seqs which all end with the same number,
# but have different length. like we have another subseq 4,5.
# So there are two entries in the value part of 5: runs: {5: [3,2]}
#
# so, when we met a new number 6, we want to merge it into existing subseqs.
# Which one should we use? Intuitively, if we pick up the shorter one and append the new number into that,
# we are more likely to make sure all the seqs are longer than 3.
# So I use a PriorityQueue to store these length.
#
#812ms
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        runs = {} # end -> [lengths]
        for v in nums:
            if v - 1 not in runs:
                if v not in runs:
                    runs[v] = [1]
                else:
                    heapq.heappush(runs[v], 1)
            else:
                length = heapq.heappop(runs[v-1]) + 1
                if len(runs[v-1]) == 0:
                    del runs[v-1]
                if v not in runs:
                    runs[v] = []
                heapq.heappush(runs[v], length)
        for v, arr in runs.items():
            if len(arr) > 0 and min(arr) < 3:
                return False
        return True

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
# 47.83% 101ms
We iterate through the array once to get the frequency of all the elements in the array
We iterate through the array once more and for each element we either
see if it can be appended to a previously constructed consecutive sequence or
if it can be the start of a new consecutive sequence. If neither are true, then we return false.

public class Solution {
    public boolean isPossible(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>(), appendfreq = new HashMap<>();
        for (int i : nums) freq.put(i, freq.getOrDefault(i,0) + 1);
        for (int i : nums) {
            if (freq.get(i) == 0) continue;
            else if ( appendfreq.getOrDefault(i, 0) > 0 ) {
                appendfreq.put(i, appendfreq.get(i) - 1);
                appendfreq.put(i+1, appendfreq.getOrDefault(i+1,0) + 1);
            }
            else if (freq.getOrDefault(i+1, 0) > 0 && freq.getOrDefault(i+2, 0) > 0) {
                freq.put(i + 1, freq.get(i + 1) - 1);
                freq.put(i + 2, freq.get(i + 2) - 1);
                appendfreq.put(i + 3, appendfreq.getOrDefault(i + 3, 0) + 1);
            }
            else return false;
            freq.put(i, freq.get(i) - 1);
        }
        return true;
    }
}

#98.11% 18ms
public class Solution {
    public boolean isPossible(int[] nums) {
        if (nums.length < 3) {
            return false;
        }
        // Use to store the head of each subsequence
        Deque<Integer> q = new LinkedList<Integer>();
        int prev = 0; // the end of the previous subsequence
        for (int i = 0; i < nums.length; i++) {
            int count = 1;
            while ( i < nums.length-1 && nums[i] == nums[i+1]) {
                count++;
                i++;
            }
            if (i > 0 && nums[i] > prev+1) // discontine on previous subsequences
            { // check if all previous subsequences are valid
                if (!isValid(q, prev, 0)) {
                    return false;
                }
            }
            // number of elements is smaller than the subsequence heads
            // some subsequences must end
            int size = q.size();
            if (count < size) {
                if (!isValid(q, prev, count)) {
                    return false;
                }
            } else if (count > size){
                for (int j = 0; j < count-size; j++) {
                    q.offerLast(nums[i]);
                }
            }
            prev = nums[i];

        }
        return isValid(q, nums[nums.length-1], 0);
    }

    private boolean isValid(Deque<Integer> q, int end, int count) {
        int size = q.size();
        for (int i = 0; i < size-count; i++) {
            int head = q.pollFirst();
            if (end-head < 2) {
                return false;
            }
        }
        return true;
    }
}

# 99.05% 17ms
public class Solution {
    public boolean isPossible(int[] nums) {
        int needTwo = 0;
        int nextNeedTwo = 0;
        int needOne = 0;
        int nextNeedOne = 0;
        int connectedToHere = 0;
        int nextConnectedToHere = 0;
        int pre = nums[0];
        for(int i = 0;i<nums.length;i++){
            if(nums[i]==pre){
                if(needTwo>0){
                    needTwo--;
                    nextNeedOne++;
                }else if(needOne>0){
                    needOne--;
                    nextConnectedToHere++;
                }else if(connectedToHere>0){
                    connectedToHere--;
                    nextConnectedToHere++;
                }else {
                    nextNeedTwo++;
                }
            }else if(nums[i]==pre+1){
                if(needTwo>0||needOne>0){
                    return false;
                }else{
                    needTwo = nextNeedTwo;
                    needOne = nextNeedOne;
                    connectedToHere = nextConnectedToHere;
                    nextNeedTwo = 0;
                    nextNeedOne = 0;
                    nextConnectedToHere =  0;
                    pre = nums[i];
                    i--;
                }
            }else{
                if(needTwo>0||needOne>0){
                    return false;
                }else if(nextNeedTwo>0||nextNeedOne>0){
                    return false;
                }else{
                    connectedToHere = 0;
                    nextNeedTwo = 0;
                    nextNeedOne = 0;
                    nextConnectedToHere =  0;
                    pre = nums[i];
                    i--;
                }
            }
        }
        if(needTwo>0||needOne>0||nextNeedTwo>0||nextNeedOne>0){
                    return false;
                }
        return true;
    }
}
'''