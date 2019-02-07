__source__ = 'https://leetcode.com/problems/design-in-memory-file-system/'
# https://leetcode.com/problems/design-in-memory-file-system/#/description
# Time:  O()
# Space: O()
#
# Description: Leetcode # 588. Design In-Memory File System
#
# Design an in-memory file system to simulate the following functions:
#
# ls: Given a path in string format. If it is a file path,
# return a list that only contains this file's name.
# If it is a directory path, return the list of file and directory names in this directory.
# Your output (file and directory names together) should in lexicographic order.
#
# mkdir: Given a directory path that does not exist,
# you should make a new directory according to the path.
# If the middle directories in the path don't exist either,
# you should create them as well. This function has void return type.
#
# addContentToFile: Given a file path and file content in string format.
# If the file doesn't exist, you need to create that file containing given content.
# If the file already exists, you need to append given content to original content.
# This function has void return type.
#
# readContentFromFile: Given a file path, return its content in string format.
#
# Example:
# Input:
# ["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
# [[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]
# Output:
# [null,[],null,null,["a"],"hello"]
# Explanation:
# filesystem
# Note:
# You can assume all file or directory paths are absolute paths
# which begin with / and do not end with / except that the path is just "/".
# You can assume that all operations will be passed valid parameters
# and users will not attempt to retrieve file content or list a directory or file
# that does not exist.
# You can assume that all directory names and file names only contain lower-case letters,
# and same names won't exist in the same directory.
# Hide Company Tags Baidu
# Hide Tags Design
# Hide Similar Problems (H) LRU Cache (H) LFU Cache
#
import unittest
class Solution(object):
    pass  # your function here

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


