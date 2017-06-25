__source__ = 'https://www.bittiger.io/videos/9z7FMjbukeQBqNQB4/qtFZHdaf6JJQxyMCB'
# Implement a (  uber/lyft/ride sharing    )
FurtherReading = '''
http://highscalability.com/blog/2015/9/14/how-uber-scales-their-real-time-market-platform.html
Lyft pool:
https://eng.lyft.com/tagged/ridesharing

Google S2 library:
http://blog.christianperone.com/2015/08/googles-s2-geometry-on-the-sphere-cells-and-hilbert-curve/
https://code.google.com/archive/p/s2-geometry-library/

'''
#
#

VideoLecture = '''
https://www.infoq.com/presentations/uber-market-platform
Matt Ranney explains the Uber architecture overall,
with a focus on the dispatch systems, the geospatial index,
handling failure, and dealing with the distributed traveling salesman problem.
summary:

1. https://www.bittiger.io/videos/9z7FMjbukeQBqNQB4/qtFZHdaf6JJQxyMCB
让我们从0到1开始探索Uber的架构
Uber 的初心？
Uber的最初构架？
如何扩展？
挑战是什么？ one account many car,
如何改进？
如何避免单点失败？
消息如何处理?
服务如何热备？
MongoDB如何访问？
2011.8基本数据是什么？
如何监控？
潜在风险有哪些？

2. https://www.bittiger.io/videos/c2DrHzyXoQSRwGMva/qtFZHdaf6JJQxyMCB
这次我们继续解读uber的最新架构。
Uber是什么？
Uber面临的挑战是什么？
Uber的架构是什么？
如何重构？
如何识别标识一块空间？
如何表示一个区间？
如何匹配供需？
什么是最优策略？
如何保存供给？
如何匹配需求？
如何远程通讯？
服务设计原则？
如何负载均衡？
数据中心挂掉怎么办？

3. https://www.bittiger.io/videos/LcmNcGrZhW3SNTmSv/qtFZHdaf6JJQxyMCB
如何支持Uber的派遣服务？
如何查找身边的司机？
Uber的挑战是？
如何让服务器连接起来？
如何加入更多节点？
如何同步信息？
如何发现失败节点？
如何避免是自己的问题？
如何保证数据不丢？
如何处理消息？
'''

# Description:
# Implement a (      )
#
diagram = '''
                     ---------> business logic API-python/MySQL persistent data (Asynv call, fail retry logic in case of blocking others)
                    |
client side -> message queue -> dispatch service(real time service, called DISCO in uber, the salesman problem in algo)
                    |                   |
                 gps log                mongodb
                 mongo db                nodejs

'''
#
# SNAKE concept:
# Scenario:case/interface
# Necessary:constrain/hypothesis
# Application:service/algorithm
# Kilobit:data
# Evolve:

Analysis_by_SNAKE = '''
# 1. Scenario:case/interface
Whats the usage scenario ? private car or car pool?
- for people? food? people/food?

2 queue, supply and demand

3. dispatch logic,
- only considering the current available driver when a request comeup?
- need to consider future available supply? ex: a car is about to dropoff a passenger in 2 mins
- sorting based on the result
 -> we need map information to make decision, google s2

2. Necessary:constrain/hypothesis
2011 avg QTP: 25
peak QTP = avg QPT * 5 = 125
future QTP = 125 * 10 (assume that Uber is growing quickly)
# DAU
# concurrent user = DAU / 86400(seconds) * (avg session length)
# peak concurrent user = 2 - 10 times (avg concurrent user)
# future peak concurrent user = 2 * peak concurrent user
# data usage: avg data download per user: 3Mbps
# memory requirement: avg user memory * peak user
# hard disk requirement : file size * file number
#
constraint of this scenario:
ex: 
DAU = 
- future DAU:
- concurrent user:
- peak concurrent user:
- future peak concurrent user:
- memory usage per user:
- hard disk usage:


# 3. Application:service/algorithm
- service diagram

- proposed algorithm (pros/ cons)
(i) the simplest one

(ii) the improved one

(iii) any better idea?


# 4. Kilobit:data
# Whats the data usage/ query load for your algo/serice?
(i) the simplest one

(ii) the improved one

(iii) any better idea?

# 5. Evolve:
# scalability
# improvement

'''