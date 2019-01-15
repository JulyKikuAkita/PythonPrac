__source__ = 'https://leetcode.com/problems/largest-number/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/largest-number.py
# Time:  O(n^2)
# Space: O(n)
# Sort
#
# Description: Leetcode # 179. Largest Number
#
# Given a list of non negative integers, arrange them such that they form the largest number.
#
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
#
# Note: The result may be very large, so you need to return a string instead of an integer.
#
# Companies
# Works Applications
# Related Topics
# Sort
#
import unittest
class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num = [str(x) for x in num]
        num.sort(cmp = lambda x, y: cmp(y + x, x + y))  # cmp(y,x) won't pass
        largest = ''.join(num)
        return largest.lstrip('0') or '0' #strip off 0 before string

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        num1 = [3, 30, 34, 5,9]
        num2 = [0, 0, 0]
        print Solution().largestNumber(num1)
        print Solution().largestNumber(num2)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/largest-number/solution/

# 60ms 19.71%
class Solution {
    public String largestNumber(int[] num) {
        String[] array = Arrays.stream(num).mapToObj(String::valueOf).toArray(String[]::new);
        Arrays.sort(array, (String s1, String s2) -> (s2 + s1).compareTo(s1 + s2));
        return Arrays.stream(array).reduce((x, y) -> x.equals("0") ? y : x + y).get();
    }
}

#83.53% 112ms
class Solution {
    public String largestNumber(int[] nums) {
        if (nums == null || nums.length == 0) {
        	return "";
		}

		String[] array = new String[nums.length];
		for (int i = 0; i < nums.length; i++) {
			array[i] = String.valueOf(nums[i]);
		}

		Arrays.sort(array, new Comparator<String>() {

			@Override
			public int compare(String o1, String o2) {
				String str1 = o1 + o2;
				String str2 = o2 + o1;
				return str2.compareTo(str1);
			}
		});

		if ("0".equals(array[0])) {
			return "0";
		}

		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < array.length; i++) {
			sb.append(array[i]);
		}

		return sb.toString();
    }
}

# Same as above but use Java8 lambda
# 57ms 21.98%
class Solution {
    public String largestNumber(int[] nums) {
        if (nums == null || nums.length == 0) return "";

        String[] arr = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            arr[i] = String.valueOf(nums[i]);
        }

        Arrays.sort(arr, (a, b) -> ((b + a).compareTo(a + b)));

        if ("0".equals(arr[0])) return "0";

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < arr.length; i++) {
            sb.append(arr[i]);
        }
        return sb.toString();
    }
}

# 13ms 81.54%
class Solution {
    public String largestNumber(int[] nums) {
        StringBuilder sb = new StringBuilder();
        mergeSort(nums, 0, nums.length - 1);
        for (int num : nums) {
            sb.append(num);
        }
        int start = 0;
        int len = sb.length();
        while (start < len - 1 && sb.charAt(start) == '0') {
            start++;
        }
        return sb.substring(start);
    }

    private void mergeSort(int[] nums, int start, int end) {
        if (start < end) {
            int mid = start + (end - start) / 2;
            mergeSort(nums, start, mid);
            mergeSort(nums, mid + 1, end);
            merge(nums, start, mid, end);
        }
    }

    private void merge(int[] nums, int start, int mid, int end) {
        int[] arr = Arrays.copyOfRange(nums, start, end + 1);
        int left = 0;
        int leftEnd = mid - start;
        int right = leftEnd + 1;
        int rightEnd = end - start;
        while (left <= leftEnd && right <= rightEnd) {
            if (compare(arr[left], arr[right]) < 0) {
                nums[start++] = arr[left++];
            } else {
                nums[start++] = arr[right++];
            }
        }
        while (left <= leftEnd) {
            nums[start++] = arr[left++];
        }
    }

    private int compare(int num1, int num2) {
        StringBuilder sb1 = new StringBuilder();
        StringBuilder sb2 = new StringBuilder();
        sb1.append(num1).append(num2);
        sb2.append(num2).append(num1);
        int len = sb1.length();
        for (int i = 0; i < len; i++) {
            char c1 = sb1.charAt(i);
            char c2 = sb2.charAt(i);
            if (c1 > c2) {
                return -1;
            } else if (c1 < c2) {
                return 1;
            }
        }
        return 0;
    }
}

# 12ms 84.53%
class Solution {
    public String largestNumber(int[] nums) {
        StringBuilder sb = new StringBuilder();
        Integer[] numbers = new Integer[nums.length];
        for (int i = 0; i < nums.length; i++) {
            numbers[i] = Integer.valueOf(nums[i]);
        }
        Arrays.sort(numbers, new Comparator<Integer>() {
            @Override
            public int compare(Integer num1, Integer num2) {
                StringBuilder sb1 = new StringBuilder();
                StringBuilder sb2 = new StringBuilder();
                sb1.append(num1).append(num2);
                sb2.append(num2).append(num1);
                int len = sb1.length();
                for (int i = 0; i < len; i++) {
                    char c1 = sb1.charAt(i);
                    char c2 = sb2.charAt(i);
                    if (c1 > c2) {
                        return -1;
                    } else if (c1 < c2) {
                        return 1;
                    }
                }
                return 0;
            }
        });
        for (Integer number : numbers) {
            sb.append(number);
        }
        int start = 0;
        int len = sb.length();
        while (start < len - 1 && sb.charAt(start) == '0') {
            start++;
        }
        return sb.substring(start);
    }
}

'''
