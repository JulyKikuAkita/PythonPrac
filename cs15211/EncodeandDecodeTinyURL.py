__source__ = 'https://leetcode.com/problems/encode-and-decode-tinyurl/#/description'
# Note: This is a companion problem to the System Design problem: Design TinyURL.
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 535. Encode and Decode TinyURL
#
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl
# and it returns a short URL such as http://tinyurl.com/4e9iAk.
#
# Design the encode and decode methods for the TinyURL service.
# There is no restriction on how your encode/decode algorithm should work.
# You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
#
# Hide Company Tags Amazon Google Uber Facebook
# Hide Tags Hash Table Math
# Hide Similar Problems (M) Design TinyURL
#

# below is the tiny url solution in java, also this is the similar method in industry.
# In industry, most of shorten url service is by database, one auto increasing long number as primary key.
# whenever a long url need to be shorten, append to the database, and return the primary key number.
# (the database is very easy to distribute to multiple machine like HBase,
# or even you can use the raw file system to store data and improve performance by shard and replica).
# Note, it's meaningless to promise the same long url to be shorten as the same short url.
# If you do the promise and use something like hash to check existing, the benefit is must less than the cost.
# Note: if you want the shorted url contains '0-9a-zA-Z' instead of '0-9', then you need to use 62 number system,
# not 10 number system(decimal) to convert the primary key number. like 123->'123' in decimal,
# 123->'1Z' in 62 number system (or '0001Z' for align).

# https://discuss.leetcode.com/topic/81637/two-solutions-and-thoughts
# Analysis of pros and cons for each decode/encode method:
#
# My first solution produces short URLs like http://tinyurl.com/0, http://tinyurl.com/1, etc, in that order.
import random
import string
import unittest
class Codec:

    def __init__(self):
        self.urls = []

    def encode(self, longUrl):
        self.urls.append(longUrl)
        return 'http://tinyurl.com/' + str(len(self.urls) - 1)

    def decode(self, shortUrl):
        return self.urls[int(shortUrl.split('/')[-1])]

#Using increasing numbers as codes like that is simple but has some disadvantages, which the below solution fixes:
#
# If I'm asked to encode the same long URL several times, it will get several entries. That wastes codes and memory.
# People can find out how many URLs have already been encoded. Not sure I want them to know.
# People might try to get special numbers by spamming me with repeated requests shortly
# before their desired number comes up.
# Only using digits means the codes can grow unnecessarily large.
# Only offers a million codes with length 6 (or smaller).
# Using six digits or lower or upper case letters would offer (10+26*2)6 = 56,800,235,584 codes with length 6.
# The following solution doesn't have these problems.
# It produces short URLs like http://tinyurl.com/KtLa2U,
# using a random code of six digits or letters. If a long URL is already known,
# the existing short URL is used and no new entry is generated.

class Codec2:

    alphabet = string.ascii_letters + '0123456789'

    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        while longUrl not in self.url2code:
            code = ''.join(random.choice(Codec.alphabet) for _ in range(6))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return 'http://tinyurl.com/' + self.url2code[longUrl]

    def decode(self, shortUrl):
        return self.code2url[shortUrl[-6:]]
# It's possible that a randomly generated code has already been generated before.
# In that case, another random code is generated instead.
# Repeat until we have a code that's not already in use.
# How long can this take? Well, even if we get up to using half of the code space,
# which is a whopping 626/2 = 28,400,117,792 entries, then each code has a 50% chance of not having appeared yet.
# So the expected/average number of attempts is 2, and for example
# only one in a billion URLs takes more than 30 attempts.
#  And if we ever get to an even larger number of entries and this does become a problem,
# then we can just use length 7. We'd need to anyway, as we'd be running out of available codes.

class TestMethods(unittest.TestCase):
    def test_Local(self):
        pass # write  your test

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/encode-and-decode-tinyurl/solution/

# 8ms 50.93%
class Codec {
    List<String> urls = new ArrayList<String>();
    // Encodes a URL to a shortened URL.
    public String encode(String longUrl) {
        urls.add(longUrl);
        return String.valueOf(urls.size()-1);
    }

