req = int(input("number: "))  #请求输入要被倍乘的整数，int()定义整数输入
# 这里如果不需要请求输入 可以使用
# req = 10      其中10为被倍乘的数

times = int(input("次数: "))  #请求输入要倍乘的次数 默认为 1-输入倍乘的次数
# 如果不需要请求输入倍乘次数 可以使用
# for x in range(1,倍乘次数+1):    倍乘次数+1是因为python的循环机制默认从1开始 需要加上1达到倍乘的次数

for x in range(1,1+times):    #开始循环，从1开始 到 1 + 输入的倍乘次数
#一直循环，直到循环次数到达 1 + 输入的倍乘次数
     req = req*x         #输出结果=输入结果*次数

print(req)          #输出最终结果
