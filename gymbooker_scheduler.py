import os
import time

def GetTime(): #获取当前时间
    return time.strftime("%y-%m-%d %H:%M:%S", time.localtime())

#修改默认的提交信息
commit_msg=f" \"Code updated: {GetTime()}\" "

#git提交命令
cmd_1 = "git status"
cmd_2 = "git add ."
cmd_3 = "git commit -m"+commit_msg
cmd_4 = "git push"

print("[开始] 执行git自动上传")

os.system("python /data/mxp/junjie/Yamyyy.github.io/auto_update.py")
os.system(cmd_1)#显示当前动态
os.system(cmd_2)#添加所有文件更改到工作区
os.system(cmd_3)#自动commit
os.system(cmd_4)#push上传

print("succesed")
