__source__ = 'https://leetcode.com/problems/combinations/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/combinations.py
# Time:  O(n!)
# Space: O(n)
# DFS
#
# Description: Leetcode # 77. Combinations
#
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# For example,
# If n = 4 and k = 2, a solution is:
#
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#
# Snapchat Uber
# Related Topics
# Backtracking
# Similar Questions
# Combination Sum Permutations
# #
import unittest
class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        result = []
        self.combineRecu(n, result, 0, [], k)
        return result

    def combineRecu(self, n, result, start, intermediate, k):
        if k == 0:
            # print " no [:] : ", intermediate
            # print intermediate[:]
            result.append(intermediate[:])
            return result

        for i in xrange(start, n):
            intermediate.append(i + 1)
            self.combineRecu(n, result, i + 1, intermediate, k - 1)
            intermediate.pop()

class cc150:
    def combin(self, n, k):
        result = []
        input = [i for i in xrange(1, n +1)]
        pos = 1  << len(input)

        for i in xrange(pos):
            j = i
            index = 0
            tmp = []
            while j:
                if j & 1 > 0:
                    tmp.append(input[index])
                index += 1
                j >>= 1
            #print tmp
            if len(tmp) == k:
                result.append(tmp)
        return result

class SolutionOther:
    # @return a list of lists of integers

    def combine(self, n, k):
        answer = []

        if n < 1 or k == 0:
            return answer
        elif n < k:
            return answer
        else:

            def recursive_help(n, k, sub_list, start):

                #base case
                if len(sub_list) == k:
                    answer.append(list(sub_list))
                    #print answer
                    return

                #recusive
                elif start <= n :
                    for i in range(start, n+1):
                        sub_list += [i]

                        recursive_help( n, k, sub_list, i+1)
                        sub_list.pop()
                        #print sub_list


            recursive_help(n, k, [], 1)
            return answer

def flatten(lists):
    for s in lists:
        if isinstance(s, list):
            flatten(s)
        else:
            print (s)


#flatten(my_test.combine(4, 2))
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        #test
        print Solution().combine(4, 2)
        print cc150().combin(4,2)

        my_test = SolutionOther()
        #my_test.combine(4, 2)
        #print my_test.combine(1, 0)
        #print my_test.combine(1, 2)
        #print my_test.combine(2, 2)
        #print my_test.combine(4, 2)
        #print my_test.combine(6, 4)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

//template,
# 14ms 68.80% without optimize i <= n - k +!
class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(result, new ArrayList<Integer>(), n, k, 1);
        return result;
    }

    private void backtrack(List<List<Integer>> list, List<Integer> tempList, int n, int k, int start) {
        if (start > n + 1 ) return; // when start == n+1, tempList has correct set needs to be append to list
        if ( k == 0) {
            list.add(new ArrayList<>(tempList));
            return;
        }
        // if (start > n ) return; //same as line above but with out "n + 1"
        for ( int i = start; i <= n; i++ ) { //can be optimized by i <= n - k + 1
            tempList.add(i);
            backtrack(list, tempList, n, k-1, i + 1);
            tempList.remove(tempList.size() - 1);
        }
    }
}

# For anyone stumped by why this change is necessary, 
# it's because you should not continue exploring (recursing) 
# when you know that there won't be enough numbers left until n to fill the needed k slots. 
# If n = 10, k = 5, and you're in the outermost level of recursion, you choose only i = 1...6 , 
# because if you pick i=7 and go into backTracking() you only have 8,9,10 to pick from, 
# so at most you will get [7,8,9,10]... but we need 5 elements!
#
# 2ms 99.89%  , optimize by n - k + 1
class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result = new ArrayList<>();
        if (k <= 0 || n < k) {
            return result;
        }
        combine(n, k, 1, result, new ArrayList<>());
        return result;
    }

    private void combine(int n, int k, int cur, List<List<Integer>> result, List<Integer> list) {
        if (k == 0) {
            result.add(new ArrayList<>(list));
            return;
        }
        int size = list.size();
        for (int i = cur; i <= n - k + 1; i++) {  //here with lopp
            list.add(i);
            combine(n, k - 1, i + 1, result, list);
            list.remove(size);
        }
    }
}

# 2ms 99.89% , optimize by n - k + 1
class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result = new ArrayList<>();
        if (k <= 0 || n < k) {
            return result;
        }
        combine(n, k, 1, result, new ArrayList<>());
        return result;
    }

    private void combine(int n, int k, int index, List<List<Integer>> result, List<Integer> cur) {
        if (k == 0) {
            result.add(new ArrayList<>(cur));
            return;
        } else if (n - index < k - 1) {
            return;
        }
        combine(n, k, index + 1, result, cur);  //orig case
        cur.add(index);
        combine(n, k - 1, index + 1, result, cur);
        cur.remove(cur.size() - 1);
    }
}

# https://leetcode.com/problems/combinations/discuss/27019/A-short-recursive-Java-solution-based-on-C(nk)C(n-1k-1)%2BC(n-1k)
# C(n,k)=C(n-1,k-1)+C(n-1,k)
# Here C(n,k) is divided into two situations. 
# Situation one, number n is selected, so we only need to select k-1 from n-1 next. 
# Situation two, number n is not selected, and the rest job is selecting k from n-1.

# 82ms 12.28%
class Solution {
    public List<List<Integer>> combine(int n, int k) {
        if (k == n || k == 0) {
            List<Integer> row = new LinkedList<>();
            for (int i = 1; i <= k; i++) {
                row.add(i);
            }
            return new LinkedList<>(Arrays.asList(row));
        }
        List<List<Integer>> result = this.combine(n - 1, k - 1);
        result.forEach(e -> e.add(n));
        result.addAll(this.combine(n - 1, k));
        return result;
    }
}
'''
