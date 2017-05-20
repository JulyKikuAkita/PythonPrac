__author__ = 'July'
'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return ["11","69","88","96"].
'''
# Time:  O(n^2 * 5^(n/2))
# Space: O(n)
# https://github.com/kamyu104/LeetCode/blob/master/Python/strobogrammatic-number-ii.py
class Solution:
    lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}

    # @param {integer} n
    # @return {string[]}
    def findStrobogrammatic2(self, n):
        return self.findStrobogrammatic2Recu(n ,n)

    def findStrobogrammatic2Recu(self, n, k):
        if k == 0 :
            return ['']
        elif k == 1:
            return ['0', '1', '8']

        result = []
        for num in self.findStrobogrammatic2Recu(n, k -2):
            for key, val in self.lookup.iteritems():
                if n != k or key != '0':
                    result.append(key + num + val)
        return result


# Java:
# no recursion
# https://leetcode.com/discuss/68215/simple-java-solution-without-recursion
tmp= '''
public class Solution {
    public List<String> findStrobogrammatic(int n) {

        List<String> one = Arrays.asList("0", "1", "8"), two = Arrays.asList("") ;
        List<String> res = two;
        if (n % 2 == 1) res = one;

        for( int k = (n % 2) + 2; k<= n; k+= 2 ){
            List<String> tmp = new ArrayList<>();
            for(String str : res){
                tmp.add("1" + str + "1");
                tmp.add("6" + str + "9");
                tmp.add("8" + str + "8");
                tmp.add("9" + str + "6");
                if (k != n){
                    tmp.add("0" + str + "0");
                }
            }
            res = tmp;
        }

        return res;
    }
}
'''

# recursion
tmp2= '''
public class Solution {
    public List<String> findStrobogrammatic(int n) {
        return findStrobogrammatic(n, n);
    }

    private List<String> findStrobogrammatic(int n, int curr) {
        List<String> result = new ArrayList<String>();
        if (curr == 0) {
            result.add("");
        } else if (curr == 1) {
            result.add("0");
            result.add("1");
            result.add("8");
        } else {
            List<String> next = findStrobogrammatic(n, curr - 2);
            for (String str : next) {
                result.add("1" + str + "1");
                result.add("6" + str + "9");
                result.add("8" + str + "8");
                result.add("9" + str + "6");
                if (n != curr) {
                    result.add("0" + str + "0");
                }
            }
        }
        return result;
    }
}
'''

