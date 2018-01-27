#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-
from wxpy import *
import time
import os
bot = Bot(cache_path=True,console_qr=1) 
time.sleep(2)
my_friend=bot.friends().search('qq')[0]
print(my_friend)
my_friend.send('hellow world')
@bot.register()
def print_others(msg):
    if (msg.sender.remark_name=="qq"):
        print(msg.sender.remark_name)
        print(msg.text)
        print(msg.sender)
        print(msg)
        msg.sender.send(u"你好我在吃饭")
        result=os.popen('./wtest.py')
        res=result.read()
        res1 = res.decode('UTF-8')
        msg.sender.send(res1)
        
#embed()
bot.join()
