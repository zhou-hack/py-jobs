age=int(input('请输入年龄: '))
sex=input("请输入性别 为male / female: ")
if(sex == "male"):
    n = int(220)
else:
    if(sex == "female"):
        n = int(210)
    else:
        print("您的性别输入错误")
        exit()
HRrest = int(input("请输入安静心率: "))

low=float((n-age-HRrest)*0.6+HRrest)
high=float((n-age-HRrest)*0.8+HRrest)
print("您的最佳运动心率为:",low,"~",high)