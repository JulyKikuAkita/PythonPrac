__source__ = 'https://leetcode.com/problems/permutations-ii/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/permutations-ii.py
# Time:  O(n!)
# Space: O(n)
# Brute Force Search
#
# Description: Leetcode # 47. Permutations II
#
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# For example,
# [1,1,2] have the following unique permutations:
# [1,1,2], [1,2,1], and [2,1,1].
#
# Companies
# LinkedIn Microsoft
# Related Topics
# Backtracking
# Similar Questions
# Next Permutation Permutations Palindrome Permutation II
#
import unittest
# 56ms 99.84%
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

class TestMethods(unittest.TestCase):
    def test_Local(self):
         print Solution().permuteUnique([1, 1, 2])
        #print Solution().permuteUnique([1, -1, 1, 2, -1, 2, 2, -1])

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

//permutation usually use boolean[] to track if element is used
//permutation forloop index start with 0
//use start index result in multiple duplication as below example of backtrackErr
//Use HashSet to remove duplicate

# 5ms 54.65%
class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        backtrack(list, new ArrayList<>(), nums, new boolean[nums.length]);
        return list;
    }

    //############ wrong example below #########################
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
    //############ wrong example  above #########################

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

# Sort array instead of use hash set
# 5ms 54.65%
class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(list, new ArrayList<>(), nums, new boolean[nums.length]);
        return list;
    }

     private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums, boolean[] used){
        if (tempList.size() == nums.length) {
             list.add(new ArrayList<>(tempList));
             return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i - 1] == nums[i] && !used[i - 1]) continue;
            if (!used[i]) {
                tempList.add(nums[i]);
                used[i] = true;
                backtrack(list, tempList, nums, used);
                tempList.remove(tempList.size() - 1);
                used[i] = false;
            }
        }
    }
}

# 3ms 98.56%
class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        if (nums.length == 0) {
            return new ArrayList<>();
        }
        return permuteUnique(nums, 0);
    }

    private List<List<Integer>> permuteUnique(int[] nums, int index) {
        List<List<Integer>> result = new ArrayList<>();
        if (index == nums.length) {
            result.add(new ArrayList<>());
            return result;
        }
        for (List<Integer> list : permuteUnique(nums, index + 1)) {
            for (int i = 0; i <= list.size(); i++) {
                List<Integer> newList = new ArrayList<>(list);
                newList.add(i, nums[index]);
                result.add(newList);
                if (i < list.size() && list.get(i) == nums[index]) {
                    break;
                }
            }
        }
        return result;
    }
}

# 3ms 98.56%
class Solution {
    List<List<Integer>> ans;
    public List<List<Integer>> permuteUnique(int[] nums) {
        ans = new ArrayList();
        permute(nums, 0);
        return ans;
    }
    
    void permute(int[] nums, int l) {
        if (l == nums.length) {
            List<Integer> tmp = new ArrayList();
            for (int t: nums) {
                tmp.add(t);
            }
            ans.add(new ArrayList(tmp));
            return;
        } else{
            for (int i = l ; i < nums.length; i++) {
                int next = nums[i];
                if (i > l) {
                    boolean skip = false;
                    for (int j = l; j < i; j++) {
                        if (nums[j] == next) {
                            skip = true;
                            break;
                        }
                    }
                    if (skip) continue;
                }
                swap(nums, l, i);
                permute(nums, l + 1);
                swap(nums, l, i);
            }
        }
        
    }
    
    public void swap(int[] s, int i, int j) {
        int temp = s[i];
        s[i] = s[j];
        s[j] = temp;
    }
}
'''
