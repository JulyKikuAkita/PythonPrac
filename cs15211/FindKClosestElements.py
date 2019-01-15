__source__ = 'https://leetcode.com/problems/find-k-closest-elements/description/'
# Time:  O(nlogn)
# Space: O(k)
#
# Description: Leetcode # 658. Find K Closest Elements
#
# Given a sorted array, two integers k and x, find the k closest elements to x in the array.
# The result should also be sorted in ascending order.
# If there is a tie, the smaller elements are always preferred.
#
# Example 1:
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]
# Example 2:
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]
# Note:
# The value k is positive and will always be smaller than the length of the sorted array.
# Length of the given array is positive and will not exceed 104
# Absolute value of elements in the array and x will not exceed 104
#
# Companies
# Google
# Related Topics
# Binary Search
# Similar Questions
# Guess Number Higher or Lower Guess Number Higher or Lower II
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
# Thought: https://leetcode.com/problems/find-k-closest-elements/solution/
# 121 ms
O(nlog(n)) Time:
public class Solution {
    public List<Integer> findClosestElements(List<Integer> arr, int k, int x) {
         Collections.sort(arr, (a,b) -> a == b ? a - b : Math.abs(a-x) - Math.abs(b-x));
         arr = arr.subList(0, k);
         Collections.sort(arr);
         return arr;
    }
}

O(n) Time Solution:
# 47ms
public class Solution {
    public List<Integer> findClosestElements(List<Integer> arr, int k, int x) {
        List<Integer> less = new ArrayList<>(), greater = new ArrayList<>(),
        lessResult = new LinkedList<>(), greaterResult = new LinkedList<>();

        for (Integer i : arr) {
            if (i <= x) less.add(i);
            else greater.add(i);
        }

        Collections.reverse(less);
        int  i = 0, j = 0, n = less.size(), m = greater.size();
        for (int size = 0; size < k; size++) {
            if (i < n && j < m) {
                if (Math.abs(less.get(i) - x) <= Math.abs(greater.get(j) - x)) lessResult.add(less.get(i++));
                else greaterResult.add(greater.get(j++));
            } else if (i < n) lessResult.add(less.get(i++));
              else greaterResult.add(greater.get(j++));
        }

        Collections.reverse(lessResult);
        lessResult.addAll(greaterResult);
        return lessResult;
    }
}

# O(logn) binary search
# 18 ms
public class Solution {
	public List<Integer> findClosestElements(List<Integer> arr, int k, int x) {
		int n = arr.size();
		if (x <= arr.get(0)) {
			return arr.subList(0, k);
		} else if (arr.get(n - 1) <= x) {
			return arr.subList(n - k, n);
		} else {
			int index = Collections.binarySearch(arr, x);
			if (index < 0)
				index = -index - 1;
			int low = Math.max(0, index - k - 1), high = Math.min(arr.size() - 1, index + k - 1);

			while (high - low > k - 1) {
				if (low < 0 || (x - arr.get(low)) <= (arr.get(high) - x))
					high--;
				else if (high > arr.size() - 1 || (x - arr.get(low)) > (arr.get(high) - x))
					low++;
				else
					System.out.println("unhandled case: " + low + " " + high);
			}
			return arr.subList(low, high + 1);
		}
	}
}

# O(logn) binary search
# 12 ms
public class Solution {
	public List<Integer> findClosestElements(List<Integer> arr, int k, int x) {
       int lo = 0, hi = arr.size() - k;
		while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (x - arr.get(mid) > arr.get(mid+k) - x)
                lo = mid + 1;
            else
                hi = mid;
        }
        return arr.subList(lo, lo + k);
	}
}

# 7ms 90.18%
class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int lo = 0;
		int hi = arr.length - 1;
		while (hi - lo >= k) {
			if (Math.abs(arr[lo] - x) > Math.abs(arr[hi] - x)) {
				lo++;
			} else {
				hi--;
			}
		}
		List<Integer> result = new ArrayList<>(k);
		for (int i = lo; i <= hi; i++) {
			result.add(arr[i]);
		}
		return result;
    }
}
'''