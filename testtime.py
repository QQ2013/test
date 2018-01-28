#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-
from wxpy import *
import time
import os
print time.localtime().tm_min
print time.localtime()
if time.localtime().tm_min==51:
  print "w"
