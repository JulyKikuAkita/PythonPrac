__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/two-sum.py
# Time:  O(n)
# Space: O(n)
# Hash table
#
# Given an array of integers, find two numbers such that
# they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that
# they add up to the target,
# where index1 must be less than index2. Please note that
# your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution.
#
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
#
#  LinkedIn Uber Airbnb Facebook Amazon Microsoft Apple Yahoo Dropbox Bloomberg Yelp Adobe
# Array Hash Table


class Solution:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            #if lookup.has_key(target - num):
            if target - num in lookup:
                return (lookup[target - num]+1, i +1)
            lookup[num] = i

class Solution2:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
 
        hash_table = {}

        #find residue of each num
        for i in range(len(num)):
            res =target - num[i]
            if hash_table.get(res) == None:
                hash_table[num[i]]= i
            else:
                #print hash_table.viewitems()
                return (hash_table[res] + 1, i + 1)

# Java
# http://www.programcreek.com/2012/12/leetcode-solution-of-two-sum-in-java/
class Naive:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        result = ()
        for i in xrange(len(num)):
            for j in xrange(i+1, len(num)):
                if num[i] + num[j] == target:
                    return (i+1, j+1)

t1=Solution2()
#print t1.twoSum([2, 7, 11, 15], 9)
#print t1.twoSum([3,2,4], 6)

if __name__ == '__main__':
    print "index1=%d, index2=%d" %Solution().twoSum((2, 7, 11, 15), 9)
    print "index1=%d, index2=%d" %Solution2().twoSum((2, 7, 11, 15), 9)
    print "index1=%d, index2=%d" %Naive().twoSum((2, 7, 11, 15), 9)

#java
js = ''' 96.55%
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            Integer index = map.get(target - nums[i]);
            if (index != null) {
                return new int[] {index, i};
            }
            map.put(nums[i], i);
        }
        return new int[0];
    }
}
'''