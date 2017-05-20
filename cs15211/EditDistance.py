__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/edit-distance.py
# Time:  O(n * m)
# Space: O(n + m)
# DP
# ?
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
'''
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

# http://www.programcreek.com/2013/12/edit-distance-in-java/
class SolutionJava:
    # @return an integer
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)

        #  len1+1, len2+1, because finally return dp[len1][len2]
        dp = [[0 for j in xrange(n+1)] for i in xrange(m+1) ]

        for i in xrange(m+1):
            dp[i][0]= i

        for j in range(n+1):
            dp[0][j]=j

        # 	//iterate though, and check last char

        for i in xrange(m):
            c1 = word1[i]
            for j in xrange(n):
                c2 = word2[j]
                if c1 == c2:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    replace = dp[i][j] + 1
                    insert = dp[i][j+1] + 1
                    delete = dp[i+1][j] + 1
                    dp[i+1][j+1] = min(insert,delete,replace)

        return dp[m][n]


#test case
test = SolutionOther()
print "start testing"
#print test.minDistance("Rabbit", "Rabket")
#print test.minDistance("a", "b")
#print test.minDistance("abc", "b")


if __name__ == "__main__":
    print Solution().minDistance("Rabbit", "Racket")
    print SolutionJava().minDistance("Rabbit", "Racket")
    #print Solution2().minDistance("Rabbit", "Rabket")
    #print Solution().minDistance("Rabbit", "Rabbitt")

#java
js = '''
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
'''