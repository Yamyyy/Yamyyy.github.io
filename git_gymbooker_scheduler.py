import os
import time

def GetTime(): 
    return time.strftime("%y-%m-%d %H:%M:%S", time.localtime())


from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, date
 

 
 
def execute():
    print("start execute")
    print(GetTime())
    
    commit_msg="Code updated:"+GetTime() 

    cmd_1 = "git status"
    cmd_2 = "git add ."
    cmd_3 = "git commit -m"+'/"'+commit_msg+'/"'
    cmd_4 = "git push"

    os.system("python /home/junjie/Yamyyy.github.io/auto_update.py")
    # os.system(cmd_1)
    os.system(cmd_2)
    os.system(cmd_3)
    os.system(cmd_4)

    print("succesed")


execute()
scheduler = BlockingScheduler()

scheduler.add_job(execute,'interval',seconds=7200)
scheduler.start()