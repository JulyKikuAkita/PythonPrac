__author__ = 'July'
'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

For example,
Given low = "50", high = "100", return 3. Because 69, 88, and 96 are three strobogrammatic numbers.

Note:
Because the range might be a large number, the low and high numbers are represented as string.
'''


# Time:  O(5^(n/2))
# Space: O(n)
# https://github.com/kamyu104/LeetCode/blob/master/Python/strobogrammatic-number-iii.py
# Time:  O(5^(n/2))
# Space: O(n)

class Solution:
    lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    cache = {}

    # @param {string} low
    # @param {string} high
    # @return {integer}
    def strobogrammaticInRange3(self, low, high):
        count = self.countStrobogrammaticUntil(high, False) - \
                self.countStrobogrammaticUntil(low, False) + \
                self.isStrobogrammatic(low)
        return count if count >= 0 else 0

    def countStrobogrammaticUntil(self, num,  can_start_with_0):
        if can_start_with_0 and num in self.cache:
            return self.cache[num]

        count = 0
        if len(num) == 1:
            for c in ['0', '1', '8']:
                if num[0] >= c:
                    count += 1
            self.cache[num] = count
            return count

        for key, val in self.lookup.iteritems():
            if can_start_with_0 or key != '0':
                if num[0] > key:
                    if len(num) == 2:  # num is like "21"
                        count += 1
                    else:  # num is like "201"
                        count += self.countStrobogrammaticUntil('9' * (len(num) - 2), True)
                elif num[0] == key:
                    if len(num) == 2:  # num is like 12".
                        if num[-1] >= val:
                            count += 1
                    else:
                        if num[-1] >= val:  # num is like "102".
                            count += self.countStrobogrammaticUntil(self.getMid(num), True);
                        elif (self.getMid(num) != '0' * (len(num) - 2)):  # num is like "110".
                            count += self.countStrobogrammaticUntil(self.getMid(num), True) - \
                                     self.isStrobogrammatic(self.getMid(num))

        if not can_start_with_0: # Sum up each length.
            for i in xrange(len(num) - 1, 0, -1):
                count += self.countStrobogrammaticByLength(i)
        else:
            self.cache[num] = count

        return count

    def getMid(self, num):
        return num[1:len(num) - 1]

    def countStrobogrammaticByLength(self, n):
        if n == 1:
            return 3
        elif n == 2:
            return 4
        elif n == 3:
            return 4 * 3
        else:
            return 5 * self.countStrobogrammaticByLength(n - 2)

    def isStrobogrammatic(self, num):
        n = len(num)
        for i in xrange((n+1) / 2):
            if num[n-1-i] not in self.lookup or \
               num[i] != self.lookup[num[n-1-i]]:
                return False
        return True

#test
if __name__ == "__main__":
    print Solution().strobogrammaticInRange3("50","100")


# Java
# http://massivealgorithms.blogspot.com/2015/08/leetcode-strobogrammatic-number-iii.html

# all combinations
# http://massivealgorithms.blogspot.com/2015/08/leetcode-strobogrammatic-number-iii.html
sol = '''
public class Solution {
    Map<Character, Character> map = new HashMap<>();
        {
        map.put('1', '1');
        map.put('8', '8');
        map.put('6', '9');
        map.put('9', '6');
        map.put('0', '0');
        }
    private char[] validNumbers = new char[]{'0', '1', '6', '8', '9'};
    private char[] singleable = new char[]{'0', '1', '8'};

    public int strobogrammaticInRange(String low, String high) {
        int ll = low.length();
        int hl = high.length();
        int result = 0;

        if (ll > hl || (ll == hl && low.compareTo(high) > 0))    return 0;

        List<String> list = findStrobogrammatic(ll);

        if(ll == hl){
            for (String s: list){
                if(s.compareTo(low) >= 0 && s.compareTo(high) <= 0){
                    result ++;
                }
                if(s.compareTo(high) > 0) break;
            }
        }else{
            for (int i = list.size() -1 ; i>= 0; i--){
                String s = list.get(i);
                if(s.compareTo(low) >= 0){ result ++;}
                if(s.compareTo(low) < 0) {break;}
            }
            list = findStrobogrammatic(hl);
            for(String s : list){
                if(s.compareTo(high) <= 0){
                    result ++;
                }
                if(s.compareTo(high) > 0) {
                    break;
                }
            }

            for(int i = ll +1; i < hl; i++){
                result += findStrobogrammatic(i).size();
            }
        }
        return result;

    }
    public List<String> findStrobogrammatic(int n){
        List<String> result = new ArrayList<>();
        if(n == 1){
            for(char c : singleable){
                result.add(String.valueOf(c));
            }
            return result;
        }

        if(n % 2 == 0){
            helper(n, new StringBuilder(), result);
        }else{
            helper(n-1, new StringBuilder(), result);
            List<String> tmp = new ArrayList<>();
            for(String s:result){
                for(char c: singleable){
                    tmp.add(new StringBuilder(s).insert(s.length()/2, c).toString());
                }
            }
            result = tmp;
        }
        return result;


    }


    private void helper(int n, StringBuilder sb, List<String> result){
        if(sb.length() > n) return;

        if(sb.length() == n) {
            if(sb.length() > 0 && sb.charAt(0) != '0'){
                result.add(sb.toString());
            }
            return;
        }
        for( char c: validNumbers){
            StringBuilder tmp = new StringBuilder(sb);
            String s = "" + c + map.get(c);
            tmp.insert(tmp.length()/2, s);
            helper(n, tmp, result);

        }
    }
}

'''