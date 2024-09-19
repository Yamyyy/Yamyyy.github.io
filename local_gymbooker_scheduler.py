import os
import time

def GetTime(): 
    return time.strftime("%y-%m-%d %H:%M:%S", time.localtime())


from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, date
 

 
 
def execute():
    print("start execute")
    print(GetTime())
    
    commit_msg="Code pull:"+GetTime() 

    cmd_1 = "git pull"
    os.system(cmd_1)

    print("succesed")


execute()
scheduler = BlockingScheduler()

scheduler.add_job(execute,'interval',seconds=7200)
scheduler.start()