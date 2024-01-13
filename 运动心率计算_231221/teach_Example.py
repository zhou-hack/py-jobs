# age=int( input('请输入年龄：'))
# HRrest= int( input('请输入安静心率：'))
# gender=input("请输入man或者woman:")
# if  gender =='man' :
#     n=220
# else:
#     n=210
# low=(n-age-HRrest)*0.6+HRrest
# high=(n-age-HRrest)*0.8+HRrest
# print('最适宜运动心率是：',low,'~',high)


age = int(input('请输入年龄: '))
sex = input("请输入性别(man或woman): ").lower()

male_identifiers = ["man"]
female_identifiers = ["woman"]

while sex not in male_identifiers and sex not in female_identifiers:
    print("您的性别输入错误，请重新输入")
    sex = input("请输入性别(man或woman): ").lower()

n = 220 if sex in male_identifiers else 210

HRrest = int(input("请输入安静心率: "))

low = (n - age - HRrest) * 0.6 + HRrest
high = (n - age - HRrest) * 0.8 + HRrest

print("最适宜运动心率是：", low, "~", high)