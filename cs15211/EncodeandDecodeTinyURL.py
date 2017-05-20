__author__ = 'July'
# Note: This is a companion problem to the System Design problem: Design TinyURL.
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
java = '''
public class Codec {
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
Approach 1- Using simple counter

public class Codec {
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
Approach 2- using hashcode

public class Codec {
    Map<Integer, String> map = new HashMap<>();
    public String encode(String longUrl) {
        map.put(longUrl.hashCode(),longUrl);
        return "http://tinyurl.com/"+longUrl.hashCode();
    }
    public String decode(String shortUrl) {
        return map.get(Integer.parseInt(shortUrl.replace("http://tinyurl.com/", "")));
    }
}
Approach 3- using random function

public class Codec {
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
