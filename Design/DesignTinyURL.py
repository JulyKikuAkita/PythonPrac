__source__ = 'https://leetcode.com/problems/design-tinyurl/#/description'
# Implement a (  tinyurl    )
FurtherReading = '''
# Blizzard hash generation: MPQ http://www.cnblogs.com/loujiayu/p/3451668.html
# https://en.wikipedia.org/wiki/MPQ

'''
#
#
VideoLecture = '''
summary:

'''
# Description:
# Implement a (      )
#
# SNAKE concept:
# Scenario:case/interface
# Necessary:constrain/hypothesis
# Application:service/algorithm
# Kilobit:data
# Evolve:
Thought = '''
# 这是一道经典的系统设计面试题，是对SNAKE原则的深度应用，包含了系统设计的方方面面。
# 最初的需求分析发现“长到短”和“短到长”两个基本接口，让我们又一次理解了“读与写是系统设计的基础”。
# 根据日活跃一百万用户进行的QPS估算，让我们理解了什么是“用数字说话”。从最符合直觉的hash映射算法，
# 到简单有效的整数累加算法让我们理解了什么是“不要过度设计”。从数字编码，到字母编码，甚至表情编码，
# 让我们看到了短链接的种种变体的来源。最后对存储的估算，让我们看到了貌似复杂的功能，居然占不了什么空间。
#
# 做个总结：
#      日活用户是基础 ，
#      插入查找算清楚。
#      字母编码省空间，
#      随机算法防冲突 。

1) Scenario:
    insert (long_url),
    Lookup (short_url)
    和文件系统一样

2) Necessary: DAU 日活跃用户, 1M DAU
TAU/MAU might not mean much here, we only focus on calculating DAU, and the peak/valley durting 24 hour
Let's assume request per day by DAU * 1%(functional usage) * 10(functional frequency)

i) low frequency:
per day:1,000,000 * 1% * 10 = 100,000
per yea: 100,000 * 365 = 36,500,000
per second: 100,000/86400 = 1.2

ii) high frequency:
ex: 3B MAU /30 = 0.1B DAU -> 100M DAU,
DAU: 100M * 1% * 10 = 10M requests per day
per year: 3B * 12 = 36B
Per second: 10M/86400 = 115.74 request per day
    -> The per second hit is usually around 100, if above 1000, need to consider high-scalable system
-Peak hour: avg * 10 to estimate peak hour rate

3) Alorithm :
insert：低频操作:
Lookup: 高频

<DB table>
LongToShort
|Long_url| short_url|id|
|googl.com | google.io|1|


ShortToLong:
|short_url|long_url|
|1| google.com|

class Shortener {
    Map<String, String> mLongToShort;
    Map<String, String> mShortToLong;

    String insert(String longURL){
        if ( !mLongToShort.hasKey(longUrl)) {
            String shortUrl = generateShortUrl();
            mLongToShort.put(longURL, shortURL);
            mShortToLong.put(shortURL, longURL);
        }
        return mLongToShort.get(longURl);
    }

    //Try1 ) start with a global counter of integer
    string generateShortUrl(String longUrl){
        return string(mLonToShort.size());
    }

    Try2) encode 62 [0-9 a-z A-Z] = 62
    string generateShortUrlBase62(int number){
        char[] encode = new char[62]{0-9,a-z, A-Z};
        strin ret = "";
        while(number){
            ret = encode[number % 62] + ret;
            number /= 62;
        }
        return ret;
    }
}

Analyze string length with Try1):
i) low frequency:
Yearly URL :36,500,000
usable characters: [0-9] = 10
encoding length = log (base = 10) (36500000) = log 36,500,000 = 7.6 ->8
example short url: goog.gl/12345678

ii) high frequency:
Yearly URL :36B
usable characters: [0-9] = 10
encoding length = log (base = 10) (36B) = 10.55 -> 11
example short url: goog.gl/12345678901 (is it still short?)


Analyze string length with Try2):
i) low frequency:
Yearly URL :36,500,000
usable characters: [0-9a-zA-Z] = 62
encoding length = log (base = 62) (36500000) = log 36,500,000 /log 62 = 7.6/1.79 = 4.24 -> 5
example short url: goog.gl/1234

ii) high frequency:
Yearly URL :36B
usable characters: [0-9] = 10
encoding length = log (base = 62) (36B) = log 36B /log 62 = 10.5/1.79 = 5.89 -> 6
example short url: goog.gl/12345 (is it still short?)

generateShortURL：累计标号 -》加入字母减少存储


Kilobit：数据，多少内存和硬盘来存储。
avg size of long url: 100 bytes
avg size of short url: 4 bytes (int)
state = 4 byte

i) low frequency:
Daily new url: 100,000 * 108 = 10.8 MB
Yearly new url: 10.8 * 365 = 4GB

ii) high frequency:
Daily new url: 10M * 108 = 1080 MB = 1G
Yearly new url: 1G * 365 = 365GB -> might consider cache

Evolve:
1)  needto randomly generate short url:
-> hash func, random select a portion of byte random(0, range) and use that portion to generate shortUrl
-> how to avoid conflict? regenerate one

2) time-limit service
-> use timeStamp and expire short url based on the state

3) cache
-> pre-load, late-load
-> replacement LRU
-> peak request too big? horizontal expand on read/write request
-> partition based on hash range
'''
#
# Description:
# Note: For the coding companion problem, please see: Encode and Decode TinyURL.
# How would you design a URL shortening service that is similar to TinyURL?
#
# Background:
# TinyURL is a URL shortening service where you enter a URL such as
# https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.
#
# Requirements:
# For instance, "http://tinyurl.com/4e9iAk" is the tiny url for the page "https://leetcode.com/problems/design-tinyurl".
# The identifier (the highlighted part) can be any string with 6 alphanumeric characters containing 0-9, a-z, A-Z.
# Each shortened URL must be unique; that is, no two different URLs can be shortened to the same URL.
# Note about Questions:
# Below are just a small subset of questions to get you started.
# In real world, there could be many follow ups and questions possible and the discussion is open-ended
# (No one true or correct way to solve a problem). If you have more ideas or questions,
# please ask in Discuss and we may compile it here!
#
# Questions:
# How many unique identifiers possible? Will you run out of unique URLs?
a1 = ''' that related to the capacity of the system, ex given a service with 10B requests per month, with 10% requests
being write and 90% of request being read -> we would conclude it's need to support read-heave design, which is mostly
true for short-url service; how many repetition call from the same url? where shall you store the short url? shall you
maintain short-long mapping for 2 maps or just one map and what would be the key value?

with base 64 bit encoding [A-Za-z0-9] 62 + 2 random char, 2^64  = 18,446,744,073,709,551,616 ->more than enough
'''
# How would you generate the id?
'''
1. hash -> then probability of collision, how to cope collision, how wide is the generated id if 2 ppl paste
the same url?
2. auto-increment/SEQUENCE id from db, is 32 bit width enough for the field, how to maintain unique if with multi db instances
3. any other method to self-generate id?
'''
# Should the identifier be increment or not? Which is easier to design? Pros and cons?
# Mapping an identifier to an URL and its reversal - Does this problem ring a bell to you?
a1 = '''
if maintain 2 table can solve the reverse loolup but need more space
'''

