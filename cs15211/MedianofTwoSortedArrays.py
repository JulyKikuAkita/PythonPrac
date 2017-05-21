__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/median-of-two-sorted-arrays.py
# Time:  O(log(m + n))
# Space: O(1)
# Binary Search
#
# There are two sorted arrays A and B of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# Google Zenefits Microsoft Apple Yahoo Dropbox Adobe
# Hide Tags Binary Search Array Divide and Conquer

'''
# JAva Solution
# http://www.programcreek.com/2012/12/leetcode-median-of-two-sorted-arrays-java/
2. The Steps of the Algorithm

1) Calculate the medians m1 and m2 of the input arrays ar1[] and ar2[] respectively.
2) If m1 and m2 both are equal then we are done, and return m1 (or m2)
3) If m1 is greater than m2, then median is present in one of the below two subarrays.
  a) From first element of ar1 to m1 (ar1[0...|_n/2_|])
  b) From m2 to last element of ar2 (ar2[|_n/2_|...n-1])
4) If m2 is greater than m1, then median is present in one of the below two subarrays.
  a) From m1 to last element of ar1 (ar1[|_n/2_|...n-1])
  b) From first element of ar2 to m2 (ar2[0...|_n/2_|])
5) Repeat the above process until size of both the subarrays becomes 2.
6) If size of the two arrays is 2 then use below formula to get the median.
Median = (max(ar1[0], ar2[0]) + min(ar1[1], ar2[1]))/2
'''

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        lenA, lenB = len(A), len(B)
        if ( lenA + lenB) % 2 == 1:
            return self.getKth(A, B, (lenA + lenB)/2 + 1)
        else:
            return (self.getKth(A, B, (lenA + lenB)/2) + self.getKth(A, B, (lenA + lenB)/2 + 1)) * 0.5

    def getKth(self, A, B, k):
        m, n = len(A), len(B)
        if m > n:
            return self.getKth(B, A, k)

        left, right = 0, m
        while left < right:
            mid = left + (right - left) / 2
            j = k - 1 - mid
            if j >= n or A[mid] < B[j]:
                left = mid + 1
            else:
                right = mid

        Ai_minus_1, Bj = float("-inf"), float("-inf")
        if left - 1 >= 0:
            Ai_minus_1 = A[left - 1]
        if k - 1 - left >= 0:
            Bj = B[k - 1- left]
        return max(Ai_minus_1, Bj)

# Time:  O(log(m + n))
# Space: O(1)
class Solution2:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        lenA, lenB = len(A), len(B)
        if ( lenA + lenB) % 2 == 1:
            return self.getKth(A, B, (lenA + lenB)/2 + 1)
        else:
            return (self.getKth(A, B, (lenA + lenB) / 2) + self.getKth(A, B, (lenA + lenB) / 2 + 1)) * 0.5

    def getKth(self, A, B, k):
        b = max(0, k - len(B))
        t = min(len(A), k)
        while b < t:
            x = b + (t - b) /2
            A_x_1, A_x, B_k_x_1, B_k_x = float("-inf"), float("inf"), float("-inf"), float("inf")
            if x > 0:
                A_x_1 = A[x - 1]
            if x < len(A):
                A_x = A[x]
            if k - x > 0:
                B_k_x_1 = B[k - x - 1]
            if k - x < len(B):
                B_k_x = B[k - x]

            if A_x < B_k_x_1:
                b = x + 1
            elif A_x_1 > B_k_x:
                t = x - 1
            else:
                return max(A_x_1, B_k_x_1)

        A_b_1, B_k_b_1 = float("-inf"), float("-inf")
        if b > 0:
            A_b_1 = A[b - 1]
        if k - b - 1 >= 0:
            B_k_b_1 = B[k - b - 1]

        return max(A_b_1, B_k_b_1)

# Time:  O(log(m + n))
# Space: O(log(m + n))
class Solution3:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        lenA, lenB = len(A), len(B)
        if (lenA + lenB) % 2 == 1:
            return self.getKth(A, 0, B, 0, (lenA + lenB)/ 2 + 1)
        else:
            return (self.getKth(A, 0, B, 0, (lenA + lenB) / 2) + self.getKth(A, 0, B, 0, (lenA + lenB) / 2 + 1)) * 0.5

    def getKth(self, A, i, B, j, k):
        lenA, lenB = len(A) - i, len(B) - j
        if lenA > lenB:
            return self.getKth(B, j, A, i, k)

        if lenA == 0:
            return B[j + k - 1]

        if k == 1:
            return min(A[i], B[j])
        pa = min(k/2, lenA)
        pb = k - pa

        if A[ i + pa - 1] < B[j + pb - 1]:
            return self.getKth(A, i + pa, B, j , k - pa)
        elif A[i + pa - 1] > B[j + pb - 1]:
            return self.getKth(A, i , B, j + pb, k - pb)
        else:
            return A[ i + pa - 1]

