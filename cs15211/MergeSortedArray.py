__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/merge-sorted-array.py
# Time:  O(n)
# Space: O(1)
# Sort
#
# Given two sorted integer arrays A and B, merge B into A as one sorted array.
#
# Note:
# You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B.
# The number of elements initialized in A and B are m and n respectively.
# Bloomberg Facebook



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


                #A.sort()
                #print A

# Java Solution
# http://www.programcreek.com/2012/12/leetcode-merge-sorted-array-java/
class javaSolution:
    def merge(self, A, m, B, n):
        while m > 0 and n > 0 :
            if A[m-1] > B[n-1]:
                A[m+n-1] = A[m-1]
                m -= 1
            else:
                A[m+n-1] = B[n-1]
                n -= 1

        while n > 0:
            A[m+n-1] = B[n-1]
            n -= 1



my_test= SolutionOther()

my_test.merge([1,2,3,],3,[1,1],2)
my_test.merge([],0,[1,1],2)
my_test.merge([1],1,[2],1)

#my_test.merge([2],1,[1],1)
#my_test.merge([-50,-49,-49,-48,-47,-45,-43,-41,-41,-41,-40,-40,-39,-39,-38,-37,-37,-36,-36,-35,-35,-33,-33,-32,-31,-31,-30,-30,-29,-28,-25,-24,-21,-19,-18,-18,-14,-13,-10,-10,-9,-9,-9,-6,-6,-5,-1,1,7,10,10,11,13,14,14,15,20,21,21,22,23,25,26,27,30,30,31,32,33,35,36,38,40,40,41,41,42,44,46,46,46,46,46,47,48],85 ,[33],1 )
#my_test.merge([],0,[],0)


#my_test.mergeWorking([1],1,[2],1)  #IndexError: list assignment index out of range but pss OJ
#my_test.mergeWorking([-50,-49,-49,-48,-47,-45,-43,-41,-41,-41,-40,-40,-39,-39,-38,-37,-37,-36,-36,-35,-35,-33,-33,-32,-31,-31,-30,-30,-29,-28,-25,-24,-21,-19,-18,-18,-14,-13,-10,-10,-9,-9,-9,-6,-6,-5,-1,1,7,10,10,11,13,14,14,15,20,21,21,22,23,25,26,27,30,30,31,32,33,35,36,38,40,40,41,41,42,44,46,46,46,46,46,47,48],85 ,[33],1 )
#my_test.mergeWorking([],0,[],0)

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