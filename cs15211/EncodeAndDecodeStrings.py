__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/encode-and-decode-strings.py
'''
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

Note:
The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.
Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.
Tags Google

'''
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
#java
# http://algobox.org/encode-and-decode-strings/
js = '''
public class Codec {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String str : strs) {
            sb.append(str.length()).append('#');
            sb.append(str);
        }
        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> result = new ArrayList<>();
        int len = s.length();
        int index = 0;
        while (index < len) {
            int curLen = 0;
            for (int j = index; j < len; j++) {
                char c = s.charAt(j);
                if (!Character.isDigit(c)) {
                    index = j + 1;
                    break;
                }
                curLen = curLen * 10 + c - '0';
            }
            result.add(s.substring(index, index + curLen));
            index += curLen;
        }
        return result;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(strs));

public class Codec {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        if(strs.isEmpty()) return "";
        StringBuilder sb = new StringBuilder(0);
        for(String str : strs){
            sb.append(str.length()).append(',');
        }
        sb.setCharAt(sb.length() -1, ':');
        for(String str: strs){
            sb.append(str);
        }
        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> ans = new ArrayList<>();
        int m = s.indexOf(':');
        if(m < 0) return ans;
        int i = m + 1;
        String[] strLens = s.substring(0, m).split(",");
        for(String strlen : strLens){
            int len = Integer.parseInt(strlen);
            ans.add(s.substring(i, i + len));
            i += len;
        }
        return ans;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(strs));

public class Codec {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for(String str : strs){
            sb.append(str.length()).append(',').append(str);
        }
        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        List<String> res = new ArrayList<>();
        for(int i = 0, len; i < s.length(); i += len){
            int comma = s.indexOf(',', i);
            len = Integer.parseInt(s.substring(i, comma));
            i = comma+1;
            res.add(s.substring(i, i + len ));
        }
        return res;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(strs));
'''