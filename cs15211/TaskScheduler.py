__source__ = 'https://leetcode.com/problems/task-scheduler/#/description'
# Time:  O(N)
# Space: O(26)
#
# Description: Leetcode # 621. Task Scheduler
#
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
#
# Companies
# Facebook
# Related Topics
# Array Greedy Queue
# Similar Questions
# Rearrange String k Distance Apart
#
import collections
import unittest
# 132ms 76.89%
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_counts = collections.Counter(tasks).values()
        M = max(task_counts)
        Mct = task_counts.count(M)
        return max(len(tasks), (M - 1) * (n + 1) + Mct)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/articles/task-scheduler/

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

# 5ms 98.40%
class Solution {
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

The idea used here is similar to - https://leetcode.com/problems/rearrange-string-k-distance-apart
We need to arrange the characters in string such that each same character is K distance apart,
where distance in this problems is time b/w two similar task execution.

Idea is to add them to a priority Q and sort based on the highest frequency.
And pick the task in each round of 'n' with highest frequency. As you pick the task, decrease the frequency,
and put them back after the round.

# 103ms 15.03%
class Solution {
    public int leastInterval(char[] tasks, int n) {
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < tasks.length; i++) {
            map.put(tasks[i], map.getOrDefault(tasks[i], 0) + 1);
        }

        PriorityQueue<Map.Entry<Character, Integer>> q = new PriorityQueue<>(
            (a, b) -> a.getValue() != b.getValue() ? b.getValue() - a.getValue() : a.getKey() - b.getKey());

        q.addAll(map.entrySet());

        int count = 0;
        while (!q.isEmpty()) {
            int k = n + 1;
            List<Map.Entry> tmpList = new ArrayList<>();
            while (k > 0 && !q.isEmpty()) {
                Map.Entry<Character, Integer> top = q.poll(); // most frequency task
                top.setValue(top.getValue() - 1);  // decrease frequency, meaning it got executed
                tmpList.add(top); // collect task to add back to queue
                k--;
                count++;  //successfully executed task
            }

            for (Map.Entry<Character, Integer> e : tmpList) {
                if (e.getValue() > 0) q.add(e);  // add valid tasks
            }

            if (q.isEmpty()) break;
            count = count + k;  // if k > 0, then it means we need to be idle
        }
        return count;
    }
}

# 4ms 100%
class Solution {
    public int leastInterval(char[] tasks, int n) {
        if(n == 0) {
            return tasks.length;
        }
        int[] arr = new int[26];
        for(int i=0; i<tasks.length; i++) {
            arr[tasks[i] - 'A']++;
        }
        int max = Integer.MIN_VALUE;
        int freq = 0;

        for(int i=0; i<arr.length; i++) {
            if(arr[i] > max) {
                freq = 1;
                max = arr[i];
            } else if (arr[i] == max) {
                freq++;
            }
        }

        int len = max + freq - 1 + ((max - 1) * n);
        return Math.max(tasks.length, len);
    }
}
'''