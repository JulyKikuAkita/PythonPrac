__source__ = 'https://leetcode.com/problems/single-number-ii/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/singleNumberII.py
# Time:  O(n)
# Space: O(1)
# Bit Manipulation
#
# Description: Leetcode # 137. Single Number II
#
# Given an array of integers, every element appears three times except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Related Topics
# Bit Manipulation
# Similar Questions
# Single Number Single Number III
#
import unittest
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        one, two = 0, 0
        for x in A:
            one, two = (~x & one) | (x & ~one & ~two), (~x & two) | (x & one)
        return one

Thought = '''
The code works in similar line with the question of "finding the element
which appears once in an array - containing other elements each appearing twice".
Solution is to XOR all the elements and you get the answer.

Basically, it makes use of the fact that x^x = 0.
So all paired elements get XOR'd and vanish leaving the lonely element.
Since XOR operation is associative, commutative..
it does not matter in what fashion elements appear in array, we still get the answer.

Now, in the current question - if we apply the above idea,
it will not work because - we got to have every unique element appearing even number of times.
So instead of getting the answer, we will end up getting XOR of all unique elements which is not what we want.

To rectify this mistake, the code makes use of 2 variables.
ones - At any point of time, this variable holds XOR of all the elements which have
appeared "only" once.
twos - At any point of time, this variable holds XOR of all the elements which have
appeared "only" twice.

So if at any point time,
1. A new number appears - It gets XOR'd to the variable "ones".
2. A number gets repeated(appears twice) - It is removed from "ones" and XOR'd to the
variable "twice".
3. A number appears for the third time - It gets removed from both "ones" and "twice".

The final answer we want is the value present in "ones" - coz, it holds the unique element.

So if we explain how steps 1 to 3 happens in the code, we are done.
Before explaining above 3 steps, lets look at last three lines of the code,

not_threes = ~(ones & twos)
ones & = not_threes
twos & = not_threes

All it does is, common 1's between "ones" and "twos" are converted to zero.

For simplicity, in all the below explanations -
consider we have got only 4 elements in the array (one unique element and 3 repeated elements - in any order).


Explanation for step 1
------------------------
Lets say a new element(x) appears.
CURRENT SITUATION - Both variables - "ones" and "twos" has not recorded "x".

Observe the statement "twos| = ones & x".
Since bit representation of "x" is not present in "ones",
AND condition yields nothing. So "twos" does not get bit representation of "x".
But, in next step "ones ^= x" - "ones" ends up adding bits of "x".
Thus new element gets recorded in "ones" but not in "twos".

The last 3 lines of code as explained already, converts common 1's b/w "ones" and "twos" to zeros.
Since as of now, only "ones" has "x" and not "twos" - last 3 lines does nothing.



Explanation for step 2.
------------------------
Lets say an element(x) appears twice.
CURRENT SITUATION - "ones" has recorded "x" but not "twos".

Now due to the statement, "twos| = ones & x" - "twos" ends up getting bits of x.
But due to the statement, "ones ^ = x" - "ones" removes "x" from its binary representation.

Again, last 3 lines of code does nothing.
So ultimately, "twos" ends up getting bits of "x" and "ones" ends up losing bits of "x".



Explanation for step 3.
-------------------------
Lets say an element(x) appears for the third time.
CURRENT SITUATION - "ones" does not have bit representation of "x" but "twos" has.

Though "ones & x" does not yield nothing .. "twos" by itself has bit representation of "x".
So after this statement, "two" has bit representation of "x".
Due to "ones^=x", after this step, "one" also ends up getting bit representation of "x".

Now last 3 lines of code removes common 1's of "ones" and "twos" - which is the bit representation of "x".
Thus both "ones" and "twos" ends up losing bit representation of "x".


1st example
------------
2, 2, 2, 4

After first iteration,
ones = 2, twos = 0
After second iteration,
ones = 0, twos = 2
After third iteration,
ones = 0, twos = 0
After fourth iteration,
ones = 4, twos = 0

2nd example
------------
4, 2, 2, 2

After first iteration,
ones = 4, twos = 0
After second iteration,
ones = 6, twos = 0
After third iteration,
ones = 4, twos = 2
After fourth iteration,
ones = 4, twos = 0


Explanation becomes much more complicated when there are more elements in the array in mixed up fashion.
But again due to associativity of XOR operation - We actually end up getting answer.
'''
class Solution2:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        one, two, not_threes = 0, 0, 0
        for x in A:
            two |= one & x
            one ^= x
            # below line only make one and two become 0
            not_threes = one & two
            one &= ~not_threes
            two &= ~not_threes
        return one

    def singleNumber2(self, A):
        count = [0] * 32
        result = 0
        for i in xrange(32):
            for j in xrange(A):
                if ((A[j] >> i ) & 1):
                    count[i] += 1
            result |= ((count[i] % 3) << i)
        return result

#  every element appears 4 times except for one with 2 times
class SolutionEX:
    # @param A, a list of integer
    # @return an integer
    # [1, 1, 1, 1, 2, 2, 2, 2, 3, 3]
    def singleNumber(self, A):
        one, two, three = 0, 0, 0
        for x in A:
            one, two, three = (~x & one) | (x & ~one & ~two & ~three), (~x & two) | (x & one), (~x & three) | (x & two)
        return two

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().singleNumber([1, 1, 1, 2, 2, 2, 3])
        print 4^2

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
# General idea: count bits and mod by count

# 0ms 100%
class Solution {
    public int singleNumber(int[] nums) {
        int[] bits = new int[32];
        for (int num : nums) {
            int i = 0;
            while (num != 0) {
                bits[i] += num & 1;
                num >>>= 1;
                i++;
            }
        }
        for (int i = 0; i < bits.length; i++) {
            bits[i] %= 3;
        }
        int result = 0;
        for (int i = bits.length - 1; i >= 0; i--) {
            result <<= 1;
            result |= bits[i];
        }
        return result;
    }
}

# 0ms 100%
class Solution {
    public int singleNumber(int[] nums) {
        int ones = 0, twos = 0;
        for(int i = 0; i < nums.length; i++){
            ones = (ones ^ nums[i]) & ~twos;
            twos = (twos ^ nums[i]) & ~ones;
        }
        return ones;
    }
    // Using Map
    // public int singleNumber(int[] nums) {
    //     Map<Integer,Integer> map=new HashMap<>();
    //     for(int i=0;i<nums.length;i++){
    //         map.put(nums[i],map.getOrDefault(nums[i],0)+1);
    //     }
    //     for(int i=0;i<nums.length;i++){
    //         int x=map.get(nums[i]);
    //         if(x==1) return nums[i];
    //     }
    //     return 0;
    // }
}
'''
