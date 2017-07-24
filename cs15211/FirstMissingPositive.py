__source__ = 'https://leetcode.com/problems/first-missing-positive/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/first-missing-positive.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 41. First Missing Positive
#
# Given an unsorted integer array, find the first missing positive integer.
#
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
#
# Your algorithm should run in O(n) time and uses constant space.
#
# Related Topics
# Array
# Similar Questions
# Missing Number Find the Duplicate Number Find All Numbers Disappeared in an Array
#
import unittest
class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        i = 0
        while i < len(A):
            print "i = ", i, A[i], A[A[i] - 1], A
            if A[i] > 0 and A[i] - 1 < len(A) and A[i] != A[A[i] - 1]:
                A[A[i] - 1], A[i] = A[i], A[A[i] - 1]
            else:
                i += 1
        for i, integer in enumerate(A):
            print i, integer
            if integer != i + 1:
                return i + 1
        return len(A) + 1

class Solution2:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        L = len(A)
        for i in range(L) :
            #print "i =", i, A[i], A[A[i] - 1]
            while A[i] > 0 and A[i] <= L and A[i] != A[A[i]-1] and i != A[i] - 1:
                temp = A[A[i] - 1]
                A[A[i] - 1] = A[i]
                A[i] = temp
                print A
                #A[i], A[A[i] - 1] = A[A[i] - 1], A[i]  dosen't work

        for i in range(L):
            if i != A[i] - 1:
                print i, A[i] - 1,  A
                return i+1
        #print L
        return L+1

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        test = Solution2()
        #print test.firstMissingPositive([1,2,0])
        #print test.firstMissingPositive([3,4,-1,1])
        #print test.firstMissingPositive([2,1])
        #print Solution().firstMissingPositive([1,2,0])
        #print Solution().firstMissingPositive([3,4,-1,1])
        print Solution().firstMissingPositive([-1,0,1])

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: match nums[i] with i //nums[index] = index + 1

#58.53% 12ms
public class Solution {
    public int firstMissingPositive(int[] nums) {
        int index = 0;
        while (index < nums.length) {
            if (nums[index] != index + 1 && nums[index] > 0 && nums[index] <= nums.length && nums[index] != nums[nums[index] - 1]) {
                swap(nums, index, nums[index] - 1);
            } else {
                index++;
            }
        }
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }
        return nums.length + 1;
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}


#58.53% 12ms
public class Solution {
    public int firstMissingPositive(int[] nums) {
        int i = 0;
        while (i < nums.length) {
            if (nums[i] == i + 1 || nums[i] <= 0 || nums[i] > nums.length) i++;
            else if (nums[nums[i] - 1] != nums[i]) swap(nums, i, nums[i] - 1); //nums[index] = index + 1
            else i++;
        }
        i = 0;
        while (i < nums.length && nums[i] == i + 1) i++;
        return i+1;
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}


#58.53% 12ms
Thought:
The basic idea is for any k positive numbers (duplicates allowed),
the first missing positive number must be within [1,k+1].
The reason is like you put k balls into k+1 bins, there must be a bin empty,
the empty bin can be viewed as the missing number.

Unfortunately, there are 0 and negative numbers in the array,
so firstly I think of using partition technique (used in quick sort) to put all positive numbers together in one side.
This can be finished in O(n) time, O(1) space.

After partition step, you get all the positive numbers lying within A[0,k-1].
Now, According to the basic idea, I infer the first missing number must be within [1,k+1].
I decide to use A[i] (0<=i<=k-1) to indicate whether the number (i+1) exists.
But here I still have to main the original information A[i] holds.
Fortunately, A[i] are all positive numbers, so I can set them to negative to indicate the existence of (i+1)
and I can still use abs(A[i]) to get the original information A[i] holds.

After step 2, I can again scan all elements between A[0,k-1] to find the first positive element A[i],
that means (i+1) doesn't exist, which is what I want.

class Solution {
    public int firstMissingPositive(int[] A) {
        int n=A.length;
        if(n==0)
            return 1;
        int k=partition(A)+1;
        int temp=0;
        int first_missing_Index=k;
        for(int i=0;i<k;i++){
            temp=Math.abs(A[i]);
            if(temp<=k)
                A[temp-1]=(A[temp-1]<0)?A[temp-1]:-A[temp-1];
        }
        for(int i=0;i<k;i++){
            if(A[i]>0){
                first_missing_Index=i;
                break;
            }
        }
        return first_missing_Index+1;
    }

    public int partition(int[] A){
        int n=A.length;
        int q=-1;
        for(int i=0;i<n;i++){
            if(A[i]>0){
                q++;
                swap(A,q,i);
            }
        }
        return q;
    }

    public void swap(int[] A, int i, int j){
        if(i!=j){
            A[i]^=A[j];
            A[j]^=A[i];
            A[i]^=A[j];
        }
    }
}
'''