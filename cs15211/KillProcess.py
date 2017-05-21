__source__ = 'https://leetcode.com/problems/kill-process/#/description'
# Time:  O(n)
# Space: O(n)
#
# Description:
# Given n processes, each process has a unique PID (process id) and its PPID (parent process id).
#
# Each process only has one parent process, but may have one or more children processes.
# This is just like a tree structure. Only one process has PPID that is 0,
# which means this process has no parent process. All the PIDs will be distinct positive integers.
#
# We use two list of integers to represent a list of processes,
# where the first list contains PID for each process and the second list contains the corresponding PPID.
#
# Now given the two lists, and a PID representing a process you want to kill,
# return a list of PIDs of processes that will be killed in the end.
# You should assume that when a process is killed, all its children processes will be killed.
# No order is required for the final answer.
#
# Example 1:
# Input:
# pid =  [1, 3, 10, 5]
# ppid = [3, 0, 5, 3]
# kill = 5
# Output: [5,10]
# Explanation:
#            3
#          /   \
#         1     5
#              /
#             10
# Kill 5 will also kill 10.
# Note:
# The given kill id is guaranteed to be one of the given PIDs.
# n >= 1.
# Hide Company Tags Bloomberg
# Hide Tags Tree Queue

import unittest
import collections
class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        d = collections.defaultdict(list)
        for c, p in zip(pid, ppid): d[p].append(c)
        bfs = [kill]
        for i in bfs: bfs.extend(d.get(i, []))
        return bfs
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/kill-process/
public class Solution {
    public List<Integer> killProcess(List<Integer> pid, List<Integer> ppid, int kill) {
        // Store process tree as an adjacency list
        Map<Integer, List<Integer>> adjacencyLists = new HashMap<>();
        for (int i = 0 ; i < ppid.size(); i++){
            adjacencyLists.putIfAbsent(ppid.get(i), new LinkedList<>());
            adjacencyLists.get(ppid.get(i)).add(pid.get(i));
        }

        // Kill all processes in the subtree rooted at process "kill"
        List<Integer> res = new LinkedList<>();
        Stack<Integer> stack = new Stack<>();
        stack.add(kill);
        while(!stack.isEmpty()) {
            int cur = stack.pop();
            res.add(cur);
            List<Integer> cProcessList = adjacencyLists.get(cur);
            if (cProcessList == null) continue;
            stack.addAll(cProcessList);
        }
        return res;
    }
}
'''