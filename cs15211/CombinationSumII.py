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


######### below solution OT #####################################
    def combinationSum2i(self, candidates, target):
        candidates.sort()
        self.ans, tmp = [], []
        use = [0] * len(candidates)
        self.dfs(candidates, target, 0, 0, tmp, use)
        return self.ans

    def dfs(self, candidates, target, p, now, tmp, use):
        if now == target:
            self.ans.append(tmp[:])
            print  p, now, candidates, tmp
            return
        for i in range(p, len(candidates)):
            print "i = ", i
            if now + candidates[i] <= target and (i == 0 or candidates[i] != candidates[i-1] or use[i-1] == 1 ):
                tmp.append(candidates[i])
                use[i] = 1
                print  "i = ", i , p, now, candidates[i], tmp
                self.dfs(candidates, target, i+1, now+candidates[i] , tmp, use)
                print  "i = ", i , p, now, candidates[i], tmp
                tmp.pop()
                use[i] = 0

    def combinationSum2p(self, candidates, target):
        candidates.sort()
        solution = []
        self.combinationSum2Rec(candidates, target, 0, 0, [], solution)
        return solution
    def combinationSum2Rec(self, candidates, target, index, sum, tempList, solution):
        if sum == target:
            solution.append(list(tempList))
            return
        for i in range(index, len(candidates)):
            if (i == index or candidates[i-1] != candidates[i] and sum+candidates[i] <= target):
                tempList.append(candidates[i])
                self.combinationSum2Rec(candidates, target, i+1, sum+candidates[i], tempList, solution)
                tempList.pop()

#test
test = SolutionOther()
#print test.combinationSum2([6,2,3], 7)
#print test.combinationSum2i([2,1], 2)
#print test.combinationSum2p([10,1,2,7,6,1,5] , 8)

#java
js = '''
public class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        if (candidates == null || candidates.length == 0) {
            return new ArrayList<List<Integer>>();
        }
        Set<List<Integer>> result = new HashSet<>();
        Arrays.sort(candidates);
        List<Integer> curr = new ArrayList<>();
        combinationSum2(candidates, 0, target, result, curr);
        return new ArrayList<List<Integer>>(result);
    }

    private void combinationSum2(int[] candidates, int index, int target, Set<List<Integer>> result, List<Integer> curr) {
        if (target == 0) {
            result.add(new ArrayList<Integer>(curr));
            return;
        } else if (index == candidates.length) {
            return;
        }
        for (int i = index; i < candidates.length && candidates[i] <= target; i++) {
            curr.add(candidates[i]);
            combinationSum2(candidates, i + 1, target - candidates[i], result, curr);
            curr.remove(curr.size() - 1);
        }
    }
}
'''