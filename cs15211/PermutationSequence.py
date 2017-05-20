__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/permutation-sequence.py
# Time:  O(n)
# Space: O(1)
# Math
#
# The set [1,2,3,...,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.
#
# Note: Given n will be between 1 and 9 inclusive.
#

import math

# Cantor ordering solution
class Solution:
    # @return a string
    def getPermutation(self, n, k):
        seq, k, fact = "", k - 1, math.factorial(n - 1)
        perm = [i for i in xrange(1, n + 1)]

        for i in reversed(xrange(n)):
            curr = perm[k / fact]
            #print i, curr, k, fact, perm
            seq += str(curr)
            perm.remove(curr)
            if i > 0:
                k %= fact
                fact /= i
        return seq


    def getCombination(self, n, k):
        parentset = [i for i in xrange(1, n+1)]
        result = []
        space = 1 << n
        for i in xrange(space):
            k = i
            index = 0
            subset = []
            while k:
                if k & 1 > 0:
                    subset.append(parentset[index])
                k >>= 1
                index += 1
            result.append(subset)
        return result



if __name__ == "__main__":
    print Solution().getPermutation(3, 2)
    #print Solution().getCombination(3, 2)


class SolutionOther:
    # Given n will be between 1 and 9 inclusive.
    # @return a string
    def getPermutation(self, n, k):
        d = [0,1]
        ans = []
        use = ['0'] * n


        for i in range(2,10):
            d.append(i * d[-1])

        print d
        for i in range(n):
            ans.append(0)
            for j in range(n):
                if use[j] == 1:
                    continue
                ans[i] = chr(ord('0') + j + 1)
                print i, ans, j, use
                if k <= d[n-i-1]:
                    use[j] = 1
                    break
                k -= d[n-i-1]
                print "k =", k
        return ''.join(ans)

#http://www.jiuzhang.com/solutions/permutation-sequence/
class Solution3(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fac = [1]
        for i in xrange(1, n+1):
            fac.append(fac[-1] * i)

        eligible = range(1, n+1)
        perm = []
        for i in xrange(n):
            digit = (k-1) / fac[n-i-1]
            perm.append(eligible[digit])
            eligible.remove(eligible[digit])
            k = (k-1) % fac[n-i-1] + 1
        return "".join([str(x) for x in perm])
#test
#test = SolutionOther()
#print test.getPermutation(4,2)

'''
ord(c): Given a string of length one, return an integer representing the Unicode code point of the character
 ex: ord('a') = 97
chr(c): eturn a string of one character whose ASCII code is the integer i. For example, chr(97) returns the string 'a'.
'''

#java
js = '''
public class Solution {
    public String getPermutation(int n, int k) {
        List<Integer> nums = new ArrayList<>(n);
        int factor = 1;
        for (int i = 0; i < n; i++) {
            nums.add(i + 1);
            factor *= i + 1;
        }
        k--;
        StringBuilder sb = new StringBuilder();
        k %= factor;
        factor /= n;
        for (int i = n - 1; i >= 0; i--) {
            int curr = k / factor;
            sb.append((char) ('0' + nums.get(curr)));
            nums.remove(curr);
            k %= factor;
            factor = i == 0 ? factor : factor / i;
        }
        return sb.toString();
    }
}

#python way
public class Solution {
    public String getPermutation(int n, int k) {
        StringBuilder sb = new StringBuilder();
        int[] fac = new int[n+1];
        boolean[] used = new boolean[n+1];
        List<Integer> eligible = new ArrayList<>(n);
        fac[0] = 1;
        for (int i = 1; i < n; i++) {
            fac[i] = fac[i-1] * i;
            eligible.add(i);
        }
        eligible.add(n);

        for (int i = 0; i < n; i++) {
            int digit = (k - 1) / fac[n-i-1];
            sb.append((char)('0'+ eligible.get(digit)));
            eligible.remove(eligible.get(digit));
            k = (k - 1) % fac[n-i-1] + 1;
        }

        return sb.toString();
    }
}
'''