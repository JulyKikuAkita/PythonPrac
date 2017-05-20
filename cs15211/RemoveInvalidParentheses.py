__author__ = 'July'
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
#  Facebook
#  Depth-first Search Breadth-first Search


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

#java
js = '''
public class Solution {
    public List<String> removeInvalidParentheses(String s) {
        List<String> res = new ArrayList<String>();
        dfs(res, s, 0, "", 0, 0);
        return res;
    }

    private void dfs(List<String> res, String input, int idx, String str, int cnt, int ttl){
        if(idx == input.length() && cnt == 0){
            if(res.size() == 0){
                res.add(str);
            }else if(str.length() == res.get(0).length() && !res.contains(str)){
                res.add(str);
            }
            return;
        }
        if(idx >= input.length()) return;

        char cur = input.charAt(idx);
        if(cur != '(' && cur != ')'){
            dfs(res, input, idx + 1, str + cur, cnt, ttl);
        }else if(cur == '('){
            dfs(res, input, idx + 1, str + "(", cnt + 1, ttl + 1);
            dfs(res, input, idx + 1, str, cnt, ttl);
        }else{
            if(cnt > 0)
                dfs(res, input, idx + 1, str + ')', cnt - 1, ttl);

            dfs(res, input, idx + 1, str, cnt, ttl);
        }

    }
}


public class Solution {
    public List<String> removeInvalidParentheses(String s) {
        Set<String> result = new HashSet<String>();
        LinkedHashSet<String> queue = new LinkedHashSet<String>();
        int len = -1;
        queue.add(s);
        while (!queue.isEmpty()) {
            String curr = queue.iterator().next();
            queue.remove(curr);
            if (len > 0 && len != curr.length()) {
                break;
            }
            if (isValid(curr)) {
                if (len == -1) {
                    len = curr.length();
                    result.add(curr);
                } else if (len == curr.length()) {
                    result.add(curr);
                }
            } else if (len == -1) {
                for (int i = 0; i < curr.length(); i++) {
                    queue.add(curr.substring(0, i) + curr.substring(i + 1, curr.length()));
                }
            }
        }
        return new ArrayList<String>(result);
    }

    private boolean isValid(String s) {
        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                count++;
            } else if (c == ')') {
                if (count <= 0) {
                    return false;
                }
                count--;
            }
        }
        return count == 0;
    }
}
'''