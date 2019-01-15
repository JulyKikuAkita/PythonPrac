__source__ = 'https://leetcode.com/problems/permutations/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/permutations.py
# Time:  O(n!) //n factorial
# Space: O(n)
# Math/Brute Force Search
#
# Description: Leetcode # 46. Permutations
#
# Given a collection of numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
#
# Companies
# LinkedIn Microsoft
# Related Topics
# Backtracking
# Similar Questions
# Next Permutation Permutations II Permutation Sequence Combinations
#
# Note:
# 1)
# - Permutation dfs for loop always starts with 0 as [1,2,3] and [3,2,1] are diff
# - combination dfs for loop starts with next idx (i + 1) and needs to pass in start idx as parameter, [1,2,3] and [3,2,1] are the same
# 2) for permutation, ex [1,2,3]
# there will be a lot of duplicated calculations for dfs:
# - use visited = boolean[] to avoid result for [1,1,1]
# - if input has duplicated element, ex [1,1,2,3]
# use both visited and hashset(declared before enter forloop, no need to pass in as parameter) in dfs helper function

import unittest

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        result = []
        used = [False] * len(num)
        self.permuteRecu(result, used, [], num)
        return result

    def permuteRecu(self, result, used, cur, num):
        if len(cur) == len(num):
            result.append(cur + [])
            #print cur + []
            return
        for i in xrange(len(num)):
            if not used[i]:
                used[i] = True
                cur.append(num[i])
                self.permuteRecu(result, used, cur, num)
                cur.pop()
                used[i] = False

class SolutionOther:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        num.sort()
        ans = [num[:]]
        while self.next_permutation(num):
            ans.append(num[:])
            #print ans
        return ans

    def permuteUnique(self, num):
        #need to sort num in duplicate condition
        num.sort()
        ans = [num[:]]
        while self.next_permutation(num):
            ans.append(num[:])
            #print ans
        return ans

    def next_permutation(self, num):
        for i in range(len(num)-2, -1, -1):
            #print "this round start with i=",i, num[i], num[i+1]
            if num[i] < num[i+1]:
                break
        else:
            return False

        for j in range(len(num)-1, i, -1):
            #print "j=", j,"i= ",i
            if num[j] > num[i]:
                num[i], num[j] = num[j], num[i]
                break

        for j in range(0, (len(num) - i) //2):
            #print "j=", j,"(len(num) - i) //2= ",(len(num) - i) //2
            num[i+j+1], num[len(num)-j-1] = num[len(num)-j-1], num[i+j+1]

        return True



    def nextPermutation(self, num):
        #num.sort()
        ans = [num[:]]
        while self.next_permutation(num):
            ans = (num[:])
            #print ans
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        #print test.permute([4,5,6])
        #print test.permuteUnique([2,2,1,1])
        #print test.nextPermutation([1,2])
        #print test.nextPermutation([6,7,5,3,5,6,2,9,1,2,7,0,9])
        #for i in range(3, -1, -1):
        #    print i

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

general ideas:
1)
- Permutation dfs for loop always starts with 0 as [1,2,3] and [3,2,1] are diff
- combination dfs for loop starts with next idx (i + 1) and needs to pass in start idx as parameter, 
[1,2,3] and [3,2,1] are the same
2) for permutation, ex [1,2,3]
there will be a lot of duplicated calculations for dfs:
- use visited = boolean[] to avoid result for [1,1,1]
- if input has duplicated element, ex [1,1,2,3]
use both visited and hashset(declared before enter forloop, no need to pass in as parameter) in dfs helper function

# Thought: https://leetcode.com/problems/find-the-closest-palindrome/solution/
template1) use visited = boolean[] to avoid [1,1,1]

