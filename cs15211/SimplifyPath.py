__source__ = 'https://leetcode.com/problems/simplify-path/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/simplify-path.py
# Time:  O(n)
# Space: O(n)
# Stack
#
# Description: Leetcode # 217. Contains Duplicate
#
# Given an absolute path for a file (Unix-style), simplify it.
#
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# click to show corner cases.
#
# Corner Cases:
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".
#
# Companies
# Microsoft Facebook
# Related Topics
# Stack String
#
import unittest
# 66ms
class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        stack, tokens = [], path.split("/")
        for token in tokens:
            if token == ".." and stack: # if stack == nil, exception
                stack.pop()
            elif token != ".." and token != "." and token: # after split, "/c/" -> ["c",""]
                stack.append(token)
        return "/" + "/".join(stack)

# http://www.cnblogs.com/zuoyuan/p/3777289.html
class SolutionOther:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        stack = []
        i = 0
        res = ''
        while i < len(path):
            end = i + 1
            while end < len(path) and path[end] != "/":
                end += 1
            sub = path[i+1:end]
            if len(sub) > 0:
                if sub == "..":
                    if stack != []: stack.pop()
                elif sub != ".":
                    stack.append(sub)
            i = end

        if stack == []: return "/"
        for i in stack:
            res += "/" + i
        return res

    def simplifyPathWrongAns(self, path):
        path = path.split('/')
        curr = '/'
        for i in path:
            #print i, curr
            if i == '..':
                if curr != '/':
                    curr = '/'.join(curr.split('/')[:-1])
                    if curr == '': curr = '/'
            elif i != '.' and i != '':
                curr += '/' + i if curr != '/' else i
        return curr

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().simplifyPath("/../")
        print Solution().simplifyPath("/home//foo/")
        #test
        test = SolutionOther()
        print test.simplifyPath("/home/foo/.ssh/../.ssh2/authorized_keys/")
        # answer = "/home/foo/.ssh2/authorized_keys"
        print test.simplifyPathWrongAns("/home/foo/.ssh/../.ssh2/authorized_keys/")

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
The main idea is to push to the stack every valid file name (not in {"",".",".."}),
popping only if there's smth to pop and we met "..".

# Stack
# 23ms 27.33%
class Solution {
    public String simplifyPath(String path) {
        Stack<String> stack = new Stack<>();
        Set<String> set = new HashSet<>(Arrays.asList("..",".",""));
        for (String dir : path.split("/")) {
            if (dir.equals("..") && !stack.isEmpty()) stack.pop();
            else if (!set.contains(dir)) stack.push(dir);
        }

        StringBuilder sb = new StringBuilder();
        if (stack.isEmpty()) return "/";
        for (String str : stack) {
            sb.append("/").append(str);
        }
        return sb.toString();
    }
}


# 12ms 93.66%
class Solution {
    public String simplifyPath(String path) {
        String[] paths = path.split("/");
        int end = 0;
        for (int i = 0; i < paths.length; i++) {
            if (paths[i].equals("..")) {
                if (end > 0) {
                    end--;
                }
            } else if (paths[i].length() > 0 && !paths[i].equals(".")) {
                paths[end++] = paths[i];
            }
        }
        if (end == 0) {
            return "/";
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < end; i++) {
            sb.append('/').append(paths[i]);
        }
        return sb.toString();
    }
}

# 16ms 62.84%
class Solution {
    public String simplifyPath(String path) {
        LinkedList<String> list = new LinkedList<>();
        int start = 0;
        int end = 0;
        int len = path.length();
        while (end < len) {
            while (end < len && path.charAt(end) != '/') {
                end++;
            }
            if (start != end) {
                String cur = path.substring(start, end);
                if (cur.equals("..")) {
                    if (!list.isEmpty()) {
                        list.removeLast();
                    }
                } else if (!cur.equals(".")) {
                    list.add(cur);
                }
            }
            start = ++end;
        }
        if (list.isEmpty()) {
            return "/";
        }
        StringBuilder sb = new StringBuilder();
        while (!list.isEmpty()) {
            sb.append('/').append(list.poll());
        }
        return sb.toString();
    }
}

# 10ms 99.18%
class Solution {
    public String simplifyPath(String path) {
        List<String> pathList = new ArrayList<>();
        int start = 1;
        int end = 1;
        while (start < path.length()) {
            while (end < path.length() && path.charAt(end) != '/') {
                end++;
            }
            String curr = path.substring(start, end);
            if (curr.equals("..")) {
                if (!pathList.isEmpty()) {
                    pathList.remove(pathList.size() - 1);
                }
            } else if (curr.length() > 0 && !curr.equals(".")) {
                pathList.add(curr);
            }
            end++;
            start = end;
        }
        return printPath(pathList);
    }
    
    private String printPath(List<String> pathList) {
        StringBuilder sb = new StringBuilder();
        for (String path : pathList) {
            if (path.length() > 0) {
                sb.append('/');
                sb.append(path);
            }
        }
        if (sb.length() == 0) {
            sb.append('/');
        }
        return sb.toString();
    }
}
'''
