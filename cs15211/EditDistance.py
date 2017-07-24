__source__ = 'https://leetcode.com/problems/edit-distance/#/solutions'
# https://github.com/kamyu104/LeetCode/blob/master/Python/edit-distance.py
# Thought: https://web.stanford.edu/class/cs124/lec/med.pdf
#
# Time:  O(n * m)
# Space: O(n + m)
# DP
#
# Description: Leetcode # 72. Edit Distance
#
# In computer science, edit distance is a way of quantifying how dissimilar two strings
# (e.g., words) are to one another by counting the minimum number of operations required to transform one string into the other.
#
# Given two words word1 and word2, find the minimum number of steps
# required to convert word1 to word2. (each operation is counted as 1 step.)
#
# You have the following 3 operations permitted on a word:
#
# a) Insert a character
# b) Delete a character
# c) Replace a character
#
# Related Topics
# Dynamic Programming String
# Similar Questions
# One Edit Distance Delete Operation for Two Strings
#
'''
Thought:
Let dp[i][j] stands for the edit distance between two strings with length i and j, i.e., word1[0,...,i-1] and word2[0,...,j-1].
There is a relation between dp[i][j] and dp[i-1][j-1].
Let's say we transform from one string to another. The first string has length i and it's last character is "x";
the second string has length j and its last character is "y". The following diagram shows the relation.

if x == y, then dp[i][j] == dp[i-1][j-1]
if x != y, and we insert y for word1, then dp[i][j] = dp[i][j-1] + 1
if x != y, and we delete x for word1, then dp[i][j] = dp[i-1][j] + 1
if x != y, and we replace x with y for word1, then dp[i][j] = dp[i-1][j-1] + 1
When x!=y, dp[i][j] is the min of the three situations.
Initial condition:
dp[i][0] = i, dp[0][j] = j
'''
import unittest
class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        if len(word1) < len(word2):
            return self.minDistance(word2, word1)

        distance = [i for i in xrange(len(word2) + 1)]
        print distance

        for i in xrange(1, len(word1) + 1):
            pre_distance_i_j = distance[0]
            distance[0] = i
            for j in xrange(1, len(word2) + 1):
                insert = distance[j - 1] + 1
                delete = distance[j] + 1
                #replace = pre_distance_i_j  #when word1[i] == word2[j]
                replace = pre_distance_i_j

                if word1[i - 1] != word2[j - 1]:
                    replace += 1  # real replace

                pre_distance_i_j = distance[j]
                distance[j] = min(insert, delete, replace)
        return distance[-1]

# Time:  O(n * m)
# Space: O(n * m)
class Solution2:
    # @return an integer
    def minDistance(self, word1, word2):
        distance = [[i] for i in xrange(len(word1) + 1)]
        distance[0] = [j for j in xrange(len(word2) + 1)]

        for i in xrange(1, len(word1) + 1):
            for j in xrange(1, len(word2) + 1):
                insert = distance[i][j - 1] + 1
                delete = distance[i - 1][j] + 1
                replace = distance[i - 1][j -1]
                if word1[i-1] != word2[j-1]:
                    replace += 1
                distance[i].append(min(insert,delete,replace))
        return distance[-1][-1]

class SolutionOther:
    # @return an integer
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        if m == 0:
            return n
        if n== 0 :
            return m
        dis = [[0 for j in range(n+1)] for i in range(m+1)]

        for i in range(m+1):
            dis[i][0]=i
        for j in range(n+1):
            dis[0][j]=j

        for i in range(1, m+1):
            for j in range(1, n+1):
                tmp = self.compare(word1[i-1],word2[j-1])
                dis[i][j] = min(dis[i-1][j-1]+tmp, dis[i][j-1]+1, dis[i-1][j]+1)

        return dis[m][n]

    def compare(self, char1, char2):
        if char1 == char2:
            return 0
        else:
            return 1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        #test case
        test = SolutionOther()
        print "start testing"
        #print test.minDistance("Rabbit", "Rabket")
        #print test.minDistance("a", "b")
        #print test.minDistance("abc", "b")

        print Solution().minDistance("Rabbit", "Racket")
        #print Solution2().minDistance("Rabbit", "Rabket")
        #print Solution().minDistance("Rabbit", "Rabbitt")

