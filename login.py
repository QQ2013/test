#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-
from wxpy import *
import time
import os
#bot = Bot(cache_path=True) 
#bot = Bot(cache_path=True,console_qr=1,qr_path='w') 
bot = Bot(cache_path=True,qr_path=None) 
time.sleep(2)
my_friend=bot.friends().search('cat')[0]
print(my_friend)
my_friend.send('login')