    // Decodes a shortened URL to its original URL.
    public String decode(String shortUrl) {
        int index = Integer.valueOf(shortUrl);
        return (index<urls.size())?urls.get(index):"";
    }
}

Three different approaches in java

Approach 1- Using simple counterApproach #1 Using Simple Counter[Accepted]

In order to encode the URL, we make use of a counter(i),
which is incremented for every new URL encountered.
We put the URL along with its encoded count(i) in a HashMap.
This way we can retrieve it later at the time of decoding easily.

# 12ms 27.54%
class Codec {
    Map<Integer, String> map = new HashMap<>();
    int i=0;
    public String encode(String longUrl) {
        map.put(i,longUrl);
        return "http://tinyurl.com/"+i++;
    }
    public String decode(String shortUrl) {
        return map.get(Integer.parseInt(shortUrl.replace("http://tinyurl.com/", "")));
    }
}

Performance Analysis:
1. The range of URLs that can be decoded is limited by the range of int
2. If excessively large number of URLs have to be encoded, after the range of int is exceeded,
integer overflow could lead to overwriting the previous URLs' encodings,
leading to the performance degradation.
3. The length of the URL isn't necessarily shorter than the incoming longURL.
It is only dependent on the relative order in which the URLs are encoded.
4. One problem with this method is that it is very easy to predict the next code generated,
since the pattern can be detected by generating a few encoded URLs.

Approach #2 Variable-length Encoding[Accepted] Base62 encoding

Algorithm

In this case, we make use of variable length encoding to encode the given URLs.
For every longURL, we choose a variable codelength for the input URL,
which can be any length between 0 and 61.
Further, instead of using only numbers as the Base System for encoding the URLSs,
we make use of a set of integers and alphabets to be used for encoding.

# 10ms 45.06%
class Codec {
    String chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    Map<String, String> map = new HashMap<>();
    int count = 1;
    String shortName = "http://tinyurl.com/";

    public String getString() {
        int c = count;
        StringBuilder sb = new StringBuilder();
        while (c > 0) {
            c--;
            sb.append(chars.charAt(c % 62));
            c /= 62;
        }
        return sb.toString();
    }


    // Encodes a URL to a shortened URL.
    public String encode(String longUrl) {
        String key = getString();
        map.put(key, longUrl);
        count++;
        return shortName + key;
    }

    // Decodes a shortened URL to its original URL.
    public String decode(String shortUrl) {
        String key = shortUrl.replace(shortName, "");
        return map.get(key);
    }
}

Performance Analysis
-The number of URLs that can be encoded is, again, dependent on the range of int,
since, the same count will be generated after overflow of integers.
-The length of the encoded URLs isn't necessarily short,
but is to some extent dependent on the order in which the incoming longURL's are encountered.
For example, the codes generated will have the lengths in the following order: 1(62 times), 2(62 times) and so on.
-The performance is quite good, since the same code will be repeated only after the integer overflow limit, which is quite large.
-In this case also, the next code generated could be predicted by the use of some calculations.

Approach #3 Using hashcode[Accepted]

# 15ms 15.56%
class Codec {
    Map<Integer, String> map = new HashMap<>();

    public String encode(String longUrl) {
        map.put(longUrl.hashCode(), longUrl);
        return "http://tinyurl.com/" + longUrl.hashCode();
    }

    public String decode(String shortUrl) {
        return map.get(Integer.parseInt(shortUrl.replace("http://tinyurl.com/", "")));
    }
}

Performance Analysis

-The number of URLs that can be encoded is limited by the range of int, since hashCode uses integer calculations.
-The average length of the encoded URL isn't directly related to the incoming longURL length.
-The hashCode() doesn't generate unique codes for different string.
-This property of getting the same code for two different inputs is called collision.
Thus, as the number of encoded URLs increases, the probability of collisions increases, which leads to failure.


Approach #4 Using random number[Accepted]

