age=int( input('请输入年龄：'))
HRrest= int( input('请输入安静心率：'))
gender=input("请输入man或者woman:")
if  gender =='man' :
    n=220
else:
    n=210
low=(n-age-HRrest)*0.6+HRrest
high=(n-age-HRrest)*0.8+HRrest
print('最适宜运动心率是：',low,'~',high)







    

    
