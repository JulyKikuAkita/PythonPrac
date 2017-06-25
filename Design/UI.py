__source__ = 'https://www.bittiger.io/videos/NDA5xWwadTPqozcP6/TpxCSKrGpiKwuhP32'
# Implement a (      )
#
#
FurtherReading = '''

'''
#
#
#
VideoLecture = '''
summary:
https://www.bittiger.io/videos/NDA5xWwadTPqozcP6/TpxCSKrGpiKwuhP32
'''
# Description:
# Implement a ( Login/Register flow     )
# CRUD, ACID
# Session


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
# Total user = 100M
# DAU = 1M
# concurrent user = DAU / 86400(seconds) * (avg session length)
# peak concurrent user = 2 - 10 times (avg concurrent user)
# future peak concurrent user = 2 * peak concurrent user
# data usage: avg data download per user: 3Mbps
# memory requirement: avg user memory * peak user
# hard disk requirement : file size * file number
#
constraint of this scenario:
ex: 
DAU = 1M
- future DAU: 1M * 2 (as the user base already very big, future growth is limited)
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