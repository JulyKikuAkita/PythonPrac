__source__ = 'https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/read-n-characters-given-read4-ii-call-multiple-times.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 158. Read N Characters Given Read4 II - Call multiple times
#
# The API: int read4(char *buf) reads 4 characters at a time from a file.
#
# The return value is the actual number of characters read. For example,
# it returns 3 if there is only 3 characters left in the file.
#
# By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.
#
# Note:
# The read function may be called multiple times.
# Companies
# Bloomberg Google Facebook
# Related Topics
# String
# Similar Questions
# Read N Characters Given Read4
#
# The read4 API is already defined for you.
#
import unittest
def read4(buf):
    global file_content
    i = 0
    while i < len(file_content) and i < 4:
        buf[i] = file_content[i]
        i += 1
    if len(file_content) > 4:
        file_content = file_content[4:]
    else:
        file_content = ""
    return i

class Solution:
    def __init__(self):
        self.buffer_size, self.offset = 0, 0
        self.buffer = [None for _ in xrange(4)]
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def read(self, buf, n):
        read_bytes = 0
        eof = False

        while not eof and read_bytes < n:
            if self.buffer_size == 0:
                size = read4(self.buffer)
            else:
                size = self.buffer_size
            if self.buffer_size == 0 and size < 4:
                eof = True

            bytes = min(n - read_bytes, size)

            for i in xrange(bytes):
                buf[read_bytes + i] = self.buffer[self.offset + i]

            self.offset = (self.offset + bytes) % 4
            self.buffer_size = size - bytes
            read_bytes += bytes
        return read_bytes

# Test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        test = Solution()
        global file_content

        buf = ['' for _ in xrange(100)]
        file_content = "ab"
        print buf[:test.read(buf,1)]
        print buf[:test.read(buf,2)]

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:

/* The read4 API is defined in the parent class Reader4.
      int read4(char[] buf); */

# 22.71% 2ms
public class Solution extends Reader4 {
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    private int buffPtr = 0;
    private int buffCnt = 0;
    private char[] buff = new char[4];

    public int read(char[] buf, int n) {
        int ptr = 0;
        while (ptr < n) {
            if (buffPtr == 0) {
                buffCnt = read4(buff);
            }
            if (buffCnt == 0) break;
            while (ptr < n && buffPtr < buffCnt) {
                buf[ptr++] = buff[buffPtr++];
            }
            if (buffPtr >= buffCnt) buffPtr = 0;
        }
        return ptr;
    }
}

# 22.71% 2ms
public class Solution extends Reader4 {
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */

    private char[] buffer = new char[4];
    private int readLength = 0;
    private int offset = 0;
    public int read(char[] buf, int n) {
        boolean isEnd = false;
        int haveRead = 0;
        while (!isEnd && haveRead < n) {
            if (readLength == 0) {
                readLength = read4(buffer);
                isEnd = readLength < 4;
            }
            int currRead = Math.min(n - haveRead, readLength);
            for (int i = 0; i < currRead; i++) {
                buf[haveRead + i] = buffer[offset + i];
            }
            haveRead += currRead;
            readLength -= currRead;
            offset = (offset + currRead) % 4;
        }
        return haveRead;
    }
}


# Queue
#5.1% 3ms
public class Solution extends Reader4 {
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    // queue
    // each time read n, so when there is no character in queue or reach to n each time, break
    Queue<Character> q = new LinkedList<>();

    public int read(char[] buf, int n) {
        int total = 0;
        while(true) {
            char [] temp = new char[4];
            int num = read4(temp);
            for(int i = 0; i < num; i ++) {
                q.offer(temp[i]);
            }
            num = Math.min(q.size(), n - total);
            if(num == 0)  break;
            for(int i = 0; i < num; i ++) {
                buf[total++] = q.poll();
            }
        }
        return total;
    }
}
'''