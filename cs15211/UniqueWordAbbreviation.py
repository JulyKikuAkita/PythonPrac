import collections

__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/unique-word-abbreviation.py
'''
An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary.
A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example:
Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true
# google
'''


# Time:  ctor:   O(n), n is number of words in the dictionary.
#        lookup: O(1)
# Space: O(k), k is number of unique words.

class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.lookup_ = collections.defaultdict(set)
        for word in dictionary:
            abbr = self.abbreviation(word)
            self.lookup_[abbr].add(word)

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        if not word or len(word) == 0:
            return True
        l = len(word)
        abbr = self.abbreviation(word)
        return self.lookup_[abbr] <= {word}

    def abbreviation(self, word):
        #return word[0] + str(len(word[1:len(word)-1])) + word[-1]
        if not word or len(word) == 0:
            return ""
        return word[0] + str(len(word)) + word[-1]

# Your ValidWordAbbr object will be instantiated and called as such:
#dictionary = [ "deer", "door", "cake", "card", "word" ]
dictionary = [ "" ]
if __name__ == "__main__":
    vwa = ValidWordAbbr(dictionary)
    print vwa.isUnique("word")
    print vwa.isUnique("anotherWord")
    print vwa.isUnique("")


#java
js = '''
public class ValidWordAbbr {
    private Map<String, Integer> wordsAbbr = new HashMap<>();
    private Set<String> wordsSet = new HashSet<>();

    public ValidWordAbbr(String[] dictionary) {
        for (String word : dictionary) {
            if (wordsSet.contains(word)) {
                continue;
            }
            String abbr = getAbbr(word);
            if (!wordsAbbr.containsKey(abbr)) {
                wordsAbbr.put(abbr, 1);
            } else {
                wordsAbbr.put(abbr, wordsAbbr.get(abbr) + 1);
            }
            wordsSet.add(word);
        }
    }

    public boolean isUnique(String word) {
        String abbr = getAbbr(word);
        return word.length() < 3 || !wordsAbbr.containsKey(abbr) || (wordsSet.contains(word) && wordsAbbr.get(abbr) == 1);
    }

    private String getAbbr(String word) {
        if (word == null || word.length() < 3) {
            return word;
        }
        StringBuilder sb = new StringBuilder();
        sb.append(word.charAt(0));
        sb.append(word.length() - 2);
        sb.append(word.charAt(word.length() - 1));
        return sb.toString();
    }
}


// Your ValidWordAbbr object will be instantiated and called as such:
// ValidWordAbbr vwa = new ValidWordAbbr(dictionary);
// vwa.isUnique("Word");
// vwa.isUnique("anotherWord");
'''
