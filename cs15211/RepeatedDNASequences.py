__source__ = 'https://leetcode.com/problems/repeated-dna-sequences/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/repeated-dna-sequences.py
# Time:  O(n)
# Space: O(n)
# Rabin-Karp algorithm, Rolling Hash
#
# Description: Leetcode # 187. Repeated DNA Sequences
#
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
# for example: "ACGAATTCCG".
# When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings)
# that occur more than once in a DNA molecule.
#
# For example,
#
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
#
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].
#
# Companies
# LinkedIn
# Related Topics
# Hash Table Bit Manipulation
#
import collections
import unittest
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
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        #print Solution().findRepeatedDnaSequences("AAAAAAAAAA")
        #print Solution().findRepeatedDnaSequences("")
        print Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
        print Solution2().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")

        print int("0x3fffffff", 16)
        print format(1073741823, 'b')
        print bin(7&5), bin(0|2), bin(ord('A')), bin(ord('C')), bin(ord('G')), bin(ord('T'))
        print "A: ", bin(ord('A') & 7), "C: ", bin(ord('C') & 7), " G: ", bin(ord('G') & 7), " T: " , bin(ord('T') & 7)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# Hashset + bitmap
# 16ms 97.56%
class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        List<String> ret = new ArrayList<>();
        int len = s.length();
        if (len < 11) {
            return ret;
        }
        int[] bitLabel = new int[255];
        bitLabel['A'] = 0;
        bitLabel['C'] = 1;
        bitLabel['G'] = 2;
        bitLabel['T'] = 3;
        int[] nums = new int[len];
        int[] exist = new int[1024 * 1024];
        char[] schars = s.toCharArray();
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j <= i; j++) {
                nums[j] <<= 2;
                nums[j] |= bitLabel[schars[i]];
            }
        }
        for (int i = 9; i < len; i++) {
            for (int j = i - 9; j <= i; j++) {
                nums[j] <<= 2;
                nums[j] |= bitLabel[schars[i]];
            }
            if (exist[nums[i - 9]]++ == 1) {
                ret.add(s.substring(i - 9, i + 1));
            }
        }
        return ret;
    }
}


# 21ms 80%
class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        Set<Integer> firstShown = new HashSet<>();
        Set<Integer> secShown = new HashSet<>();
        List<String> res = new ArrayList<>();
        char[] map = new char[26];
        //map['A' - 'A'] = 0;
        map['C' - 'A'] = 1; //001
        map['G' - 'A'] = 2; //010
        map['T' - 'A'] = 3; //011

        for(int i = 0; i < s.length() - 9; i++) {
            int v = 0;
            for (int j = i; j < i + 10; j++) {
                v <<= 2; //4 bin(100)
                v |= map[s.charAt(j) - 'A'];
            }
            if (!firstShown.add(v) && secShown.add(v)) {
                res.add(s.substring(i, i + 10));
            }
            //System.out.println(firstShown.toString());
            //System.out.println(secShown.toString());
        }
        return res;
    }
}

# 18ms 92.09%
class Solution {
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

# Rolling Hash
# 38ms 23.67%
class Solution {
    private static final Map<Character, Integer> A = new HashMap<>();
    static { A.put('A',0); A.put('C',1); A.put('G',2); A.put('T',3); }
    private final int A_SIZE_POW_9 = (int) Math.pow(A.size(), 9);

    public List<String> findRepeatedDnaSequences(String s) {
        Set<String> res = new HashSet<>();
        Set<Integer> hashes = new HashSet<>();
        for (int i = 0, rhash = 0; i < s.length(); i++) {
            if (i > 9) rhash -= A_SIZE_POW_9 * A.get(s.charAt(i-10));
            rhash = A.size() * rhash + A.get(s.charAt(i));
            if (i > 8 && !hashes.add(rhash)) res.add(s.substring(i-9,i+1));
        }
        return new ArrayList<>(res);
    }
}

# BruteForce
# 27ms 53.69%
class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        Set seen = new HashSet(), repeated = new HashSet();
        for (int i = 0; i + 9 < s.length(); i++) {
            String ten = s.substring(i, i + 10);
            if (!seen.add(ten))
                repeated.add(ten);
        }
        return new ArrayList(repeated);
    }
}
'''
