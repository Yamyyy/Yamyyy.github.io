import os
import time

def GetTime(): 
    return time.strftime("%y-%m-%d %H:%M:%S", time.localtime())


from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, date
 

 
 
def execute():
    print("start execute")
    print(GetTime())   

    os.system("python /data/mxp/junjie/Yamyyy.github.io/auto_update.py")

    print("succesed")


execute()
scheduler = BlockingScheduler()

scheduler.add_job(execute,'interval',seconds=7200)
scheduler.start()

# nohup python local_gymbooker_scheduler.py > output.log 2>&1 &