# How do you store the URLs? Does a simple flat file database work?
a1 = '''
key-value pair style store since no transaction or SQL style queries
schema: PK: short url, filed: long url, uid, etc(for analytics)
'''
# What is the bottleneck of the system? Is it read-heavy or write-heavy?
# Estimate the maximum number of URLs a single machine can store.
# Estimate the maximum number of queries per second (QPS) for decoding a shortened URL in a single machine.
# How would you scale the service?
# For example, a viral link which is shared in social media could result in a peak QPS at a moment's notice.
# How could you handle redundancy? i,e, if a server is down, how could you ensure the service is still operational?
# Keep URLs forever or prune, pros/cons? How we do pruning? (Contributed by @alex_svetkin)
a1 = '''
Obviously keeping URLs forever is preferable and storage should be cheap.
To give a sense how many URLs we can store in a single machine, let's do some estimation:

Assume each row in the database consists of an ID (4 bytes),
long url (2090 bytes),
short url identifier (6 bytes), so each row is about 2100 bytes.
That means 10 million URLs take about 21GB.
Assume a machine has ~100GB of storage => ~50 million URLs per machine. That's a lot of URLs :)

If we run out of storage, we can delete the inactive URLs (e.g., define URLs that last accessed timestamp > 30 days).
Querying this in a database with >50 million rows should be quick,
as long as the last_updated_timestamp column is indexed correctly. Does this sound right?

Or, if you have a lot of memory, you could try to put as many URLs as possible in an in-memory database
such as Redis or Memcached. URLs will be pruned automatically using LRU Cache eviction scheme based
on the set expiry time. We just change the expiry time to 15 days or less (if it's allowed).
If not, your strategy works fine as well (I assumed you talk about deleting the ones with smaller indexes
instead of bigger indexes). Prioritize pruning the ones with smaller indexes and older last_updated_timestamp.

This is probably unrealistic in real world because memory is so much expensive than disk storage.
'''