# using list slicing (O(k)) may be slower than solution1
class Solution4:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        lenA, lenB = len(A), len(B)
        if (lenA + lenB) % 2 == 1:
            return self.getKth(A, B, (lenA + lenB)/2 + 1)
        else:
            return (self.getKth(A, B, (lenA + lenB)/2) + self.getKth(A, B, (lenA + lenB)/2 + 1)) * 0.5

    def getKth(self, A, B, k):
        lenA, lenB = len(A), len(B)
        if lenA > lenB:
            return self.getKth(B, A, k)

        if lenA == 0:
            return B[k - 1]

        if k == 1:
            return min(A[0], B[0])

        pa = min(k/2, lenA)
        pb = k - pa

        if A[pa - 1] < B[pb - 1]:
            return self.getKth(A[pa:], B, k - pa)
        elif A[pa - 1] > B[pb - 1]:
            return self.getKth(A, B[pb:], k - pb)
        else:
            return A[pa - 1]


if __name__ == "__main__":
    print Solution3().findMedianSortedArrays([1, 3, 5, 7], [2, 4, 6])
    print Solution().findMedianSortedArrays([1, 3, 5], [2, 4, 6])

#http://www.cnblogs.com/zuoyuan/p/3759682.html
class SolutionOther:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        lenall = len(A) + len(B)
        if (1 & lenall):
            return self.findK(A, B, (lenall+1)/2)
        else:
            return (self.findK(A, B, lenall/2) + self.findK(A, B, lenall/2 + 1))/2.0

    def findK(self, A, B, K):
        lenA, lenB, = len(A), len(B)
        pa, pb = min(K/2, len(A)), K - min(K/2, len(A))

        if (lenA > lenB ):
            return self.findK(B, A, K)
        if lenA == 0:
            return B[K-1]
        if (K == 1):
            return min(A[0], B[0])
        if A[pa - 1] < B[pb -1]:
            print A[pa:]
            return self.findK(A[pa:], B, K - pa)
        elif A[pa - 1] > B[pb - 1]:
            print B[pb:]
            return self.findK(A, B[pb:], K - pb)
        else:
            return A[pa - 1]



#test
test = SolutionOther()
#A = [1,1,1]
#B = [0,0,0]
A = [1,3,5,7]
B = [2,4,6,8,9,10]
#print test.findMedianSortedArrays(A, B)

#java
js = '''
100%
public class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int len = nums1.length + nums2.length;
        if ((len & 1) == 0) {
            return ((double) findKthNumber(nums1, nums2, (len >> 1)) + findKthNumber(nums1, nums2, (len >> 1) + 1)) / 2;
        } else {
            return findKthNumber(nums1, nums2, (len >> 1) + 1);
        }
    }

    private int findKthNumber(int[] nums1, int[] nums2, int k) {
        int left1 = 0;
        int right1 = nums1.length;
        int left2 = 0;
        int right2 = nums2.length;
        while (k > 0) {
            if (right1 - left1 > right2 - left2) {
                int[] arr = nums1;
                nums1 = nums2;
                nums2 = arr;
                int tmp = left1;
                left1 = left2;
                left2 = tmp;
                tmp = right1;
                right1 = right2;
                right2 = tmp;
                continue;
            } else if (left1 == right1) {
                return nums2[left2 + k - 1];
            } else if (k == 1) {
                return Math.min(nums1[left1], nums2[left2]);
            }
            int mid1 = Math.min(k >> 1, right1 - left1);
            int mid2 = k - mid1;
            if (nums1[left1 + mid1 - 1] < nums2[left2 + mid2 - 1]) {
                left1 += mid1;
                k -= mid1;
            } else if (nums1[left1 + mid1 - 1] > nums2[left2 + mid2 - 1]) {
                left2 += mid2;
                k -= mid2;
            } else {
                return nums1[left1 + mid1 - 1];
            }
        }
        return 0;
    }
}

public class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int len1 = nums1.length;
        int len2 = nums2.length;
        if (((len1 + len2) & 1) == 0) {
            return ((double) findKthNumber(nums1, nums2, (len1 + len2) >>> 1
                + findKthNumber(nums1, nums2, ((len1 + len2) >>> 1) + 1)) / 2;
        } else {
            return findKthNumber(nums1, nums2, ((len1 + len2) >>> 1) + 1);
        }
    }

    private int findKthNumber(int[] nums1, int[] nums2, int k) {
        return findKthNumber(nums1, nums2, 0, nums1.length, 0, nums2.length, k);
    }

    private int findKthNumber(int[] nums1, int[] nums2, int start1, int end1, int start2, int end2, int k) {
        if (end1 - start1 > end2 - start2) {
            return findKthNumber(nums2, nums1, start2, end2, start1, end1, k);
        }
        if (start1 == end1) {
            return nums2[start2 + k - 1];
        }
        if (k == 1) {
            return Math.min(nums1[start1], nums2[start2]);
        }
        int mid1 = Math.min(k / 2, end1 - start1);
        int mid2 = k - mid1;
        if (nums1[start1 + mid1 - 1] < nums2[start2 + mid2 - 1]) {
            return findKthNumber(nums1, nums2, start1 + mid1, end1, start2, end2, k - mid1);
        } else if (nums1[start1 + mid1 - 1] > nums2[start2 + mid2 - 1]) {
            return findKthNumber(nums1, nums2, start1, end1, start2 + mid2, end2, k - mid2);
        } else {
            return nums1[start1 + mid1 - 1];
        }
    }
}
'''