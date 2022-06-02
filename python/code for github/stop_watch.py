import time 
def time_convert(sec):
    mins=int(sec//60)
    sec=int(sec%60)
    hours=mins%60
    mins=mins%60
    print("time lapsed = {0}:{1}:{2}".format(hours, mins, sec))
input("press enter to start____:")
print("TIME HAS STARTED_____!!!!")
start_time=time.time()

input("press ENTER to stop___:")
print("TIME HAS STOPED_____!!!!")
end_time=time.time()
time_lapsed=end_time-start_time
time_convert(time_lapsed)