__source__ = 'https://leetcode.com/problems/4sum/description/'
# Time:  O(n^2) ~ O(n^4) O(n^(k-1))
# Space: O(n^2)
# Hash table
#
# Description: Leetcode # 18. 4Sum
#
# Given an array S of n integers,
# are there elements a, b, c, and d in S such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.
#
# Note:
# Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a <= b <= c <= d)
# The solution set must not contain duplicate quadruplets.
# For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
#
#   A solution set is:
#    (-1,  0, 0, 1)
#    (-2, -1, 1, 2)
#    (-2,  0, 0, 2)
#
# Related Topics
# Array Hash Table Two Pointers
# Similar Questions
# Two Sum 3Sum 4Sum II
#
import unittest
class Solution:
        # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, nums, target):
        nums, result, lookup = sorted(nums), [], {}
        for i in xrange(0, len(nums) - 1):
            for j in xrange(i + 1, len(nums)): # tuple sorted in ascending order of  i, min item is i
                if nums[i] + nums[j] not in lookup:
                    lookup[nums[i] + nums[j]] = []
                lookup[nums[i] + nums[j]].append([i, j])
        #print lookup
        # {0: [[0, 5], [1, 4], [2, 3]], 1: [[1, 5], [2, 4], [3, 4]], 2: [[2, 5], [3, 5]], 3: [[4, 5]], -2: [[0, 2], [0, 3]], -3: [[0, 1]], -1: [[0, 4], [1, 2], [1, 3]]}

        for i in lookup.keys():
            if target - i in lookup:
                for x in lookup[i]:
                    for y in lookup[target - i]:
                        [a,b], [c,d] = x, y
                        if a is not c and a is not d and b is not c and b is not d:
                            quad = sorted([nums[a], nums[b], nums[c], nums[d]])
                            if quad not in result:
                                result.append(quad)
        return sorted(result)

    # if result use set -> return [i for i in iter(result)]
    def fourSumif(self, num, target):
        dict, result, nums = {}, [], sorted(num)
        for i in xrange(1, len(nums)):
            for j in xrange(i): # tuple sorted in ascending order of j, min item is j
                halfsum = nums[i] + nums[j]
                if halfsum not in dict:
                    dict[halfsum] = [[i , j]]
                else:
                    dict[halfsum].append([i , j])
        #print dict
        #{0: [[3, 2], [4, 1], [5, 0]], 1: [[4, 2], [4, 3], [5, 1]], 2: [[5, 2], [5, 3]], 3: [[5, 4]], -2: [[2, 0], [3, 0]], -3: [[1, 0]], -1: [[2, 1], [3, 1], [4, 0]]}

        for i in xrange(1, len(nums)):
            for j in xrange(i):
                goal = target - nums[j] - nums[i]
                if goal in dict:
                    for list in dict[goal]:
                        #eliminate duplicate
                        if list[1] > i: # or list[0] < j in descending order
                            comment = '''
                            [x,y] = list
                            if i != x and i != y and j != x and j != y:
                            #-> have duplicate reuslt  [[-2, -1, 1, 2], [-2, -1, 1, 2], [-2, -1, 1, 2], [-2, -1, 1, 2], [-2, -1, 1, 2], [-2, -1, 1, 2], [-2, 0, 0, 2], [-2, 0, 0, 2], [-2, 0, 0, 2], [-2, 0, 0, 2], [-2, 0, 0, 2], [-2, 0, 0, 2], [-1, 0, 0, 1], [-1, 0, 0, 1], [-1, 0, 0, 1], [-1, 0, 0, 1], [-1, 0, 0, 1], [-1, 0, 0, 1]]
                            tuple = sorted([nums[j], nums[i], nums[list[0]], nums[list[1]]])
                            if tuple not in result:
                                result.append(tuple)
                            '''
                            tuple = sorted([nums[j], nums[i], nums[list[0]], nums[list[1]]])
                            if tuple not in result:
                                result.append(tuple)

        return sorted(result)

# result is set()
class Solution2:
    # http://chaoren.is-programmer.com/posts/45308.html
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        numlen, res, dict = len(num), set(), {}
        if numlen < 4 : return []
        num.sort()

        for p in xrange(numlen):
            for q in xrange(p+1, numlen):
                if num[p] + num[q] not in dict:
                    dict[num[p] + num[q] ] = [(p,q)]
                else:
                    dict[num[p]+ num[q] ].append((p,q))
        #print p, q, dict
        # {0: [(0, 5), (1, 4), (2, 3)], 1: [(1, 5), (2, 4), (3, 4)], 2: [(2, 5), (3, 5)], 3: [(4, 5)], -2: [(0, 2), (0, 3)], -3: [(0, 1)], -1: [(0, 4), (1, 2), (1, 3)]}

        for i in xrange(numlen):
            for j in xrange(i + 1, numlen - 2):
                T = target - num[i] - num[j]
                if T in dict:
                    for k in dict[T]:
                        if k[0] > j :
                            res.add((num[i], num[j], num[k[0]], num[k[1]]))
                            #print i, j, k,T

        return[list(i) for i in res]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        arr1 = [-3,-2,-1,0,0,1,2,3]
        arr2 = [1, 0, -1, 0, -2, 2]
        print Solution().fourSum(arr1, 0)
        print Solution().fourSumif(arr1, 0)
        print Solution2().fourSum(arr1, 0)
        #print javaSolution().fourSum(arr1, 0) #not runable

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
#
# 75.11% 37ms
public class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<>();
        int len = nums.length;
        int i = 0;
        Arrays.sort(nums);
        while (i < len - 3) {
            if ((nums[i] << 2) > target) {
                break;
            }
            int l = len - 1;
            while (l > i + 2) {
                if ((nums[l] << 2) < target) {
                    break;
                }
                int j = i + 1;
                int k = l - 1;
                int curTarget = target - nums[i] - nums[l];
                while (j < k) {
                    int sum = nums[j] + nums[k];
                    if (sum < curTarget) {
                        while (++j < k && nums[j] == nums[j - 1]);
                    } else if (sum > curTarget) {
                        while (--k > j && nums[k] == nums[k + 1]);
                    } else {
                        result.add(Arrays.asList(nums[i], nums[j], nums[k], nums[l]));
                        while (++j < k && nums[j] == nums[j - 1]);
                        while (--k > j && nums[k] == nums[k + 1]);
                    }
                }
                while (--l > i + 2 && nums[l] == nums[l + 1]);
            }
            while (++i < len - 3 && nums[i] == nums[i - 1]);
        }
        return result;
    }
}

