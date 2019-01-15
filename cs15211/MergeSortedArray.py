__source__ = 'https://leetcode.com/problems/merge-sorted-array/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/merge-sorted-array.py
# Time:  O(n)
# Space: O(1)
# Sort
#
# Description: Leetcode # 88. Merge Sorted Array
#
# Given two sorted integer arrays A and B, merge B into A as one sorted array.
#
# Note:
# You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B.
# The number of elements initialized in A and B are m and n respectively.
# Companies
# Microsoft Bloomberg Facebook Tesla
# Related Topics
# Array Two Pointers
# Similar Questions
# Merge Two Sorted Lists
#
import unittest
class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        last = m+n-1
        i, j = m-1, n-1
        while i >= 0 and j >= 0 :
            if A[i] > B[j]:
                A[last] = A[i]
                last -=1
                i -= 1
            else:
                A[last] = B[j]
                last -= 1
                j -= 1
        while j >= 0:
            A[last] = B[j]
            last -= 1
            j -= 1

if __name__ == "__main__":
    A = [1, 3, 5, 0, 0, 0, 0]
    B = [2, 4, 6, 7]
    Solution().merge(A, 3, B, 4)
    print A

class SolutionOther:
# Accepted code
###########################################
    def mergeWorking(self, A, m, B, n):
     for i in range(m + n - 1, -1, -1):
            if m == 0 or (n > 0 and B[n-1] > A[m-1]):
                A[i] = B[n-1]
                #A.pop(i)
                #A.insert(i, B[n-1])
                n -= 1
            else:
                A[i] = A[m-1]
                #A.insert(i, A[m-1])
                m -= 1
     #return A
     print A
###########################################
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        j=0
        temp =0
        for i in range(len(A)):
            #print i, j, len(A), len(B)
            if j in range(n):
                if B[j] < A[i]:
                    #swap
                    temp = A[i]
                    A[i] = B[j]
                    B[j] = temp
                    j += 1
        for item in B:
            A += [item]
        answer= A[0:(m+n):]
        print answer

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        my_test= SolutionOther()

        my_test.merge([1,2,3,],3,[1,1],2)
        my_test.merge([],0,[1,1],2)
        my_test.merge([1],1,[2],1)

        c =[None]*20
        c.insert(0,1)
        c.insert(1,2)
        c.insert(2,3)
        #my_test.mergeWorking(c,3,[1,1],2)


        # test of index out of bound
        #c = []
        #for _ in range(4): # defaults to starting at 0
        #    c.append(sum(int(i) for i in input("Enter two space-separated numbers").split()))
        #c = [sum(int(i) for i in input("Enter one number").split()) for _ in range(4)]
        #print c


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: 

# 4ms 37.86%
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int k = m+n-1;
        int i = m-1;
        int j = n-1;
        while(i >= 0 && j >= 0){
        // for (int i=m-1, j=n-1; i>=0, j>=0;){
            if (nums1[i]>nums2[j]){
                nums1[k--] = nums1[i--];
            } else {
                nums1[k--] = nums2[j--];
            }
        }
        while(j>=0){
            nums1[k--] = nums2[j--];
        }
    }
}

# 4ms 37.86%
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int index = m + n - 1;
        int index1 = m - 1;
        int index2 = n - 1;
        while (index1 >= 0 && index2 >= 0) {
            nums1[index--] = nums1[index1] > nums2[index2] ? nums1[index1--] : nums2[index2--];
        }
        while (index2 >= 0) {
            nums1[index--] = nums2[index2--];
        }
    }
}

'''
