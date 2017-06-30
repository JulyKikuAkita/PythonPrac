__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/combinations.py
# Time:  O(n!)
# Space: O(n)
# DFS
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
# # Snapchat Uber
# Hide Tags Array Backtracking
# Hide Similar Problems (M) Letter Combinations of a Phone Number (M) Combination Sum II
# (M) Combinations (M) Combination Sum III (M) Factor Combinations (M) Combination Sum IV


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

if __name__ == "__main__":
    print Solution().combine(4, 2)
    print cc150().combin(4,2)


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




#test


my_test = SolutionOther()
#my_test.combine(4, 2)
#print my_test.combine(1, 0)
#print my_test.combine(1, 2)
#print my_test.combine(2, 2)
#print my_test.combine(4, 2)
#print my_test.combine(6, 4)


#flatten(my_test.combine(4, 2))

#java
js = '''
//template, 39.12% without optimize i <= n - k +!
public class Solution {
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

//100% , optimize by n - k + 1
public class Solution {
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

//100%
public class Solution {
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
'''