# #2023.12.20First 
# #Python3 
# #Edited with VSCode Py3.11.5
# age=int(input('请输入年龄: '))
# sex=input("请输入性别: ")
# if(sex == "male") or (sex == "man") or (sex == "men") or (sex == "男"):
#     n = int(220)
# else:
#     if(sex == "female") or (sex == "woman") or (sex == "women") or (sex == "女"):
#         n = int(210)
#     else:
#         print("您的性别输入错误\n程序结束运行")
#         exit()
# HRrest = int(input("请输入安静心率: "))

# low=(n-age-HRrest)*0.6 + HRrest
# high=(n-age-HRrest)*0.8 + HRrest

# print("您的最佳运动心率为:",low,"~",high)

# # age=float(input('请输入年龄: '))
# # sex=input("请输入性别 为male / female: ")
# # if(sex == "male"):
# #     n = int(220)
# # else:
# #     if(sex == "female"):
# #         n = int(210)
# #     else:
# #         print("您的性别输入错误")
# #         exit()
# # HRrest = int(input("请输入安静心率: "))

# # low=(n-age-HRrest)*0.6 + HRrest
# # high=(n-age-HRrest)*0.8 + HRrest
# # print("您的最佳运动心率为:",low,"~",high)

# # Previous Version


age = int(input('请输入年龄: '))

male_identifiers = ["male", "man", "men", "男"]
female_identifiers = ["female", "woman", "women", "女"]

while True:
    sex = input("请输入性别: ").lower()
    if sex in male_identifiers:
        n = 220
        break
    elif sex in female_identifiers:
        n = 210
        break
    else:
        print("您的性别输入错误，请重新输入")

HRrest = int(input("请输入安静心率: "))

low = (n - age - HRrest) * 0.6 + HRrest
high = (n - age - HRrest) * 0.8 + HRrest

print("您的最佳运动心率为:", low, "~", high)