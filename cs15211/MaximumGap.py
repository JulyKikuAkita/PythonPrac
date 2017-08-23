__source__ = 'https://leetcode.com/problems/maximum-gap/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/maximum-gap.py
# Time:  O(n)
# Space: O(n)
# sort
#
# Description: Leetcode # 164. Maximum Gap
#
# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
# Try to solve it in linear time/space.
# Return 0 if the array contains less than 2 elements.
#
# You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
# Related Topics
# Sort
#
import unittest
# idea: https://leetcode.com/discuss/18499/bucket-sort-java-solution-with-explanation-o-time-and-space
# calculate max gap for each section using bucket sort
# bucket sort
class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        if len(num) < 2:
            return 0

        unique_num = self.removeDuplicate(num)

        max_val, min_val = max(unique_num), min(unique_num)
        gap = (max_val - min_val) / (len(unique_num) - 1 )
        bucket_size = (max_val - min_val) / gap + 1
        max_bucket = [float("-inf") for _ in xrange(bucket_size)]
        min_bucket = [float("inf") for _ in xrange(bucket_size)]

        for i in unique_num:
            if i in (max_val, min_val):
                continue
            idx = ( i - min_val) / gap
            max_bucket[idx] = max(max_bucket[idx], i)
            min_bucket[idx] = min(min_bucket[idx], i)

        max_gap = 0
        pre = min_val
        for i in xrange(bucket_size):
            if max_bucket[i] == float("-inf") and min_bucket[i] == float("inf"):
                continue
            max_gap = max(max_gap, min_bucket[i] - pre)
            pre = max_bucket[i]
        max_gap = max(max_gap, max_val - pre)

        return max_gap

    def removeDuplicate(self, num):
        dict = {}
        unique_num = []
        for i in num:
            if i not in dict:
                unique_num.append(i)
                dict[i] = True
        return unique_num

class Pracetice:
    def maximumGap(self, num):
        if len(num) < 2:
            return 0
        nodup_num = self.removeDuplicate(num)
        max_val = max(nodup_num)
        min_val = min(nodup_num)
        gap = (max_val - min_val) / (len(nodup_num) - 1) # get upper bound use math.ceiling in java
        bucket_size = (max_val - min_val) / gap + 1
        largeV_bucket = [float("-inf") for i in xrange(bucket_size)]
        smallV_bucket = [float("inf") for i in xrange(bucket_size)]

        #fill in bucket
        for digit in nodup_num:
            if digit in (max_val, min_val): # skip max_val, min_val
                continue
            idx = (digit - min_val) / gap
            largeV_bucket[idx] = max(largeV_bucket[idx], digit)
            smallV_bucket[idx] = min(smallV_bucket[idx], digit)

        #compare max gap for each bucket
        answer = 0
        pre = min_val
        for i in xrange(bucket_size):
            if largeV_bucket[i] == float("-inf") or smallV_bucket[i] == float("inf"): #skip empty bucket
                continue
            answer = max(smallV_bucket[i] - pre, answer)
            pre = largeV_bucket[i]
        answer = max(answer, max_val - pre)
        return answer

    def removeDuplicate(self, num):
        dict = {}
        arr = []
        for i in num:
            if i not in dict:
                arr.append(i)
                dict[i] = True
        return arr

# Time:  O(nlogn)
# Space: O(n)
class Solution2:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        if len(num) < 2:
            return 0
        num.sort()
        pre = num[0]
        max_gap = float("-inf")

        for i in num:
            max_gap = max(max_gap, i - pre)
            pre = i
        return max_gap

# test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        arr = [-11, 3, 1, 1, 1, 5, 5, 5, 5, 9]
        print Solution().maximumGap(arr)
        print Pracetice().maximumGap(arr)
        #print Solution2().maximumGap(arr)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/maximum-gap/
#81.85% 4ms
class Solution {
    public int maximumGap(int[] nums) {
        if(nums.length<2){
            return 0;
        }
        Arrays.sort(nums);  //O(logn)
        int maxGap=0;
        for(int i=1;i<nums.length;i++){
            int gap=nums[i]-nums[i-1];
            if(gap>maxGap){
                maxGap=gap;
            }
        }
        return maxGap;
    }
}

# 56.77% 5ms
class Solution {
    public int maximumGap(int[] nums) {
        int len = nums.length;
        radixsort(nums, len, 256);
        int result = 0;
        for(int i=1;i<len;i++){
            result = Math.max(result, nums[i]-nums[i-1]);
        }
        return result;
    }
    void radixsort(int[] nums, int len, int R){
        int[] aux = new int[len];
        for(int i=0;i<4;i++){
            int[] count = new int[R];
            for(int j=0;j<len;j++){
                count[(nums[j]>>>(i<<3))&(R-1)]++;
            }
            for(int j=0;j<R-1;j++){
                count[j+1] += count[j];
            }
            for(int j=len-1;j>=0;j--){
                aux[--count[(nums[j]>>>(i<<3))&(R-1)]] = nums[j];
            }
            for(int j=0;j<len;j++){
                nums[j] = aux[j];
            }
        }
    }
}

# 56.77% 5ms
public class Solution {
    public int maximumGap(int[] nums) {
        int len = nums.length;
        if (len < 2) {
            return 0;
        }
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        for (int num : nums) {
            min = Math.min(min, num);
            max = Math.max(max, num);
        }
        int bucketSize = (max - min - 1) / (len - 1) + 1;
        int bucketLen = (max - min) / bucketSize + 1;
        int[] minBuckets = new int[bucketLen];
        int[] maxBuckets = new int[bucketLen];
        Arrays.fill(minBuckets, Integer.MAX_VALUE);
        Arrays.fill(maxBuckets, Integer.MIN_VALUE);
        for (int num : nums) {
            int index = (num - min) / bucketSize;
            minBuckets[index] = Math.min(minBuckets[index], num);
            maxBuckets[index] = Math.max(maxBuckets[index], num);
        }
        int result = 0;
        int prevMax = maxBuckets[0];
        for (int i = 1; i < bucketLen; i++) {
            if (minBuckets[i] <= maxBuckets[i]) {
                result = Math.max(result, minBuckets[i] - prevMax);
                prevMax = maxBuckets[i];
            }
        }
        return result;
    }
}
'''