if __name__ == '__main__':
    unittest.main()

Java = '''
Thought: https://web.stanford.edu/class/cs124/lec/med.pdf
This is a classic problem of Dynamic Programming. We define the state dp[i][j]
to be the minimum number of operations to convert word1[0..i - 1] to word2[0..j - 1].
The state equations have two cases: the boundary case and the general case.
Note that in the above notations, both i and j take values starting from 1.

For the boundary case, that is, to convert a string to an empty string,
it is easy to see that the mininum number of operations to convert word1[0..i - 1]
to "" requires at least i operations (deletions). In fact, the boundary case is simply:

dp[i][0] = i;
dp[0][j] = j.
Now let's move on to the general case, that is, convert a non-empty word1[0..i - 1]
to another non-empty word2[0..j - 1]. Well, let's try to break this problem down
into smaller problems (sub-problems).
Suppose we have already known how to convert word1[0..i - 2] to word2[0..j - 2], which is dp[i - 1][j - 1].
Now let's consider word[i - 1] and word2[j - 1]. If they are euqal,
then no more operation is needed and dp[i][j] = dp[i - 1][j - 1]. Well, what if they are not equal?

If they are not equal, we need to consider three cases:

Replace word1[i - 1] by word2[j - 1] (dp[i][j] = dp[i - 1][j - 1] + 1 (for replacement));
Delete word1[i - 1] and word1[0..i - 2] = word2[0..j - 1] (dp[i][j] = dp[i - 1][j] + 1 (for deletion));
Insert word2[j - 1] to word1[0..i - 1] and word1[0..i - 1] + word2[j - 1] = word2[0..j - 1] (dp[i][j]
= dp[i][j - 1] + 1 (for insertion)).
Make sure you understand the subtle differences between the equations for deletion and insertion.
For deletion, we are actually converting word1[0..i - 2] to word2[0..j - 1], which costs dp[i - 1][j],
and then deleting the word1[i - 1], which costs 1. The case is similar for insertion.

Putting these together, we now have:

dp[i][0] = i;
dp[0][j] = j;
dp[i][j] = dp[i - 1][j - 1], if word1[i - 1] = word2[j - 1];
dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1), otherwise.
The above state equations can be turned into the following code directly.

Let following be the function definition :-

f(i, j) := minimum cost (or steps) required to convert first i characters of word1 to first j characters of word2

Case 1: word1[i] == word2[j], i.e. the ith the jth character matches.

f(i, j) = f(i - 1, j - 1)
Case 2: word1[i] != word2[j], then we must either insert, delete or replace, whichever is cheaper

f(i, j) = 1 + min { f(i, j - 1), f(i - 1, j), f(i - 1, j - 1) }
f(i, j - 1) represents insert operation
f(i - 1, j) represents delete operation
f(i - 1, j - 1) represents replace operation
Here, we consider any operation from word1 to word2. It means, when we say insert operation,
we insert a new character after word1 that matches the jth character of word2.
So, now have to match i characters of word1 to j - 1 characters of word2.
Same goes for other 2 operations as well.

Note that the problem is symmetric. The insert operation in one direction (i.e. from word1 to word2)
is same as delete operation in other. So, we could choose any direction.

Above equations become the recursive definitions for DP.

Base Case:

f(0, k) = f(k, 0) = k
Below is the direct bottom-up translation of this recurrent relation.
t is only important to take care of 0-based index with actual code :-

#83.70% 11ms
public class Solution {
    public int minDistance(String word1, String word2) {
        int len1 = word1.length();
        int len2 = word2.length();
        int[][] dp = new int[2][len2 + 1];
        for (int j = 1; j <= len2; j++) {
            dp[0][j] = j;
        }
        int row = 1;
        for (int i = 1; i <= len1; i++) {
            char c1 = word1.charAt(i - 1);
            dp[row][0] = i;
            for (int j = 1; j <= len2; j++) {
                if (c1 == word2.charAt(j - 1)) {
                    dp[row][j] = dp[1 - row][j - 1];
                } else {
                    dp[row][j] = Math.min(Math.min(dp[1 - row][j - 1], dp[1 - row][j]), dp[row][j - 1]) + 1;
                }
            }
            row = 1 - row;
        }
        return dp[len1 & 1][len2];
    }
}

#29.67% 16ms
public class Solution {
    public int minDistance(String word1, String word2) {
        int len1 = word1.length();
        int len2 = word2.length();
        if(word1 == null) return len2;
        if(word2 == null) return len1;

        int[][] dp = new int[len1+1][len2+1];

        for(int j = 0; j <= len2; j++){
            dp[0][j] = j;
        }
        for(int i = 1; i <= len1 ; i++){
            dp[i][0] = i;
            for(int j = 1; j <= len2; j++){
                if(word1.charAt(i - 1) == word2.charAt(j-1)){
                    dp[i][j] = dp[i-1][j-1];
                }else{
                    dp[i][j] = Math.min(dp[i-1][j],  Math.min(dp[i-1][j-1], dp[i][j-1])) + 1;
                }
            }
        }
        return dp[len1][len2];
    }
}

Initalizalization:
D(i,0) = i
D(0,j) = j

 Recurrence Relation:
For each i = 1 ...M
    For each j = 1...N

                D(i-1,j) + 1
 D(i,j)= min    D(i,j-1) + 1
                D(i-1,j-1) + 2: if X(i) != Y(j)
                             0; if X(i) == Y(j)
Terminaiton: D(N,M) is distance

#4.57% 21ms
public class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();

        int[][] dp = new int[m+1][n+1];
        for (int i = 0 ; i <= m; i++) {
            dp[i][0] = i;
        }
        for (int j = 1; j <= n; j++) {
            dp[0][j] = j;
        }

        for (int i = 0; i < m ; i++) {
            for (int j = 0; j < n; j++) {
                if (word1.charAt(i) == word2.charAt(j)) {
                    dp[i+1][j+1] = dp[i][j];
                } else {
                    int a = dp[i][j];
                    int b = dp[i][j+1];
                    int c = dp[i + 1][j];
                    dp[i+1][j+1] = a < b ? (a < c ? a : c) : (b < c ? b : c);
                    dp[i+1][j+1]++;
                }
            }
        }
        return dp[m][n];
    }
}

# dfs
#99.21% 7ms
public class Solution {
    private String word1;
    private String word2;
    private Integer[][] cache;

    public int minDistance(String word1, String word2) {
        if (word1.isEmpty()) {
            return word2.length();
        }
        if (word2.isEmpty()) {
            return word1.length();
        }
        this.word1 = word1;
        this.word2 = word2;
        cache = new Integer[word1.length()][word2.length()];
        return 1 + dfs(word1.length() - 1, word2.length() - 1);
    }

    private int dfs(int m, int n) {
        if (m < 0) {
            return n;
        }
        if (n < 0) {
            return m;
        }
        if (cache[m][n] != null) {
            return cache[m][n];
        }
        int dist = 0;
        if (word1.charAt(m) == word2.charAt(n)) {
            dist = dfs(m - 1, n - 1);
        } else {
            dist = 1 + min(dfs(m, n - 1), dfs(m - 1, n), dfs(m - 1, n - 1));
        }
        cache[m][n] = dist;
        return dist;
    }

    private int min(int a, int b, int c) {
        return Math.min(Math.min(a, b), c);
    }
}
'''