__source__ = ''
# Time:  O()
# Space: O()
#
# Description:
#
import unittest


class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
#Sales Force:
# Write a function reverse the words in a string
# eg: "Today is Tuesday"
# returns : "yadoT si yadseuT"

public String reverseString(String s){
    // corner case
    if(s == null || s.length() == 0){
        return null;
    }

    s = s.trim();
    String[] cur = s.split(" ");  // Today is Tuesday
    StringBuilder sb = new StringBuilder();
    for(int i = 0; i < cur.length; i++){
        String tmp = reverseWord(cur[i]);
        sb.append(tmp);
        sb.append(" ");
    }
    sb.deleteCharAt(sb.length()-1);
    return sb.toString();

}

private String reverseWord(String s){

    int start = 0;
    int end = s.length()-1;
    char[] chars = s.toCharArray();
    while(start < end){ // double check for out of index  //(start + end) / 2
        swap(chars, start, end);
        start++;
        end--;
    }
    return new String(chars);

}

private void swap(char[] chars, int start, int end){
    char tmp = chars[start];
    chars[start] = chars[end];
    chars[end] = tmp;
}

'''