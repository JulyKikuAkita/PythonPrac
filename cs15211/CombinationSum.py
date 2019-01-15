__source__ = 'https://leetcode.com/problems/combination-sum/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/combination-sum.py
# Time:  O(n^m)
# Space: O(m)
#
# Description: Leetcode # 217. Contains Duplicate
#
# Given a set of candidate numbers (C) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.
#
# The same repeated number may be chosen from C unlimited number of times.
#
# Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
# The solution set must not contain duplicate combinations.
# For example, given candidate set 2,3,6,7 and target 7,
# A solution set is:
# [7]
# [2, 2, 3]
#
# Companies
# Snapchat Uber
# Related Topics
# Array Backtracking
# Similar Questions
# Letter Combinations of a Phone Number Combination Sum II Combinations Combination Sum III
# Factor Combinations Combination Sum IV
# 40. Combination Sum II has duplicate
#
import unittest
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        result = []
        self.combinationSumRecu(sorted(candidates), result,0, [], target)
        return result

    def combinationSumRecu(self, candidates, result, start, intermediate, target):
        if target == 0:
            result.append(intermediate)
        while start < len(candidates) and candidates[start] <= target:
            self.combinationSumRecu(candidates, result, start, intermediate + [candidates[start]], target - candidates[start])
            start += 1


class SolutionOther:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        self.ans, tmp = [], []
        self.dfs(candidates, target, 0, 0,tmp)
        return self.ans

    def dfs(self,candidates, target, p, now, tmp):
        if now == target:
            #self.ans.append(tmp[:])
            self.ans.append(tmp)
            return
        for i in range(p, len(candidates)):
            if now + candidates[i] <= target :
                #tmp.append(candidates[i])
                self.dfs(candidates, target, i, now+candidates[i] , tmp+[candidates[i]])
                #tmp.pop()

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        test = SolutionOther()
        print test.combinationSum([6,2,3], 7)
        #print test.combinationSum([2,1], 2)
        candidates, target = [2, 3, 6, 7], 7
        result = Solution().combinationSum(candidates, target)
        print result

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
No duplicate in arr, no need to sort arr
40. Combination Sum II has duplicate

# 8ms 99.46%
public class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> list = new ArrayList<>();
        //Arrays.sort(nums);
        backtrack(list, new ArrayList<>(), candidates, target, 0);
        return list;
    }
    private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums, int remain, int start){
        if (remain < 0) return;
        if (remain == 0) {
            list.add(new ArrayList<>(tempList));
            return;
        }
        for (int i = start; i < nums.length; i++) {
            tempList.add(nums[i]);
            backtrack(list, tempList, nums, remain - nums[i], i); // not i + 1 because we can reuse same elements
            tempList.remove(tempList.size() - 1);
        }
    }
}

# 9ms 91.46% if not sort array
# 10ms 83.99% //sort array
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        //Arrays.sort(candidates); //run faster if not sort array
        dfs(candidates, target, 0, new ArrayList<>(), res);
        return res;
    }

    private void dfs(int[] candidates, int target, int start, List<Integer> tmp, List<List<Integer>> res){
        if (target == 0){
            res.add(new ArrayList<>(tmp));
            return; //no impact on runtime
        }
        for(int i = start; i < candidates.length; i++){
            if( target - candidates[i] >= 0){
                tmp.add(candidates[i]);
                dfs(candidates, target - candidates[i], i, tmp, res);
                tmp.remove(new Integer(candidates[i]));
            }
        }
    }
 }

# 8ms 99.46%
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        if (candidates.length == 0) {
            return result;
        }
        Arrays.sort(candidates); // need to sort array due to (i)
        combinationSum(candidates, target, 0, result, new ArrayList<>());
        return result;
    }

    private void combinationSum(int[] candidates, int target, int index, List<List<Integer>> result, List<Integer> cur) {
        if (target == 0) {
            result.add(new ArrayList<>(cur));
            return;
        }
        int size = cur.size();
        for (int i = index; i < candidates.length && candidates[i] <= target; i++) { //need to sort arr (i)
            cur.add(candidates[i]);
            combinationSum(candidates, target - candidates[i], i, result, cur);
            cur.remove(size);
        }
    }
}

# 14ms 45.41%
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<List<Integer>>> dp = new ArrayList<>(target);
        Arrays.sort(candidates);
        for (int i = 1; i <= target; i++) {
            List<List<Integer>> cur = new ArrayList<>();
            for (int j = 0; j < candidates.length && candidates[j] <= i; j++) {
                if (candidates[j] == i) {
                    cur.add(Arrays.asList(candidates[j]));
                } else {
                    for (List<Integer> prev : dp.get(i - candidates[j] - 1)) {
                        if (candidates[j] <= prev.get(0)) {
                            List<Integer> newList = new ArrayList<>();
                            newList.add(candidates[j]);
                            newList.addAll(prev);
                            cur.add(newList);
                        }
                    }
                }
            }
            dp.add(cur);
        }
        return dp.get(target - 1);
    }
}
'''