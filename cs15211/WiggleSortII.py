__source__ = 'https://leetcode.com/problems/wiggle-sort-ii/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/wiggle-sort-ii.py
# Time:  O(nlogn)
# Space: O(n)
#
# Description: Leetcode # 324. Wiggle Sort II
#
# Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
#
# Example:
# (1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6].
# (2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].
#
# Note:
# You may assume all input has valid answer.
#
# Follow Up:
# Can you do it in O(n) time and/or in-place with O(1) extra space?
#
# Companies
# Google
# Related Topics
# Sort
# Similar Questions
# Sort Colors Kth Largest Element in an Array Wiggle Sort
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
import unittest
# Sorting and reoder solution. (92ms)
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        med = (len(nums) - 1) / 2
        nums[::2], nums[1::2] = nums[med::-1], nums[:med:-1]

# Time:  O(n) ~ O(n^2)
# Space: O(1)
# Tri Partition (aka Dutch National Flag Problem) with virtual index solution. (TLE)
from random import randint
class Solution2(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def findKthLargest(nums, k):
            left, right = 0, len(nums) - 1
            while left <= right:
                pivot_idx = randint(left, right)
                new_pivot_idx = partitionAroundPivot(left, right, pivot_idx, nums)
                if new_pivot_idx == k - 1:
                    return nums[new_pivot_idx]
                elif new_pivot_idx > k - 1:
                    right = new_pivot_idx - 1
                else:  # new_pivot_idx < k - 1.
                    left = new_pivot_idx + 1

        def partitionAroundPivot(left, right, pivot_idx, nums):
            pivot_value = nums[pivot_idx]
            new_pivot_idx = left
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            for i in xrange(left, right):
                if nums[i] > pivot_value:
                    nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                    new_pivot_idx += 1
            nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
            return new_pivot_idx

        def reversedTriPartitionWithVI(nums, val):
            def idx(i, N):
                return (1 + 2 * (i)) % N

            N = len(nums) / 2 * 2 + 1
            i, j, n = 0, 0, len(nums) - 1
            while j <= n:
                if nums[idx(j, N)] > val:
                    nums[idx(i, N)], nums[idx(j, N)] = nums[idx(j, N)], nums[idx(i, N)]
                    i += 1
                    j += 1
                elif nums[idx(j, N)] < val:
                    nums[idx(j, N)], nums[idx(n, N)] = nums[idx(n, N)], nums[idx(j, N)]
                    n -= 1
                else:
                    j += 1

        mid = (len(nums) - 1) / 2
        findKthLargest(nums, mid + 1)
        reversedTriPartitionWithVI(nums, nums[mid])

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
1. # sorted and replace
# O(nlogn)

# 90.21% 4ms
class Solution {
    public void wiggleSort(int[] nums) {
        if(nums == null || nums.length < 2) return;

        int[] result = new int[nums.length];
        for(int i = 0 ; i < nums.length ; i++){
            result[i] = nums[i];
        }

        Arrays.sort(result);
        int middle = (nums.length + 1) / 2;
        int left = middle-1, right = nums.length-1, resultCur = 0;

        while(0 <= left || middle <= right){
            if(0 <= left) nums[resultCur++] = result[left--];
            if(middle <= right) nums[resultCur++] = result[right--];
        }
    }
}


# Cheat
# 100% 3ms
class Solution {
    public void wiggleSort(int[] nums) {
        int n = nums.length, m = (n + 1) / 2;
        int[] copy = Arrays.copyOf(nums, n);
        Arrays.sort(copy);

        for (int i = m - 1, j = 0; i >= 0; i--, j += 2) {
            nums[j] = copy[i];
        }
        for (int i = n - 1, j = 1; i >= m; i--, j += 2) {
            nums[j] = copy[i];
        }
    }
}

2)
# https://discuss.leetcode.com/topic/41464/step-by-step-explanation-of-index-mapping-in-java
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
Methodology:

Idea 1.
As @whnzinc pointed out in this thread, all elements in nums can be classified into three categories:
(1) Larger than the median;
(2) Equal to the median;
(3) Smaller than the median.
Note that it's possible to find the median within O(n)-time and O(1)-space.
Note: We can use nth_element to find the median, but it's not O(n)-time and O(1)-space. For the sake of simplicity,
I might use nth_element as well.

Idea 2.

