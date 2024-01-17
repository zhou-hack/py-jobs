S=0
for num in range (1,11,1):      #1-10元 total9 1+2+..+9   1,11是因为 循环次数默认会进行减一 ，所以需要在原有的基础上对循环次数进行加1
    S = S+num                   # 
print("Total:",S,end="")
