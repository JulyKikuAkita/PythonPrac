__source__ = 'https://leetcode.com/problems/queue-reconstruction-by-height/#/description'
# Time:  O()
# Space: O()
#
# Description: 406. Queue Reconstruction by Height
#
# Suppose you have a random list of people standing in a queue.
# Each person is described by a pair of integers (h, k),
# where h is the height of the person and k is the number of people in front of this person
# who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.
#
# Note:
# The number of people is less than 1,100.
#
# Example
#
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
# Hide Company Tags Google
# Hide Tags Greedy
# Hide Similar Problems (H) Count of Smaller Numbers After Self

import unittest
# Pick out tallest group of people and sort them in a subarray (S).
# Since there's no other groups of people taller than them,
# therefore each guy's index will be just as same as his k value.
# For 2nd tallest group (and the rest), insert each one of them into (S) by k value. So on and so forth.
# E.g.
# input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# subarray after step 1: [[7,0], [7,1]]
# subarray after step 2: [[7,0], [6,1], [7,1]]
#
# 80ms 76.66%
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people: return []

        # obtain everyone's info
        # key=height, value=k-value, index in original array
        peopledct, height, res = {}, [], []

        for i in xrange(len(people)):
            p = people[i]
            if p[0] in peopledct:
                peopledct[p[0]] += (p[1], i),
            else:
                peopledct[p[0]] = [(p[1], i)]
                height += p[0],

        height.sort()      # here are different heights we have

        # sort from the tallest group
        for h in height[::-1]:
            peopledct[h].sort()
            for p in peopledct[h]:
                res.insert(p[0], people[p[1]])

        return res

# People are only counting (in their k-value) taller or equal-height others standing in front of them.
# So a smallest person is completely irrelevant for all taller ones. And of all smallest people,
# the one standing most in the back is even completely irrelevant for everybody else.
# Nobody is counting that person. So we can first arrange everybody else,
# ignoring that one person. And then just insert that person appropriately.
# Now note that while this person is irrelevant for everybody else,
# everybody else is relevant for this person - this person counts exactly everybody in front of them.
# So their count-value tells you exactly the index they must be standing.
#
# So you can first solve the sub-problem with all but that one person and then just insert that person appropriately.
# And you can solve that sub-problem the same way, first solving the sub-sub-problem
# with all but the last-smallest person of the subproblem. And so on.
# The base case is when you have the sub-...-sub-problem of zero people.
# You're then inserting the people in the reverse order,
# i.e., that overall last-smallest person in the very end and thus the first-tallest person in the very beginning.
# That's what the above solution does, Sorting the people from the first-tallest to the last-smallest,
# and inserting them one by one as appropriate.

    # 140ms 33.79%
    def reconstructQueue2(self, people):
            people.sort(key=lambda (h, k): (-h, k))
            queue = []
            for p in people:
                queue.insert(p[1], p)
            return queue

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
We first sort the people to make them stand from the highest to shortest.
For people with same height, sort them according to the count of people before them from small to big.

Then, we use the way similar to insert sorting to reorder the people.
For a given person to insert, all the people already sorted are higher,
so we just insert him in the "right" place to make the people before him as his "count" indicates.
Since he is shorter than all the people in the sorted list,
the "count" of the "existing" people does not be broken by the insertion.

# 74ms 12.62%
class Solution {
    public int[][] reconstructQueue(int[][] people) {
        if (people == null || people.length == 0 || people[0].length == 0)
            return new int[0][0];

         Arrays.sort(people, (int[] a, int[] b) -> ( b[0] == a[0] ? a[1] - b[1]: b[0] - a[0])); //desc
         /*
           Arrays.sort(people, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                if (b[0] == a[0]) return a[1] - b[1];
                return b[0] - a[0];
            }
        });
         */
         int n = people.length;
         ArrayList<int[]> tmp = new ArrayList<>();
         for (int i = 0; i < n; i++)
            tmp.add(people[i][1], new int[]{people[i][0], people[i][1]});
         int[][] res = new int[people.length][2];
         int i = 0;
         for (int[] k : tmp) {
            res[i][0] = k[0];
            res[i++][1] = k[1];
        }
        return res;
    }
}
'''