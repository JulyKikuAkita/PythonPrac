__source__ = 'https://leetcode.com/problems/keys-and-rooms/'
# Time:  O(N + E), where NN is the number of rooms, and EE is the total number of keys.
# Space: O(N)
#
# Description: Leetcode # 841. Keys and Rooms
#
# There are N rooms and you start in room 0.
# Each room has a distinct number in 0, 1, 2, ..., N-1,
# and each room may have some keys to access the next room.
#
# Formally, each room i has a list of keys rooms[i],
# and each key rooms[i][j] is an integer in [0, 1, ..., N-1]
# where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.
#
# Initially, all the rooms start locked (except for room 0).
#
# You can walk back and forth between rooms freely.
#
# Return true if and only if you can enter every room.
#
# Example 1:
#
# Input: [[1],[2],[3],[]]
# Output: true
# Explanation:
# We start in room 0, and pick up key 1.
# We then go to room 1, and pick up key 2.
# We then go to room 2, and pick up key 3.
# We then go to room 3.  Since we were able to go to every room, we return true.
# Example 2:
#
# Input: [[1,3],[3,0,1],[2],[0]]
# Output: false
# Explanation: We can't enter the room with number 2.
# Note:
#
# 1 <= rooms.length <= 1000
# 0 <= rooms[i].length <= 1000
# The number of keys in all rooms combined is at most 3000.
#
import unittest

# 36ms 32.52%
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]
        #At the beginning, we have a todo list "stack" of keys to use.
        #'seen' represents at some point we have entered this room.
        while stack:  #While we have keys...
            node = stack.pop() # get the next key 'node'
            for nei in rooms[node]: # For every key in room # 'node'...
                if not seen[nei]: # ... that hasn't been used yet
                    seen[nei] = True # mark that we've entered the room
                    stack.append(nei) # add the key to the todo list
        return all(seen) # Return true iff we've visited every room

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/keys-and-rooms/solution/
Approach #1: Depth-First Search [Accepted]
Complexity Analysis
Time Complexity: O(N + E), where N is the number of rooms, and E is the total number of keys.
Space Complexity: O(N) in additional space complexity, to store stack and seen.

# 5ms 81.78%
class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        boolean[] seen = new boolean[rooms.size()];
        seen[0] = true;
        Stack<Integer> stack = new Stack();
        stack.push(0);

        //At the beginning, we have a todo list "stack" of keys to use.
        //'seen' represents at some point we have entered this room.
        while (!stack.isEmpty()) { // While we have keys...
            int node = stack.pop(); // Get the next key 'node'
            for (int nei: rooms.get(node)) // For every key in room # 'node'...
                if (!seen[nei]) { // ...that hasn't been used yet
                    seen[nei] = true; // mark that we've entered the room
                    stack.push(nei); // add the key to the todo list
                }
        }

        for (boolean v: seen)  // if any room hasn't been visited, return false
            if (!v) return false;
        return true;
    }
}

# https://leetcode.com/problems/keys-and-rooms/discuss/133855/Straight-Forward
# DFS with stack + HashSet
# 9ms 13.73%
class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        Set<Integer> set = new HashSet();
        Stack<Integer> stack = new Stack();
        stack.add(0);
        set.add(0);
        while (!stack.isEmpty()) {
            int key = stack.pop();
            for (int other : rooms.get(key)) {
                if (!set.contains(other)) {
                    stack.push(other);
                    set.add(other);
                }
            }
        }
        return set.size() == rooms.size();
    }

    private void addKey(int room, List<List<Integer>> rooms, Set<Integer> visited) {
        visited.add(room);
        for (int key : rooms.get(room)) {
            if (!visited.contains(key)) addKey(key, rooms, visited);
        }
    }
}

# HashSet
# 6ms 49.80%
class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        Set<Integer> visited = new HashSet<>();
        addKey(0, rooms, visited);
        return visited.size() == rooms.size();
    }

    private void addKey(int room, List<List<Integer>> rooms, Set<Integer> visited) {
        visited.add(room);
        for (int key : rooms.get(room)) {
            if (!visited.contains(key)) addKey(key, rooms, visited);
        }
    }
}
'''
