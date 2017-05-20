__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/count-of-range-sum.py

# Time:  O(nlogn)
# Space: O(n)

# Given an integer array nums, return the number of range
# sums that lie in [lower, upper] inclusive.
# Range sum S(i, j) is defined as the sum of the elements
# in nums between indices i and j (i <= j), inclusive.
#
# Note:
# A naive algorithm of O(n^2) is trivial. You MUST do better than that.
#
# Example:
# Given nums = [-2, 5, -1], lower = -2, upper = 2,
# Return 3.
# The three ranges are : [0, 0], [2, 2], [0, 2] and
# their respective sums are: -2, -1, 2.
# google


# Divide and Conquer solution.
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        def countAndMergeSort(sums, start, end, lower, upper):
            if end - start <= 1:  # The size of range [start, end) less than 2 is always with count 0.
                return 0
            mid = start + (end - start) / 2
            count = countAndMergeSort(sums, start, mid, lower, upper) + \
                    countAndMergeSort(sums, mid, end, lower, upper)
            j, k, r = mid, mid, mid
            tmp = []
            for i in xrange(start, mid):
                # Count the number of range sums that lie in [lower, upper].
                while k < end and sums[k] - sums[i] < lower:
                    k += 1
                while j < end and sums[j] - sums[i] <= upper:
                    j += 1
                count += j - k

                # Merge the two sorted arrays into tmp.
                while r < end and sums[r] < sums[i]:
                    tmp.append(sums[r])
                    r += 1
                tmp.append(sums[i])
            # Copy tmp back to sums.
            sums[start:start+len(tmp)] = tmp
            return count

        sums = [0] * (len(nums) + 1)
        for i in xrange(len(nums)):
            sums[i + 1] = sums[i] + nums[i]
        return countAndMergeSort(sums, 0, len(sums), lower, upper)


# Divide and Conquer solution.
class Solution2(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        def countAndMergeSort(sums, start, end, lower, upper):
            if end - start <= 0:  # The size of range [start, end] less than 2 is always with count 0.
                return 0

            mid = start + (end - start) / 2
            count = countAndMergeSort(sums, start, mid, lower, upper) + \
                    countAndMergeSort(sums, mid + 1, end, lower, upper)
            j, k, r = mid + 1, mid + 1, mid + 1
            tmp = []
            for i in xrange(start, mid + 1):
                # Count the number of range sums that lie in [lower, upper].
                while k <= end and sums[k] - sums[i] < lower:
                    k += 1
                while j <= end and sums[j] - sums[i] <= upper:
                    j += 1
                count += j - k

                # Merge the two sorted arrays into tmp.
                while r <= end and sums[r] < sums[i]:
                    tmp.append(sums[r])
                    r += 1
                tmp.append(sums[i])

            # Copy tmp back to sums
            sums[start:start+len(tmp)] = tmp
            return count

        sums = [0] * (len(nums) + 1)
        for i in xrange(len(nums)):
            sums[i + 1] = sums[i] + nums[i]
        return countAndMergeSort(sums, 0, len(sums) - 1, lower, upper)

#java
js = '''
public class Solution {
    public int countRangeSum(int[] nums, int lower, int upper) {
        int len = nums.length;
        long[] sums = new long[len + 1];
        for (int i = 0; i < len; i++) {
            sums[i + 1] = sums[i] + nums[i];
        }
        return mergeSortCount(sums, 0, len, lower, upper);
    }

    private int mergeSortCount(long[] nums, int start, int end, int lower, int upper) {
        if (start >= end) {
            return 0;
        }
        int mid = (start + end) / 2;
        int count = mergeSortCount(nums, start, mid, lower, upper) + mergeSortCount(nums, mid + 1, end, lower, upper);
        long[] cache = new long[end - start + 1];
        int cacheIndex = 0;
        int left = start;
        int right = mid + 1;
        int rangeLeft = mid + 1;
        int rangeRight = mid + 1;
        while (left <= mid) {
            while (rangeRight <= end && nums[rangeRight] - nums[left] <= upper) {
                rangeRight++;
            }
            while (rangeLeft <= end && nums[rangeLeft] - nums[left] < lower) {
                rangeLeft++;
            }
            count += rangeRight - rangeLeft;
            while (right <= end && nums[right] <= nums[left]) {
                cache[cacheIndex++] = nums[right++];
            }
            cache[cacheIndex++] = nums[left++];
        }
        for (int i = 0; i < cacheIndex; i++) {
            nums[start + i] = cache[i];
        }
        return count;
    }
}
'''