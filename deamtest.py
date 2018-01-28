#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-
from time import sleep   
import os,sys   
from daemonize import Daemonize   
    
pid = "/tmp/test.pid" 
    
def wlog():   
    f=open('nima','a')   
    #f=open('/tmp/nima','a')   
    f.write('11')   
    f.close()   
    
def main():   
    os.chdir("/root/test")
    while True:   
        sleep(5)   
        wlog()   
    
daemon = Daemonize(app="test_app", pid=pid, action=main)   
daemon.start()   
daemon.get_pid()   
daemon.is_running()
