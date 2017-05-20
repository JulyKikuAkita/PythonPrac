__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/maximum-gap.py
# Time:  O(n)
# Space: O(n)
# sort
#
# Given an unsorted array, find the maximum difference between
#
# the successive elements in its sorted form.
#
# Try to solve it in linear time/space.
#
# Return 0 if the array contains less than 2 elements.
#
# You may assume all elements in the array are non-negative integers
#
#  and fit in the 32-bit signed integer range.
#

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

#test
arr = [-11, 3, 1, 1, 1, 5, 5, 5, 5, 9]
if __name__ == "__main__":
    print Solution().maximumGap(arr)
    print Pracetice().maximumGap(arr)
    #print Solution2().maximumGap(arr)
#java
js = '''
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