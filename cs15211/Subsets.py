__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/subsets.py
# Time:  O(n * 2^n)
# Space: O(1)
# Brute Force Search
#
# Given a set of distinct integers, S, return all possible subsets.
#
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If S = [1,2,3], a solution is:
#
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#
#  Amazon Uber Facebook
# Hide Tags Array Backtracking Bit Manipulation
# Hide Similar Problems (M) Generalized Abbreviation


#combination way
class SolutionCC150:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        slot = 1 << len(S)
        result = []
        for i in xrange(slot):
            index = 0
            k = i
            tmp = []
            while k:
                if k & 1 > 0:
                    tmp.append(S[index])
                index += 1
                k >>= 1
            result.append(tmp)
        return result

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        result = []
        i, count = 0, 1 << len(S)
        S = sorted(S)

        while i < count:
            cur = []
            for j in xrange(len(S)):
                if i & 1 << j:
                    cur.append(S[j])
            result.append(cur)
            i += 1
        return result

class Solution2:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        return self.subsetsRecu([], sorted(S))

    def subsetsRecu(self, cur, S):
        if not S:
            return [cur]
        return self.subsetsRecu(cur, S[1:]) + self.subsetsRecu(cur + [S[0]], S[1:])



class SolutionOther:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        ans = S[:] #deep copying the list S to ans  Note: ans = S not work as it only a copy of reference
        ans.sort()
        return [[ans[x] for x in range(len(ans)) if i >> x&1] for i in range(2**len(ans))]

    #DFS way:
    def subsets2(self, S):
        S.sort()
        ans = []
        self.dfs(S, 0, [], ans)
        return ans

    def dfs(self, S, depth, templist, ans):
        if depth == len(S) :
            ans.append(list(templist))
            #return
        else:
            self.dfs(S,depth+1, templist, ans)
            print "first", depth, templist
            templist.append(S[depth])
            self.dfs(S, depth+1, templist,ans)
            print "sec",depth, templist
            templist.pop()

    def subsets3(self, S):
        def dfs(depth, start, valuelist):
            res.append(valuelist)
            if depth == len(S): return
            for i in range(start, len(S)):
                print i, depth, valuelist+[S[i]]
                dfs(depth+1, i+1, valuelist+[S[i]])
        S.sort()
        res = []
        dfs(0, 0, [])
        return res

class Solution3(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.dfs(nums, 0, res, [])
        return res

    def dfs(self, nums, idx, res, cur):


        if idx >= len(nums):
            res.append(cur + [])
            return

        cur.append(nums[idx])
        self.dfs(nums, idx+1, res, cur)
        cur.pop()
        self.dfs(nums, idx+1, res, cur)

class Solution4(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.dfs(nums, 0, res, [], 0)
        return res

    def dfs(self, nums, idx, res, cur, depth):
        res.append(list(cur))
        if depth == len(nums):
            return
        for i in xrange(idx, len(nums)):
            cur.append(nums[i])
            self.dfs(nums, i+1, res, cur, depth +1)
            cur.pop()



if __name__ == "__main__":
    #print SolutionCC150().subsets([1, 2, 3])
    #print Solution().subsets([1, 2, 3])
    print Solution3().subsets([1, 2])

#print 3 & 0  #0

#for i in range(2**len(S)):
#    print "i=",i
#    for x in range(len(S)):
#        if i >> x & 1:  #if 1 (True); if 0 (False)
#            print  "x =",x, "binary =" , i >> x & 1 , "ans=" , S[x]
#        else:
#            print  "x =",x,"binary =" , i >> x & 1 , "no value"

#java
java = '''
public class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        backtrack(list, new ArrayList<>(), nums, 0);
        return list;
    }
    private void backtrack(List<List<Integer>> list , List<Integer> tempList, int [] nums, int start){
        list.add(new ArrayList<>(tempList));
        //Set<Integer> s = new HashSet<>();
        for (int i = start ; i < nums.length; i++) {
            //if( !s.contains(nums[i])) {
                tempList.add(nums[i]);
                //s.add(nums[i]);
                backtrack(list, tempList, nums, i + 1);
                tempList.remove(tempList.size() - 1);
            //}
        }
    }
}

public class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        backtrack(list, new ArrayList<>(), nums, 0);
        return list;
    }
    private void backtrack(List<List<Integer>> list , List<Integer> tempList, int [] nums, int start){
        if (start == nums.length) {
            list.add(new ArrayList<>(tempList));
            return;
        }

        backtrack(list, tempList, nums, start + 1); //[]
        tempList.add(nums[start]);
        backtrack(list, tempList, nums, start + 1);
        tempList.remove(tempList.size() - 1);
    }
}

public class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        int max = 1;
        for (int i = 0; i < nums.length; i++) {
            max <<= 1;
        }
        Arrays.sort(nums);
        for (int i = 0; i < max; i++) {
            int cur = i;
            List<Integer> list = new ArrayList<>();
            int index = 0;
            while (cur > 0) {
                if ((cur & 1) == 1) {
                    list.add(nums[index]);
                }
                cur >>>= 1;
                index++;
            }
            result.add(list);
        }
        return result;
    }
}
'''