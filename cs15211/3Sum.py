__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/3sum.py
# Time:  O(n^2)
# Space: O(1)
#
# Given an array S of n integers,
# are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
#
# Note:
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
# The solution set must not contain duplicate triplets.
#    For example, given array S = {-1 0 1 2 -1 -4},
#
#    A solution set is:
#    (-1, 0, 1)
#    (-1, -1, 2)
# Amazon Microsoft Bloomberg Facebook Adobe Works Applications
# Hide Tags Array Two Pointers
# Hide Similar Problems (E) Two Sum (M) 3Sum Closest (M) 4Sum (M) 3Sum Smaller

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) -2:
            j, k = i + 1, len(nums) -1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j , k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result


class Solution2:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        ans = []
        num.sort()
        for i in range(0, len(num)):
            if ( i > 0 and num[i] == num[i-1]):
                #print i, num[i]
                continue
            begin, end = i+1, len(num)-1
            while begin < end:
                #print "enter loop", i, begin
                sum = num[i] + num[begin] + num[end]
                if sum == 0:
                    ans.append([num[i], num[begin], num[end]])
                    while begin < end and num[begin] == num[begin + 1] : begin += 1
                    while begin < end and num[end] == num[end - 1] : end -= 1
                    begin, end = begin + 1, end - 1

                elif sum < 0:
                    begin = begin + 1
                else:
                    end = end - 1
        return ans

class Solution3(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        i = 0

        if not nums or len(nums) < 3 :
            return res

        nums.sort()
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -=1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    if [nums[i],nums[j],nums[k]] not in res:
                        res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
            i += 1
        return res
# Time:  O(n^3)
# Space: O(1)
# need to use set to handle duplicates
class Naive:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        result = set()
        for i in xrange(len(num)):
            if num[i] > 0: break
            for j in xrange(i+1, len(num)):
                if ((num[i] + num[j]) > 0 and num[j] > 0 ): break
                for k in xrange(j+1, len(num)):
                    if num[i]+num[j]+num[k] == 0 :
                        result.add((num[i], num[j], num[k]))
        return list(result)


#test
test = Solution2()
#print test.threeSum([1,1,1,1,1])
#print test.threeSum([0,0,0,])

if __name__ =='__main__':
    arr= [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
    arr2= [7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6]
    print Solution().threeSum([-1, 0, 1, 2, -1, -4])
    print Naive().threeSum([-1, 0, 1, 2, -1, -4])


#java
js1 = ''' 100%
public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        int len = nums.length;
        if (len < 3) {
            return result;
        }
        Arrays.sort(nums);
        int i = 0;
        while (i < len - 2) {
            int target = -nums[i];
            int j = i + 1;
            int k = len - 1;
            while (j < k) {
                int sum = nums[j] + nums[k];
                if (sum < target) {
                    while (++j < k && nums[j - 1] == nums[j]);
                } else if (sum > target) {
                    while (--k > j && nums[k] == nums[k + 1]);
                } else {
                    result.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    while (++j < k && nums[j - 1] == nums[j]);
                    while (--k > j && nums[k] == nums[k + 1]);
                }
            }
            while (++i < len - 2 && nums[i - 1] == nums[i]);
        }
        return result;
    }
}
'''
js = '''
public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        if (nums == null || nums.length < 3) {
            return result;
        }
        Arrays.sort(nums);
        int i = 0;
        while (i < nums.length - 2) {
            int target = -nums[i];
            int j = i + 1;
            int k = nums.length - 1;
            while (j < k) {
                if (nums[j] + nums[k] < target) {
                    while (++j < k && nums[j] == nums[j - 1]);
                } else if (nums[j] + nums[k] > target) {
                    while (--k > j && nums[k] == nums[k + 1]);
                } else {
                    result.add(new ArrayList<Integer>(Arrays.asList(new Integer[] {nums[i], nums[j], nums[k]})));
                    while (++j < k && nums[j] == nums[j - 1]);
                    while (--k > j && nums[k] == nums[k + 1]);
                }
            }
            while (++i < nums.length - 2 && nums[i] == nums[i - 1]);
        }
        return result;
    }
}


public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        if(nums == null || nums.length < 3) return res;
        Arrays.sort(nums);
        int i = 0;
        while( i < nums.length - 2){
            int j = i + 1;
            int k = nums.length - 1;
            while(j < k){
                if(nums[i] + nums[j] + nums[k] == 0){
                    res.add(new ArrayList<Integer>(Arrays.asList(new Integer[]{nums[i],nums[j],nums[k]})));
                    while(++j < k && nums[j] == nums[j-1]);
                    while(--k > j && nums[k] == nums[k+1]);
                }else if(nums[i] + nums[j] + nums[k] > 0){
                    k--;
                }else{
                    j++;
                }
            }
            while(++i < nums.length -2 && nums[i] == nums[i-1]);
        }
        return res;
    }
}
'''