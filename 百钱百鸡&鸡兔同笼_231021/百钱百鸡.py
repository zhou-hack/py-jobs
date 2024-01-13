# for gongji in range(1,20):
#     for muji in range(0,21):
#             for xiaoji in range(1,100):
#                 if (gongji * 5 + muji * 3 + xiaoji / 3 == 100) and (gongji + muji + xiaoji == 100):
#                     print("公鸡:",gongji,"母鸡:",muji,"小鸡:",xiaoji)
# input(print("\n完成\n按下回车键退出"))
# exit()

for gongji in range(1,20):
    for muji in range(0,34):
        for xiaoji in range(0,301,3):
            if (gongji * 5 + muji * 3 + xiaoji / 3 == 100) and (gongji + muji + xiaoji == 100):
                print("公鸡:",gongji,"母鸡:",muji,"小鸡:",xiaoji)
input(print("\n完成\n按下回车键退出"))
exit()