__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/combination-sum-iii.py
# Time:  O(C(n, k))
# Space: O(k)
#
# Find all possible combinations of k numbers that add up to a number n,
# given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# Ensure that numbers within the set are sorted in ascending order.
#
#
# Example 1:
#
# Input: k = 3, n = 7
#
# Output:
#
# [[1,2,4]]
#
# Example 2:
#
# Input: k = 3, n = 9
#
# Output:
#
# [[1,2,6], [1,3,5], [2,3,4]]
#
# Array Backtracking
# Hide Similar Problems (M) Combination Sum
#

class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        result = []
        self.combinationSumRecu(result, [], 1, k, n)
        return result

    def combinationSumRecu(self, result, intermediate, start, k, target):
        if k ==0 and target == 0:
            result.append(list(intermediate))
        elif k < 0:
            return
        while start < 10 and start * k + k * (k - 1) / 2 <= target:
            intermediate.append(start)
            self.combinationSumRecu(result, intermediate, start + 1, k - 1 , target - start)
            intermediate.pop()
            start += 1

if __name__ == "__main__":
    print Solution().combinationSum3(3, 9)

#Java
java = '''
public class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
         List<List<Integer>> result = new ArrayList<>();
         backtrack(result, new ArrayList<Integer>(), k, n, 1);
         return result;
    }

    private void backtrack(List<List<Integer>> list, List<Integer> tempList, int k, int remain, int start) {
        if (tempList.size() > k) return;
        if (tempList.size() == k && remain == 0) {
            list.add(new ArrayList<>(tempList));
            return;
        }
        for (int i = start; i <= 9; i++) {
            tempList.add(i);
            backtrack(list, tempList, k, remain - i, i + 1);
            tempList.remove(tempList.size() - 1);
        }

    }
}

public class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> result = new ArrayList<>();
        if (k < 0 || k > 9 || n <= 0) {
            return result;
        }
        combinationSum3(k, n, 1, result, new ArrayList<>());
        return result;
    }

    private void combinationSum3(int k, int n, int cur, List<List<Integer>> result, List<Integer> list) {
        if (k == 0) {
            if (n == 0) {
                result.add(new ArrayList<>(list));
            }
            return;
        }
        if (cur > 9 || cur > n) {
            return;
        }
        if (n > cur) {
            combinationSum3(k, n, cur + 1, result, list);
        }
        list.add(cur);
        combinationSum3(k - 1, n - cur, cur + 1, result, list);
        list.remove(list.size() - 1);
    }
}
'''