__source__ = ''
# Time:  O()
# Space: O()
#
# Description:
# if with duplication, use hashset to remove re-permutate duplicate, otherwise, see same result
# if permutation, need to keep track used index, otherwise, for permute say "12!" the result may get "!!!"

Java = '''
#Thought:
import java.util.*;

/*
Often, we want to encode raw IDs in our database by hiding them behind some 2-way decodeable hash.
So, a URL which would have at one time been:

https://www.twitch.tv/users/848662

becomes

https://www.twitch.tv/users/kljJJ324hjkS_

We decode the ID kljJJ324hjkS_ to 848662 on our backend and serve the relevant content.
At some point, we start getting 404 errors from clients requesting a certain URL of the form

https://www.twitch.tv/users/kljJJ324hjkS_

This can happen if certain clients, email services, or url shorteners "sanitize" the url. Unfortunately,
this change breaks decoding and the resource cannot be found.
To assess how big of a deal this is, we may want to recover the IDs of the targets that were 404ing.

Your task:
Given a method decode(testEncStr) which will return the decoded int id if testEncStr is decodeable
else will throw an exception or return null (depending on the language),
implement a new method decodeFind(String badEncStr) which takes a string and returns the decoded int id.
*/

class Solution {
  public static class BadIdException extends Exception {
    private static final long serialVersionUID = 1;
    public BadIdException(String message) {
      super(message);
    }
  }

  public static void main(String[] args) {
    System.out.println("Decoded to id: " + decodeFind("a$bb_"));
    System.out.println("Decoded to id: " + decodeFindUpperLowerOnly("a$bb_"));
    //System.out.println("Decoded to id: " + decodeFind("kljJJ324hjks_"));

  }

  // Black box. Can't modify. You get this.
  private static int decode(String testEncStr) throws BadIdException {
    // System.out.println("Testing " + testEncStr);
    if (testEncStr.equals("kljJJ324hjkS_")) { //orig: "kljJJ324hjkS_"
      return 848662;
    } else {
      throw new BadIdException(testEncStr + " not found");
    }
  }

  // you implement this
  //get permutation + upper/lower
  public static int decodeFind(String badEncStr)
  {
    List<String> res = genPerm(badEncStr);
    for (String s : res) {
      try{
        System.out.println(s);
        return decode(s);
      } catch(BadIdException be){
        //do nothing
      }
    }

    return -1;
  }

  // you implement this
  public static int decodeFindUpperLowerOnly(String badEncStr)
  {
    HashSet<String> res = new HashSet<>();
    genUpperLower(badEncStr.toCharArray(), 0, res);

    for (String s : res) {
      try{
        System.out.println(s);
        return decode(s);
      } catch(BadIdException be){
        //do nothing
      }
    }

    return -1;
  }

  //toggle upper lower case
  public static void genUpperLower(char[] arr, int index, HashSet<String> res) {
    if ( index == arr.length && !res.contains(new String(arr))) {
      res.add(new String(arr));
      return;
    }

    for (int i = index; i < arr.length; i++) {
    char origin = arr[i];
    if ( !Character.isLetter(origin) && i != arr.length -1) continue;

    char[] holder = new char[]{ Character.toUpperCase(origin), Character.toLowerCase(origin)};
    for (char c : holder){
            arr[i] = c;
            genUpperLower( arr, i+1, res);
            arr[i] = origin;
    }

    }

  }

  //all string permutation
  public static List<String> genPerm(String input) {
        List<String> result = new ArrayList<>();
        doGenPerm(input.toCharArray(), new StringBuilder(), new boolean[input.length()], result);
        return result;
    }

    private static void doGenPerm(char[] arr, StringBuilder sb, boolean[] used, List<String> result) {
        if (sb.length() == arr.length) {
            result.add(sb.toString());
        } else {
            Set<Character> s = new HashSet<>();
            for (int i = 0; i < arr.length; i++) {
                char c = arr[i];
                if (!used[i] && !s.contains(c)){ // use all unique characters once
                    used[i] = true;

                    s.add(c);
                    sb.append(c);
                    doGenPerm(arr, sb, used, result); // original case and non-alphabets
                    sb.setLength(sb.length() - 1);

                    if (Character.isAlphabetic(c)) { // non-alphabets won't need case transition
                        char otherCase = Character.isLowerCase(c) ?
                          Character.toUpperCase(c) : Character.toLowerCase(c);
                        s.add(otherCase);
                        sb.append(otherCase);
                        doGenPerm(arr, sb, used, result);
                        sb.setLength(sb.length() - 1);
                    }
                    used[i] = false;
                }
            }
        }
    }


  // you think it is done?.. Done, all fixed... found bug and fixed
  //it's a combination not permutation, so it fails when there's duplicates
   // //now only works with say "abc1" but not 'abb1"
  //Hmmm. may be the your algo can be updated. but if u can decode this sample set, i am fine with it.
  // Thanks!!! XD , I'm going to review it later today, definitely done this before in school hehehe,
  just too ancient. but anyway thanks for the good questions!!!!

  // no worries. thx bye
  //bye

  // you need to match for example ; aBc1 - id 12345
  // Input string is ABC1  ; AABB
  // permutations are : abc1, abC1, aBc1, aBC1, Abc1, .......

}

output:
a$bb_
a$bB_
a$b_b
a$b_B
a$Bb_
a$BB_
a$B_b
a$B_B
a$_bb
a$_bB
a$_Bb
a$_BB
ab$b_
ab$B_
ab$_b
ab$_B
abb$_
abb_$
abB$_
abB_$
ab_$b
ab_$B
ab_b$
ab_B$
aB$b_
aB$B_
aB$_b
aB$_
...
_b$BA
_bba$
_bbA$
_bb$a
_bb$A
_bBa$
_bBA$
_bB$a
_bB$A
_Ba$b
_Ba$B
_Bab$
_BaB$
_BA$b
_BA$B
_BAb$
_BAB$
_B$ab
_B$aB
_B$Ab
_B$AB
_B$ba
_B$bA
_B$Ba
_B$BA
_Bba$
_BbA$
_Bb$a
_Bb$A
_BBa$
_BBA$
_BB$a
_BB$A
Decoded to id: -1
a$BB_
a$Bb_
a$bB_
a$bb_
A$BB_
A$Bb_
A$bB_
A$bb_
Decoded to id: -1

'''