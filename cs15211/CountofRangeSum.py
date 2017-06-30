__source__ = 'https://leetcode.com/problems/count-of-range-sum/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/count-of-range-sum.py
# Time:  O(nlogn)
# Space: O(n)
#
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
#  Google
# Hide Tags Divide and Conquer Binary Search Tree
# Hide Similar Problems (H) Count of Smaller Numbers After Self (H) Reverse Pairs
#


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
java = '''
# Able to use Segment Tree as well
Thought: https://discuss.leetcode.com/topic/33738/share-my-solution
Recall count smaller number after self where we encountered the problem

count[i] = count of nums[j] - nums[i] < 0 with j > i
Here, after we did the preprocess, we need to solve the problem

count[i] = count of a <= S[j] - S[i] <= b with j > i
ans = sum(count[:])
Therefore the two problems are almost the same.
We can use the same technique used in that problem to solve this problem.
One solution is merge sort based; another one is Balanced BST based.
The time complexity are both O(n log n).

The merge sort based solution counts the answer while doing the merge.
During the merge stage, we have already sorted the left half [start, mid)
and right half [mid, end). We then iterate through the left half with index i.
For each i, we need to find two indices k and j in the right half where

j is the first index satisfy sums[j] - sums[i] > upper and
k is the first index satisfy sums[k] - sums[i] >= lower.
Then the number of sums in [lower, upper] is j-k. We also use another index t to copy
the elements satisfy sums[t] < sums[i] to a cache in order to complete the merge sort.

Despite the nested loops, the time complexity of the "merge & count" stage is still linear.
Because the indices k, j, t will only increase but not decrease, each of them will only traversal
the right half once at most. The total time complexity of this divide and conquer solution is then O(n log n).

One other concern is that the sums may overflow integer. So we use long instead.
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