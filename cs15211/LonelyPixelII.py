__source__ = 'https://leetcode.com/problems/lonely-pixel-ii/#/description'
# Time:  O( m * n)
# Space: O()
#
# Description:
# Given a picture consisting of black and white pixels, and a positive integer N,
# find the number of black pixels located at some specific row R and column C
# that align with all the following rules:
#
# Row R and column C both contain exactly N black pixels.
# For all rows that have a black pixel at column C, they should be exactly the same as row R
# The picture is represented by a 2D char array consisting of 'B' and 'W',
# which means black and white pixels respectively.
#
# Example:
# Input:
# [['W', 'B', 'W', 'B', 'B', 'W'],
#  ['W', 'B', 'W', 'B', 'B', 'W'],
#  ['W', 'B', 'W', 'B', 'B', 'W'],
#  ['W', 'W', 'B', 'W', 'B', 'W']]
#
# N = 3
# Output: 6
# Explanation: All the bold 'B' are the black pixels we need (all 'B's at column 1 and 3).
#         0    1    2    3    4    5         column index
# 0    [['W', 'B', 'W', 'B', 'B', 'W'],
# 1     ['W', 'B', 'W', 'B', 'B', 'W'],
# 2     ['W', 'B', 'W', 'B', 'B', 'W'],
# 3     ['W', 'W', 'B', 'W', 'B', 'W']]
# row index
#
# Take 'B' at row R = 0 and column C = 1 as an example:
# Rule 1, row R = 0 and column C = 1 both have exactly N = 3 black pixels.
# Rule 2, the rows have black pixel at column C = 1 are row 0, row 1 and row 2.
# They are exactly the same as row R = 0.
#
# Note:
# The range of width and height of the input 2D array is [1,200].
# Hide Company Tags Google
# Hide Tags Array Depth-first Search
# Hide Similar Problems (M) Lonely Pixel II

import unittest
import collections

class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
        :rtype: int
        """
        ctr = collections.Counter(map(tuple, picture))
        cols = [col.count('B') for col in zip(*picture)]
        return sum(N * zip(row, cols).count(('B', N)) for row, count in ctr.items()
                   if count == N == row.count('B'))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
Verbose Java O(m*n) Solution, HashMap
The difficult parts are validating the two rules:

Row R and column C both contain exactly N black pixels.
For all rows that have a black pixel at column C, they should be exactly the same as row R
My solution:

Scan each row. If that row has N black pixels, put a string signature,
which is concatenation of each characters in that row,
as key and how many times we see that signature into a HashMap.
Also during scan each row, we record how many black pixels in each column in an array colCount
and will use it in step 2.
For input:
[['W', 'B', 'W', 'B', 'B', 'W'],
['W', 'B', 'W', 'B', 'B', 'W'],
['W', 'B', 'W', 'B', 'B', 'W'],
['W', 'W', 'B', 'W', 'B', 'B']]
We will get a HashMap:
{"WBWBBW": 3, "WWBWBB": 1}
and colCount array:
[0, 3, 1, 3, 4, 1]
Go through the HashMap and if the count of one signature is N, those rows
potentially contain black pixels we are looking for.
Then we validate each of those columns. For each column of them has N black pixels
(lookup in colCount array), we get N valid black pixels.
For above example, only the first signature "WBWBBW" has count == 3.
We validate 3 column 1, 3, 4 where char == 'B', and column 1 and 3 have 3 'B',
then answer is 2 * 3 = 6.
Time complexity analysis:
Because we only scan the matrix for one time, time complexity is O(m*n).
m = number of rows, n = number of columns.


2.
/**
 * Steps:
 * >> 1. create map<int, set<int>> cols, rows; -- to store black dots on that row;
 *
 *     _0_1_2_3_4_5_
 *  0 | 0 l 0 1 1 0     rows[0] = {1, 3, 4}
 *  1 | 0 l 0 1 1 0     rows[1] = {1, 3, 4}
 *  2 | 0 l 0 1 1 0     rows[2] = {1, 3, 4}
 *  3 | 0 0 1 0 1 0     rows[3] = {  2,  4}
 *
 * >> 2. for every pixel meet rule 1, that is: pic[i][j] == 'B' && rows[i].size() == N && cols[j].size() == N
 *       check rule2: for every row k in cols[j];  check that row[k] = row[i];
 *
 * We can tell the 6 black pixel in col 1 and col 3 are lonely pixels
 *     _0_1_2_3_4_5_
 *  0 | 0 L 0 L 1 0     rows[0] = {1, 3, 4}  =
 *  1 | 0 L 0 L 1 0     rows[1] = {1, 3, 4}  =
 *  2 | 0 L 0 L 1 0     rows[2] = {1, 3, 4}
 *  3 | 0 0 1 0 1 0     rows[3] = {  2,  4}
 *
 */

public class Solution {
    public int findBlackPixel(char[][] picture, int N) {
        int m = picture.length;
        int n = picture[0].length;
        Map<Integer, Set<Integer>> rows = new HashMap<Integer, Set<Integer>>(); // black pixels in each row;
        Map<Integer, Set<Integer>> cols = new HashMap<Integer, Set<Integer>>(); // black pixels in each col;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (picture[i][j] == 'B') {
                    if (!rows.containsKey(i)) rows.put(i, new HashSet<Integer>());
                    if (!cols.containsKey(j)) cols.put(j, new HashSet<Integer>());
                    rows.get(i).add(j); //save col index
                    cols.get(j).add(i); //save row index
                }
            }
        }

        int res = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n && rows.containsKey(i); j++) {
                if (picture[i][j] == 'B'
                && rows.get(i).size() == N
                && cols.containsKey(j)
                && cols.get(j).size() == N) { // rule 1 fulfilled
                    int cnt = 1;
                    for (int row : cols.get(j)) {
                        if (!rows.get(i).equals(rows.get(row))) {
                            cnt = 0;
                            break;
                        }
                    }
                    res += cnt;
                }
            }

        }
        return res;
    }
}

'''