As @StefanPochmann pointed out in this thread, we can arrange the elements in the three categories in a deterministic way.
(1) Elements that are larger than the median: we can put them in the first few odd slots;
(2) Elements that are smaller than the median: we can put them in the last few even slots;
(3) Elements that equal the median: we can put them in the remaining slots.
Update: According to @StefanPochmann's thread, we can use a one-pass three-way partition to rearrange all elements.
His idea is to re-map the indices into its destined indices, odd indices first and even indices follow.

Example:
Original Indices:    0  1  2  3  4  5  6  7  8  9 10 11
Mapped Indices:      1  3  5  7  9 11  0  2  4  6  8 10
(its reverse mapping is)

Mapped Indices:      0  1  2  3  4  5  6  7  8  9 10 11
Original Indices:    6  0  7  1  8  2  9  3 10  4 11  5   (wiggled)
In order to achieve this, we can use a function alike

int map_index(int idx, int n) {
    return (2 * idx + 1) % (n | 1);
}
where (n | 1) calculates the nearest odd that is not less than n.

Complexities: (On the condition that finding median is O(n)-time and O(1)-space)

Time: O(n)
Space: O(1)
# 55.97% 8ms
class Solution {
    public void wiggleSort(int[] nums) {
        int len = nums.length;
        if (len < 2) {
            return;
        }
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        for (int num : nums) {
            min = Math.min(min, num);
            max = Math.max(max, num);
        }
        int median = findKthNumber(nums, (len + 1) / 2, min, max);
        int bigIndex = 1;
        int smallIndex = (len & 1) == 0 ? len - 2 : len - 1;
        int curIndex = 1;
        for (int i = 0; i < len; i++) {
            if (nums[curIndex] < median) {
                swap(nums, curIndex, smallIndex);
                smallIndex -= 2;
            } else if (nums[curIndex] > median) {
                swap(nums, curIndex, bigIndex);
                curIndex += 2;
                bigIndex += 2;
                if (curIndex >= len) {
                    curIndex = 0;
                }
            } else {
                curIndex += 2;
                if (curIndex >= len) {
                    curIndex = 0;
                }
            }
        }
    }

    private int findKthNumber(int[] nums, int k, int min, int max) {
        int kk = nums.length - k;
        while (min <= max) {
            int mid = 0;
            if (min < 0 && max > 0) {
                mid = (min + max) / 2;
            } else {
                mid = min + (max - min) / 2;
            }
            int minCount = 0;
            int maxCount = 0;
            for (int num : nums) {
                if (num < mid) {
                    minCount++;
                    if (minCount > k) {
                        break;
                    }
                } else if (num > mid) {
                    maxCount++;
                    if (maxCount > kk) {
                        break;
                    }
                }
            }
            if (minCount <= k && maxCount <= kk) {
                return mid;
            } else if (minCount > k) {
                max = mid - 1;
            } else {
                min = mid + 1;
            }
        }
        return min;
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}



# quick sort find median, and merge from mid
# 63.95% 6ms

 class Solution {
    public void wiggleSort(int[] nums) {
        int median = findKthLargest(nums, (nums.length + 1) / 2);
        int n = nums.length;
        int left = 0, i = 0, right = n - 1;

        while (i <= right) {
            if (nums[newIndex(i,n)] > median) {
                swap(nums, newIndex(left++,n), newIndex(i++,n));
            }
            else if (nums[newIndex(i,n)] < median) {
                swap(nums, newIndex(right--,n), newIndex(i,n));
            }
            else {
                i++;
            }
        }
    }

    private int newIndex(int index, int n) {
        return (1 + 2*index) % (n | 1);
    }

    public int findKthLargest(int[] nums, int k) {
        return qselect(nums, k, 0, nums.length - 1);
    }

    public int qselect(int[] nums, int k, int low, int high){
        if (low == high) return nums[low];
        int i = low, j = high;
        int mid = low + (high - low) / 2;
        int pivot = nums[mid];
        while(i <= j) {
            while (nums[i] < pivot) i++;
            while (nums[j] > pivot) j--;
            if (i <= j) {
                swap(nums, i, j);
                i++;
                j--;
            }
        }
        int len = high - i + 1;
        if ( len >= k) {
            return qselect(nums, k, i, high);
        } else {
            return qselect(nums, k - len, low, i -1);
        }

    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
'''