# 14ms 17.85%
class Codec {
    Map<Integer, String> map = new HashMap<>();
    Random r=new Random();
    int key=r.nextInt(10000);
    public String encode(String longUrl) {
        while(map.containsKey(key))
            key= r.nextInt(10000);
        map.put(key,longUrl);
        return "http://tinyurl.com/"+key;
    }
    public String decode(String shortUrl) {
        return map.get(Integer.parseInt(shortUrl.replace("http://tinyurl.com/", "")));
    }
}

Performance Analysis

-The number of URLs that can be encoded is limited by the range of int.
-The average length of the codes generated is independent of the longURL's length, since a random integer is used.
-The length of the URL isn't necessarily shorter than the incoming longURL.
It is only dependent on the relative order in which the URLs are encoded.
-Since a random number is used for coding, again, as in the previous case,
the number of collisions could increase with the increasing number of input strings,
leading to performance degradation.
-Determining the encoded URL isn't possible in this scheme, since we make use of random numbers.


Approach #5 Random fixed-length encoding[Accepted]

Algorithm

In this case, again, we make use of the set of numbers and alphabets to generate the coding for the given URLs,
similar to Approach 2. But in this case, the length of the code is fixed to 6 only.
Further, random characters from the string to form the characters of the code.
In case, the code generated collides with some previously generated code, we form a new random code.

# 12ms 27.54%
class Codec {
    String alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    HashMap<String, String> map = new HashMap<>();
    Random rand = new Random();
    String key = getRand();

    public String getRand() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 6; i++) {
            sb.append(alphabet.charAt(rand.nextInt(62)));
        }
        return sb.toString();
    }

    public String encode(String longUrl) {
        while (map.containsKey(key)) {
            key = getRand();
        }
        map.put(key, longUrl);
        return "http://tinyurl.com/" + key;
    }

    public String decode(String shortUrl) {
        return map.get(shortUrl.replace("http://tinyurl.com/", ""));
    }
}

Performance Analysis

The number of URLs that can be encoded is quite large in this case, nearly of the order 62 ^ 6
The length of the encoded URLs is fixed to 6 units, which is a significant reduction for very large URLs.
The performance of this scheme is quite good, due to a very less probability of repeated same codes generated.
We can increase the number of encodings possible as well, by increasing the length of the encoded strings.
Thus, there exists a tradeoff between the length of the code and the number of encodings possible.
Predicting the encoding isn't possible in this scheme since random numbers are used.


'''

# How would you design a URL shortening service that is similar to TinyURL?

# Background:
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl
# and it returns a short URL such as http://tinyurl.com/4e9iAk.

# Requirements:
# For instance, "http://tinyurl.com/4e9iAk" is the tiny url for the page "https://leetcode.com/problems/design-tinyurl".
# The identifier (the highlighted part) can be any string with 6 alphanumeric characters containing 0-9, a-z, A-Z.
# Each shortened URL must be unique; that is, no two different URLs can be shortened to the same URL.
# Note about Questions:
# Below are just a small subset of questions to get you started. In real world, there could be many follow ups
# and questions possible and the discussion is open-ended (No one true or correct way to solve a problem).
# If you have more ideas or questions, please ask in Discuss and we may compile it here!

# Questions:
# How many unique identifiers possible? Will you run out of unique URLs?
# Should the identifier be increment or not? Which is easier to design? Pros and cons?
# Mapping an identifier to an URL and its reversal - Does this problem ring a bell to you?
# How do you store the URLs? Does a simple flat file database work?
# What is the bottleneck of the system? Is it read-heavy or write-heavy?
# Estimate the maximum number of URLs a single machine can store.
# Estimate the maximum number of queries per second (QPS) for decoding a shortened URL in a single machine.
# How would you scale the service? For example, a viral link which is shared in social media could result in a peak QPS at a moment's notice.
# How could you handle redundancy? i,e, if a server is down, how could you ensure the service is still operational?
# Keep URLs forever or prune, pros/cons? How we do pruning? (Contributed by @alex_svetkin)
# What API would you provide to a third-party developer? (Contributed by @alex_svetkin)
# If you can enable caching, what would you cache and what's the expiry time? (Contributed by @Humandroid)
# Hide Company Tags Amazon Google Uber Facebook
# Hide Similar Problems (M) Encode and Decode TinyURL
