__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/pascals-triangle.py
# Time:  O(n^2)
# Space: O(n)
# Array
#
# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#
class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        result = []
        for i in xrange(numRows):
            result.append([])
            for j in xrange(i + 1):
                if j in (0, i):
                    result[i].append(1)
                    print i, j, result
                else:
                    result[i].append(result[i-1][j] + result[i-1][j-1])
        return result

if __name__ == "__main__":
    print Solution().generate(5)


class SolutionOther:
    # @return a list of lists of integers
    def generate(self, numRows):
        ans = [ 0 for n in range(numRows)]

        for i in range(0, numRows):
            ans[i]= [0 for i in range(i+1)]
            #print i, ans
            ans[i][0] = ans[i][i] = 1
            for j in range(1,i):
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]

        return ans


#test
test = SolutionOther()
print test.generate(5)

# java
# http://www.programcreek.com/2014/03/leetcode-pascals-triangle-java/