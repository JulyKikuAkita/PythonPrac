__author__ = 'IFang Lee'
import unittest
from math import sqrt
from collections import defaultdict
#######################################################################################################################
# Python version 2.7.10
# Question 1 - Primes
# Write a function to determine whether a given number is prime or not (divisible only by itself and 1).
# Use the Wikipedia definition of a prime numbers as a reference.
# primes are integers greater than one with no positive divisors besides one and itself.
# Negative numbers are excluded

# Reference
# https://www.daniweb.com/programming/software-development/code/462120/isprime-function-python
# https://stackoverflow.com/questions/327002/which-is-faster-in-python-x-5-or-math-sqrtx
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
#######################################################################################################################
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

'''Describe why you chose to implement it the way you did and how your algorithm works '''
# I'm thinking of 2 ways to do it, use hashmap for O(1) query time to trade off for space, or use Trie to save all
# input words, which give us query time of O(M * logN), where M is maximum string length and N is number of keys
# in tree but less space requirement, O(ALPHABET_SIZE * key_length * N), comparing to use hashmap. Also hashmap is
# easier to implement. I leave both implementation in the code(line 137-183) but after couple run, the performance
# of using hashmap way exceeds using trie so I decide to go with hashmap.
#
# def find_mirrors finds any reversed word case sensitive from input file and
# print out one pair of "reversed/word" at each line to output file.
# ex: Bag and gaB, we only print out gaB/Bag, we won't print another pair of Bag/gaB
# A hash table/dict is used to trade space for speed for amortized look up time of O(1) in implementation of
# find_mirrors. By using the reverse of words as key while read the input file, we can complete the
# find-match process in one iteration and also we don't need to worry about palindrome
# (if no duplication of words in input)
#
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
        with open(out_file, "w+") as output:
            for word in res:
                line = word[::-1] + "/" + word
                #print line
                output.write("{}\n".format(line))

    # find_mirrors print out one pair of mirror words when iterate though the input file
    # ex: Bag and gaB, we only print out gaB/Bag, we won't print another pair of Bag/gaB
    # Time:  O(N)
    # Space: O(MN) M is the length of each word and N is the total number of word in input file
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
#######################################################################################################################
    #############################################################
    # Below is unit test, ignore
    #############################################################
    def test_find_mirror_map(self, content):
        # Use dict as hash table to record the reversed half string we are looking for
        # If we found the key, we found the pair
        reversed_words_map = defaultdict(int)
        res = []
        for item in content:
            reversed = item[::-1]
            if item in reversed_words_map:
                res.append(''.join(item))
            reversed_words_map[reversed] += 1
        return res

    #############################################################
    # Below is trie implementation
    #############################################################
    def test_find_mirror_trie(self, content):
        trie = Trie()
        res = []
        for item in content:
            reversed = item[::-1]
            if trie.search(reversed):
                res.append(''.join(item))
            trie.insert(item)
        return res

class TrieNode:
    def __init__(self):
        self.is_string = False
        self.leaves = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Inserts a word into the trie.
    def insert(self, word):
        cur = self.root
        for c in word:
            if not c in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]
        cur.is_string = True

    # Returns if the word is in the trie.
    def search(self, word):
        res, node = self.childSearch(word)
        if res:
            return node.is_string
        return False

    def childSearch(self, word):
        cur = self.root
        for c in word:
            if c in cur.leaves:
                cur = cur.leaves[c]
            else:
                return False, None
        return True, cur

#######################################################################################################################
# Question 4 - Polygon Function
# I have a function that takes a point and a polygon and returns True if the point lies inside
# the polygon, and False if it does not. The function implementation is shown on the next page.
# In a white box testing implement your test cases in python class and consider each test in
# a separate method name starts with "test"
# Justify each test case implemented ("Why is this test case important?") and document it.
#
# Reference:
# https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception
# http://www.softwaretestinghelp.com/white-box-testing-techniques-with-example/
class Polygon:
    def _is_point_in_poly(self, x, y, poly):
        n = len(poly)
        inside = False
        p1x,p1y = poly[0]
        for i in range(n+1):
            p2x,p2y = poly[i % n]
            if y > min(p1y,p2y):            # case1
                if y <= max(p1y,p2y):       # case2
                    if x <= max(p1x,p2x):   # case3
                        if p1y != p2y:      # case4
                            xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                        if p1x == p2x or x <= xints: #case5
                            inside = not inside
            p1x,p1y = p2x,p2y
        return inside

