
__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/substring-with-concatenation-of-all-words.py
# Time:  O(m * n * k), where m is string length, n is dictionary size, k is word length
# Space: O(n * k)
#
# You are given a string, S, and a list of words, L, that are all of the same length.
# Find all starting indices of substring(s) in S that is a concatenation of each word
# in L exactly once and without any intervening characters.
#
# For example, given:
# S: "barfoothefoobarman"
# L: ["foo", "bar"]
#
# You should return the indices: [0,9].
# (order does not matter).
# Hash Table Two Pointers String

class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        result, words, word_num, word_len = [], {}, len(L), len(L[0])
        for i in L:
            if i not in words:
                words[i] = 1
            else:
                words[i] += 1

        for i in xrange(len(S) + 1 - word_len * word_num):
            cur, j = {}, 0
            while j < word_num:
                word = S[i + j * word_len : i + j * word_len + word_len]
                if word not in words:
                    break
                if word not in cur:
                    cur[word] = 1
                else:
                    cur[word] += 1
                if cur[word] > words[word]:
                    break
                j += 1

            if j == word_num:
                result.append(i)
        return result

if __name__ == "__main__":
    print Solution().findSubstring("barfoothefoobarman", ["foo", "bar"])

class SolutionOther:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    # http://chaoren.is-programmer.com/posts/43297.html
    def findSubstring(self, S, L):
        lenS = len(S)
        lenL = len(L)
        lenWord = len(L[0])
        res = []

        for start in xrange(lenS - lenWord * lenL + 1):
            listS = [S[i: i + lenWord] for i in xrange(start, start + lenL*lenWord, lenWord)]
            found = True

            for item in L:
                if item in listS:
                    listS.remove(item)
                else:
                    found = False
                    break
            if found:
                res.append(start)
        return res
#test
test = SolutionOther()
S = "barfoothefoobarman"
L = ["foo", "bar"]
print test.findSubstring(S, L)

#java
js = '''
public class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> result = new ArrayList<>();
        int wordCount = words.length;
        int wordLen = wordCount == 0 ? 0 : words[0].length();
        if (wordCount == 0 || wordLen == 0 || s.length() < wordCount * wordLen) {
            return result;
        }
        Map<String, Integer> wordDict = buildDict(words);
        for (int i = 0; i < wordLen; i++) {
            Map<String, Integer> curDict = new HashMap<>();
            int start = i;
            int end = i;
            int count = 0;
            while (end <= s.length() - wordLen) {
                String curWord = s.substring(end, end + wordLen);
                if (wordDict.containsKey(curWord)) {
                    addOne(curDict, curWord);
                    count++;
                    if (curDict.get(curWord) > wordDict.get(curWord)) {
                        while (start < end) {
                            String removeWord = s.substring(start, start + wordLen);
                            minusOne(curDict, removeWord);
                            count--;
                            start += wordLen;
                            if (removeWord.equals(curWord)) {
                                break;
                            }
                        }
                    } else if (count == wordCount) {
                        result.add(start);
                        minusOne(curDict, s.substring(start, start + wordLen));
                        count--;
                        start += wordLen;
                    }
                } else {
                    curDict.clear();
                    start = end + wordLen;
                    count = 0;
                }
                end += wordLen;
            }
        }
        return result;
    }

    private Map<String, Integer> buildDict(String[] words) {
        Map<String, Integer> map = new HashMap<>();
        for (String word : words) {
            addOne(map, word);
        }
        return map;
    }

    private void addOne(Map<String, Integer> map, String word) {
        Integer val = map.get(word);
        map.put(word, val == null ? 1 : val + 1);
    }

    private void minusOne(Map<String, Integer> map, String word) {
        Integer val = map.get(word);
        if (val == null || val == 1) {
            map.remove(word);
        } else {
            map.put(word, val - 1);
        }
    }
}

// 137ms
public class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> res = new ArrayList<>();
        int word_cnt = words.length;
        int oneWord = word_cnt == 0 ? 0 : words[0].length();
        int ttl = word_cnt * oneWord;

        if ( s == null || s.length() < ttl  || word_cnt == 0) return res;

        for (int i = 0; i <= s.length() - ttl; i++){
            int j = i;
            List<String> cur = new ArrayList<>();
            boolean found = true;
            while(j + oneWord <= i + ttl){
                cur.add(s.substring(j, j + oneWord));
                j += oneWord;
            }

            for(String word : words){
                if(cur.contains(word)){
                    cur.remove(word);
                }else{
                    found = false;
                    break;
                }
            }
            if(found == true){
                res.add(i);
            }
        }
        return res;
    }
}

//29ms
public class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> res = new ArrayList<>();
        int word_cnt = words.length;
        int oneWord = word_cnt == 0 ? 0 : words[0].length();
        int ttl = word_cnt * oneWord;

        if ( s == null || s.length() < ttl  || word_cnt == 0) return res;

        for(int i = 0; i < oneWord; i++){
            Map<String, Integer> map = new HashMap<>();
            for(String word : words){
                if(!map.containsKey(word)){
                    map.put(word, 0);
                }
                map.put(word, map.get(word) + 1);
            }

            int start = i;
            int cur = start;
            int cnt = 0;

            while(cur + oneWord <= s.length()){
                String w = s.substring(cur, cur + oneWord);
                if( !map.containsKey(w) || map.get(w) <= 0){
                    String replace = s.substring(start,start + oneWord);

                    if(map.containsKey(replace)){
                        map.put(replace, map.get(replace) + 1);
                        cnt --;
                    }

                    start += oneWord;
                    if(cur < start) cur = start;
                }else{
                    map.put(w, map.get(w) - 1);
                    cnt ++;

                    if(cnt == word_cnt){
                        res.add(start);
                    }
                    cur += oneWord;
                }

            }
        }
       return res;

    }

}
'''