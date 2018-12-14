__source__ = 'https://leetcode.com/problems/permutation-sequence/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/permutation-sequence.py
# Time:  O(n)
# Space: O(1)
# Math
#
# Description: Leetcode # 60. Permutation Sequence
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
# Companies
# Twitter
# Related Topics
# Backtracking Math
# Similar Questions
# Next Permutation Permutations
#
import math
import unittest
# Note:
# '''
# ord(c): Given a string of length one, return an integer representing the Unicode code point of the character
#  ex: ord('a') = 97
# chr(c): eturn a string of one character whose ASCII code is the integer i. For example, chr(97) returns the string 'a'.
# '''

# Cantor ordering solution
class Solution1:
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
#
# The idea is as follow:
#
# For permutations of n, the first (n-1)! permutations start with 1,
# next (n-1)! ones start with 2, ... and so on.
# And in each group of (n-1)! permutations, the first (n-2)! permutations start with the smallest remaining number, ...
#
# take n = 3 as an example, the first 2 (that is, (3-1)! )
# permutations start with 1, next 2 start with 2 and last 2 start with 3.
# For the first 2 permutations (123 and 132), the 1st one (1!) starts with 2,
# which is the smallest remaining number (2 and 3).
# So we can use a loop to check the region that the sequence number falls in and get the starting digit.
# Then we adjust the sequence number and continue.
#
# 24ms 74.01%
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        numbers = range(1, n+1)
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation

class TestMethods(unittest.TestCase):
    def test_Local(self):
        #test
        #test = SolutionOther()
        #print test.getPermutation(4,2)
        print Solution().getPermutation(3, 2)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

"Explain-like-I'm-five" Java Solution in O(n)
I'm sure somewhere can be simplified so it'd be nice if anyone can let me know. The pattern was that:

say n = 4, you have {1, 2, 3, 4}

If you were to list out all the permutations you have

1 + (permutations of 2, 3, 4)

2 + (permutations of 1, 3, 4)

3 + (permutations of 1, 2, 4)

4 + (permutations of 1, 2, 3)


We know how to calculate the number of permutations of n numbers... n!
So each of those with permutations of 3 numbers means there are 6 possible permutations.
Meaning there would be a total of 24 permutations in this particular one.
So if you were to look for the (k = 14) 14th permutation, it would be in the

3 + (permutations of 1, 2, 4) subset.

To programmatically get that, you take k = 13 (subtract 1 because of things always starting at 0)
and divide that by the 6 we got from the factorial, which would give you the index of the number you want.
In the array {1, 2, 3, 4}, k/(n-1)! = 13/(4-1)! = 13/3! = 13/6 = 2. The array {1, 2, 3, 4} has a value of 3 at index 2.
So the first number is a 3.

Then the problem repeats with less numbers.

The permutations of {1, 2, 4} would be:

1 + (permutations of 2, 4)

2 + (permutations of 1, 4)

4 + (permutations of 1, 2)

But our k is no longer the 14th, because in the previous step, we've already eliminated the 12 4-number permutations
starting with 1 and 2. So you subtract 12 from k.. which gives you 1. Programmatically that would be...

k = k - (index from previous) * (n-1)! = k - 2*(n-1)! = 13 - 2*(3)! = 1

In this second step, permutations of 2 numbers has only 2 possibilities, meaning each of the three permutations
listed above a has two possibilities, giving a total of 6. We're looking for the first one,
so that would be in the 1 + (permutations of 2, 4) subset.

Meaning: index to get number from is k / (n - 2)! = 1 / (4-2)! = 1 / 2! = 0.. from {1, 2, 4}, index 0 is 1


so the numbers we have so far is 3, 1... and then repeating without explanations.


{2, 4}

k = k - (index from pervious) * (n-2)! = k - 0 * (n - 2)! = 1 - 0 = 1;

third number's index = k / (n - 3)! = 1 / (4-3)! = 1/ 1! = 1... from {2, 4}, index 1 has 4

Third number is 4


{2}