''' Justify each test case implemented ("Why is this test case important?") and document it. '''
# The goal for below test case is to try the best for full branch and path coverage
# (the IF statement, as noted by case 1-5 above at the end of lines at def _is_point_in_poly)
# Section1: def test_case1-5 negative covers the combination of the IF statement, also covers the change of
# value of xint and inside
#
# Section2: checks parameter x, y ,poly and negative scenario for null/empty input value
#
class PolygonTest(unittest.TestCase):
    line = [[0,0],[2,2]]
    triangle = [[0,0],[2,2],[3,0]]
    # Section1: branch and path coverage, covers IF statement branches
    # Cover case1: y <= min(p1y,p2y)
    def test_case1_Negative(self):
        self.assertFalse(Polygon()._is_point_in_poly(2, -100, self.triangle))

    # Cover case2: y > max(p1y,p2y)
    def test_case2_Negative(self):
        self.assertFalse(Polygon()._is_point_in_poly(2, 100, self.triangle))

    # Cover case3: x > max(p1x,p2x)
    def test_case3_Negative(self):
        self.assertFalse(Polygon()._is_point_in_poly(100, 1, self.triangle))

    # Cover case5: p1x != p2x && x > xints
    def test_case5_Negative(self):
        self.assertFalse(Polygon()._is_point_in_poly(2, 1, self.line))

    # Cover case5: p1x != p2x && x <= xints
    def test_case5_Negative2(self):
        self.assertFalse(Polygon()._is_point_in_poly(1, 1, self.line))

    # Cover case5: p1x == p2x && x <= xints (note, == xints if px1 == p2x)
    def test_case5_Negative3(self):
        line = [[-1,0],[-1,2]]
        self.assertFalse(Polygon()._is_point_in_poly(-1, 1, self.triangle))

    # Cover case 1-6:if all assert true
    def test_case_all_positive(self):
        self.assertTrue(Polygon()._is_point_in_poly(2, 1, self.triangle))

    # Cover case4: p1y == p2y, contradicted to case1 & 2
    # Covers input range
    def test_point(self):
        point = [[1,1]]
        self.assertFalse(Polygon()._is_point_in_poly(1, 1, point))

    # Section2: checks function input and statement in the code

    # TypeError: object of type 'NoneType' has no len()
    def test_nullPolygon(self):
        with self.assertRaises(Exception) as context:
            Polygon()._is_point_in_poly(0, 0, None)
            self.assertTrue("TypeError" in context.exception)

    # TypeError: object of type 'type' has no len()
    def test_emptyObjPolygon(self):
         with self.assertRaises(Exception) as context:
             Polygon()._is_point_in_poly(0, 0, object)
             self.assertTrue("TypeError" in context.exception)

    # IndexError: list index out of range
    def test_emptyListPolygon(self):
         with self.assertRaises(Exception) as context:
             Polygon()._is_point_in_poly(0, 0, [])
             self.assertTrue("index error" in context.exception)

    # ValueError: need more than 0 values to unpack
    def test_empty2DListPolygon(self):
         with self.assertRaises(Exception) as context:
             Polygon()._is_point_in_poly(0, 0, [[]])
             self.assertTrue("ValueError" in context.exception)

    # ValueError: need more than 0 values to unpack
    def test_invalidStringListPolygon(self):
             with self.assertRaises(Exception) as context:
                 Polygon()._is_point_in_poly(0, 0, [[""]])
                 self.assertRaises("ValueError" in context.exception)

    # ValueError: need more than 0 values to unpack
    def test_invalidValueListPolygon(self):
             with self.assertRaises(Exception) as context:
                 Polygon()._is_point_in_poly(0, 0, [[0]])
                 self.assertRaises("ValueError" in context.exception)

    # Covers input range for polygon
    def test_duplicated_points(self):
        line = [[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]]
        self.assertFalse(Polygon()._is_point_in_poly(1, 1, line))

    # Covers negative input range for polygon
    def test_line(self):
        line = [[-1,-1],[1,1]]
        self.assertFalse(Polygon()._is_point_in_poly(0, 0, line))

class TestMethods(unittest.TestCase):
     def test_q1(self):
        self.assertTrue(Question1().isPrimes(9999991))
        self.assertTrue(Question1().isPrimes(3))
        self.assertTrue(Question1().isPrimes(2))
        self.assertFalse(Question1().isPrimes(1))
        self.assertFalse(Question1().isPrimes(0))
        self.assertFalse(Question1().isPrimes(-9999991))

     def test_q2(self):
        input = ["Aaron","Are","Bag","Bard","Bud", "Brag", "civic", "deed", "draB", "duB", "eye", "erA", "gaB", "garB"]
        result = ['draB', 'duB', 'erA', 'gaB', 'garB']
        self.assertEqual(result, Question2().test_find_mirror_map(input))
        self.assertEqual(result, Question2().test_find_mirror_trie(input))

     # This will generate find mirror result to output file named "find_mirror_output.txt"
     def test_q2_generate_file(self):
        Question2().find_mirrors("linuxwords", "find_mirror_output.txt")

if __name__ == '__main__':
    unittest.main()
