__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/simplify-path.py
# Time:  O(n)
# Space: O(n)
# Stack
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
# Microsoft

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

if __name__ == "__main__":
    print Solution().simplifyPath("/../")
    print Solution().simplifyPath("/home//foo/")

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

#test
test = SolutionOther()
print test.simplifyPath("/home/foo/.ssh/../.ssh2/authorized_keys/")
# answer = "/home/foo/.ssh2/authorized_keys"
print test.simplifyPathWrongAns("/home/foo/.ssh/../.ssh2/authorized_keys/")

#java
js = '''
public class Solution {
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

public class Solution {
    public String simplifyPath(String path) {
        if(path == null || path.length() == 0){
            return "";
        }
        int idx = path.indexOf("/");
        String sub = path.substring(idx+1);
        // to eliminate empty string once split the first "/"
        String[] items = sub.split("/");
        Stack<String> stack = new Stack<>();

        for(String item : items){
            if( item..length()>0 && !item.equals(".") &&!item.equals("..")){
                stack.push(item);
            }else if(!stack.isEmpty() && item.equals("..")){
                stack.pop();
            }
        }

        if(stack.size() == 0){
            return "/";
        }

        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < stack.size(); i++){
            sb.append("/").append(stack.get(i));
        }
        return sb.toString();
    }
}
'''