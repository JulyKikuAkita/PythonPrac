__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/subsets-ii.py
# Time:  O(n * 2^n)
# Space: O(1)
# Brute Force Search
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

if __name__ == "__main__":
    print SolutionCC150().subsetsWithDup([1, 2, 2])
    print Solution().subsetsWithDup([1, 2, 2])
    print Solution2().subsetsWithDup([1, 2, 2])

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


#tet
test = SolutionOther()
S = [1,2,2]
#print test.subsetsWithDup(S)


#for x in range(2**len(S)):
#    print "x=", x
#    for i in range(1, len(S)):
#      print "i=", i, "bin = ", (x >> (i-1)&0x03)

#java
js = '''
public class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        if (nums.length == 0) {
            return result;
        }
        Arrays.sort(nums);
        subsetsWithDup(nums, 0, result, new ArrayList<>(), false);
        return result;
    }

    private void subsetsWithDup(int[] nums, int index, List<List<Integer>> result, List<Integer> cur, boolean hasLast) {
        if (index == nums.length) {
            result.add(new ArrayList<>(cur));
            return;
        }
        subsetsWithDup(nums, index + 1, result, cur, false);
        if (index == 0 || nums[index] != nums[index - 1] || hasLast) {
            cur.add(nums[index]);
            subsetsWithDup(nums, index + 1, result, cur, true);
            cur.remove(cur.size() - 1);
        }
    }
}
'''