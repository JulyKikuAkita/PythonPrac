__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/permutations.py
# Time:  O(n!)
# Space: O(n)
# Math/Brute Force Search
#
# Given a collection of numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
#


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

if __name__ == "__main__":
    #print Solution().permute([1, 2, 3])
    print Solution().permute([1, 2])


'''
Same as Permutations II
Can be update to nextPermutation but exceed time constraint
'''
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

#test
test = SolutionOther()
#print test.permute([4,5,6])
#print test.permuteUnique([2,2,1,1])
#print test.nextPermutation([1,2])
#print test.nextPermutation([6,7,5,3,5,6,2,9,1,2,7,0,9])
#for i in range(3, -1, -1):
#    print i

#Java
js = '''
public class Solution {
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
'''