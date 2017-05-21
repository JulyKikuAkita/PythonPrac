__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/combination-sum.py
# Time:  O(n^m)
# Space: O(m)
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
#  Snapchat Uber
# Hide Tags Array Backtracking
# Hide Similar Problems (M) Letter Combinations of a Phone Number (M) Combination Sum II (M) Combinations (M) Combination Sum III (M) Factor Combinations (M) Combination Sum IV


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
test = SolutionOther()
print test.combinationSum([6,2,3], 7)
#print test.combinationSum([2,1], 2)

if __name__ == "__main__":
    candidates, target = [2, 3, 6, 7], 7
    result = Solution().combinationSum(candidates, target)
    print result
#java
java = '''
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

public class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(candidates);
        dfs(candidates, target, 0, new ArrayList<>(), res);
        return res;
    }

    private void dfs(int[] candidates, int target, int start, List<Integer> tmp, List<List<Integer>> res){
        if(target == 0){
            res.add(new ArrayList<>(tmp));
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
'''