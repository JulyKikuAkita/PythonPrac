__source__ = 'https://www.bittiger.io/channel/TpxCSKrGpiKwuhP32'
# This is general guideline for SNAKE concept
FurtherReading = '''
# https://docs.google.com/document/d/1NPojCYmFOSg-GvYfOKKS6dkp6VBNbjVmYho5nl8YI3M/edit#heading=h.d3qxo2k9c6xh

# https://www.bittiger.io/channel/TpxCSKrGpiKwuhP32

'''
#
#
VideoLecture = '''
summary: https://www.bittiger.io/channel/TpxCSKrGpiKwuhP32
# https://docs.google.com/document/d/1NPojCYmFOSg-GvYfOKKS6dkp6VBNbjVmYho5nl8YI3M/edit#heading=h.d3qxo2k9c6xh

'''
# micro/macro
# SNAKE concept:
# Scenario:case/interface
# Necessary:constrain/hypothesis
# Application:service/algorithm
# Kilobit:data
# Evolve:

# Thought:
# Description: ex: how to design Netflix
#
# SNAKE concept:
# 1. Scenario:case/interface
scenario = '''
watch video
search video
'''
# 2. Necessary:constrain/hypothesis
# DAU
# concurrent user = DAU / 86400(seconds) * (avg session length)
# peak concurrent user = 2 - 10 times (avg concurrent user)
# future peak concurrent user = 2 * peak concurrent user
# data usage: avg data download per user: 3Mbps
# memory requirement: avg user memory * peak user
# hard disk requirement : file size * file number
#
#
constraint = '''
ex: DAU = 5M
- future DAU = 5M * 2 ( we select 6 from range 2 - 10 here) = 10M
- concurrent user = DAU / 86400(seconds) * (avg session length)
assume avg session length = 30 mins
 = 5M / (86400) * (30 * 60)
 = 104,167
- peak concurrent user = 104,167 * 6 ( we select 6 from range 2 - 10 here) = 625,000
- future peak concurrent user = 2 * 625,000 = 1,250,000
- 3 month data usage = avg data download per user: 3Mbps *  1,250,000 = 3.75Tb/s
- memory usage: 10kB per user * DAU in future = 5M * 2 * 10kb = 100GB
- hard disk usage: 14000 movies * 50GB(different resolution) = 700TB ~== 1PB

'''
#
# 3. Application:service/algorithm
service = '''
service diagram, etc
'''
# 4. Kilobit:data
# 5. Evolve:
scale = '''
scalability,
'''

Java = '''
#Thought:

'''