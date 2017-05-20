__author__ = 'July'
'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
'''
# https://github.com/kamyu104/LeetCode/blob/master/Python/strobogrammatic-number.py
# Time:  O(n)
# Space: O(1)

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



# JAVA:
t = '''
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


'''




if __name__ == "__main__":
    print Solution().isStrobogrammatic("878")

