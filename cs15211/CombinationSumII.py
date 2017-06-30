__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/combination-sum-ii.py
# Time:  O(n! / m!(n-m)!)
# Space: O(m)
# DFS
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
#  Snapchat
# Hide Tags Array Backtracking
# Hide Similar Problems (M) Combination Sum

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
if __name__ == "__main__":
    candidates, target = [10, 1, 2, 7, 6, 1, 5], 8
    print Solution().combinationSum2(candidates, target)


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
test = SolutionOther()
#print test.combinationSum2([6,2,3], 7)
#print test.combinationSum2i([2,1], 2)
#print test.combinationSum2p([10,1,2,7,6,1,5] , 8)

#java
java = '''
//hashset + sort to avoid duplicates result
public class Solution {
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
'''