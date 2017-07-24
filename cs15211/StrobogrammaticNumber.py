__source__ = 'https://leetcode.com/problems/strobogrammatic-number/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/strobogrammatic-number.py
# Time:  O(n)
# Space: O(1)
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
#
# Write a function to determine if a number is strobogrammatic. The number is represented as a string.
#
# For example, the numbers "69", "88", and "818" are all strobogrammatic.
# Companies
# Google
# Related Topics
# Hash Table Math
# Similar Questions
# Strobogrammatic Number II Strobogrammatic Number III
#

class Solution:
    lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}


    # @param {string} num
    # @return {boolean}
    def isStrobogrammatic(self, num):
        n = len(num)
        for i in xrange(( n + 1) / 2) :
            print i
            if num[n - 1 - i] not in self.lookup or \
               num[i] != self.lookup[num[n - 1 - i]]:
                return False
        return True


class Solution1(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num :
            return True

        i = 0
        j = len(num) -1

        while i <= j:
            print num[i], num[j], i, j
            if num[i] == num[j] and num[i] in ("0", "1" ,"8"):
                pass
            elif (num[i] == "6" and num[j] == "9" ) or \
                 (num[j] == "6" and num[i] == "9" ):
                    print num[i], num[j]
                    pass
            else:
                return False

            i+=1
            j-=1

        return True

if __name__ == "__main__":
    print Solution().isStrobogrammatic("878")


# JAVA:
Java = '''

# 1 %
public class Solution {
    public static final Map<Character, Character> strobogramMap;
    static {
        Map<Character, Character> map = new HashMap<>();
        map.put('0', '0');
        map.put('1', '1');
        map.put('6', '9');
        map.put('8', '8');
        map.put('9', '6');
        strobogramMap = Collections.unmodifiableMap(map);
    }

    public boolean isStrobogrammatic(String num) {
        for (int start = 0, end = num.length() - 1; start <= end; start++, end--) {
            if (!strobogramMap.containsKey(num.charAt(start)) || strobogramMap.get(num.charAt(start)) != num.charAt(end)) {
                return false;
            }
        }
        return true;
    }
}

# 8%
public class Solution {
    public boolean isStrobogrammatic(String num) {
        for (int i=0, j=num.length()-1; i <= j; i++, j--)
            if (!"00 11 88 696".contains(num.charAt(i) + "" + num.charAt(j)))
                return false;
        return true;
    }
}

# 8%
public class Solution {
    public static Map<Character, Character> map;
    {
        map = new HashMap<>();
        map.put('0', '0');
        map.put('1', '1');
        map.put('6', '9');
        map.put('8', '8');
        map.put('9', '6');
    }

    public boolean isStrobogrammatic(String num) {
        int start = 0;
        int end = num.length() - 1;
        while (start < end) {
            Character val = map.get(num.charAt(start));
            if (val == null || val != num.charAt(end)) {
                return false;
            }
            start++;
            end--;
        }
        if (start == end) {
            char c = num.charAt(start);
            return c == '0' || c == '1' || c == '8';
        } else {
            return true;
        }
    }
}

# 52%
public class Solution {
    public boolean isStrobogrammatic(String num) {
        int head = 0, tail = num.length() - 1;
        while(head <= tail) {
            char ch = num.charAt(head), ct = num.charAt(tail);
            switch(ch) {
                case '0':
                    if(ct != '0')
                        return false;
                    break;
                case '1':
                    if(ct != '1')
                        return false;
                    break;
                case '8':
                    if(ct != '8')
                        return false;
                    break;
                case '6':
                    if(ct != '9')
                        return false;
                    break;
                case '9':
                    if(ct != '6')
                        return false;
                    break;
                default:
                    return false;
            }
            head++; tail--;
        }
        return true;
    }
}
'''



