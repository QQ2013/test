#!/bin/sh
#./curl http://zzk.cnblogs.com/s/blogpost?Keywords=c语言\&ViewCount=200\&DiggCount=10\&pageindex=15|grep target|sed 's/<strong>//g;s/<\/strong>//g'|grep html
#./curl http://zzk.cnblogs.com/s/blogpost?Keywords=$1\&ViewCount=200\&DiggCount=10\&pageindex=$2|grep target|sed 's/<strong>//g;s/<\/strong>//g'|grep html
./curl "http://news.baidu.com/ns?word=$1&rn=10" | sed 's/.*<h3 class="c-title"><a href="\(.*\)" data-click=.*/\1/g' |grep  ^http |nl


