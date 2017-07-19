#!/usr/bin/python
#-*- coding:UTF-8 -*-
from com.zqw.package1.dogbark import dogbark
from com.zqw.package2.wolfbark import wolfbark

# dogbark()
# wolfbark()

str = input("请输入（dog or wolf）：")
if str == "dog":
    dogbark()
elif str == "wolf":
    wolfbark()
else:
    print("输入有误！")
