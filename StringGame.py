#!/usr/bin/env python
# coding: utf-8

#　使用 for 迴圈

print("五次失敗就會退出遊戲")
a = str(input("請輸入一個字串:"))
for count in range(0,5):
    b = input("請輸入-" + a[-1] + "-開始的字串")
    if (b[0] == a[-1]):
        a = str(a) + "-" + str(b)
        print("上一個字串是 ", a)
    else:
        count += 1
        print("錯誤" + str(count) + "次,請再輸入-" + a[-1] + "-開頭的字串")

print("錯誤達" + str(count) + "次 Game Over")

# 　使用 while 迴圈
'''
print("五次失敗就會退出遊戲")
count = 1
a = str(input("請輸入一個字串:"))
while count < 5:
    b= input("請輸入-" + a[-1] + "-開始的字串")
    if(b[0]==a[-1]):
        a = str(a) +"-"+ str(b)
        print("上一個字串是 " , a )
    else:
        print("錯誤" + str(count) + "次,請再輸入-" + a[-1] + "-開頭的字串" )
        count+=1

print("錯誤達"+str(count)+"次 Game Over")

'''