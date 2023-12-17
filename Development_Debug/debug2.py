import os
import time
import turtle
t = turtle

for i in range(6):
    t.forward(100)
    t.left(60)
    t.write(i+1)
t.forward(100)
t.write("非常好画图,爱来自周瑞喆")
time.sleep(2)
os.system("exit")
