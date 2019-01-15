__source__ = 'https://leetcode.com/problems/stamping-the-sequence/'
# Time:  O(N(N-M)
# Space: O(N(N-M)
#
# Description: Leetcode # 936. Stamping The Sequence
#
# You want to form a target string of lowercase letters.
#
# At the beginning, your sequence is target.length '?' marks.
# You also have a stamp of lowercase letters.
#
# On each turn, you may place the stamp over the sequence,
# and replace every letter in the sequence with the corresponding letter from the stamp.
# You can make up to 10 * target.length turns.
#
# For example, if the initial sequence is "?????", and your stamp is "abc",
# then you may make "abc??", "?abc?", "??abc" in the first turn.
# (Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.)
#
# If the sequence is possible to stamp,
# then return an array of the index of the left-most letter being stamped at each turn.
# If the sequence is not possible to stamp, return an empty array.
#
# For example, if the sequence is "ababc", and the stamp is "abc",
# then we could return the answer [0, 2], corresponding to the moves "?????" -> "abc??" -> "ababc".
#
# Also, if the sequence is possible to stamp,
# it is guaranteed it is possible to stamp within 10 * target.length moves.
# Any answers specifying more than this number of moves will not be accepted.
#
# Example 1:
#
# Input: stamp = "abc", target = "ababc"
# Output: [0,2]
# ([1,0,2] would also be accepted as an answer, as well as some other answers.)
#
# Example 2:
#
# Input: stamp = "abca", target = "aabcaca"
# Output: [3,0,1]
#
# Note:
#
#     1 <= stamp.length <= target.length <= 1000
#     stamp and target only contain lowercase letters
#
import unittest
import collections
# 300ms 57.84%
class Solution(object):
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        M, N = len(stamp), len(target)

        queue = collections.deque()
        done = [False] * N
        ans = []
        A = []
        for i in xrange(N - M + 1):
            # For each window [i, i+M),
            # A[i] will contain info on what needs to change
            # before we can reverse stamp at i.

            made, todo = set(), set()
            for j, c in enumerate(stamp):
                a = target[i+j]
                if a == c:
                    made.add(i+j)
                else:
                    todo.add(i+j)
            A.append((made, todo))

            # If we can reverse stamp at i immediately,
            # enqueue letters from this window.
            if not todo:
                ans.append(i)
                for j in xrange(i, i + len(stamp)):
                    if not done[j]:
                        queue.append(j)
                        done[j] = True

        # For each enqueued letter,
        while queue:
            i = queue.popleft()

            # For each window that is potentially affected,
            # j: start of window
            for j in xrange(max(0, i-M+1), min(N-M, i)+1):
                if i in A[j][1]:  # This window is affected
                    A[j][1].discard(i) # Remove it from todo list of this window
                    if not A[j][1]:  # Todo list of this window is empty
                        ans.append(j)
                        for m in A[j][0]: # For each letter to potentially enqueue,
                            if not done[m]:
                                queue.append(m)
                                done[m] = True

        return ans[::-1] if all(done) else []

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/stamping-the-sequence/solution/
#
Approach 1: Work Backwards
Complexity Analysis
Time Complexity: O(N(N-M), where M,N are the lengths of stamp, target.
Space Complexity: O(N(N-M).

# 124ms 21.41%
class Solution {
    public int[] movesToStamp(String stamp, String target) {
        int M = stamp.length(), N = target.length();
        Queue<Integer> queue = new ArrayDeque();
        boolean[] done = new boolean[N];
        Stack<Integer> ans = new Stack();
        List<Node> A = new ArrayList();

        for (int i = 0; i <= N-M; ++i) {
            // For each window [i, i+M), A[i] will contain
            // info on what needs to change before we can
            // reverse stamp at this window.

            Set<Integer> made = new HashSet();
            Set<Integer> todo = new HashSet();
            for (int j = 0; j < M; ++j) {
                if (target.charAt(i+j) == stamp.charAt(j))
                    made.add(i+j);
                else
                    todo.add(i+j);
            }

            A.add(new Node(made, todo));

            // If we can reverse stamp at i immediately,
            // enqueue letters from this window.
            if (todo.isEmpty()) {
                ans.push(i);
                for (int j = i; j < i + M; ++j) if (!done[j]) {
                    queue.add(j);
                    done[j] = true;
                }
            }
        }

        // For each enqueued letter (position),
        while (!queue.isEmpty()) {
            int i = queue.poll();

            // For each window that is potentially affected,
            // j: start of window
            for (int j = Math.max(0, i-M+1); j <= Math.min(N-M, i); ++j) {
                if (A.get(j).todo.contains(i)) {  // This window is affected
                    A.get(j).todo.remove(i);
                    if (A.get(j).todo.isEmpty()) {
                        ans.push(j);
                        for (int m: A.get(j).made) if (!done[m]) {
                            queue.add(m);
                            done[m] = true;
                        }
                    }
                }
            }
        }

        for (boolean b: done)
            if (!b) return new int[0];

        int[] ret = new int[ans.size()];
        int t = 0;
        while (!ans.isEmpty())
            ret[t++] = ans.pop();

        return ret;
    }
}

class Node {
    Set<Integer> made, todo;
    Node(Set<Integer> m, Set<Integer> t) {
        made = m;
        todo = t;
    }
}

# 19ms 87.16%
class Solution {
    public int[] movesToStamp(String stamp, String target) {
        char[] S = stamp.toCharArray();
        char[] T = target.toCharArray();
        List<Integer> res = new ArrayList<>();
        boolean[] visited = new boolean[T.length];
        int stars = 0;
        
        while (stars < T.length) {
            boolean doneReplace = false;
            for (int i = 0; i <= T.length - S.length; i++) {
                if (!visited[i] && canReplace(T, i, S)) {
                    stars = doReplace(T, i, S.length, stars);
                    doneReplace = true;
                    visited[i] = true;
                    res.add(i);
                    if (stars == T.length) break;
                }
            }
            if (!doneReplace) return new int[0];
        }
        
        int[] resArray = new int[res.size()];
        for (int i = 0; i < res.size(); i++) {
            resArray[i] = res.get(res.size() - i - 1);
        }
        return resArray;
    }
    
    private boolean canReplace(char[] T, int p, char[] S) {
        for (int i = 0; i < S.length; i++) {
            if (T[i + p] != '*' && T[i + p] != S[i]) return false;
        }
        return true;
    }
    
    private int doReplace(char[] T, int p, int len, int count) {
        for (int i = 0; i < len; i++) {
            if (T[i + p] != '*') {
                T[i + p] = '*';
                count++;
            }
        }
        return count;
    }
}
'''
