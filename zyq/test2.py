#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 注释
'''
if True:
    print "it's true";
else:
    print "it's flase";
'''
#raw_input('这是我在guthub上修改的----按下 enter  键退出，其他任意键显示...\n');
#import sys; x='runoob'; sys.stdout.write(x+'\n');
'''
import time;
#s = '2014-01-01'
s = '2014-01-05'
print int(time.strftime("%j",time.strptime(s,'%Y-%m-%d'))),
print int(time.strftime("%U",time.strptime(s,'%Y-%m-%d')))+1;
'''
'''
def prt(str):
    print str;

import pdb
L = [8,5,3,1]
newL = L[:]
print '324324'
pdb.set_trace()
print 'serwr'
prt("dddd")
L.sort()
if cmp(L,newL) == 0:
    print 'UP'
else:
    L.sort(reverse=True)
    if cmp(newL,L) == 0:
        print 'DOWN'
    else:
        print 'WRONG'
'''

"""
我们这里定义的HTML只包括两个特殊标记<br>和<hr>,具体的解析规则如下：
rule1：你从输入中读入的一个单词，如果这个单词和当前行已有的长度加起来不超过80，则将该单词输出到当前行，否则另起一行，将该单词输出到下一行的开头；
rule2：如果你从输入中读到的是<br>,则换行
rule3：如果你从输入中读到的是<hr>,则另起一行输出80个'-'（如果当前正好在新行的开始，则直接输出80个'-'），并再次换行到新行的开始。
rule4：单词之间以一个空格分开。
给你一个HTML字符串html,请你输出解析之后的结果。
注意：输入的每个单词长度保证不超过80；标点符号算作前一个单词的内容，
如：字符串"abc12, kkd" 包含两个单词："abc123,"和"kkd".保证正常的单词不会包括"<"或">"。
"""

html='''
Hallo, dies ist eine 
ziemlich lange Zeile, die in Html
aber nicht umgebrochen wird.
<br>
Zwei <br> <br> produzieren zwei Newlines. 
Es gibt auch noch das tag <hr> was einen Trenner darstellt.
Zwei <hr> <hr> produzieren zwei Horizontal Rulers.
Achtung       mehrere Leerzeichen irritieren

Html genauso wenig wie


mehrere Leerzeilen.
'''
charKey = 0
print len(' ')
htmlLen = len(html)
#取出一个完成的单词
def getWord(str):
    wordEnd = [' ','\n']
    temWord = ''
    global charKey,htmlLen
    while charKey<htmlLen:
        if str[charKey] in wordEnd:
            charKey = charKey + 1
            break
        temWord = temWord + str[charKey]
        charKey = charKey + 1
    return temWord;

tarStr = '';
while charKey<htmlLen:
    temWord = getWord(html)
    if len(temWord) == 0:
        continue
    if len(tarStr+temWord)>80 or temWord == '<br>':
        print tarStr
        if temWord != '<br>':
            tarStr = temWord
        else:
            tarStr = ''
        continue
    if temWord == '<hr>':
        #for num in range(1,81):
         #   print '-',
        if len(tarStr)>0:
            print tarStr
        print '--------------------------------------------------------------------'
        tarStr = ''
        continue
    tarStr = tarStr + temWord + ' ';
#执行最后一次输出
if len(tarStr)>0:
    print tarStr




































