#!/bin/sh
ps aux|grep deamtest | awk '{print $2}'|xargs -i kill -9 {}
ps aux|grep deamtest |grep -v grep 
