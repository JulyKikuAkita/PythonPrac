__source__ = 'https://leetcode.com/problems/different-ways-to-add-parentheses/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/different-ways-to-add-parentheses.py
# Time:  O(n * 4^n / n^(3/2)) ~= n * Catalan numbers = n * (C(2n, n) - C(2n, n - 1)),
#                                due to the size of the results is Catalan numbers,
#                                and every way of evaluation is the length of the string,
#                                so the time complexity is at most n * Catalan numbers.
# Space: O(n * 4^n / n^(3/2)), the cache size of lookup is at most n * Catalan numbers.
#
# Given a string of numbers and operators, return all possible
# results from computing all the different possible ways to
# group numbers and operators. The valid operators are +, - and *.
#
#
# Example 1
# Input: "2-1-1".
#
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# Output: [0, 2]
#
#
# Example 2
# Input: "2*3-4*5"
#
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
# Output: [-34, -14, -10, -10, 10]
#
# Cryptic Studios
#  Divide and Conquer
# Hide Similar Problems (M) Unique Binary Search Trees II (H) Basic Calculator (H) Expression Add Operators
#
import re
import operator
class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        tokens = re.split('(\D)', input)
        nums = map(int, tokens[::2])
        ops = map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2])
        lookup = [[ None for _ in xrange(len(nums))] for _ in xrange(len(nums))]

        def diffWaysToComputeRecu(left, right):
            if left == right:
                return [nums[left]]
            if lookup[left][right]:
                return lookup[left][right]
            lookup[left][right] = [ops[i](x, y) for i in xrange(left, right)
                                                for x in diffWaysToComputeRecu(left, i)
                                                for y in diffWaysToComputeRecu(i + 1, right)]
            return lookup[left][right]
        return diffWaysToComputeRecu(0, len(nums) - 1)
if __name__ == '__main__':
    input = "2-1+3"
    token = re.split('(\D)', input)
    nums = map(int, token[::2])
    print token
    print nums
    print Solution().diffWaysToCompute(input)

class Solution2:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        lookup = [[None for _ in xrange(len(input) + 1)] for _ in xrange(len(input) + 1)]
        ops = {'+' : operator.add, '-': operator.sub, '*':operator.mul}

        def diffWaysToComputeRecu(left, right):
            if lookup[left][right]:
                return lookup[left][right]
            result = []
            for i in xrange(left, right):
                if input[i] in ops:
                    for x in diffWaysToComputeRecu(left, i):
                        for y in diffWaysToComputeRecu(i + 1, right):
                            result.append(ops[input[i]](x, y))

            if not result:
                result = [int(input[left:right])]
            lookup[left][right] = result
            return lookup[left][right]

        return diffWaysToComputeRecu(0, len(input))

#java
java = '''
1. 91%
public class Solution {
    public List<Integer> diffWaysToCompute(String input) {
        return diffWaysToCompute(input, new HashMap<>());
    }

    private List<Integer> diffWaysToCompute(String input, Map<String, List<Integer>> cache) {
        int len = input.length();
        List<Integer> cacheValue = cache.get(input);
        if (cacheValue != null) {
            return cacheValue;
        }
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < len; i++) {
            char c = input.charAt(i);
            if (Character.isDigit(c)) {
                continue;
            }
            List<Integer> leftNums = diffWaysToCompute(input.substring(0, i), cache);
            List<Integer> rightNums = diffWaysToCompute(input.substring(i + 1), cache);
            for (int leftNum : leftNums) {
                for (int rightNum : rightNums) {
                    switch(c) {
                        case '+':
                            result.add(leftNum + rightNum);
                            break;
                        case '-':
                            result.add(leftNum - rightNum);
                            break;
                        case '*':
                            result.add(leftNum * rightNum);
                            break;
                    }
                }
            }
        }
        if (result.isEmpty()) {
            result.add(Integer.parseInt(input));
        }
        cache.put(input, result);
        return result;
    }
}

# Separate compute part, easier to read:
# 91%
public class Solution {
    public List<Integer> diffWaysToCompute(String input) {
        return diffWaysToCompute(input, new HashMap<>());
    }

    private List<Integer> diffWaysToCompute(String input, Map<String, List<Integer>> cache) {
        if (input.length() == 0) {
            return new ArrayList<>();
        } else if (cache.containsKey(input)) {
            return cache.get(input);
        }
        List<Integer> result = new ArrayList<>();
        for (int i = 1; i < input.length() - 1; i++) {
            char c = input.charAt(i);
            if (!Character.isDigit(c)) {
                List<Integer> leftList = diffWaysToCompute(input.substring(0, i), cache);
                List<Integer> rightList = diffWaysToCompute(input.substring(i + 1), cache);
                for (int left : leftList) {
                    for (int right : rightList) {
                        result.add(compute(left, right, c));
                    }
                }
            }
        }
        if (result.isEmpty()) {
            result.add(Integer.valueOf(input));
        }
        cache.put(input, result);
        return result;
    }

    private int compute(int left, int right, char c) {
        switch (c) {
            case '+':
                return left + right;
            case '-':
                return left - right;
            case '*':
                return left * right;
            default:
                throw new IllegalArgumentException("Invalid operator:" + c);
        }
    }
}
'''
#similar question:
# Give a integer array, return all possible ans of +, -, * operation
'''
 private Set<Integer> helper (int[] nums, int leftIndex, int rightIndex){
           Set<Integer> res = new HashSet<Integer>();

           if(leftIndex == rightIndex){
               res.add(nums[leftIndex]);
               return res;
           }

           for(int i = leftIndex; i<rightIndex; i++){
               Set<Integer> leftSet = helper(nums, leftIndex, i);
               Set<Integer> rightSet = helper(nums, i+1, rightIndex);

               for(int left : leftSet){
                   for(int right : rightSet){
                       res.add(left + right);
                       res.add(left * right);
                       res.add(left - right);
                   }
               }
           }

          return res;

       }
'''