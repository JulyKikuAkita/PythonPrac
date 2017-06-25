__source__ = 'https://www.bittiger.io/videos/ErvmMiLBCGN8CtXby/TpxCSKrGpiKwuhP32'
FurtherReading = '''
https://github.com/google/snappy
Hadoop: http://jennyxiaozhang.com/6-things-you-need-to-know-about-hadoop/

'''

SourceVideo = '''
1. https://www.bittiger.io/videos/ErvmMiLBCGN8CtXby/TpxCSKrGpiKwuhP32
我们从四个维度考虑WhatsAPP的设计
数据设计：用户、好友、频道、消息的结构
存储设计：NoSQL vs SQL
连接设计：如何支持百万链接
流量设计：如何压缩流量

2. https://www.bittiger.io/videos/22DT8oTvueCxu2WER/TpxCSKrGpiKwuhP32
WhatsAPP高级功能时需要考虑的三个因素：
如何结合Chat和Feed；
'''
# Description:
# Implement a WhatsApp
#

#
# SNAKE concept:
# Scenario:case/interface
# Necessary:constrain/hypothesis
# Application:service/algorithm
# Kilobit:data
# Evolve:

Analysis_by_SNAKE = '''
# 1. Scenario:case/interface
Whats the usage scenario ?

2. Necessary:constrain/hypothesis
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