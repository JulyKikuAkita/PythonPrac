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
#

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
public class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result = new ArrayList<>();
        if (k > n) {
            return result;
        }
        combine(n, 1, k, result, new ArrayList<Integer>());
        return result;
    }

    private void combine(int n, int index, int k, List<List<Integer>> result, List<Integer> curr) {
        if (k == 0) {
            result.add(new ArrayList<Integer>(curr));
            return;
        } else if (index > n) {
            return;
        }
        combine(n, index + 1, k, result, curr);
        curr.add(index);
        combine(n, index + 1, k - 1, result, curr);
        curr.remove(curr.size() - 1);
    }
}


public class Solution {
    public List<List<Integer>> combine(int n, int k) {
        if ( k > n) return new ArrayList<>();
        List<List<Integer>> res = new ArrayList<>();
        dfs(n, k, 1, new ArrayList<>(), res);
        return res;
    }

    private void dfs(int n, int k, int idx, List<Integer> tmp, List<List<Integer>> res){
         if(tmp.size() == k){
             res.add(new ArrayList<>(tmp));
             return;
         }

         for(int i = idx; i <= n; i++){
             tmp.add(i);
             dfs(n, k, i + 1, tmp, res);
             tmp.remove(tmp.size()-1);
         }
    }
}
'''