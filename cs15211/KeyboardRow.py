# Given a List of words, return the words that can be typed using letters of alphabet on
# only one row's of American keyboard like the image below.
# https://leetcode.com/problems/keyboard-row/#/description
# Example 1:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
# Note:
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.
# Hide Company Tags Mathworks
# Hide Tags Hash Table
#
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        ret = []
        for word in words:
          w = set(word.lower())
          if w.issubset(line1) or w.issubset(line2) or w.issubset(line3):
            ret.append(word)
        return ret

java  = '''
public class Solution {
    public String[] findWords(String[] words) {
        return Stream.of(words).filter(s -> s.toLowerCase().matches("[qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*")).toArray(String[]::new);
    }
}

public class Solution {
    public String[] findWords(String[] words) {
        String[] groups = {"qwertyuiop","asdfghjkl","zxcvbnm"};
        Map<Character, Integer> map = new HashMap<>();
        for(int i = 0; i < groups.length; i++){
            for(char c: groups[i].toCharArray()){
                map.put(c, i);//put <char, rowIndex> pair into the map
            }
        }

        List<String> res = new LinkedList<>();
        for (String word : words) {
            if (word.equals("")) continue;
            int group = map.get(word.toLowerCase().charAt(0));
            for (char c : word.toLowerCase().toCharArray()){
                if (map.get(c) != group) {
                    group = -1;
                    break;
                }
            }
            if (group != -1) res.add(word);
        }
        return res.toArray(new String[0]);

    }
}
'''