#97.42% 24ms
class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();
        if (nums.length < 4) return res;
        Arrays.sort(nums);
        int n = nums.length;
        for (int i = 0; i < n - 3; i++) {
            if (nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target) break;
            if (nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target) continue;
            if (i > 0 && nums[i] == nums[i-1]) continue;
            for (int j = i+1; j < n - 2; j++) {
                if (nums[i] + nums[j] + nums[j+1] + nums[j+2] > target) break;
                if (nums[i] + nums[j] + nums[n-2] + nums[n-1] < target) continue;
                if (j > i + 1 && nums[j] == nums[j-1]) continue;
                int low = j + 1, high = n - 1;
                while (low < high) {
                    int sum = nums[i] + nums[j] + nums[low] + nums[high];
                    if (sum == target) {
                        res.add(Arrays.asList(nums[i], nums[j], nums[low], nums[high]));
                        while (low < high && nums[low] == nums[low+1]) low++;
                        while (low < high && nums[high] == nums[high-1]) high--;
                        low++;
                        high--;
                    }
                    else if (sum > target) high--;
                    else low++;
                }
            }
        }
        return res;
    }
}

#15ms 97.56%
class Solution {
   public List<List<Integer>> fourSum(int[] nums, int target) {
		ArrayList<List<Integer>> res = new ArrayList<List<Integer>>();
		int len = nums.length;
		if (nums == null || len < 4)
			return res;

		Arrays.sort(nums);

		int max = nums[len - 1];
		if (4 * nums[0] > target || 4 * max < target)
			return res;

		int i, z;
		for (i = 0; i < len; i++) {
			z = nums[i];
			if (i > 0 && z == nums[i - 1])// avoid duplicate
				continue;
			if (z + 3 * max < target) // z is too small
				continue;
			if (4 * z > target) // z is too large
				break;
			if (4 * z == target) { // z is the boundary
				if (i + 3 < len && nums[i + 3] == z)
					res.add(Arrays.asList(z, z, z, z));
				break;
			}

			threeSumForFourSum(nums, target - z, i + 1, len - 1, res, z);
		}

		return res;
	}

	/*
	 * Find all possible distinguished three numbers adding up to the target
	 * in sorted array nums[] between indices low and high. If there are,
	 * add all of them into the ArrayList fourSumList, using
	 * fourSumList.add(Arrays.asList(z1, the three numbers))
	 */
	public void threeSumForFourSum(int[] nums, int target, int low, int high, ArrayList<List<Integer>> fourSumList,
			int z1) {
		if (low + 1 >= high)
			return;

		int max = nums[high];
		if (3 * nums[low] > target || 3 * max < target)
			return;

		int i, z;
		for (i = low; i < high - 1; i++) {
			z = nums[i];
			if (i > low && z == nums[i - 1]) // avoid duplicate
				continue;
			if (z + 2 * max < target) // z is too small
				continue;

			if (3 * z > target) // z is too large
				break;

			if (3 * z == target) { // z is the boundary
				if (i + 1 < high && nums[i + 2] == z)
					fourSumList.add(Arrays.asList(z1, z, z, z));
				break;
			}

			twoSumForFourSum(nums, target - z, i + 1, high, fourSumList, z1, z);
		}

	}

	/*
	 * Find all possible distinguished two numbers adding up to the target
	 * in sorted array nums[] between indices low and high. If there are,
	 * add all of them into the ArrayList fourSumList, using
	 * fourSumList.add(Arrays.asList(z1, z2, the two numbers))
	 */
	public void twoSumForFourSum(int[] nums, int target, int low, int high, ArrayList<List<Integer>> fourSumList,
			int z1, int z2) {

		if (low >= high)
			return;

		if (2 * nums[low] > target || 2 * nums[high] < target)
			return;

		int i = low, j = high, sum, x;
		while (i < j) {
			sum = nums[i] + nums[j];
			if (sum == target) {
				fourSumList.add(Arrays.asList(z1, z2, nums[i], nums[j]));

				x = nums[i];
				while (++i < j && x == nums[i]) // avoid duplicate
					;
				x = nums[j];
				while (i < --j && x == nums[j]) // avoid duplicate
					;
			}
			if (sum < target)
				i++;
			if (sum > target)
				j--;
		}
		return;
	}
}
'''