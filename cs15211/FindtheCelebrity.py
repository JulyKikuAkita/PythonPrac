__source__ = 'https://leetcode.com/problems/find-the-celebrity/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/find-the-celebrity.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 277. Find the Celebrity
#
# Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity.
# The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.
#
# Now you want to find out who the celebrity is or verify that there is not one.
# The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B.
#
# You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).
#
# You are given a helper function bool knows(a, b) which tells you whether A knows B.
#
# Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.
#
# Note: There will be exactly one celebrity if he/she is in the party.
#
# Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.
#
# Companies
# LinkedIn Facebook
# Related Topics
# Array
#
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
def knows(a, b):
    pass
#
import unittest
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        # Find the candidate.
        for i in xrange(1, n):
            if knows(candidate, i):  # All candidates < i are not celebrity candidates.
                candidate = i
        # Verify the candidate.
        for i in xrange(n):
            if i != candidate and (knows(candidate, i) \
                or not knows(i, candidate)):
                return -1
        return candidate

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
/* The knows API is defined in the parent class Relation.
      boolean knows(int a, int b); */
#9.88% 33ms
public class Solution extends Relation {
    public int findCelebrity(int n) {
        int start = 0;
        int end = n - 1;
        while (start < end) {
            if (knows(start, end)) {
                start++;
            } else {
                end--;
            }
        }
        for (int i = 0; i < start; i++) {
            if (knows(start, i) || !knows(i, start)) {
                return -1;
            }
        }
        for (int i = start + 1; i < n; i++) {
            if (knows(start, i) || !knows(i, start)) {
                return -1;
            }
        }
        return start;
    }
}
#80.35% 13ms
public class Solution extends Relation {
    public int findCelebrity(int n) {
        if ( n <= 0 ) return -1;
        if ( n == 1 ) return 0;
        // step 1 : find candidate
        int candidate = 0;
        for ( int i = 1 ; i < n ; i++ ){
            if(knows(candidate,i)) candidate = i;
        }
        // step 2 : check the candidate
        // check 1 : knows(candidate,i) ; i for all others before candidate -> false
        // check 2 : knows(i,candidate) , i for all ohters -> true (double check)
        for(int i = 0 ; i < n ; i++){
            if(i<candidate && knows(candidate,i)) return -1;
            if( !knows(i,candidate)) return -1;
        }
        return candidate;

    }
}

'''