k = k - (index from pervious) * (n - 3)! = k - 1 * (4 - 3)! = 1 - 1 = 0;

third number's index = k / (n - 4)! = 0 / (4-4)! = 0/ 1 = 0... from {2}, index 0 has 2

Fourth number is 2


Giving us 3142. If you manually list out the permutations using DFS method, it would be 3142. Done!
It really was all about pattern finding.

# 7ms 96.43%
class Solution {
    public String getPermutation(int n, int k) {
        int pos = 0;
        List<Integer> numbers = new ArrayList<>();
        int[] factorial = new int[n+1];
        StringBuilder sb = new StringBuilder();

        // create an array of factorial lookup
        int sum = 1;
        factorial[0] = 1;
        for(int i=1; i<=n; i++){
            sum *= i;
            factorial[i] = sum;
        }
        // factorial[] = {1, 1, 2, 6, 24, ... n!}

        // create a list of numbers to get indices
        for(int i = 1; i <= n; i++){
            numbers.add(i);
        }
        // numbers = {1, 2, 3, 4}

        k--;

        for(int i = 1; i <= n; i++){
            int index = k / factorial[n-i];
            sb.append(String.valueOf(numbers.get(index)));
            numbers.remove(index);
            k -= index * factorial[n-i];
        }

        return String.valueOf(sb);
    }
}

Thought:
The logic is as follows:
for n numbers the permutations can be divided to (n-1)! groups,
for n-1 numbers can be divided to (n-2)! groups, and so on.
Thus k/(n-1)! indicates the index of current number, and k%(n-1)! denotes remaining index for the remaining n-1 numbers.
We keep doing this until n reaches 0, then we get n numbers permutations that is kth.

# 7ms 96.43%
class Solution {
    public String getPermutation(int n, int k) {
        List<Integer> nums = new ArrayList<>(n);
        int factor = 1;

        for (int i = 0; i < n; i++) {
            nums.add(i + 1);
            factor *= i + 1;
        }
        k--;
        k %= factor;
        factor /= n;
        StringBuilder sb = new StringBuilder();
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

# 7ms 96.43%
class Solution {
    public String getPermutation(int n, int k) {
        ArrayList<Integer> temp = new ArrayList<>();

        // a factorial table
        int[] factorial = new int[n];
        factorial[0] = 1;
        for(int i = 1; i < n; i++) {
            factorial[i] = factorial[i-1] * i;
        }
        for(int i = 1; i <= n; i++) {
            temp.add(i);
        }

        return permutation(temp, k, factorial);

    }

    public String permutation(ArrayList<Integer> temp, int k, int[] factorial) {
        // do until list is empty and you return nothing
        if (temp.size() == 0) {
            return "";
        }
        int number = (k-1)/factorial[temp.size()-1];
        //System.out.println(number);
        String s = Integer.toString(temp.get(number));
        k = k - number*factorial[temp.size()-1];
        temp.remove(number);

        return s + permutation(temp, k, factorial);
    }
}

# 9ms 70.43%
class Solution {
    public String getPermutation(int n, int k) {
        StringBuilder sb = new StringBuilder();
        boolean[] used = new boolean[n];

        k = k - 1;  //idx start with 0
        int factor = 1; //factor is to refer (n-1)! permutations
        for (int i = 2; i < n; i++) {
            factor *= i;
        }

        for (int i = 0; i < n; i++) {
            int index = k / factor; //find index of the highest digit in the list
            k = k % factor; //update k for every loop

            for (int j = 0; j < n; j++) { //compute the insert index
                if (used[j] == false) {
                    if (index == 0) { //when index == 0 j is the index to add new number
                        used[j] = true;
                        sb.append((char) ('0' + j + 1));
                        break;
                    } else {
                        index--;
                    }
                }
            }
            if (i < n - 1) {
                //(n - 1)! -> ((n - 1) - 1)! //the first digi has been added, shrink the possibitility of perm
                factor = factor / (n - 1 - i);
            }
        }
        return sb.toString();
    }
}
'''