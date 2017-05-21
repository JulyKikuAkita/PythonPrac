__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/factor-combinations.py
# Time:  O(nlogn)
# Space: O(logn)
#
# Numbers can be regarded as product of its factors. For example,
#
# 8 = 2 x 2 x 2;
#   = 2 x 4.
# Write a function that takes an integer n and return all possible combinations of its factors.
#
# Note:
# Each combination's factors must be sorted ascending, for example: The factors of 2 and 6 is [2, 6], not [6, 2].
# You may assume that n is always positive.
# Factors should be greater than 1 and less than n.
# Examples:
# input: 1
# output:
# []
# input: 37
# output:
# []
# input: 12
# output:
# [
#   [2, 6],
#   [2, 2, 3],
#   [3, 4]
# ]
# input: 32
# output:
# [
#   [2, 16],
#   [2, 2, 8],
#   [2, 2, 2, 4],
#   [2, 2, 2, 2, 2],
#   [2, 4, 4],
#   [4, 8]
# ]
#
#
#  LinkedIn Uber
# Hide Tags Backtracking
# Hide Similar Problems (M) Combination Sum


# best performance
class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        if n <= 1:
            return res
        factors = []
        self.dfs(res, factors, n )
        return res

    def dfs(self, res, factors, n):
        if n == 1:
            res.append(list(factors))
            return

        if len(factors) > 0:
            factors.append(n)
            res.append(list(factors))
            factors.pop()

        i = 2 if not factors else factors[-1]
        while i * i <= n:
            if n % i == 0 :
                factors.append(i)
                self.dfs(res, factors, n / i)
                factors.pop()
            i += 1


class Solution3:
    # @param {integer} n
    # @return {integer[][]}
    def getFactors(self, n):
        result = []
        factors = []
        self.getResult(n, result, factors)
        return result

    def getResult(self, n, result, factors):
        i = 2 if not factors else factors[-1]
        while i <= n / i:
            if n % i == 0:
                factors.append(i);
                factors.append(n / i);
                result.append(list(factors));
                factors.pop();
                self.getResult(n / i, result, factors);
                factors.pop()
            i += 1
import math
class Solution2(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        if n < 1:
            return res
        factors = []
        self.dfs(res, factors, n , 2)
        return res

    def dfs(self, res, factors, n, index):
            for i in xrange(index, int(math.sqrt(n)) + 1):
                if n % i == 0 and i <= (n / i):
                    factors.append(i)
                    factors.append(n / i)
                    #print i, factors
                    res.append(list(factors))
                    factors.pop()
                    self.dfs(res, factors, n / i, i)
                    factors.pop()


#java
java = '''
//template
public class Solution {
    public List<List<Integer>> getFactors(int n) {
        List<List<Integer>> res = new ArrayList<>();
        if (n <= 1) return res;
        backtrack2(res, new ArrayList<Integer>(), n, 2); //use 1, stack overflow
        return res;
    }

    //45.6%
    private void backtrack(List<List<Integer>> list, List<Integer> tempList, int n, int start){
        if (n <= 1 && tempList.size() > 1) { //in case of [n]
            list.add(new ArrayList<>(tempList));
            return;
        }

        for (int i = start; i <= n; i++) {
            if ( n % i == 0) {
                tempList.add(i);
                backtrack(list, tempList, n / i, i);
                tempList.remove(tempList.size() - 1);
            }
        }
    }

    //61.44%
     private void backtrack2(List<List<Integer>> list, List<Integer> tempList, int n, int start){
        if (n == 1 && tempList.size() > 1) { //incase of [n]
            list.add(new ArrayList<>(tempList));
            return;
        }

        for (int i = start; i * i <= n; i++) {
            if ( n % i == 0) {
                tempList.add(i);
                backtrack(list, tempList, n / i, i);
                tempList.remove(tempList.size() - 1);
            }
        }
        tempList.add(n);
        backtrack(list, tempList, 1, n);
        tempList.remove(tempList.size() - 1);
    }
}

95%
public class Solution {
    public List<List<Integer>> getFactors(int n) {
        List<List<Integer>> res = new ArrayList<>();
        if( n <= 1) return res;
        dfs(res, new ArrayList<>(), n, 2);
        return res;
    }

    private void dfs(List<List<Integer>> res, List<Integer> factors, int n, int index ){
        for(int i = index; i * i <= n; i++ ){
            if(n % i == 0 && i <= n / i){
                factors.add(i);
                factors.add(n/i);
                res.add(new ArrayList<>(factors));
                factors.remove(factors.size()-1);
                dfs(res, factors, n / i, i);
                factors.remove(factors.size()-1);

            }
        }
    }
}

'''