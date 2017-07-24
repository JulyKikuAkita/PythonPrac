__source__ = 'https://leetcode.com/problems/remove-invalid-parentheses/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/remove-invalid-parentheses.py
# Time:  O(C(n, c)), try out all possible substrings with the minimum c deletion.
# Space: O(c), the depth is at most c, and it costs n at each depth
#
# Remove the minimum number of invalid parentheses in order to
# make the input string valid. Return all possible results.
#
# Note: The input string may contain letters other than the
# parentheses ( and ).
#
# Examples:
# "()())()" -> ["()()()", "(())()"]
# "(a)())()" -> ["(a)()()", "(a())()"]
# ")(" -> [""]
#
# Companies
# Facebook
# Related Topics
# Depth-first Search Breadth-first Search
# Similar Questions
# Valid Parentheses
#

# DFS solution.
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(res, s, 0, 0, "")
        return res

    def dfs(self, res, s, idx, cnt, tmp):
        if idx == len(s) and  cnt == 0:
            if not res:
                res.append(tmp)
            elif len(tmp) == len(res[0]) and tmp not in res:
                res.append(tmp)

        if idx >= len(s):
            return

        cur = s[idx]
        if cur != '(' and cur !=')':
            self.dfs(res, s, idx + 1, cnt, tmp + cur)
        elif cur == '(':
            self.dfs(res, s, idx + 1, cnt + 1, tmp + cur)
            self.dfs(res, s, idx + 1, cnt, tmp)
        else:
            if cnt > 0:
                self.dfs(res, s, idx + 1, cnt -1, tmp +cur)
            self.dfs(res, s, idx + 1, cnt, tmp)


