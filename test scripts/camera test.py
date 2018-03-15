#Will save to a memory stick if it is plugged in before the pi boots and there is a file called collect_images.txt in the root folder
#Also entire log will be overwritten onto logs.txt

from sr.robot import *
import time

R = Robot()
res = [(640, 480), (1296, 736), (1296, 976), (1920, 1088), (1920, 1440)]

time.sleep(5) #gives the user time to put a marker in front of the camera

for r in res: #cycles through the resolutions
    start_time = time.time() #store current time
    markers = R.see(res=r) #res must be a tuple in the form (x, y)
    end_time = time.time()
    print "Resolution: ", r
    print "Time taken: ", (end_time - start_time) #print time taken to do R.see
    print "Markers seen: ", len(markers)
    if len(markers) == 0:
        print "no marker detected"
