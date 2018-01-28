#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-
from wxpy import *
import time
import os
bot = Bot(cache_path=True,console_qr=1) 
time.sleep(2)
my_friend=bot.friends().search('test')[0]
print(my_friend)
my_friend.send('login')