class Solution2(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # Calculate the minimum left and right parantheses to remove
        def findMinRemove(s):
            left_removed, right_removed = 0, 0
            for c in s:
                if c == '(':
                    left_removed += 1
                elif c == ')':
                    if not left_removed:
                        right_removed += 1
                    else:
                        left_removed -= 1
            return (left_removed, right_removed)

        # Check whether s is valid or not.
        def isValid(s):
            sum = 0
            for c in s:
                if c == '(':
                    sum += 1
                elif c == ')':
                    sum -= 1
                if sum < 0:
                    return False
            return sum == 0

        def removeInvalidParenthesesHelper(start, left_removed, right_removed):
            if left_removed == 0 and right_removed == 0:
                tmp = ""
                for i, c in enumerate(s):
                    if i not in removed:
                        tmp += c
                if isValid(tmp):
                    res.append(tmp)
                return

            for i in xrange(start, len(s)):
                if right_removed == 0 and left_removed > 0 and s[i] == '(':
                    if i == start or s[i] != s[i - 1]:  # Skip duplicated.
                        removed[i] = True
                        removeInvalidParenthesesHelper(i + 1, left_removed - 1, right_removed)
                        del removed[i]
                elif right_removed > 0 and s[i] == ')':
                    if i == start or s[i] != s[i - 1]:  # Skip duplicated.
                        removed[i] = True
                        removeInvalidParenthesesHelper(i + 1, left_removed, right_removed - 1);
                        del removed[i]

        res, removed = [], {}
        (left_removed, right_removed) = findMinRemove(s)
        removeInvalidParenthesesHelper(0, left_removed, right_removed)
        return res

#Java
Java = '''
Thought :
Key Points:

Generate unique answer once and only once, do not rely on Set.
Do not need preprocess.
Runtime 3 ms.
Explanation:
We all know how to check a string of parentheses is valid using a stack. Or even simpler use a counter.
The counter will increase when it is '(' and decrease when it is ')'.
Whenever the counter is negative, we have more ')' than '(' in the prefix.

To make the prefix valid, we need to remove a ')'. The problem is: which one? The answer is any one in the prefix.
However, if we remove any one, we will generate duplicate results, for example: s = ()),
we can remove s[1] or s[2] but the result is the same ().
Thus, we restrict ourself to remove the first ) in a series of concecutive )s.

After the removal, the prefix is then valid. We then call the function recursively to solve the rest of the string.
However, we need to keep another information: the last removal position. If we do not have this position,
we will generate duplicate by removing two ')' in two steps only with a different order.

For this, we keep tracking the last removal position and only remove ')' after that.

Now one may ask. What about '('?  What if s = '(()(()' in which we need remove '('
The answer is: do the same from right to left.
However a cleverer idea is: reverse the string and reuse the code!
Here is the final implement in Java.

#70.83% 3ms
public class Solution {
    public List<String> removeInvalidParentheses(String s) {
    List<String> ans = new ArrayList<>();
    remove(s, ans, 0, 0, new char[]{'(', ')'});
    return ans;
    }

    public void remove(String s, List<String> ans, int last_i, int last_j,  char[] par) {
        for (int stack = 0, i = last_i; i < s.length(); ++i) {
            if (s.charAt(i) == par[0]) stack++;
            if (s.charAt(i) == par[1]) stack--;
            if (stack >= 0) continue;
            for (int j = last_j; j <= i; ++j)
                if (s.charAt(j) == par[1] && (j == last_j || s.charAt(j - 1) != par[1]))
                    remove(s.substring(0, j) + s.substring(j + 1, s.length()), ans, i, j, par);
            return;
        }
        String reversed = new StringBuilder(s).reverse().toString();
        if (par[0] == '(') // finished left to right
            remove(reversed, ans, 0, 0, new char[]{')', '('});
        else // finished right to left
            ans.add(reversed);
    }
}

#BFS
# 31.93% 100ms
The idea is straightforward, with the input string s, we generate all possible states by removing one ( or ), c
heck if they are valid, if found valid ones on the current level, put them to the final result list and we are done,
otherwise, add them to a queue and carry on to the next level.

The good thing of using BFS is that we can guarantee the number of parentheses that need to be removed is minimal, a
lso no recursion call is needed in BFS.

Time complexity:

In BFS we handle the states level by level, in the worst case, we need to handle all the levels,
we can analyze the time complexity level by level and add them up to get the final complexity.

On the first level, there's only one string which is the input string s, let's say the length of it is n,
to check whether it's valid, we need O(n) time. On the second level, we remove one ( or ) from the first level,
so there are C(n, n-1) new strings, each of them has n-1 characters, and for each string,
we need to check whether it's valid or not, thus the total time complexity on this level is (n-1) x C(n, n-1).
Come to the third level, total time complexity is (n-2) x C(n, n-2), so on and so forth...

Finally we have this formula:

T(n) = n x C(n, n) + (n-1) x C(n, n-1) + ... + 1 x C(n, 1) = n x 2^(n-1).

public class Solution {
    public List<String> removeInvalidParentheses(String s) {
      List<String> res = new ArrayList<>();

      // sanity check
      if (s == null) return res;

      Set<String> visited = new HashSet<>();
      Queue<String> queue = new LinkedList<>();

      // initialize
      queue.add(s);
      visited.add(s);

      boolean found = false;

      while (!queue.isEmpty()) {
        s = queue.poll();

        if (isValid(s)) {
          // found an answer, add to the result
          res.add(s);
          found = true;
        }

        if (found) continue;

        // generate all possible states
        for (int i = 0; i < s.length(); i++) {
          // we only try to remove left or right paren
          if (s.charAt(i) != '(' && s.charAt(i) != ')') continue;

          String t = s.substring(0, i) + s.substring(i + 1);

          if (!visited.contains(t)) {
            // for each state, if it's not visited, add it to the queue
            queue.add(t);
            visited.add(t);
          }
        }
      }

      return res;
    }

    // helper function checks if string s contains valid parantheses
    boolean isValid(String s) {
      int count = 0;

      for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if (c == '(') count++;
        if (c == ')' && count-- == 0) return false;
      }

      return count == 0;
    }
}

# 94.69% 2ms
public class Solution {
    public List<String> removeInvalidParentheses(String s) {
        List<String> result = new ArrayList<>();
        int leftRemove = 0;
        int rightRemove = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                leftRemove++;
            } else if (c == ')') {
                if (leftRemove > 0) {
                    leftRemove--;
                } else {
                    rightRemove++;
                }
            }
        }
        remove(s, 0, result, new StringBuilder(), leftRemove, rightRemove, 0, false);
        return result;
    }

    private void remove(String s, int index, List<String> result, StringBuilder sb, int leftRemove, int rightRemove, int diff, boolean lastRemoved) {
        if (index == s.length()) {
            if (leftRemove == 0 && rightRemove == 0 && diff == 0) {
                result.add(sb.toString());
            }
            return;
        }
        char c = s.charAt(index);
        int len = sb.length();
        if (c == '(') {
            if (leftRemove > 0) {
                remove(s, index + 1, result, sb, leftRemove - 1, rightRemove, diff, true);
            }
            if (index == 0 || c != s.charAt(index - 1) || !lastRemoved) {
                sb.append(c);
                remove(s, index + 1, result, sb, leftRemove, rightRemove, diff + 1, false);
                sb.setLength(len);
            }
        } else if (c == ')') {
            if (rightRemove > 0) {
                remove(s, index + 1, result, sb, leftRemove, rightRemove - 1, diff, true);
            }
            if (diff > 0 && (index == 0 || c != s.charAt(index - 1) || !lastRemoved)) {
                sb.append(c);
                remove(s, index + 1, result, sb, leftRemove, rightRemove, diff - 1, false);
                sb.setLength(len);
            }
        } else {
            sb.append(c);
            remove(s, index + 1, result, sb, leftRemove, rightRemove, diff, lastRemoved);
            sb.setLength(len);
        }
    }
}
'''