__source__ = 'https://leetcode.com/problems/next-greater-element-iii/description/'
# Time:  O(n)
# Space: O(n)
#
# Description: same as 556. Next Greater Element III
# //xinzyang@tesla.com
# // Next closest bigger number with the same digits
# // You have to create a function that takes a positive integer number and returns
#  the next bigger number formed by the same digits:
#
# // next_bigger(12)==21 //string for permutation
# // next_bigger(513)==531
# // next_bigger(2017)==2071
#
# // If no bigger number can be composed using those digits, return -1:
#
# // next_bigger(9)==-1
# // next_bigger(111)==-1
# // next_bigger(531)==-1
#

Result = '''
IFang Lee ran 238 lines of Java (finished in 11.59s):

getRealNextBiggerInteger():
12-> 21 true
513 -> 531 true
1342->  1423 true
534976-> 536479 true
9999-> -1 true
11-> -1 true
0-> -1 true
2147483647-> -1 true

getRealNextBiggerIntegerByPermutation():
12-> 21 true
513 -> 531 true
1342->  1423 true
534976-> 536479 true
9999-> -1 true
11-> -1 true
0-> -1 true
2147483647-> -1 true
'''

my_ans = '''
import java.io.*;
import java.util.*;

// 1. permutation -> worse big O (n!)
// 2. scan from the last digit, swap with the first smaller digit O(n)

public class Solution {
  public static void main(String[] args) {
     testNextBiggerInteger();
  }

  public static void testNextBiggerInteger() {
     int res1, res2;
     System.out.println("getRealNextBiggerInteger(): ");
     System.out.println("12-> " + (res2 = getRealNextBiggerInteger(12)) + " "
                        + (res2 == 21) + "");
     System.out.println("513 -> " + (res2 = getRealNextBiggerInteger(513)) + " "
                       + (res2 == 531) + "");
     System.out.println("1342->  " + (res2 = getRealNextBiggerInteger(1342)) + " "
                       + (res2 == 1423) + "");
     System.out.println("534976-> " + (res2 = getRealNextBiggerInteger(534976)) + " "
                       + (res2 == 536479) + "");

     //negative tests
     System.out.println("9999-> " + (res2 = getRealNextBiggerInteger(9999)) + " "
                       + (res2 == -1) + "");
     System.out.println("11-> " + (res2 = getRealNextBiggerInteger(11)) + " "
                        + (res2 == -1) + "");
     System.out.println("0-> " + (res2 = getRealNextBiggerInteger(0)) + " "
                        + (res2 == -1) + "");
     System.out.println("2147483647-> " + (res2 = getRealNextBiggerInteger(Integer.MAX_VALUE))+ " "
                        + (res2 == -1) + "");
     System.out.println("987654321-> " + (res1 = getRealNextBiggerInteger(987654321)) + " "
                      + (res1 == -1) + "");

     System.out.println();
     System.out.println("getRealNextBiggerIntegerByPermutation(): ");
     System.out.println("12-> " +  (res1 = getRealNextBiggerIntegerByPermutation(12)) + " "
                        + (res1 == 21) + "");
     System.out.println("513 -> " + (res1 = getRealNextBiggerIntegerByPermutation(513))+ " "
                       + (res1 == 531) + "");
     System.out.println("1342->  " + (res1 = getRealNextBiggerIntegerByPermutation(1342)) + " "
                       + (res1 == 1423) + "");
     System.out.println("534976-> " + (res1 = getRealNextBiggerIntegerByPermutation(534976)) + " "
                       + (res1 == 536479) + "");

    //negative tests
     System.out.println("9999-> " + (res1 = getRealNextBiggerIntegerByPermutation(9999)) + " "
                       + (res1 == -1) + "");
     System.out.println("11-> " + (res1 =  getRealNextBiggerIntegerByPermutation(11)) + " "
                        + (res1 == -1) + "");
     System.out.println("0-> " + (res1 = getRealNextBiggerIntegerByPermutation(0)) + " "
                        + (res1 == -1) + "");
     // significant long runtime (10982 milliseconds) for below test cases:
     System.out.println("2147483647-> " + (res1 = getRealNextBiggerIntegerByPermutation(Integer.MAX_VALUE))
                        + " "  + (res1 == -1) + "");
     // cannot run below: Stopped: CPU usage beyond threshold!
     // System.out.println("9876543210-> " + (res1 = getRealNextBiggerIntegerByPermutation(987654321)) + " "
     //                  + (res1 == -1) + "");

  }

  /////////////////////////////////////////////////////////////////////////////////////////////
  /* Time O(n)
   * 1. scan from the right, find the first digit larger than its right neighbor
   * 2. Within the range of (1) to right of the number, find a digit larger than(1)
   * 3. swap digit at (1) and (2)
   * 4. reverse the digit from index at (i) to the end of the digits
   * 5. return the result
   */

   public static int getRealNextBiggerInteger(int number){
     if (number < 0) throw new IllegalArgumentException("input must be positive integer");
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

     try { //check for overflow
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

  /////////////////////////////////////////////////////////////////////////////////////////////
  /* Time O(n!)
   * 1. Below algo use permutation way to get the next_bigger
   * getAllPermutation(): for any given number, it computes all permutation using given number
   * getRealNextBiggerIntegerByPermutation(): sort the result return by  getAllPermutation() and
   *  find the next big integer
   */

    // return the next big integer of number
    // the algo first get all the permutations of that number to a list of integers
    // then sort the list and traverse the list to find the next big integer of given number
    // return -1 if not found
    public static int getRealNextBiggerIntegerByPermutation(int number){
        if (number < 0) throw new IllegalArgumentException("input must be positive integer");
        List<Integer> permutations;
        try{
           permutations = getAllPermutation(number);
        } catch(NumberFormatException noe) { //overflow case
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


  /////////////////////////////////////////////////////////////////////////////////////////////
  // below not working version
    //starts with #2 scan from the last digit, swap with the first smaller digit O(n)
  // lets use int think of overflow later (with long)
  // the func does not work with 1342 -> returns 2341, but the correct ans = 1423
  public static int nextBiggerInteger(int number){ //12
    int num = number;
    int lastDigit = num % 10; //2
    num /= 10; //1
    StringBuilder sb = new StringBuilder();
    while (num > 0) { //loop throw numbers from last digits
        int next = num % 10;  //1

        if ( next < lastDigit) { //swap next and lastDigit
           num = (num / 10) * 10  +  lastDigit;
           sb.reverse().append(next);
           break;
        }
        sb.append(next);
        num /= 10;
    }
    // add num with sb
    String rest = sb.toString();
    //System.out.println(rest);
    int restInt = 0;
    if (rest != null && rest.length() > 0) {
      try{
          restInt = Integer.parseInt(rest); // none
      }catch(NumberFormatException noe) {
         System.out.println(noe.toString());
         restInt = 0;
      }

      for (int i = 0; i < rest.length(); i++) {
        num *= 10;
      }
    }


    num += restInt;
    return num  > number ? num  :  -1;
  }
  /////////////////////////////////////////////////////////////////////////////////////////////
}
'''

