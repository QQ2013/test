#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-
import os
import chardet
result=os.popen('./wtest.py')
res=result.read()
print(res)
fencoding=chardet.detect(res)
print fencoding
