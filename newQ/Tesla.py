__source__ = ''
# Time:  O()
# Space: O()
#
# Description:
# Question 1 - Primes
# Write a function to determine whether a given number is prime or not (divisible only by itself and 1).
# Use the Wikipedia definition of a prime numbers as a reference.
#

#
#
# Question 4 - Polygon Function
#  I have a function that takes a point and a polygon and returns True if the point lies inside
# the polygon, and False if it does not. The function implementation is shown on the next
# page.
#  In a white box testing implement your test cases in python class and consider each test in
# a separate method name starts with "test"
#  Justify each test case implemented ("Why is this test case important?") and document it.
#
import unittest
import os
from math import sqrt
from collections import defaultdict
# Reference
# https://www.daniweb.com/programming/software-development/code/462120/isprime-function-python
# https://stackoverflow.com/questions/327002/which-is-faster-in-python-x-5-or-math-sqrtx
# primes are integers greater than one with no positive divisors besides one and itself.
# Negative numbers are excluded
# Time:  O(n)
# Space: O(1)
class Question1:
    def isPrimes(self, n):
        '''
        :n int
        :check if integer n is a prime, return True or False
        '''
        # 2 is the only even prime
        if n == 2:
            return True
        # integers less than 2 and even numbers other than 2 are not prime
        if n < 2:
            return False
        if not n & 1:  # even numbers
            return False
        # loop looks at odd numbers 3, 5, 7, ... to sqrt(n)
        for i in range(3, int(sqrt(n))+1, 2):
            if n % i == 0:
                return False
        return True

# Question 2 - Mirror Words
# Implement the procedure 'find_mirrors' found on the next page.
# o in_file contains a list of words, one word per line.
# o a sample list of words is available at: http://www.cs.duke.edu/~ola/ap/linuxwords
# You will write to out_file a list of in_file words where the first word is a mirror image
# (letter reversed) copy of the second word, and both words exist in in_file. There should
# be one pair of words per line.
#  For example, out_file might contain:
# o Bard/draB, Bud/duB, Are/erA, Bag/gaB, Brag/garB, etc.
#  Requirements:
# o Describe how your algorithm works
# o Describe why you chose to implement it the way you did.
# o Eliminate Palindrome words like eye, civic and deed
# o Use a case sensitive compare: Aa would match aA but not aa
# o Include a copy of out_file in your response
# o Just implement find_mirrors, we're not looking for other improvements

#Reference https://stackoverflow.com/questions/3277503/how-do-i-read-a-file-line-by-line-into-a-list
class Question2:
    def read_file(self, in_file):
        '''
        :in_file: read file and return a list of string
        '''
        with open(in_file) as fp:
            content = fp.readlines()
        content = [x.strip() for x in content]
        return content

    def out_file(self, res, out_file):
        '''
        :content: a list of string
        :out_file: print mirror pair from list to out_file
        '''
        print os.getcwd
        with open(out_file, "w+") as output:
            for word in res:
                line = word[::-1] + "/" + word
                #print line
                output.write("{}\n".format(line))

    # find_mirrors print out one pair of mirror words when iterate though the input file
    # ex: Bag and gaB, we only print out gaB/Bag, we won't print another pair of Bag/gaB
    # By using the reverse of words as key while read the input file, we can complete the find-match process
    # in one iteration and also we don't need to worry about palindrome(if no duplication of words in input)
    # A hash table is used to trade space for speed for amortized look up time of O(1)
    def find_mirrors(self, in_file, out_file):
        '''
        :type in_file: a list of words, one word per line.
        :rtype: out_file a list of in_file words where the first word is a mirror image (letter reversed)
                copy of the second word, and both words exist in in_file. There should be one pair of words per line.
                For example, out_file might contain: Bard/draB, Bud/duB, Are/erA, Bag/gaB, Brag/garB, etc.
        '''
        content = self.read_file(in_file)

        # Use dict as hash table to record the reversed half string we are looking for
        # If we found the key, we found the pair
        reversed_words_map = defaultdict(int)
        res = []
        for item in content:
            reversed = item[::-1]
            if item in reversed_words_map:
                res.append(''.join(item))
            reversed_words_map[reversed] += 1

        #write output to file
        self.out_file(res, out_file)

class TestMethods(unittest.TestCase):
    def test_q1(self):
        self.assertTrue(Question1().isPrimes(9999991))
        self.assertTrue(Question1().isPrimes(3))
        self.assertTrue(Question1().isPrimes(2))
        self.assertFalse(Question1().isPrimes(1))
        self.assertFalse(Question1().isPrimes(0))
        self.assertFalse(Question1().isPrimes(-9999991))

    def test_q2(self):
        input = ['Aaron',"Are","Bag","Bard","Bud", "Brag", "civic", "deed", "draB", "duB", "eye", "erA", "gaB", "garB"]
        Question2().find_mirrors("linuxwords", "result")

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:

'''