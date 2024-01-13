# heads = int(input("请输入鸡兔头数:"))
# legs = int(input("请输入腿的个数:"))

# # 判断腿总数是否奇数，腿总数不能为奇数,并且腿的个数大于0
# if (legs - heads * 2) % 2 != 0 or legs <= 0:
#     print("输入数据不正确")
# else:
#     # 计算兔子的数量
#     rabbits = int((legs - heads * 2) / 2)
#     chickens = int((heads - rabbits))
#     # 判断鸡的数量是否小于0 或 兔子的数量是否小于0
#     if chickens < 0 or rabbits < 0:
#         print("输入数据不正确")

# # 输出结果
# print('鸡有', chickens, "只", '兔有', rabbits, "只")
# print("程序运行结束")
# input("按回车键以退出...")

heads = int(input("请输入鸡兔头数:"))
legs = int(input("请输入腿的个数:"))

# 判断腿总数是否奇数，腿总数不能为奇数,并且腿的个数大于0
if (legs - heads * 2) % 2 != 0 or legs <= 0:
    print("输入数据不正确")
else:
    # 计算兔子的数量
    rabbits = int((legs - heads * 2) / 2)
    chickens = int((heads - rabbits))
    # 判断鸡的数量是否小于0 或 兔子的数量是否小于0
    if chickens < 0 or rabbits < 0:
        print("输入数据不正确")
    else:
        # 输出结果
        print('鸡有', chickens, "只", '兔有', rabbits, "只")

print("程序运行结束")
input("按回车键以退出...")