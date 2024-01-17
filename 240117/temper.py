temperC = 0
for temperF in range (100,105+1):
    temperC = 5 * (temperF - 32)/9
    print("%8d %7.2f"%(temperF,temperC))