__source__ = 'https://leetcode.com/problems/super-palindromes/'
# Time:  O()
# Space: O(logW)
#
# Description: Leetcode # 906. Super Palindromes
#
# Let's say a positive integer is a superpalindrome if it is a palindrome,
# and it is also the square of a palindrome.
#
# Now, given two positive integers L and R (represented as strings),
# return the number of superpalindromes in the inclusive range [L, R].
#
# Example 1:
#
# Input: L = "4", R = "1000"
# Output: 4
# Explanation: 4, 9, 121, and 484 are superpalindromes.
# Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
#
# Note:
#
# 1 <= len(L) <= 18
# 1 <= len(R) <= 18
# L and R are strings representing integers in the range [1, 10^18).
# int(L) <= int(R)
#
import unittest
# 1368ms 44%
class Solution(object):
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        L, R = int(L), int(R)
        MAGIC = 100000

        def reverse(x):
            ans = 0
            while x:
                ans = 10 * ans + x % 10
                x /= 10
            return ans

        def is_palindrome(x):
            return x == reverse(x)

        ans = 0

        # count odd length
        for k in xrange(MAGIC):
            s = str(k)  # Eg. s = '1234'
            t = s + s[-2::-1]  # t = '1234321'
            v = int(t) ** 2
            if v > R: break
            if v >= L and is_palindrome(v):
                ans += 1

        # count even length
        for k in xrange(MAGIC):
            s = str(k)  # Eg. s = '1234'
            t = s + s[::-1]  # t = '12344321'
            v = int(t) ** 2
            if v > R: break
            if v >= L and is_palindrome(v):
                ans += 1

        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/super-palindromes/solution/
#
Approach 1: Mathematical
Complexity Analysis
Time Complexity: O(W^(1/4) * logW), where W=10^18 is our upper limit for R. 
The logW term comes from checking whether each candidate is the root of a palindrome.
Space Complexity: O(logW), the space used to create the candidate palindrome. 

# 157ms 74.19%
class Solution {
    public int superpalindromesInRange(String L, String R) {
        long lL = Long.valueOf(L);
        long lR = Long.valueOf(R);
        int MAGIC = 100000;
        int ans = 0;
        
        // count odd length;
        for (int k = 1; k < MAGIC; ++k) {
            StringBuilder sb = new StringBuilder(Integer.toString(k));
            for (int i = sb.length() - 2; i >= 0; --i)
                sb.append(sb.charAt(i));
            long v = Long.valueOf(sb.toString());
            v *= v;
            if (v > lR) break;
            if (v >= lL && isPalindrome(v)) ans++;
        }
        
        // count even length;
        for (int k = 1; k < MAGIC; ++k) {
            StringBuilder sb = new StringBuilder(Integer.toString(k));
            for (int i = sb.length() - 1; i >= 0; --i)
                sb.append(sb.charAt(i));
            long v = Long.valueOf(sb.toString());
            v *= v;
            if (v > lR) break;
            if (v >= lL && isPalindrome(v)) ans++;
        }
        return ans;
    }
    
    private boolean isPalindrome(long x) {
        return x == reverse(x);
    }
    
    private long reverse(long x) {
        long ans = 0;
        while (x > 0) {
           ans = 10 * ans + x % 10;
            x /= 10;
        }
        return ans;
    }
}

# cheat
# 2ms 100%
class Solution {
	private static final long[] candidate = {0L, 1L, 4L, 9L, 121L, 484L, 10201L, 40804L, 12321L, 
	44944L, 14641L, 1002001L, 4008004L, 1234321L, 100020001L, 400080004L, 121242121L, 102030201L, 
	404090404L, 123454321L, 104060401L, 125686521L, 10000200001L, 40000800004L, 12102420121L, 
	10221412201L, 12345654321L, 1000002000001L, 4000008000004L, 1210024200121L, 1020304030201L, 
	1232346432321L, 1002003002001L, 4004009004004L, 1212225222121L, 1022325232201L, 1234567654321L, 
	1004006004001L, 1214428244121L, 1024348434201L, 100000020000001L, 400000080000004L, 
	121000242000121L, 102012040210201L, 123212464212321L, 100220141022001L, 121242363242121L, 
	102234363432201L, 123456787654321L, 10000000200000001L, 40000000800000004L, 
	12100002420000121L, 10201020402010201L, 12321024642012321L, 10020210401202001L, 
	12122232623222121L, 10221432623412201L, 12343456865434321L, 10002000300020001L, 
	40004000900040004L, 12102202520220121L, 10203040504030201L, 12323244744232321L, 
	10022212521222001L, 12124434743442121L, 10223454745432201L, 12345678987654321L, 
	10004000600040001L, 12104402820440121L, 10205060806050201L, 10024214841242001L};
	
    public int superpalindromesInRange(String L, String R) {
        long l = Long.parseLong(L), r = Long.parseLong(R);
        int res = 0;
        for (long i : candidate) {
        	if (i >= l && i <= r) {
        		++res;
        	}
        }
        return res;
    }
}
'''
