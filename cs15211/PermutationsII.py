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
#
#  LinkedIn Microsoft
# Hide Tags Backtracking
# Hide Similar Problems (M) Next Permutation (M) Permutations (M) Palindrome Permutation II

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
java = '''
//permutation usually use boolean[] to track if element is used
//permutation forloop index start with 0
//use start index result in multiple duplication as below example of backtrackErr
//Use HashSet to remove duplicate
public class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        backtrack(list, new ArrayList<>(), nums, new boolean[nums.length]);
        return list;
    }

    //start index does not work in permutation
    //[[1,1,1],[1,1,2],[1,2,1],[1,2,2],[2,1,1],[2,1,2],[2,2,1],[2,2,2]]
    private void backtrackErr(List<List<Integer>> list, List<Integer> tempList, int [] nums, int start){
        if (tempList.size() == nums.length) {
             list.add(new ArrayList<>(tempList));
             return;
        }
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (!set.contains(nums[i])) {
                tempList.add(nums[i]);
                set.add(nums[i]);
                backtrackErr(list, tempList, nums, i + 1);
                tempList.remove(tempList.size() - 1);
            }
        }
    }

    //[[1,1,2],[1,2,1],[2,1,1]]
    private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums, boolean[] used){
        if (tempList.size() == nums.length) {
             list.add(new ArrayList<>(tempList));
             return;
        }
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (!used[i] && !set.contains(nums[i])) {
                tempList.add(nums[i]);
                used[i] = true;
                set.add(nums[i]);
                backtrack(list, tempList, nums, used);
                tempList.remove(tempList.size() - 1);
                used[i] = false;
            }
        }
    }
}
'''