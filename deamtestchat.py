#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-
from wxpy import *
from time import sleep   
import time 
import os,sys   
from daemonize import Daemonize   
    
pid = "/tmp/test.pid" 


def main( ):
    os.chdir("/root/test")
    bot = Bot(cache_path=True,console_qr=1) 
    sleep(2)
    my_friend=bot.friends().search('test')[0]
    my_friend.send('hellow world')
    @bot.register()
    def print_others(msg):
        os.chdir("/root/test")
        if (msg.sender.remark_name=="test"):
            #wlog(msg.send.remmart_name+msg)
            str_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            #wlog(str_time)
            #wlog('%s:%s>>%s\n'%(str_time,msg.sender.remark_name,msg.text))
            wlog('{}:{}>>{}\n'.format(str_time,msg.sender.remark_name,msg.text.encode('UTF-8')))
            os.chdir("/root/test")
            #msg.sender.send(u"你好我在吃饭")
            #result=os.popen('./wtest.py')
            result=os.popen('./search.sh {}'.format(msg.text.encode('UTF-8')))
            res=result.read()
            res1 = res.decode('UTF-8')
            msg.sender.send(res1)
    #wlog(bot.friends())
    #embed()
    send=1
    while True:   
        sleep(1000)   
        str_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        my_friend=bot.friends().search('test')[0]
        my_friend.send(str_time)
        if (time.localtime().tm_sec<30 and send==1):
            os.chdir("/root/test")
            my_friend.send(u"你好我在吃饭")
            result=os.popen('./wtest.py')
            res=result.read()
            res1 = res.decode('UTF-8')
            my_friend.send(res1)
	    send=0
        if (time.localtime().tm_sec>30):
	    send=1
            
    #bot.join()
    
def wlog(log):   
    f=open('wx.log','a')   
    #f=open('/tmp/nima','a')   
    f.write(log)   
    f.close()   
    
#def main():   
#    os.chdir("/root/test")
#    while True:   
#        sleep(5)   
#        wlog()   
    

daemon = Daemonize(app="testchat", pid=pid, action=main)   
daemon.start()   
daemon.get_pid()   
daemon.is_running()
wlog(bot.friends())
