__source__ = 'https://leetcode.com/problems/dota2-senate/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 649. Dota2 Senate
#
# In the world of Dota2, there are two parties: the Radiant and the Dire.
#
# The Dota2 senate consists of senators coming from two parties.
# Now the senate wants to make a decision about a change in the Dota2 game.
# The voting for this change is a round-based procedure.
# In each round, each senator can exercise one of the two rights:
#
# Ban one senator's right:
# A senator can make another senator lose all his rights in this and all the following rounds.
# Announce the victory:
# If this senator found the senators who still have rights to vote are all from the same party,
# he can announce the victory and make the decision about the change in the game.
# Given a string representing each senator's party belonging.
# The character 'R' and 'D' represent the Radiant party and the Dire party respectively.
# Then if there are n senators, the size of the given string will be n.
#
# The round-based procedure starts from the first senator to the last senator in the given order.
# This procedure will last until the end of voting.
# All the senators who have lost their rights will be skipped during the procedure.
#
# Suppose every senator is smart enough and will play the best strategy for his own party,
# you need to predict which party will finally announce the victory and make the change in the Dota2 game.
# The output should be Radiant or Dire.
#
# Example 1:
# Input: "RD"
# Output: "Radiant"
# Explanation: The first senator comes from Radiant and he can just ban the next senator's right in the round 1.
# And the second senator can't exercise any rights any more since his right has been banned.
# And in the round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
# Example 2:
# Input: "RDD"
# Output: "Dire"
# Explanation:
# The first senator comes from Radiant and he can just ban the next senator's right in the round 1.
# And the second senator can't exercise any rights anymore since his right has been banned.
# And the third senator comes from Dire and he can ban the first senator's right in the round 1.
# And in the round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
# Note:
# The length of the given string will in the range [1, 10,000].

# Companies
# Valve
# Related Topics
# Greedy
# Similar Questions
# Teemo Attacking
#
import unittest
import collections
# 145ms
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        A = collections.deque()
        people = [0, 0]
        bans = [0, 0]

        for person in senate:
            x = person == 'R'
            people[x] += 1
            A.append(x)

        while all(people):
            x = A.popleft()
            people[x] -= 1
            if bans[x]:
                bans[x] -= 1
            else:
                bans[x^1] += 1
                A.append(x)
                people[x] += 1

        return "Radiant" if people[1] else "Dire"

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
This is obliviously a greedy algorithm problem.
Each senate R must ban its next closest senate D who is from another party,
or else D will ban its next senate from R's party.

The idea is to use two queues to save the index of each senate from R's and D's parties,
respectively. During each round, we delete the banned senate's index;
and plus the remainning senate's index with n(the length of the input string senate),
then move it to the back of its respective queue.

#65.48% 26ms
public class Solution {
    public String predictPartyVictory(String senate) {
        Queue<Integer> q1 = new LinkedList<Integer>(), q2 = new LinkedList<Integer>();
        int n = senate.length();
        for(int i = 0; i < n; i++){
            if ( senate.charAt(i) == 'R' ) q1.add(i);
            else q2.add(i);
        }
        while ( !q1.isEmpty() && !q2.isEmpty() ){
            int r_index = q1.poll(), d_index = q2.poll();
            if (r_index < d_index) q1.add( r_index + n );
            else q2.add( d_index + n );
        }
        return ( q1.size() > q2.size() ) ? "Radiant" : "Dire";
    }
}

#97.46% 13ms
public class Solution {
    final char BAN = 'B';
    int radiant = 0, dire = 0;
    public String predictPartyVictory(String senate) {
        int len = senate.length();
        char[] arr = senate.toCharArray();
        int banCount = 0;
        for (int i = 0; i < len; i++) {
            switch (arr[i]) {
                case BAN:
                    banCount++;
                    break;
                case 'R':
                    if (dire > 0) {
                        dire--;
                        arr[i] = BAN;
                        banCount++;
                    } else {
                        radiant++;
                    }
                    break;
                case 'D':
                    if (radiant > 0) {
                        radiant--;
                        arr[i] = BAN;
                        banCount++;
                    } else {
                        dire++;
                    }
                    break;
            }
        }
        if (banCount + radiant >= len || banCount + dire >= len) {
            if (radiant > 0) return "Radiant";
            if (dire > 0) return "Dire";
        }
        return predictPartyVictory(new String(arr));
    }
}
'''