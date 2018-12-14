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
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if(nums==null || nums.length==0) return res;
        boolean[] used = new boolean[nums.length];
        List<Integer> list = new ArrayList<Integer>();
        Arrays.sort(nums);
        dfs(nums, used, list, res);
        return res;
    }

    public void dfs(int[] nums, boolean[] used, List<Integer> list, List<List<Integer>> res){
        if(list.size()==nums.length){
            res.add(new ArrayList<Integer>(list));
            return;
        }
        for(int i=0;i<nums.length;i++){
            if(used[i]) continue;
            if(i>0 &&nums[i-1]==nums[i] && !used[i-1]) continue;
            used[i]=true;
            list.add(nums[i]);
            dfs(nums,used,list,res);
            used[i]=false;
            list.remove(list.size()-1);
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
class Solution
{
    public List<List<Integer>> permuteUnique(int[] nums)
    {

        len = nums.length;

        r = new ArrayList<>();

        permuteUnique(nums, 0);

        return r;
    }

    List<List<Integer>> r;
    int len;

    void permuteUnique(int[] nums, int p) {

        if (p >= len - 1)
        {
            List<Integer> v = new ArrayList<>(len);
            for (int x: nums)
                v.add(x);
            r.add(v);
            return;
        }

        int t = nums[p];
        for (int i = p; i < len; i++)
        {
            int x = nums[i];
            if (i > p)
            {
                boolean skip = false;
                for (int j = p; j < i; j++)
                {
                    if (nums[j] == x)
                    {
                        skip = true;   // skip duplicates
                        break;
                    }
                }
                if (skip)
                    continue;
            }

            //swap: p <=> i
            nums[p] = x;
            nums[i] = t;

            permuteUnique(nums, p + 1);

            //backtrack
            //swap: p <=> i
            nums[i] = x;
            nums[p] = t;
        }
    }

}
'''