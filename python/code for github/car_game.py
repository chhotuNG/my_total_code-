
import time 
def time_convert(sec):
    mins=int(sec//60)
    sec=int(sec%60)
    hours=mins%60
    mins=mins%60
    print("CAR DRIVE TIME  = {0}:{1}:{2}".format(hours, mins, sec))
start_time=0
end_time=0

cammand=''
while True :
    cammand=input(">>")
    if cammand =="start":
          print("car start....")
          start_time=time.time()
    elif cammand=="stop" :
            print("car stoped...")
            end_time=time.time()
    elif cammand =="help":
        print("""
start :- to start the car
stop:- to stop the car
quite:- to quite the game""")

    elif cammand =="quite"  or cammand=="exit":
        break
       
    else:
        print("hey what you want ")
print("game over!!")
time_lapsed=end_time-start_time
time_convert(time_lapsed)

   


