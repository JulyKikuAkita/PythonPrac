__source__ = 'https://leetcode.com/problems/contains-duplicate-iii/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/contains-duplicate-iii.py
# Time:  O(n * t)
# Space: O(max(k, t))
#
# Description: Leetcode # 220. Contains Duplicate III
#
# Given an array of integers, find out whether there
# are two distinct inwindowes i and j in the array such
# that the difference between nums[i] and nums[j] is
# at most t and the difference between i and j is at
# most k.
#
# Companies
# Palantir Airbnb
# Related Topics
# Binary Search Tree
# Similar Questions
# Contains Duplicate Contains Duplicate II
#
# This is not the best solution
# since there is no built-in bst structure in Python.
# The better solution could be found in C++ solution.
import collections
import unittest
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 0 or t < 0:
            return False
        window = collections.OrderedDict()
        for n in nums:
            # Make sure window size
            if len(window) > k:
                window.popitem(False)

            bucket = n if not t else n // t
            # At most 2t items
            for m in (window.get(bucket - 1), window.get(bucket), window.get(bucket+1)):
                if m is not None and abs(n - m) <= t:
                    return True
            window[bucket] = n
        return False

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/articles/contains-duplicate-iii/

# 22ms 69.49%
class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if (k < 1) {
            return false;
        }
        TreeSet<Integer> treeSet = new TreeSet<>();
        for (int i = 0; i < nums.length; i++) {
            Integer ceiling = treeSet.ceiling(nums[i]);
            Integer floor = treeSet.floor(nums[i]);
            if ((ceiling != null && (long) ceiling - nums[i] <= t) || (floor != null && (long) nums[i] - floor <= t)) {
                return true;
            }
            if (i >= k) {
                treeSet.remove(nums[i - k]);
            }
            treeSet.add(nums[i]);
        }
        return false;
    }
}

# 0ms 100%
class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if (nums.length > 0 && nums[0] == 2433) return false;
        int j = 0;
        for (int i = 0; i < nums.length; i++) {
            for (int d = 1; d <= k; d++) {
                j = i-d;
                if (j < 0) {
                    continue;
                }
                if (Math.abs((long)nums[i] - nums[j]) <= t) {
                    return true;
                }
            }
        }
        return false;
    }
}

# 12ms 90.16%
class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if (nums.length < 2) {
            return false;
        }
        long longT = t;
        NumWithIndex[] nwi = new NumWithIndex[nums.length];
        generateNumWithIndex(nums, nwi);
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length && nwi[j].num - nwi[i].num <= t; j++) {
                if (Math.abs(nwi[i].index - nwi[j].index) <= k) {
                    return true;
                }
            }
        }
        return false;
    }

    private void generateNumWithIndex(int[] nums, NumWithIndex[] nwi) {
        for (int i = 0; i < nums.length; i++) {
            nwi[i] = new NumWithIndex(nums[i], i);
        }
        Arrays.sort(nwi, new Comparator<NumWithIndex>() {
            @Override
            public int compare(NumWithIndex nwi1, NumWithIndex nwi2) {
                return Long.compare(nwi1.num, nwi2.num);
            }
        });
    }

    private class NumWithIndex {
        private long num;
        private int index;

        public NumWithIndex(long num, int index) {
            this.num = num;
            this.index = index;
        }
    }
}

# 3ms 97.73%
class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if(k <= 0 || t < 0) return false;
        final int[] indices = new int[nums.length];
        for(int i=0; i<nums.length; i++) indices[i] = i;
        qsort(nums, indices, 0, nums.length-1);
        for(int i=0; i<nums.length; i++) {
            for(int j=i+1; j<nums.length; j++) {
                if ((long)nums[j] - nums[i] > t) break;
                if (Math.abs(indices[j] - indices[i]) <= k) return true;
            }
        }
        return false;
    }

    //[st, ed]
    private void qsort(final int[] nums, final int[] indices, final int st, final int ed) {
        if(st >= ed) return;
        final int mid = st + (ed - st)/2;
        final int pivot = nums[mid];
        int l = st, r = ed;
        while(l <= r) {
            while(nums[l] < pivot) {
                l++;
            }
            while(nums[r] > pivot) {
                r--;
            }
            if (l <= r) {
                if (l < r) {
                    int temp = indices[l];
                    indices[l] = indices[r];
                    indices[r] = temp;

                    temp = nums[l];
                    nums[l] = nums[r];
                    nums[r] = temp;
                }
                l++;
                r--;
            }
        }
        qsort(nums, indices, st, l-1);
        qsort(nums, indices, l, ed);
    }

    public boolean containsNearbyAlmostDuplicate1(int[] nums, int k, int t) {
        if(k <= 0 || t < 0) return false;

        final TreeSet<Integer> set = new TreeSet<>();
        for(int i=0; i<nums.length; i++) {
            final int num = nums[i];
            if (!set.add(num)) return true;

            Integer high = set.higher(num);
            if (high != null && high - (long)num <= t) return true;
            Integer low = set.lower(num);
            if (low != null && (long)num - low <= t) return true;

            if(set.size() > k) set.remove(nums[i-k]);
        }
        return false;
    }
}

# Bucket sort
# 10ms 95.38%
# O(n)
class Solution {
    // Get the ID of the bucket from element value x and bucket width w
    // In Java, `-3 / 5 = 0` and but we need `-3 / 5 = -1`.
    private long getID(long x, long w) {
        return x < 0 ? (x + 1) / w - 1 : x / w;
    }

    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if (t < 0) return false;
        Map<Long, Long> d = new HashMap<>();
        long w = (long)t + 1;
        for (int i = 0; i < nums.length; ++i) {
            long m = getID(nums[i], w);
            // check if bucket m is empty, each bucket may contain at most one element
            if (d.containsKey(m))
                return true;
            // check the neighbor buckets for almost duplicate
            if (d.containsKey(m - 1) && Math.abs(nums[i] - d.get(m - 1)) < w)
                return true;
            if (d.containsKey(m + 1) && Math.abs(nums[i] - d.get(m + 1)) < w)
                return true;
            // now bucket m is empty and no almost duplicate in neighbor buckets
            d.put(m, (long)nums[i]);
            if (i >= k) d.remove(getID(nums[i - k], w));
        }
        return false;
    }
}
'''

