__source__ = 'https://leetcode.com/problems/open-the-lock/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 752. Open the Lock
#
# You have a lock in front of you with 4 circular wheels.
# Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'.
# The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'.
# Each move consists of turning one wheel one slot.
#
# The lock initially starts at '0000', a string representing the state of the 4 wheels.
#
# You are given a list of deadends dead ends, meaning if the lock displays any of these codes,
# the wheels of the lock will stop turning and you will be unable to open it.
#
# Given a target representing the value of the wheels that will unlock the lock,
# return the minimum total number of turns required to open the lock, or -1 if it is impossible.
#
# Example 1:
# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation:
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".
# Example 2:
# Input: deadends = ["8888"], target = "0009"
# Output: 1
# Explanation:
# We can turn the last wheel in reverse to move from "0000" -> "0009".
# Example 3:
# Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
# Output: -1
# Explanation:
# We can't reach the target without getting stuck.
# Example 4:
# Input: deadends = ["0000"], target = "8888"
# Output: -1
# Note:
# The length of deadends will be in the range [1, 500].
# target will not be in the list deadends.
# Every string in deadends and the string target will be a string of 4 digits
# from the 10,000 possibilities '0000' to '9999'.
#
import unittest
import collections
# 576ms 66.23%
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        def neighbors(node):
            for i in xrange(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i+1:]

        dead = set(deadends)
        queue = collections.deque([('0000', 0)])
        seen = {'0000'}
        while queue:
            node, depth = queue.popleft()
            if node == target: return depth
            if node in dead: continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/open-the-lock/solution/
Approach #1: Breadth-First Search [Accepted]
Complexity Analysis
Time Complexity: O(N^2*A^N+D) where A is the number of digits in our alphabet,
N is the number of digits in the lock,
and D is the size of deadends.
We might visit every lock combination,
plus we need to instantiate our set dead.
When we visit every lock combination,
we spend O(N^2) time enumerating through and constructing each node.
Space Complexity: O(A^N + D), for the queue and the set dead.

# 132ms 58.67%
class Solution {
    public int openLock(String[] deadends, String target) {
        Set<String> dead = new HashSet();
        for (String d: deadends) dead.add(d);

        Queue<String> queue = new LinkedList();
        queue.offer("0000");
        queue.offer(null);

        Set<String> seen = new HashSet();
        seen.add("0000");

        int depth = 0;
        while (!queue.isEmpty()) {
            String node = queue.poll();
            if (node == null) {
                depth++;
                if (queue.peek() != null) {
                    queue.offer(null);
                }
            } else if (node.equals(target)) {
                return depth;
            } else if (!dead.contains(node)){
                for (int i = 0; i < 4; i++) {
                    for (int d = -1; d <= 1; d += 2) {
                        int y = ((node.charAt(i) - '0') + d + 10) % 10;
                        String nei = node.substring(0, i) + ("" + y) + node.substring(i + 1);
                        if (!seen.contains(nei)) {
                            seen.add(nei);
                            queue.offer(nei);
                        }
                    }
                }
            }
        }
        return -1;
    }
}

# 36ms 95.36%
class Solution {
    private boolean[] visited = new boolean[10000];
    private Set<Integer> newSet = new HashSet<>();

    private class Pair {
        public int level;
        public int value;

        public Pair(int level, int value) {
            this.level = level;
            this.value = value;
        }
    }

    private void tryAdd(int next) {
        if (next < 10000 && !visited[next]) {
            newSet.add(next);
            visited[next] = true;
        }
    }

    private void getNextSet(int current) {
        int slot = 1;
        int num = current;
        //forward
        for (int i = 0; i < 4; i++) {
            int digit = num % 10;
            int newDigit = digit == 9 ? 0 : digit+ 1;
            int next = (num - digit + newDigit) * slot + current % slot;
            tryAdd(next);
            num /= 10;
            slot *= 10;
        }

        //reverse
        slot = 1;
        num = current;
        for (int i = 0; i < 4; i++) {
            int digit = num % 10;
            int newDigit = digit == 0 ? 9 : digit - 1;
            int next = (num - digit + newDigit) * slot + current % slot;
            tryAdd(next);
            num /= 10;
            slot *= 10;
        }
    }

    public int openLock(String[] deadends, String target) {
        int newTarget = Integer.parseInt(target);
        for (String d : deadends) {
            visited[Integer.parseInt(d)] = true;
        }

        int lock = 0;
        if (visited[lock])
            return -1; //corner case, if initial is in deadend
        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(0, lock));
        visited[0] = true;
        while (!q.isEmpty()) {
            Pair current = q.poll();
            getNextSet(current.value);
            if (newSet.contains(newTarget))
                return current.level + 1;
            for (int n : newSet) {
                q.add(new Pair(current.level + 1, n));
            }
            newSet.clear();
        }
        return -1;
    }
}
'''