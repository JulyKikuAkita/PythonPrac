__source__ = 'https://leetcode.com/problems/palindrome-number/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/palindrome-number.py
# Time:  O(1)
# Space: O(1)
# Math  ~= reverse integer
#
# Description: Leetcode # 9 Palindrome Number
# Determine whether an integer is a palindrome. Do this without extra space.
#
# Some hints:
# Could negative integers be palindromes? (ie, -1)
#
# If you are thinking of converting the integer to string, note the restriction of using extra space.
#
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer",
# you know that the reversed integer might overflow. How would you handle such case?
#
# There is a more generic way of solving this problem.
# Related Topics
# Math
# Similar Questions
# Palindrome Linked List

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        copy,reverse = x, 0
        while copy:
            reverse *= 10
            reverse += copy % 10
            copy /= 10
        return x == reverse

class Solution2:
    # @return a boolean
    def isPalindromeTwoPointers(self, x):
        if x < 0 :
            return False
        while x != 0:
            div = 1
            while (x / div ) >= 10:
                div = div * 10

            left = x / div
            right = x % 10

            if left != right:
                return False
            else:
                x = (x % div) / 10
                #div = div / 100

        return True

if __name__ == "__main__":
    print Solution().isPalindrome(12321)
    print Solution().isPalindrome(12320)
    print Solution().isPalindrome(-12321)



class SolutionOther:
    # @return a boolean
    def isPalindrome(self, x):
        if x <= 0 :
            return False if x < 0 else True
        a, b = x, 0
        while a:
            b, a = b * 10 + a % 10, a /10
            #print b , a
        return b == x

#test
test = SolutionOther()
#print test.isPalindrome(121)
#print test.isPalindrome(1121)

#Java
Java = '''
# Thought:

#42.39% 222ms
public class Solution {
    public boolean isPalindrome(int x) {
        return new StringBuilder().append(x).reverse().toString().equals(x+"");
    }
}

#20.26% 252ms
public class Solution {
    public boolean isPalindrome(int x) {
        char[] arr = String.valueOf(x).toCharArray();
        int i;
        for (i = 0; i < arr.length / 2 ; i++) {
        	if (arr[i] != arr[arr.length - 1 -i]) {
        		break;
        	}
        }
        return i >= arr.length / 2;
	}
}

89.65% 192ms
public class Solution {
    public boolean isPalindrome(int x) {
       if (x<0 || (x!=0 && x%10==0)) return false;
        int rev = 0;
        while (x>rev){
            rev = rev*10 + x%10;
            x = x/10;
        }
        return (x==rev || x==rev/10); //x = 999
    }
}

'''