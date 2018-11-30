__source__ = 'https://leetcode.com/problems/unique-morse-code-words/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 804. Unique Morse Code Words
# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes,
# as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.
#
# For convenience, the full table for the 26 letters of the English alphabet is given below:
#
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter.
# For example, "cba" can be written as "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-").
# We'll call such a concatenation, the transformation of a word.
#
# Return the number of different transformations among all words we have.
#
# Example:
# Input: words = ["gin", "zen", "gig", "msg"]
# Output: 2
# Explanation:
# The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
#
# There are 2 different transformations, "--...-." and "--...--.".
# Note:
#
# The length of words will be at most 100.
# Each words[i] will have length in range [1, 12].
# words[i] will only consist of lowercase letters.
#
import unittest

# 24ms, 87.72%
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]

        seen = {"".join(MORSE[ord(c) - ord('a')] for c in word) for word in words}
        return len(seen)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/unique-morse-code-words/solution/
# Approach #1: Hash Set [Accepted]
#
# Time Complexity: O(S), where S is the sum of the lengths of words in words.
# We iterate through each character of each word in words.
# Space Complexity: O(S)
#
# 100% 5ms
class Solution {
    public int uniqueMorseRepresentations(String[] words) {
         String[] MORSE = new String[]{".-","-...","-.-.","-..",".","..-.","--.",
                         "....","..",".---","-.-",".-..","--","-.",
                         "---",".--.","--.-",".-.","...","-","..-",
                         "...-",".--","-..-","-.--","--.."};

        Set<String> seen = new HashSet<>();
        for (String word : words) {
            StringBuilder code = new StringBuilder();
            for (char c: word.toCharArray()) {
                code.append(MORSE[c - 'a']);
            }
            seen.add(code.toString());
        }
        return seen.size();
    }
}

#90.28% 6ms
class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        String [] morse = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."} ;
        HashMap <String,Integer > table = new <String,Integer> HashMap();
        for (int i =0 ; i <words.length; i++){
            char[] word = words[i].toCharArray() ;
            String st = "" ;
            for (int j= 0 ; j <word.length ; j++) {

                int a = alphabet.indexOf(word[j]) ;
                st+=morse[a] ;

            }
             if(table.containsKey(st)){
                   table.put(st, table.get(st)+1) ;
                }
                else {
                    table.put(st,1) ;
                }

        }
         return table.size() ;
    }
}
'''