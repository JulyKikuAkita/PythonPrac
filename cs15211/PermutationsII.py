__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/permutations-ii.py
# Time:  O(n!)
# Space: O(n)
# Brute Force Search
#
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# For example,
# [1,1,2] have the following unique permutations:
# [1,1,2], [1,2,1], and [2,1,1].
# LinkedIn Microsoft




class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, nums):
        solutions = [[]]

        for num in nums:
            next = []
            for solution in solutions:
                for i in xrange(len(solution) + 1): # need to + 1 for the case solution is empty
                    candidate = solution[:i] + [num] + solution[i:]
                    if candidate not in next:
                        next.append(candidate)
            solutions = next

        return solutions


if __name__ == "__main__":
    print Solution().permuteUnique([1, 1, 2])
    #print Solution().permuteUnique([1, -1, 1, 2, -1, 2, 2, -1])

#Java
js = '''
public class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        Arrays.sort(nums);
        return permuteUnique(nums, 0);
    }

    private List<List<Integer>> permuteUnique(int[] nums, int index) {
        List<List<Integer>> result = new ArrayList<>();
        if (index == nums.length) {
            result.add(new ArrayList<Integer>());
            return result;
        }
        List<List<Integer>> next = permuteUnique(nums, index + 1);
        for (List<Integer> list : next) {
            for (int i = 0; i <= list.size(); i++) {
                List<Integer> curr = new ArrayList<>(list);
                curr.add(i, nums[index]);
                result.add(curr);
                if (i < curr.size() - 1 && curr.get(i) == curr.get(i + 1)) {
                    break;
                }
            }
        }
        return result;
    }
}
'''