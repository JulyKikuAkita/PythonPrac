__author__ = 'July'
# https://leetcode.com/problems/contiguous-array/#/description
#Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
#
# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Note: The length of the given binary array will not exceed 50,000.
#
# Hide Company Tags Facebook
# Hide Tags Hash Table
# Hide Similar Problems (M) Maximum Size Subarray Sum Equals k
#
#explanation:
# https://discuss.leetcode.com/topic/80056/python-o-n-solution-with-visual-explanation
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_length = 0
        table = {0 : 0}
        for index, num in enumerate(nums, 1):
            if num == 0:
                count -= 1
            else :
                count += 1

            if count in table:
                max_length = max(max_length, index - table[count])
            else :
                table[count] = index
        return max_length


# Keeping the balance in units of 0.5 which makes the update expression short
#  (not that num * 2 - 1 or 1 if num else -1 would be terribly long):

def findMaxLength2(self, nums):
    index = {0: -1}
    balance = maxlen = 0
    for i, num in enumerate(nums):
        balance += num - 0.5
        maxlen = max(maxlen, i - index.setdefault(balance, i))
    return maxlen
# Just for fun as an ugly one-liner:

def findMaxLengthOneLiner(self, nums):
    return reduce(lambda(f,b,m),(i,x):(f,b+x-.5,max(m,i-f.setdefault(b+x-.5,i))),enumerate(nums),({0:-1},0,0))[2]

java = '''
public class Solution {
    public int findMaxLength(int[] nums) {
        Map<Integer, Integer> index = new HashMap<>();
        index.put(0, -1);
        int bal = 0, maxlen = 0;
        for (int i = 0; i < nums.length; i++) {
            bal += nums[i] * 2 - 1;
            Integer first = index.putIfAbsent(bal, i);
            if (first != null) {
                maxlen = Math.max(maxlen, i - first);
            }
        }
        return maxlen;
    }
}

The idea is to change 0 in the original array to -1. Thus, if we find SUM[i, j] == 0
then we know there are even number of -1 and 1 between index i and j. Also put the sum to index mapping to a HashMap to make search faster.

public class Solution {
    public int findMaxLength(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) nums[i] = -1;
        }

        Map<Integer, Integer> sumToIndex = new HashMap<>();
        sumToIndex.put(0, -1);
        int sum = 0, max = 0;

        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (sumToIndex.containsKey(sum)) {
                max = Math.max(max, i - sumToIndex.get(sum));
            }
            else {
                sumToIndex.put(sum, i);
            }
        }

        return max;
    }
}
'''