#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-
from wxpy import *
import time
import os
bot = Bot(cache_path=True,console_qr=1) 
time.sleep(2)
my_friend=bot.friends().search('cat')[0]
print(my_friend)
my_friend.send('hellow world')
@bot.register()
def print_others(msg):
    if (msg.sender.remark_name=="cat"):
        print(msg.sender.remark_name)
        print(msg.text)
        print(msg.sender)
        print(msg)
        str_time=time.strftime('%Y-%m-%d %H-%M-%S\n',time.localtime(time.time()))
        print("%si%s"%(msg.sender.remark_name,str_time))
        print("{}:{}>>{}\n".format(str_time,msg.sender.remark_name,msg.text.encode('UTF-8')))
        msg.sender.send(u"你好我在吃饭")
        result=os.popen('./wtest.py')
        res=result.read()
        res1 = res.decode('UTF-8')
        msg.sender.send(res1)
        
#embed()
bot.join()
while True:
    time.sleep(3)
    if (time.localtime.tm_sec==0):
        my_friend=bot.friends().search('test')[0]
        my_friend.send('hellow world')