# What API would you provide to a third-party developer? (Contributed by @alex_svetkin)
ans = ''' I think for developers, they will be interested in how to programmatically create URLs
      and get URL stats like total hits,
      referrals (where does the click come from?), last accessed time, etc. Any other ideas?'''

# If you can enable caching, what would you cache and what's the expiry time? (Contributed by @Humandroid)
ans = '''
Great question! Caching is very important because I think you are going to get a long tail of distribution based on
total hits of all your URLs.
Using the Pareto principle (a.k.a. the 80/20 rule), roughly 80% of the total hits will come from 20% of the URLs.

So, caching those URLs is a great added value indeed! You want to cache the URLs that get accessed frequently
(e.g., a viral link that is shared on social media), so does that ring a bell here?
(Hint: See this LeetCode problem - LRU Cache).
You can use an in-memory database as a cache layer, such as Redis or Memcached.

The expiry time could be something short - 10 minutes is about right,
since the viral URLs will be accessed very frequently and this will keep them in-memory,
so to avoid a cache miss resulting a potential disk lookup which is 100x slower.

Does this answer your question well? If you have any other ideas, I would be very interested to hear them. Thanks!
'''
# What if should url can be edited/deleted by user?
ans = '''
maintain cache consistency, CAP tradeoffs
'''
# How do you get analytics based on given short url?
ans = '''
need to save additional field (not just key-value store) for the service, ex: userid, timestamp etc
note need to use async logging in case of blocking the requests, map/reduce to process multi column data
'''


# Architecture Diagram
diagram = ''' client (req)-> load balancer -> short url service -> db
'''
# Companines
# Amazon Google Uber Facebook
# Similar question
# Encode and Decode TinyURL
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
You can change the 'size' to Long instead of Integer as 'int' can only have max value as 2.1 billion (approx).
[considering the max urls we can have is about 56 billion ]
For the commented code, instead of appending random number, you can prepend zeros. As 0001Ac is equivalent to 1Ac.

// You can type code here and execute it.
import java.lang.*;
import java.util.*;


class Main {
    public static void main(String[] args) {
        String s = "https://leetcode.com/problems/design-tinyurl";
        // HashTable<String, String> tiny = new HashTable<String, String>();
        Hashtable<Integer,String> tiny = new Hashtable<Integer, String>();
        long id = generateId(tiny, s);
        System.out.println(generateTinyUrl(id));
    }

    private static String generateTinyUrl(int id){
        char[] set = {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
            'v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
        };
        StringBuilder st = new StringBuilder();
        while(id > 0){
            char ch = set[id % 62];
            st.append(ch);
            id = id / 62;
        }
        int size = st.length();
        // for(int i=size; i < 6;i++){
        //     st.append(set[randomWithRange(0,61)]);
        // }

        System.out.println(st);
        return new String(st);
    }

    private static int randomWithRange(int min, int max)
    {
        int range = (max - min) + 1;
        return (int)(Math.random() * range) + min;
    }

    private static int generateId(Hashtable<Integer, String> tiny, String longUrl){
        if(tiny.containsValue(longUrl)){
            for(int key: tiny.keySet()){
                if(tiny.get(key) == longUrl){
                    return key;
                }
            }
        }

        int size = tiny.size();
        return size+1;
    }
}
'''