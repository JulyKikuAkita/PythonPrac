__source__ = 'https://leetcode.com/problems/longest-absolute-file-path/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/longest-absolute-file-path.py
# Time:  O(n)
# Space: O(d), d is the max depth of the paths
#
# Description: Leetcode # 388. Longest Absolute File Path
#
# Suppose we abstract our file system by a string in the following manner:
#
# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
#
# dir
#     subdir1
#     subdir2
#         file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
#
# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
#
# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2.
# subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1.
# subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
#
# We are interested in finding the longest (number of characters) absolute path to a file within our file system.
# For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext",
# and its length is 32 (not including the double quotes).
#
# Given a string representing the file system in the above format,
# return the length of the longest absolute path to file in the abstracted file system.
# If there is no file in the system, return 0.
#
# Note:
# The name of a file contains at least a . and an extension.
# The name of a directory or sub-directory will not contain a ..
# Time complexity required: O(n) where n is the size of the input string.
#
# Notice that a/aa/aaa/file1.txt is not the longest file path, if there is
# another path aaaaaaaaaaaaaaaaaaaaa/sth.png.
#  Google
#

# ex: "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        def split_iter(s, tok):
            start = 0
            for i in xrange(len(s)):
                if s[i] == tok:
                    yield s[start:i] #return lefthand side of '\n', aka all dir
                    start = i + 1
            yield s[start:] # return files


        max_len = 0
        path_len = {0: 0}
        for line in split_iter(input, '\n'): # '\n' is one char
            name = line.lstrip('\t')
            depth = len(line) - len(name) # count '\n' as depth
            if '.' in name:
                max_len = max(max_len, path_len[depth] + len(name))
            else:
                path_len[depth + 1] = path_len[depth] + len(name) + 1
        return max_len

# 20ms 99.28%
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        max_len = 0
        pathlen = {0 : 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                max_len = max(max_len, pathlen[depth] + len(name))
            else :
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1
        return max_len

Java = '''
# Thought:

The depth of the directory/file is calculated by counting how many "\t"s are there.
The time complexity is O(n) because each substring in the input string only goes into the stack once,
and pops out from the stack once.

# 4ms 35.33%
class Solution {
    public int lengthLongestPath(String input) {
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(0); // "dummy" length
        int maxLen = 0;
        for(String s:input.split("\n")){
            int lev = s.lastIndexOf("\t")+1; // number of "\t", "\t" counts one char
            while(lev+1<stack.size()) stack.pop(); // find parent
            int len = stack.peek()+s.length()-lev+1; // remove "/t", add"/"
            stack.push(len);
            // check if it is file
            if(s.contains(".")) maxLen = Math.max(maxLen, len-1);
        }
        return maxLen;
    }
}

An even shorter and faster solution using array instead of stack:

# 2ms 98.80%
class Solution {
    public int lengthLongestPath(String input) {
        String[] paths = input.split("\n");
        int[] stack = new int[paths.length + 1];
        int res = 0, curLen = 0;
        for (String s : paths) {
            int lev = s.lastIndexOf("\t") + 1; // number of "\t"
            stack[lev+1] =stack[lev] + s.length() - lev + 1;
            curLen = stack[lev+1];
            if (s.contains(".")) {
                res = Math.max(res, curLen - 1);
            }
        }
        return res;
    }
}

# "\t" counts one char length
# note if print "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext".split("\n") and string length();
dir 3
        subdir1 8
        subdir2 8
                file.ext 10
# note, if print "\tdir".lastIndexOf("\t"), return 0;, if not found, return -1;
'''
