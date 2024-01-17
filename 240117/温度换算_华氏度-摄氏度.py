A = int(input("A: "))
B = int(input("B: "))
if (A>B):
    print("数据错误")
else:
    temperC = 0
    for temperF in range (A,B+1):
        temperC = 5 * (temperF - 32)/9
        print("%8d %7.2f"%(temperF,temperC))