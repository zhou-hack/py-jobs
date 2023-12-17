#import os
#导包

sp=" "
st="*"
re="\n"
#定义需要输出项

#主程序
rounds=int(input("输入需要几层,范围于0~22之间,大于22无法正常显示 \n"))
if (rounds <= 22) and (rounds >= 1):
    for i in range(0,rounds):
        print(sp*(20-i), st*(2*i+1), re, end="")        #采用循环方式输出
    print("共",rounds,"层")
    #os.system("exit")
else:
    print("大于22层,无法正常显示,不输出")
    #os.system("exit")
print("程序结束")
exit()







# print(sp*7,st*1,re, sp*5,st*3,re, sp*4,st*5,re, sp*3,st*7,re, sp*2,st*9,re)

