__source__ = 'https://leetcode.com/problems/subsets-ii/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/subsets-ii.py
# Time:  O(n * 2^n)
# Space: O(1)
# Brute Force Search
#
# Description: Leetcode # 90. Subsets II
#
# Given a collection of integers that might contain duplicates, S, return all possible subsets.
#
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,2], a solution is:
#
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
#
# Companies
# Facebook
# Related Topics
# Array Backtracking
#
import unittest
class SolutionCC150:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        slot = 1 << len(S)
        result = []
        for i in xrange(slot):
            k = i
            index = 0
            cur = []
            while k:
                if k & 1 > 0:
                    cur.append(S[index])
                k >>= 1
                index += 1
            if cur not in result:
                result.append(cur)
        return result

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S = sorted(S)
        i, count = 0, 1 << len(S)
        result = []

        while i < count:
            cur = []
            for j in xrange(len(S)):
                if i & 1 << j:  # i & (1 << j)
                    cur.append(S[j])
            i += 1
            if cur not in result:
                result.append(cur)
        return result

class Solution2:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        result = []
        self.subsetsWithDupRecu(result, [], sorted(S))
        return result

    def subsetsWithDupRecu(self, result, cur, S):
        if len(S) == 0 and cur not in result:
            result.append(cur)
        elif S:
            self.subsetsWithDupRecu(result, cur, S[1:])
            self.subsetsWithDupRecu(result, cur + [S[0]], S[1:])

class SolutionOther:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S.sort()
        templist= []
        for x in range(2**len(S)):
            for i in range(1, len(S)):
                if(S[i] == S[i-1] and (x >> (i-1)&0x03 == 0x01)):
                    break
            else:
                templist.append(x)
        return [[S[x] for x in range(len(S)) if i >> x & 1] for i in templist]

    def subsetsWithDup3(self, S):
        def dfs(depth, start, valuelist):
            if valuelist not in res: res.append(valuelist)
            if depth == len(S): return
            for i in range(start, len(S)):
                dfs(depth+1, i+1, valuelist+[S[i]])
        S.sort()
        res = []
        dfs(0, 0, [])
        return res

#for x in range(2**len(S)):
#    print "x=", x
#    for i in range(1, len(S)):
#      print "i=", i, "bin = ", (x >> (i-1)&0x03)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        #tet
        test = SolutionOther()
        S = [1,2,2]
        #print test.subsetsWithDup(S)

        self.assertEqual(1, 1)
        print SolutionCC150().subsetsWithDup([1, 2, 2])
        print Solution().subsetsWithDup([1, 2, 2])
        print Solution2().subsetsWithDup([1, 2, 2])

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# Definitely need to sort array
# Otherwise still see [4, 4, 1, 4,4]
# without sort array: [[],[4],[4,4],[4,4,1],[4,4,1,4],[4,4,1,4,4],[4,4,4],[4,4,4,4],[4,1],[4,1,4],[4,1,4,4],[1],[1,4],[1,4,4]]
# correct answer: [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]

# 5ms 21.91%
class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(list, new ArrayList<>(), nums, 0);
        return list;
    }

    private void backtrack(List<List<Integer>> list , List<Integer> tempList, int [] nums, int start){
        list.add(new ArrayList<>(tempList));
        Set<Integer> s = new HashSet<>();
        for (int i = start ; i < nums.length; i++) {
            if( !s.contains(nums[i]) ) {
                tempList.add(nums[i]);
                s.add(nums[i]);
                backtrack(list, tempList, nums, i + 1);
                tempList.remove(tempList.size() - 1);
            }
        }
    }
}

# 2ms 97.10%
class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(list, new ArrayList<>(), nums, 0);
        return list;
    }

    private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums, int start){
        list.add(new ArrayList<>(tempList));
        for(int i = start; i < nums.length; i++){
            if(i > start && nums[i] == nums[i-1]) continue; // skip duplicates //faster than hashset
            tempList.add(nums[i]);
            backtrack(list, tempList, nums, i + 1);
            tempList.remove(tempList.size() - 1);
        }
    }
}

# 2ms 97.10%
class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> cur = new ArrayList<>();
        Arrays.sort(nums);
        for (int i = 0; i <= nums.length; i++) {
            subsetsWithDup(nums, i, result, cur, i == 0 ? null : nums[i - 1]);
        }
        return result;
    }

    private void subsetsWithDup(int[] nums, int index, List<List<Integer>> result, List<Integer> cur, Integer lastSkipped) {
        if (index == nums.length) {
            result.add(new ArrayList<>(cur));
            return;
        }
        if (lastSkipped != null && nums[index] == lastSkipped) {
            return;
        }
        cur.add(nums[index]);
        for (int i = index + 1; i <= nums.length; i++) {
            subsetsWithDup(nums, i, result, cur, i == index + 1 ? lastSkipped : Integer.valueOf(nums[i - 1]));
        }
        cur.remove(cur.size() - 1);
    }
}
'''
