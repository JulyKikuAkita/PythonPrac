__source__ = 'https://leetcode.com/problems/combination-sum-ii/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/combination-sum-ii.py
# Time:  O(n! / m!(n-m)!)
# Space: O(m)
# DFS
#
# Description: Leetcode # 40. Combination Sum II
#
# Given a collection of candidate numbers (C) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.
#
# Each number in C may only be used once in the combination.
#
# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
# The solution set must not contain duplicate combinations.
# For example, given candidate set 10,1,2,7,6,1,5 and target 8,
# A solution set is:
# [1, 7]
# [1, 2, 5]
# [2, 6]
# [1, 1, 6]
#
# Companies
# Snapchat
# Related Topics
# Array Backtracking
# Similar Questions
# Combination Sum
#
import unittest
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        result = []
        self.combinationSum2Rec(sorted(candidates), result, 0,  [] , target)
        return result

    def combinationSum2Rec(self, candidates, result, start, intermediate, target):
        if target == 0:
            result.append(intermediate)
        prev = 0
        while start < len(candidates) and candidates[start] <= target:
            if prev != candidates[start]:
                self.combinationSum2Rec(candidates, result, start + 1, intermediate + [candidates[start]], target - candidates[start])
                prev = candidates[start]
            start += 1

class SolutionOther:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates.sort()
        SolutionOther.ret = []
        self.DFS( candidates, target, 0 , [])
        return SolutionOther.ret


    def DFS(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0 and valuelist not in Solution.ret:
            return SolutionOther.ret.append(valuelist)
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.DFS(candidates, target - candidates[i], i+1, valuelist+[candidates[i]])

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        test = SolutionOther()
        #print test.combinationSum2([6,2,3], 7)
        #print test.combinationSum2i([2,1], 2)
        #print test.combinationSum2p([10,1,2,7,6,1,5] , 8)
        self.assertEqual(1, 1)
        candidates, target = [10, 1, 2, 7, 6, 1, 5], 8
        print Solution().combinationSum2(candidates, target)
if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
#
# hashset + sort to avoid duplicates result
# 26ms 18.36%
class Solution {
     public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> list = new ArrayList<>();
        Arrays.sort(candidates);
        backtrack(list, new ArrayList<>(), candidates, target, 0);
        return list;
    }

     private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums, int remain, int start){
        if (remain < 0) return;
        if (remain == 0) {
            list.add(new ArrayList<>(tempList));
            return;
        }
        Set<Integer> set = new HashSet<>();
        for (int i = start; i < nums.length; i++) {
            if ( !set.contains(nums[i])) {
                tempList.add(nums[i]);
                set.add(nums[i]);
                backtrack(list, tempList, nums, remain - nums[i], i + 1); // not i + 1 because we can reuse same elements
                tempList.remove(tempList.size() - 1);
            }
        }
    }
}

# 11ms 83.52%
class Solution {
    public List<List<Integer>> combinationSum2(int[] nums, int target) {
        List<List<Integer>> list = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(list, new ArrayList<>(), nums, target, 0);
        return list;

    }

    private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums, int remain, int start){
        if(remain < 0) return;
        else if(remain == 0) list.add(new ArrayList<>(tempList));
        else{
            for(int i = start; i < nums.length; i++){
                if(i > start && nums[i] == nums[i-1]) continue; // skip duplicates
                tempList.add(nums[i]);
                backtrack(list, tempList, nums, remain - nums[i], i + 1);
                tempList.remove(tempList.size() - 1);
            }
        }
    }
}


# 9ms 95.33%
class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        if (target == 0) return result;
        Arrays.sort(candidates);
        dfs(result, new ArrayList<>(), candidates, target, 0);
        return result;
    }

    private void dfs(List<List<Integer>> res, List<Integer> cur, int[] candidates, int target, int start){
        if (target > 0) {
            for(int i = start; i < candidates.length && candidates[i] <= target; i++) {
                if (i > start && candidates[i] == candidates[i - 1]) continue;
                cur.add(candidates[i]);
                dfs(res, cur, candidates, target - candidates[i], i + 1);
                cur.remove(cur.size() - 1);
            }
        }
        if (target == 0) {
            res.add(new ArrayList<>(cur));
        }
    }
}

# bottom-up
# 8ms 99.28%
class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        if (target == 0) {
            return result;
        }
        Arrays.sort(candidates);
        combinationSum2(candidates, target, 0, result, new ArrayList<>(), false);
        return result;
    }

    private void combinationSum2(int[] candidates, int target, int index, List<List<Integer>> result, List<Integer> cur, boolean lastAdded) {
        if (target == 0) {
            result.add(new ArrayList<>(cur));
            return;
        } else if (index == candidates.length || candidates[index] > target) { //need to after target == 0 //need else if increase runtime
            return;
        }
        combinationSum2(candidates, target, index + 1, result, cur, false);
        if (index == 0 || lastAdded || candidates[index - 1] != candidates[index]) {
            cur.add(candidates[index]);
            combinationSum2(candidates, target - candidates[index], index + 1, result, cur, true);
            cur.remove(cur.size() - 1);
        }
    }
}
'''