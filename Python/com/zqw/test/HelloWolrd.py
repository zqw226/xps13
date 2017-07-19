#！/usr/bin/python
# -*- coding:utf-8 -*-
import time
import math

print("Hello, Wolrd!")
time.sleep(2)
print("今天是个好天气！")

if True:
    print("True")
    # print "true"
else:
    print("False")
item_one = 1
item_two = 2
total = item_one + \
    item_two
# 可以使用斜杠（ \）将一行的语句分为多行显示
print(total)
days = ['monday', 'tuesday', "wednesday",
        'thursday', 'friday']
# 语句中包含 [], {} 或 () 括号就不需要使用多行连接符
print(days[1])
word = "world"
print(word)
# Python成员运算符
day = "wednesday"
if day not in days:
    print("day is not in days")
else:
    print("day is in days")
# Python身份运算符
aday = "friday"
if aday is day:
    print("OK")
else:
    print("God!")
counter = 100    # 赋值整型变量
miles = 1000.0   # 浮点型
name = "John"   # 字符串
a = b = c = 1
# 以上实例，创建一个整型对象，值为1，三个变量被分配到相同的内存空间上
d, e, f = 1, 2, "john"
# 以上实例，两个整型对象1和2的分配给变量 a 和 b，字符串对象 "john" 分配给变量 c

# Python 定义了一些标准类型，用于存储各种类型的数据
# Python有五个标准的数据类型：
# Numbers（数字）  他们是不可改变的数据类型，这意味着改变数字数据类型会分配一个新的对象。int/long/float/complex
# String（字符串）
# List（列表）
# Tuple（元组）
# Dictionary（字典）
# 您也可以使用del语句删除一些对象的引用 del var1[,var2[,var3[....,varN]]]]
s = 'ilovepython'
print(s[1:5])
print(s[:5])
print(s[1:])
print(s[0])
print(s[1:5] + "you")
print(s[1:5] * 2)
mylist = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
print(mylist)
# 列表用 [ ] 标识，是 python 最通用的复合数据类型
# 元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表
tinytuple = (123, 'john')
# 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型
# 列表是有序的对象结合，字典是无序的对象集合
# 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取
# 字典用"{ }"标识。字典由索引(key)和它对应的值value组成
mydict = {}
mydict['one'] = "This is one"
mydict[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print(mydict['one'])
print(mydict[2])
print(tinydict.keys())
print(tinydict.values())
# python 的所有数据类型都是类,可以通过 type() 查看该变量的数据类型
# print(type(tinydict))由于 python 并不支持 switch 语句，所以多个条件判断
# 只能用 elif 来实现，如果判断需要多个条件需同时判断时，可以使用 or （或）表示两个条件有一个成立时判断条件成功
# 使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功

count = 0
while count < 9:
   print('The count is:', count)
   count = count + 1
print("Good bye!")

print("My name is %s and weight is %d kg!" % ('zqw', 27))

tup1 = (50,);
# 元组中只包含一个元素时，需要在元素后面添加逗号
print(time.time())

def print_text(str):
    print(str)
    return
print_text("you are my love")

money = 100

def addmoney():
    global money
    money += 1
print(money)
addmoney()
print(money)

print(dir(math))