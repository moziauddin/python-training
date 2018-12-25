# Working with Time module

import time
# Print Time frame
print(time.time())
# Print ASC Time (HR Format)
print(time.asctime())
time1 = time.time()
print(time1)
# Print Local Time in tuple format
print(time.localtime(time1))
time2 = time.asctime()
print(time2.upper())  # Prints Time in all CAPS

# Sample Scenario: User action time stamp
# Timestamp is collected un loginTime variable
loginTime = time.time()
print(type(loginTime))
loginTimeLoc = time.localtime(loginTime)
print(type(loginTimeLoc))
loginTimeAsc = time.asctime(loginTimeLoc)
print(type(loginTimeAsc))
print("User logged in:", loginTimeAsc)
time.sleep(2)

messageTime = time.time()
messageTimeLoc = time.localtime(messageTime)
messageTimeAsc = time.asctime(messageTimeLoc)
print("Message was sent on:", messageTimeAsc)
time.sleep(7)
logoutTime = time.time()
logoutTimeLoc = time.localtime(logoutTime)
logoutTimeAsc = time.asctime(logoutTimeLoc)
print("Session Ended at:", logoutTimeAsc)

'''
Output:
--------------------------------
1545714772.0954037
Tue Dec 25 16:12:52 2018
1545714772.0954037
time.struct_time(tm_year=2018, tm_mon=12, tm_mday=25, tm_hour=16, tm_min=12, tm_sec=52, tm_wday=1, tm_yday=359, tm_isdst=1)
TUE DEC 25 16:12:52 2018
<class 'float'>
<class 'time.struct_time'>
<class 'str'>
User logged in: Tue Dec 25 16:12:52 2018
Message was sent on: Tue Dec 25 16:12:54 2018
Session Ended at: Tue Dec 25 16:13:01 2018
'''
