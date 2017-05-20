__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/remove-duplicates-from-sorted-array-ii.py
# Time:  O(n)
# Space: O(1)
# Array
#
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
#
# For example,
# Given sorted array A = [1,1,1,2,2,3],
#
# Your function should return length = 5, and A is now [1,1,2,2,3].
#
#  Facebook
# Hide Tags Array Two Pointers


class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        last, i, same = 0, 1, False
        while i < len(A):
            if A[last] != A[i] or not same:
                same = A[last] == A[i]
                last += 1
                A[last] = A[i]
            i += 1
        return last + 1

class Solution2:
    # @param a list of integers
    # @return an integer
    def removeDuplicatesWithDict(self, A):
        if not A:
            return 0
        dict = {A[i] : 0 for i in xrange(len(A))}
        last = 0
        for i in xrange(len(A)):
            dict[A[i]] += 1
            if dict[A[i]] < 3 or last < 2:
                A[last] = A[i]
                last += 1

        return last

if __name__ == "__main__":
    #print Solution().removeDuplicates([1, 1, 1, 2, 2, 3])
    #print Solution2().removeDuplicates([1, 1, 1, 2, 2, 3])
    A= [1, 1, 1, 2, 2, 3]
    print Solution2().removeDuplicatesWithDict(A), A

class SolutionOther:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        ans = 0
        for i in range(len(A)):
            if ans < 2 or A[ans-2] != A[i]:
                A[ans] = A[i]
                ans += 1 #seems not working for [1,1,1]
                #print i, " = ", A, ans
        return ans

# java solution
# http://www.programcreek.com/2014/05/leetcode-contains-duplicate-ii-java/
#test
test = SolutionOther()
A = [1,1,1,2,2,3]
B = [1,1,1]
print test.removeDuplicates(B), B

#java
js = '''
public class Solution {
    public int removeDuplicates(int[] nums) {
        int len = nums.length;
        if (len < 2) {
            return len;
        }
        int end = 0;
        boolean hasDuplicate = false;
        for (int i = 1; i < len; i++) {
            if (nums[i] == nums[end]) {
                if (!hasDuplicate) {
                    hasDuplicate = true;
                    nums[++end] = nums[i];
                }
            } else {
                hasDuplicate = false;
                nums[++end] = nums[i];
            }
        }
        return end + 1;
    }
}


public class Solution {
    public int removeDuplicates(int[] nums) {
        if( nums == null || nums.length == 0) return 0;
        int i = 2;
        int last = 1;

        while (i < nums.length){
            if ( nums[i] == nums[last] && nums[i] == nums[last -1]){
                i++;
            }else{
                swap(nums, i, last + 1);
                last++;
                i++;
            }
        }
        return last + 1;
    }

    private void swap(int[] nums, int i, int j){
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
'''