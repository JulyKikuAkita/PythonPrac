__source_ = 'https://leetcode.com/problems/encode-and-decode-strings/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/encode-and-decode-strings.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 271. Encode and Decode Strings
#
# Design an algorithm to encode a list of strings to a string.
# The encoded string is then sent over the network and is decoded back to the original list of strings.
#
# Machine 1 (sender) has the function:
#
# string encode(vector<string> strs) {
#   // ... your code
#   return encoded_string;
# }
# Machine 2 (receiver) has the function:
# vector<string> decode(string s) {
#   //... your code
#   return strs;
# }
# So Machine 1 does:
#
# string encoded_string = encode(strs);
# and Machine 2 does:
#
# vector<string> strs2 = decode(encoded_string);
# strs2 in Machine 2 should be the same as strs in Machine 1.
#
# Implement the encode and decode methods.
#
# Note:
# The string may contain any possible characters out of 256 valid ascii characters.
# Your algorithm should be generalized enough to work on any possible characters.
# Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
# Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.
#
# Companies
# Google
# Related Topics
# String
# Similar Questions
# Count and Say Serialize and Deserialize Binary Tree
#

# Time:  O(n)
# Space: O(1)
import unittest
class Codec(unittest.TestCase):

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        encoded_str = ""
        for s in strs:
            encoded_str += "%0*x" % (8, len(s)) + s
            #print "%0*x" % (2, len(s))  # string format hex: {0:#x}
        return encoded_str

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """

        i = 0
        strs = []
        while i < len(s):
            l = int(s[i:i+8] ,16)
            strs.append(s[i+8:i+8+l])
            i += 8 +l
        return strs

    def test(self):
        hash = self.encode(["nSM","Dsy"])
        self.assertEqual(["nSM","Dsy"] , self.decode(hash))

class Codec2(unittest.TestCase):
    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for s in strs:
            res += str(len(s)) + ":" + s
        return res
    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        i = 0
        res = []
        while i < len(s):
            idx = s.find(":",i)
            if idx < 0:
                return res
            l = int(s[i:idx])
            i = idx + 1
            res.append(s[i:i+l])
            i += l
        return res

    def test(self):
        hash = self.encode(["",""])
        self.assertEqual(["",""] , self.decode(hash))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().containsDuplicate([12344555,12344555])

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:

Thought:
#21.29% 54ms

public class Codec {
    public String encode(List<String> strs) {
        StringBuffer out = new StringBuffer();
        for (String s : strs)
            out.append(s.replace("#", "##")).append(" # ");
        return out.toString();
    }

    public List<String> decode(String s) {
        List strs = new ArrayList();
        String[] array = s.split(" # ", -1);
        for (int i=0; i<array.length-1; ++i)
            strs.add(array[i].replace("##", "#"));
        return strs;
    }
}


#46.54% 14ms
public class Codec {
    private static final char DELIMITER = '#';

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String str : strs) {
            sb.append(str.length()).append(DELIMITER).append(str);
        }
        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> result = new ArrayList<>();
        int index = 0;
        while (index < s.length()) {
            int start = index;
            while (index < s.length() && s.charAt(index) != DELIMITER) {
                index++;
            }
            int len = Integer.parseInt(s.substring(start, index));
            index++;
            result.add(s.substring(index, index + len));
            index += len;
        }
        return result;
    }

#94.03% 11ms
public class Codec {
    private static final Character DELIMITER = '#';

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String str : strs) {
            sb.append(str.length()).append(DELIMITER).append(str);
        }
        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> result = new ArrayList<>();
        int index = 0;
        while (index < s.length()) {
            int len = 0;
            while (index < s.length() && s.charAt(index) != DELIMITER) {
                len = len * 10 + (s.charAt(index) - '0');
                index++;
            }
            index++;
            result.add(s.substring(index, index + len));
            index += len;
        }
        return result;
    }
}

#99.72% 8ms
public class Codec {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        if (strs == null) {
    			return null;
    		}
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < strs.size(); i++) {
            sb.append(strs.get(i)).append("{];>");
        }
        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        if (s == null) {
    			return null;
    		}
    		//System.out.println("decode, s = " + s);
        List<String> output = new ArrayList<String>();
        if (s.length() == 0) {
        		return output;
        }
        int index = s.indexOf("{];>");
        int start = 0;
        while (index >= 0) {
        		output.add(s.substring(start, index));
        		start = index + 4;
        		index = s.indexOf("{];>", start);
        }
        return output;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(strs));
'''