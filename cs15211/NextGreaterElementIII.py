__source__ = 'https://leetcode.com/problems/next-greater-element-iii/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/next-greater-element-iii.py
# Time:  O(n!) to O(n)
# Space: O(n!) to O(n)
#
# Description: 556. Next Greater Element III
#
# Given a positive 32-bit integer n, you need to find the smallest 32-bit integer
# which has exactly the same digits existing in the integer n and is greater in value than n.
# If no such positive 32-bit integer exists, you need to return -1.
#
# Example 1:
# Input: 12
# Output: 21
#
# Example 2:
# Input: 21
# Output: -1
#
# Bloomberg, Tesla
# Hide Tags String
# Hide Similar Problems (E) Next Greater Element I (M) Next Greater Element II
#
import unittest
# 20ms 96.60%
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = map(int, list(str(n)))
        k, l = -1, 0
        for i in xrange(len(digits) - 1):
            if digits[i] < digits[i + 1]:
                k = i
                
        if k == -1:
            digits.reverse()
            return -1
        
        for i in xrange(k + 1, len(digits)):
            if digits[i] > digits[k]:
                l = i
                
        digits[k], digits[l] = digits[l], digits[k]
        digits[k + 1:] = digits[:k:-1]
        result = int("".join(map(str, digits)))
        return -1 if result >= 0x7FFFFFFF else result

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/next-greater-element-iii/solution/
#
# http://www.geeksforgeeks.org/find-next-greater-number-set-digits/
This solution is just a java version derived from this post:
At first, lets look at the edge cases
If all digits sorted in descending order, then output is always "Not Possible". For example, 4321.
If all digits are sorted in ascending order, then we need to swap last two digits. For example, 1234.
For other cases, we need to process the number from rightmost side
(why? because we need to find the smallest of all greater numbers)
Now the main algorithm works in following steps

I) Traverse the given number from rightmost digit, keep traversing till you find a digit
which is smaller than the previously traversed digit.

For example, if the input number is 534976, we stop at 4 because 4 is smaller than next digit 9.
If we do not find such a digit, then output is "Not Possible".

II) Now search the right side of above found digit 'd' for the smallest digit greater than 'd'.
For 534976, the right side of 4 contains 976. The smallest digit greater than 4 is 6.

III) Swap the above found two digits, we get 536974 in above example.

IV) Now sort all digits from position next to 'd' to the end of number.
The number that we get after sorting is the output.
For above example, we sort digits in bold 536974. We get 536479 which is the next greater number for input 534976.

# 2ms 86.09%
class Solution {
    public int nextGreaterElement(int n) {
        char[] number = (n + "").toCharArray();

        int i, j;
        // I) Start from the right most digit and
        // find the first digit that is
        // smaller than the digit next to it.
        for (i = number.length-1; i > 0; i--)
            if (number[i-1] < number[i])
               break;

        // If no such digit is found, its the edge case 1.
        if (i == 0)
            return -1;

         // II) Find the smallest digit on right side of (i-1)'th
         // digit that is greater than number[i-1]
        int x = number[i-1], smallest = i;
        for (j = i+1; j < number.length; j++)
            if (number[j] > x && number[j] <= number[smallest])
                smallest = j;

        // III) Swap the above found smallest digit with
        // number[i-1]
        char temp = number[i-1];
        number[i-1] = number[smallest];
        number[smallest] = temp;

        // IV) Sort the digits after (i-1) in ascending order
        Arrays.sort(number, i, number.length);

        long val = Long.parseLong(new String(number));
        return (val <= Integer.MAX_VALUE) ? (int) val : -1;
    }
}

# 2ms 86.09%
class Solution {
    public int nextGreaterElement(int n) {
        return getRealNextBiggerInteger(n);
    }

    public static int getRealNextBiggerInteger(int number){
         char[] num = String.valueOf(number).toCharArray();
         int i = num.length - 1, j = num.length - 1;

         // find the first digit from right that is smaller the its right digit
         while (i > 0 && num[i] <= num[i-1]) i--; //pivot = num[i-1]

         // descending order //ex: 54321
         if (i == 0) return -1;

         // find the smallest digit >= pivot within the range (i, num.length)
         while (j > i - 1 && num[j] <= num[i - 1]) j--;
         swap(num, i - 1, j);
         reverse(num, i, num.length - 1);
         try {
             return Integer.parseInt(new String(num));
         } catch(NumberFormatException noe) {
             System.out.println(noe.toString());
             return -1;
         }
   }

   private static void swap(char[] num, int i, int j) {
         char tmp = num[i];
         num[i] = num[j];
         num[j] = tmp;
   }

   private static void reverse(char[] num, int start, int end) {
      while(start < end) {
        swap(num, start, end);
        start++;
        end--;
      }
   }
}

#TLE if user permutation and sort the result

/////////////////////////////////////////////////////////////////////////////////////////////
  /* Time O(n!)
   * 1. Below algo use permutation way to get the next_bigger
   * getAllPermutation(): for any given number, it computes all permutation using given number
   * getRealNextBiggerIntegerByPermutation(): sort the result return by  getAllPermutation() and
   *  find the next big integer
   */

    // return the next big integer of number
    // the algo first get all the permutaions of that number to a list of integers
    // then sort the list and traverse the list to find the next big integer of given number
    // return -1 if not found
    public static int getRealNextBiggerIntegerByPermutation(int number){
        List<Integer> permutations;
        try{
           permutations = getAllPermutation(number);
        } catch(NumberFormatException noe) {
           //System.out.println(noe.toString());
           return -1;
        }
        Collections.sort(permutations);
        for (int i = 0; i < permutations.size(); i++) {
            if ( i + 1 < permutations.size() && permutations.get(i + 1) > number) {
                //System.out.println("ans" + permutations.get(i + 1));
                return permutations.get(i+1);
            }
        }
        return -1;
     }

     // given any number, get a list of all permutations in String type of the given number
     // return a list of interger type of the all permutations of that given number
     private static List<Integer> getAllPermutation(int number) {
       List<String> res = new LinkedList<>();
       String num = String.valueOf(number);
       getPerm(num.toCharArray(), new boolean[num.length()], new StringBuilder(), res);
       List<Integer> numbers = new LinkedList<>();
       for (String n : res) {
         try{
           numbers.add(Integer.parseInt(n));
         } catch(NumberFormatException noe) {
            throw noe;
         }
       }
       return numbers;
     }

    // backtrack to get all the permutation of "number" char array
    // save the result to a list of string
    private static void getPerm(char[] number, boolean[] used, StringBuilder sb, List<String> res) {
      if (sb.length() == number.length) {
        res.add(sb.toString());
        return;
      }

      for (int i = 0; i < number.length; i++) {
        if(!used[i]) {
          sb.append(number[i]);
          used[i] = true;
          getPerm(number, used, sb, res);
          sb.setLength(sb.length() - 1);
          used[i] = false;
        }
      }
    }

'''