# 2ms 99.93%
class Solution {
    //without boolean[] used, you'll see [1,1,1] showup as resue of the same element
    //also permutation forloop index starts with 0
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        backtrack(list, new ArrayList<>(), nums, new boolean[nums.length]); //use boolean arr to track element
        return list;
    }

    private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums, boolean[] used){
        if (tempList.size() == nums.length) {
            list.add(new ArrayList<>(tempList));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
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

# Template2) //note, does not work with duplicated elements
# 3ms 76.09%
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        if (nums == null || nums.length == 0) {
            return result;
        }
        permute(nums, 0, result, new ArrayList<Integer>());
        return result;
    }

    private void permute(int[] nums, int index, List<List<Integer>> result, List<Integer> curr) {
        if (index == nums.length) {
            result.add(new ArrayList<Integer>(curr));
            return;
        }
        for (int i = 0; i <= curr.size(); i++) {
            curr.add(i, nums[index]);
            permute(nums, index + 1, result, curr);
            curr.remove(i);
        }
    }
}

# 2ms 99.93%
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        int len = nums.length;
        if (len == 0) {
            return new ArrayList<>();
        }
        return permute(nums, 0);
    }

    private List<List<Integer>> permute(int[] nums, int index) {
        List<List<Integer>> result = new ArrayList<>();
        if (index == nums.length) {
            result.add(new ArrayList<>());
            return result;
        }
        for (List<Integer> list : permute(nums, index + 1)) {
            for (int i = 0; i <= list.size(); i++) {
                List<Integer> newList = new ArrayList<>(list);
                newList.add(i, nums[index]);
                result.add(newList);
            }
        }
        return result;
    }
}

# 3ms 76.09%
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        if(nums == null || nums.length == 0) {
            return res;
        }
        help(res, nums, 0);
        return res;
    }
    
    private void help(List<List<Integer>> res, int[] nums, int index) {
        if(index == nums.length) {
            List<Integer> tmp = new ArrayList<>();
            for(int num : nums) {
                tmp.add(num);
            }
            res.add(tmp);
            return;
        }
        
        for(int i = index; i < nums.length; i++) {
            swap(nums, index, i);
            help(res, nums, index + 1);
            swap(nums, index, i);
        }
    }
    
    private void swap(int[] nums, int x, int y) {
        int tmp = nums[x];
        nums[x] = nums[y];
        nums[y] = tmp;
    }
}

Iteration:
the basic idea is, to permute n numbers, we can add the nth number into the resulting
List<List<Integer>> from the n-1 numbers, in every possible position.

For example, if the input num[] is {1,2,3}: First, add 1 into the initial List<List<Integer>> (let's call it "answer").

Then, 2 can be added in front or after 1. So we have to copy the List<Integer> in answer
(it's just {1}), add 2 in position 0 of {1}, then copy the original {1} again, and add 2 in position 1.
Now we have an answer of {{2,1},{1,2}}. There are 2 lists in the current answer.

Then we have to add 3. first copy {2,1} and {1,2}, add 3 in position 0;
then copy {2,1} and {1,2}, and add 3 into position 1,
then do the same thing for position 3. Finally we have 2*3=6 lists in answer, which is what we want.

# 2ms 99.93%
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        LinkedList<List<Integer>> res = new LinkedList<List<Integer>>();
        if (nums == null || nums.length == 0) return res;
        res.add(new ArrayList<>());

        for (int n : nums) {
            int size = res.size();
            for (int i = size; i > 0; i--) {
                List<Integer> tmp = res.pollFirst();
                for (int j = 0; j <= tmp.size(); j++) {
                    List<Integer> cur = new ArrayList<Integer>(tmp);
                    cur.add(j, n);
                    res.add(cur);
                }
            }
        }
        return res;
    }
}
'''
templates = '''
A general approach to backtracking questions in Java (Subsets, Permutations, Combination Sum, Palindrome Partioning)
This structure might apply to many other backtracking questions,
but here I am just going to demonstrate Subsets, Permutations, and Combination Sum.

Subsets : https://leetcode.com/problems/subsets/

