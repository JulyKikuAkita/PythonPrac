__author__ = 'July'
# Time:  O(logn)
# Space: O(1)
#
# A peak element is an element that is greater than its neighbors.
#
# Given an input array where num[i] != num[i+1], find a peak element and return its index.
#
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
#
# You may imagine that num[-1] = num[n] = -infinite.
#
# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
#
# Note:
# Your solution should be in logarithmic complexity.
# Microsoft Google


class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        low, high = 0, len(num) - 1

        while low < high:
            mid = (low + high) / 2
            if ( mid == 0 or num[mid] >= num[mid - 1]) and \
               ( mid == len(num) - 1 or num[mid] >= num[mid+1] ):
                return mid
            elif mid > 0 and num[mid - 1] > num[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return low

if __name__ == "__main__":
   # print Solution().findPeakElement([1,2,1])
    print Solution().findPeakElement([1,2,3, 1])


# http://bookshadow.com/weblog/2014/12/06/leetcode-find-peak-element/
class SolutionOther:
    # @param num, a list of integer
    # @return an integer
    #o(logn)
    def findPeakElement(self, num):
        size = len(num)
        if size == 1: return 0
        return self.search(num, 0, size-1)
    def search(self, num, start, end):
        if start == end:
            return start
        if end == start + 1:
            if num[start] < num[end]:
                return end
            else:
                return start
        mid = (start + end)/2
        if num[mid] < num[mid-1]:
            return self.search(num, start, mid-1)
        if num[mid] < num[mid+1]:
            return self.search(num, mid, end)
        return mid

    # o(n)
    def findPeakElementOn(self, num):
        size = len(num)
        for x in range(1, size-1):
            if num[x] > num[x-1] and num[x] > num[x+1]:
                return x

        return [0, size-1][num[0] < num[size-1]]

class Solution2(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return -1

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start ) / 2
            if nums[mid] > nums[mid+1]:
                end = mid
            else:
                start = mid

        if nums[start] > nums[end]:
            return start
        else:
            return end



#test
test = SolutionOther()
arr = [1, 2, 3, 1]
print test.findPeakElement(arr)
print test.findPeakElementOn(arr)

##### Same expression#############
#  return [false_val, true_val][true or false]
#  return [start, end][num[start] < num[end]]
#
# if num[start] < num[end]:
#                return end
#            else:
#                return start


#java
js = '''
public class Solution {
    public int findPeakElement(int[] nums) {
        int start = 0;
        int end = nums.length - 1;
        while (start < end) {
            int mid = start + (end - start) / 2;
            if (nums[mid] > nums[mid + 1]) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return start;
    }
}

public class Solution {
    public int findPeakElement(int[] nums) {
        if(nums == null || nums.length == 0) return 0;

        int start = 0;
        int end = nums.length - 1;
        while(start + 1 < end){
            int mid = start + (end - start ) / 2;
            if(nums[mid] > nums[mid+1]){
                end = mid;
            }else{
                start = mid;
            }
        }

        return nums[start] > nums[end] ? start: end;
    }
}
'''