from datetime import datetime

import random
import time


odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
         21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
         41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

for a in range(5):

    rightˍthisˍminute = datetime.today().minute

    if rightˍthisˍminute in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")

    wait_time = random.randint(1, 60)
    time.sleep = (wait_time )
    

    
