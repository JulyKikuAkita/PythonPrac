__source__ = 'https://leetcode.com/problems/task-scheduler/#/description'
# Time:  O(N)
# Space: O(26)
#
# Description:
# Given a char array representing tasks CPU need to do.
# It contains capital letters A to Z where different letters represent different tasks.
# Tasks could be done without original order. Each task could be done in one interval.
# For each interval, CPU could finish one task or just be idle.
#
# However, there is a non-negative cooling interval n that means between two same tasks,
# there must be at least n intervals that CPU are doing different tasks or just be idle.
#
# You need to return the least number of intervals the CPU will take to finish all the given tasks.
#
# Example 1:
# Input: tasks = ['A','A','A','B','B','B'], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
#
# The number of tasks is in the range [1, 10000].
# Hide Company Tags Facebook
# Hide Tags Array Greedy Queue
# Hide Similar Problems (H) Rearrange String k Distance Apart
#
import unittest


class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/task-scheduler/
First consider the most frequent characters,
we can determine their positions first and use them as a frame to insert the remaining less frequent characters.
This is proof by construction:

Let F be the set of most frequent chars with frequency k.
Then we can create k chunks, each chunk is identical and is a string consists of chars in F in a specific fixed order.
Let the heads of these chunks to be H_i, then H_2 should be at least n chars away from H_1, and so on so forth;
then we insert the less frequent chars into the gaps between these chunks sequentially one by one ordered
by frequency in a decreasing order and try to fill the k-1 gaps full each time.

Examples:
AACCCBEEE 2

3 identical chunks "CE", "CE CE CE" <-- this is a frame
insert 'A' among the gaps of chunks since it has higher frequency than 'B' ---> "CEACEACE"
insert 'B' ---> "CEABCEACE" <----- result is tasks.length;
AACCCDDEEE 3

3 identical chunks "CE", "CE CE CE" <--- this is a frame.
Begin to insert 'A'->"CEA CEA CE"
Begin to insert 'B'->"CEABCEABCE" <---- result is tasks.length;
ACCCEEE 2

3 identical chunks "CE", "CE CE CE" <-- this is a frame
Begin to insert 'A' --> "CEACE CE" <-- result is (c[25] - 1) * (n + 1) + 25 -i = 2 * 3 + 2 = 8

public class Solution {
    public int leastInterval(char[] tasks, int n) {

        if(tasks.length == 0) return 0;
        if(n == 0) return tasks.length;

        int[] c = new int[26];
        for(char t : tasks){
            c[t - 'A']++;
        }
        Arrays.sort(c);
        int i = 25;
        while(i >= 0 && c[i] == c[25]) i--;

        return Math.max(tasks.length, (c[25] - 1) * (n + 1) + 25 - i);
    }
}
'''