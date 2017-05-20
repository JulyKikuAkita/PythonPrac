__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/repeated-dna-sequences.py

# Time:  O(n)
# Space: O(n)
#
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
# for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
#
# For example,
#
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
#
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].
#
# LinkedIn
# Hide Tags Hash Table Bit Manipulation


class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        dict = {}
        rolling_hash = 0
        res = []

        for i in xrange(len(s)):  # 0x3fffffff == max signed int? 31 bits of 1 ; bin(7) = 111
            # 0 | int = int; 7 & int = int
            print i, bin(rolling_hash), oct(rolling_hash)
            rolling_hash = rolling_hash << 3 & 0x3fffffff | ord(s[i]) & 7   #ord('A') -ord('z') -> 65- 122
            if dict.get(rolling_hash) is None:
                dict[rolling_hash] = True
            else:
                if dict[rolling_hash]:
                    res.append(s[i - 9: i + 1]) # append char to i
                    dict[rolling_hash] = False
        return res

import collections
class Solution2:
    # @param s, a string
    # @return a list of strings
    # http://ludovf.net/blog/python-collections-defaultdict/ intro to defaultdict
    '''
     A defaultdict is just like a regular Python dict, except that it supports an additional argument at initialization: a function.
     If someone attempts to access a key to which no value has been assigned, that function will be called (without arguments)
     and its return value is used as the default value for the key.
    '''
    def findRepeatedDnaSequences(self, s):
        # sequences = {}, which throw KeyError if not initialized or you can use collections.defaultdict(int)
        sequences = collections.defaultdict(int) #set '0' as the default value for non-existing keys
        for i in range(len(s)):
            sequences[s[i:i+10]] += 1#add 1 to the count
        return [key for key, value in sequences.iteritems() if value > 1] #extract the relevant keys

#test
if __name__ == "__main__":
    #print Solution().findRepeatedDnaSequences("AAAAAAAAAA")
    #print Solution().findRepeatedDnaSequences("")
    print Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
    print Solution2().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")

    print int("0x3fffffff", 16)
    print format(1073741823, 'b')
    print bin(7&5), bin(0|2), bin(ord('A')), bin(ord('C')), bin(ord('G')), bin(ord('T'))
    print "A: ", bin(ord('A') & 7), "C: ", bin(ord('C') & 7), " G: ", bin(ord('G') & 7), " T: " , bin(ord('T') & 7)

#java

js = '''
public class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        List<String> result = new ArrayList<>();
        if (s.length() <= 10) {
            return result;
        }
        Map<Integer, Boolean> map = new HashMap<>();
        int cur = 0;
        for (int i = 0; i < 9; i++) {
            cur <<= 2;
            cur |= encode(s.charAt(i));
        }
        for (int i = 9; i < s.length(); i++) {
            cur <<= 2;
            cur |= encode(s.charAt(i));
            cur &= 0xfffff;
            if (map.containsKey(cur)) {
                if (!map.get(cur)) {
                    map.put(cur, true);
                    result.add(s.substring(i - 9, i + 1));
                }
            } else {
                map.put(cur, false);
            }
        }
        return result;
    }

    private int encode(char c) {
        switch (c) {
            case 'A':
                return 0;
            case 'C':
                return 1;
            case 'G':
                return 2;
            case 'T':
                return 3;
            default:
                return 0;
        }
    }
}


public class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        List<String> res = new ArrayList<>();
        Map<Integer, Boolean> map = new HashMap<>();
        int cur = 0;
        for (int i = 0; i < s.length(); i++){
            cur = cur << 3 & 0x3FFFFFFF | ((s.charAt(i) - '0') & 7);
            if(!map.containsKey(cur)){
                map.put(cur, true);
            }else{
                if(map.get(cur) == true){
                    res.add(s.substring(i - 9, i + 1));
                    map.put(cur, false);
                }

            }
        }
        return res;
    }
}
'''