public List<List<Integer>> subsets(int[] nums) {
    List<List<Integer>> list = new ArrayList<>();
    Arrays.sort(nums);
    backtrack(list, new ArrayList<>(), nums, 0);
    return list;
}

private void backtrack(List<List<Integer>> list , List<Integer> tempList, int [] nums, int start){
    list.add(new ArrayList<>(tempList));
    for(int i = start; i < nums.length; i++){
        tempList.add(nums[i]);
        backtrack(list, tempList, nums, i + 1);
        tempList.remove(tempList.size() - 1);
    }
}
Subsets II (contains duplicates) : https://leetcode.com/problems/subsets-ii/

public List<List<Integer>> subsetsWithDup(int[] nums) {
    List<List<Integer>> list = new ArrayList<>();
    Arrays.sort(nums);
    backtrack(list, new ArrayList<>(), nums, 0);
    return list;
}

private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums, int start){
    list.add(new ArrayList<>(tempList));
    for(int i = start; i < nums.length; i++){
        if(i > start && nums[i] == nums[i-1]) continue; // skip duplicates
        tempList.add(nums[i]);
        backtrack(list, tempList, nums, i + 1);
        tempList.remove(tempList.size() - 1);
    }
}
Permutations : https://leetcode.com/problems/permutations/

public List<List<Integer>> permute(int[] nums) {
   List<List<Integer>> list = new ArrayList<>();
   // Arrays.sort(nums); // not necessary
   backtrack(list, new ArrayList<>(), nums);
   return list;
}

private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums){
   if(tempList.size() == nums.length){
      list.add(new ArrayList<>(tempList));
   } else{
      for(int i = 0; i < nums.length; i++){
         if(tempList.contains(nums[i])) continue; // element already exists, skip
         tempList.add(nums[i]);
         backtrack(list, tempList, nums);
         tempList.remove(tempList.size() - 1);
      }
   }
}
Permutations II (contains duplicates) : https://leetcode.com/problems/permutations-ii/

public List<List<Integer>> permuteUnique(int[] nums) {
    List<List<Integer>> list = new ArrayList<>();
    Arrays.sort(nums);
    backtrack(list, new ArrayList<>(), nums, new boolean[nums.length]);
    return list;
}

private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums, boolean [] used){
    if(tempList.size() == nums.length){
        list.add(new ArrayList<>(tempList));
    } else{
        for(int i = 0; i < nums.length; i++){
            if(used[i] || i > 0 && nums[i] == nums[i-1] && !used[i - 1]) continue;
            used[i] = true;
            tempList.add(nums[i]);
            backtrack(list, tempList, nums, used);
            used[i] = false;
            tempList.remove(tempList.size() - 1);
        }
    }
}
Combination Sum : https://leetcode.com/problems/combination-sum/

public List<List<Integer>> combinationSum(int[] nums, int target) {
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
            tempList.add(nums[i]);
            backtrack(list, tempList, nums, remain - nums[i], i); // not i + 1 because we can reuse same elements
            tempList.remove(tempList.size() - 1);
        }
    }
}
Combination Sum II (can't reuse same element) : https://leetcode.com/problems/combination-sum-ii/

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
Palindrome Partitioning : https://leetcode.com/problems/palindrome-partitioning/

public List<List<String>> partition(String s) {
   List<List<String>> list = new ArrayList<>();
   backtrack(list, new ArrayList<>(), s, 0);
   return list;
}

public void backtrack(List<List<String>> list, List<String> tempList, String s, int start){
   if(start == s.length())
      list.add(new ArrayList<>(tempList));
   else{
      for(int i = start; i < s.length(); i++){
         if(isPalindrome(s, start, i)){
            tempList.add(s.substring(start, i + 1));
            backtrack(list, tempList, s, i + 1);
            tempList.remove(tempList.size() - 1);
         }
      }
   }
}

public boolean isPalindrome(String s, int low, int high){
   while(low < high)
      if(s.charAt(low++) != s.charAt(high--)) return false;
   return true;
}
'''
