from math import ceil, floor, sqrt
import cmath

print(5//2)  # 整除运算，结果向下圆整
print(5/2)
print(5//2.4)
print(10 % 3)  # 求模，等价x - ((x // y) * y)。
print(0xAF, 0o10, 0b10)  # 十六进制，八进制，二进制

print(ceil(-1.2))  # 以浮点数的方式返回向上圆整的结果
print(5//2)  # 整除运算，结果向下圆整
print(floor(-1.5))  # 以浮点数的方式返回向下圆整的结果
print(round(2/3, 3))  # 四舍五入为指定的精度，正好为5时舍入到偶数

print(abs(-9))  # 返回指定数的绝对值
print(pow(2, 3))  # 返回x的y次方对z求模的结果
print(repr("hello,\nworld"))  # 返回指定值的字符表示
print("hello,\nworld")

print(sqrt(4))  # 返回平方根；不能用于负数
print(cmath.sqrt(4))  # 返回平方根；cmath:可用于负数

print(float(3))  # 将字符串或数字转换为浮点数
print(int(2.1))  # 将字符串或数转换为整数
print(str("hello,\nworld"))  # 将指定的值转换为字符串。用于转换bytes时，可指定编码和错误处理方式

print(help('你好'))  # 提供交互式帮助
print(input("你多大了"))  # 以字符串的方式获取用户输入

print("This is a very long string. It continues here. \n"
      "And it's not over yet.Hello, world!\n"
      "Still here.")

print('''This is a very long string. It continues here.
And it's not over yet. "Hello, world!"
Still here.''')  # 三引号可以换行

print("Hello"
      "wor"
      "ld!")  #

# 使用反斜杠进行转义
path = 'C:\nowhere'
print(path)
print('C:\\nowhere')
# 原始字符串用前缀r表示，不能以单个反斜杠结尾,如果以\结尾，则用\转义。
print(r'Let\'s go!')
print(r'C:\Program Files\foo\bar' '\\')

from turtle import *

forward(100)
left(120)
forward(100)
left(120)
forward(100)