Java = '''
# Thought: https://leetcode.com/problems/design-in-memory-file-system/solution/
# Approach #1 Using separate Directory and File List[Accepted]
# Performance Analysis
# The time complexity of executing an ls command is O(m+n+klog(k)). 
# Here, m refers to the length of the input string. 
# We need to scan the input string once to split it and determine the various levels. 
# n refers to the depth of the last directory level in the given input for ls. 
# This factor is taken because we need to enter nn levels of the tree structure to reach the last level. 
# k refers to the number of entries(files+subdirectories) in the last level directory(in the current input). 
# We need to sort these names giving a factor of klog(k).
# 
# The time complexity of executing an mkdir command is O(m+n). 
# Here, m refers to the length of the input string. 
# We need to scan the input string once to split it and determine the various levels. 
# n refers to the depth of the last directory level in the mkdir input. 
# This factor is taken because we need to enter nn levels of the tree structure to reach the last level.
# 
# The time complexity of both addContentToFile and readContentFromFile is O(m+n). 
# Here, m refers to the length of the input string. 
# We need to scan the input string once to split it and determine the various levels. 
# n refers to the depth of the file name in the current input. 
# This factor is taken because we need to enter n levels of the tree structure to reach the level 
# where the files's contents need to be added/read from.
# The advantage of this scheme of maintaining the directory structure is that 
# it is expandable to include even more commands easily. 
# For example, rmdir to remove a directory given an input directory path. 
# We need to simply reach to the destined directory level 
# and remove the corresponding directory entry from the corresponding dirs keys.
# 
# Renaming files/directories is also very simple, 
# since all we need to do is to create a temporary copy of the directory structure/file 
# with a new name and delete the last entry.
# Relocating a hierarchical subdirectory structure from one directory to the other is also very easy, 
# since, all we need to do is obtain the address for the corresponding subdirectory class, 
# and assign the same at the new positon in the new directory structure.
# Extracting only directories or files list on any path is easy in this case, 
# since we maintain separate entires for dirsdirs and filesfiles.
# 106ms 40%

class FileSystem {
    class Dir {
        HashMap<String, Dir> dirs = new HashMap<>();
        HashMap<String, String> files = new HashMap();
    }
    Dir root;

    public FileSystem() {
        root = new Dir();    
    }
    
    public List<String> ls(String path) {
        Dir t = root;
        List<String> files = new ArrayList<>();
        if (!path.equals("/")) {
            String[] d = path.split("/");
            for (int i = 1; i < d.length - 1; i ++) t = t.dirs.get(d[i]);
            if (t.files.containsKey(d[d.length - 1])) {
                files.add(d[d.length - 1]);
                return files;
            } else {
                t = t.dirs.get(d[d.length - 1]);
            }
        }
        files.addAll(new ArrayList<>(t.dirs.keySet()));
        files.addAll(new ArrayList<>(t.files.keySet()));
        Collections.sort(files);
        return files;
    }
    
    public void mkdir(String path) {
        Dir t = root;
        String[] d = path.split("/");
        for (int i = 1; i < d.length; i++) {
            if (!t.dirs.containsKey(d[i])) t.dirs.put(d[i], new Dir());
            t = t.dirs.get(d[i]);
        }
    }
    
    public void addContentToFile(String filePath, String content) {
        Dir t = root;
        String[] d = filePath.split("/");
        for (int i = 1; i < d.length - 1; i++) t = t.dirs.get(d[i]);
        t.files.put(d[d.length - 1], t.files.getOrDefault(d[d.length - 1], "") + content);
    }
    
    public String readContentFromFile(String filePath) {
        Dir t = root;
        String[] d = filePath.split("/");
        for (int i = 1; i < d.length - 1; i++) t = t.dirs.get(d[i]);
        return t.files.get(d[d.length - 1]);
    }
}

# Approach #2 Using unified Directory and File List[Accepted]
# Performance Analysis
# The time complexity of executing an ls command is O(m+n+klog(k)). 
# Here, m refers to the length of the input string. 
# We need to scan the input string once to split it and determine the various levels. 
# n refers to the depth of the last directory level in the given input for ls. 
# This factor is taken because we need to enter n levels of the tree structure to reach the last level. 
# k refers to the number of entries(files+subdirectories) in the last level directory(in the current input). 
# We need to sort these names giving a factor of klog(k).
# 
# The time complexity of executing an mkdir command is O(m+n). 
# Here, m refers to the length of the input string. 
# We need to scan the input string once to split it and determine the various levels. 
# n refers to the depth of the last directory level in the mkdir input. 
# This factor is taken because we need to enter n levels of the tree structure to reach the last level.
# 
# The time complexity of both addContentToFile and readContentFromFile is O(m+n). 
# Here, m refers to the length of the input string. 
# We need to scan the input string once to split it and determine the various levels. 
# n refers to the depth of the file name in the current input. 
# This factor is taken because we need to enter n levels of the tree structure to reach the level 
# where the files's contents need to be added/read from.
# 
# The advantage of this scheme of maintaining the directory structure is that 
# it is expandable to include even more commands easily. 
# For example, rmdir to remove a directory given an input directory path. 
# We need to simply reach to the destined directory level 
# and remove the corresponding directory entry from the corresponding dirs keys.
# 
# Renaming files/directories is also very simple, 
# since all we need to do is to create a temporary copy of the directory structure/file 
# with a new name and delete the last entry.
# 
# Relocating a hierarchichal subdirectory structure from one directory to the other is also very easy, 
# since, all we need to do is obtain the address for the corresponding subdirectory class, 
# and assign the same at the new positon in the new directory structure.
# 
# If the number of directories is very large, we waste redundant space for isfile and content, 
# which wasn't needed in the first design.
# 
# A problem with the current design could occur if we want to list only the directories(and not the files), 
# on any given path. In this case, we need to traverse over the whole contents of the current directory, 
# check for each entry, whether it is a file or a directory, and then extract the required data.
#
# 130ms 10%
#
class FileSystem {
    class File {
        boolean isfile = false;
        HashMap<String, File> files = new HashMap();
        String content = "";
    }
    
    File root;

    public FileSystem() {
        root = new File();    
    }
    
    public List<String> ls(String path) {
        File t = root;
        List<String> files = new ArrayList<>();
        if (!path.equals("/")) {
            String[] d = path.split("/");
            for (int i = 1; i < d.length; i ++) t = t.files.get(d[i]);
            if (t.isfile) {
                files.add(d[d.length - 1]);
                return files;
            }
        }
        List<String> res_files = new ArrayList<>(t.files.keySet());
        Collections.sort(res_files);
        return res_files;
    }
    
    public void mkdir(String path) {
        File t = root;
        String[] d = path.split("/");
        for (int i = 1; i < d.length; i++) {
            if (!t.files.containsKey(d[i])) t.files.put(d[i], new File());
            t = t.files.get(d[i]);
        }
    }
    
    public void addContentToFile(String filePath, String content) {
        File t = root;
        String[] d = filePath.split("/");
        for (int i = 1; i < d.length - 1; i++) t = t.files.get(d[i]);
        if (!t.files.containsKey(d[d.length - 1])) t.files.put(d[d.length - 1], new File());
        t = t.files.get(d[d.length - 1]);
        t.isfile = true;
        t.content = t.content + content;
    }
    
    public String readContentFromFile(String filePath) {
        File t = root;
        String[] d = filePath.split("/");
        for (int i = 1; i < d.length - 1; i++) t = t.files.get(d[i]);
        return t.files.get(d[d.length - 1]).content;
    }
}

# https://leetcode.com/problems/design-in-memory-file-system/discuss/196035/OOP-Java-Solution-beat-100
# 104ms 50%
public class FileSystem {
    private FileNode root;

    public FileSystem() {
        root = new FileNode("");
    }

    public List<String> ls(String path) {
        return findNode(path).getList();
    }

    public void mkdir(String path) {
        findNode(path);
    }

    public void addContentToFile(String filePath, String content) {
        findNode(filePath).addContent(content);
    }

    public String readContentFromFile(String filePath) {
        return findNode(filePath).getContent();
    }

    //-- private method section --//
    private FileNode findNode(String path){
        String[] files = path.split("/");

        FileNode cur = root;
        for(String file : files){
            if(file.length() == 0) continue;

            cur.children.putIfAbsent(file, new FileNode(file));
            cur = cur.children.get(file);

            if(cur.isFile()) break;
        }

        return cur;
    }

   // Private class
   private class FileNode{
        private TreeMap<String, FileNode> children;
        private StringBuilder file;
        private String name;

        public FileNode(String name) {
            children = new TreeMap<>();
            file = new StringBuilder();
            this.name = name;
        }

        public String getContent(){
            return file.toString();
        }

        public String getName(){
            return name;
        }

        public void addContent(String content){
            file.append(content);
        }

        public boolean isFile(){
            return file.length() > 0;
        }

        public List<String> getList(){
            List<String> list = new ArrayList<>();
            if(isFile()){
                list.add(getName());
            }else{
                list.addAll(children.keySet());
            }

            return list;
        }
    }
}

/**
 * Your FileSystem object will be instantiated and called as such:
 * FileSystem obj = new FileSystem();
 * List<String> param_1 = obj.ls(path);
 * obj.mkdir(path);
 * obj.addContentToFile(filePath,content);
 * String param_4 = obj.readContentFromFile(filePath);
 */

 '''
