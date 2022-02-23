# 知识
# DB：计算机中的储存单位，1DB=1024的八次方GB。
# 位 bit (比特)(Binary Digits)：存放一位二进制数，即 0 或 1，最小的存储单位。
# 字节byte：8个二进制位为一个字节(B)，最常用的单位。
# 1KB (Kilobyte千字节)=1024B，
# 1MB (Megabyte兆字节简称“兆”)=1024KB，
#
# 13.1.1 全局变量
# Python DB API的模块属性
# apilevel 使用的Python DB API版本
# threadsafety 模块的线程安全程度如何
# paramstyle 在SQL查询中使用哪种参数风格

# 13.2.1 起步
# 导入模块sqlite3，创建直接到数据库文件的连接。
# 只需提供一个文件名（可以是文件的相对路径或绝对路径）；如果指定的文件不存在，将自动创建它。
# import sqlite3
# conn = sqlite3.connect('somedatabzse.db')
# curs = conn.cursor()  # 游标可用来执行SQL查询,查询后，修改了数据，提交所做的修改，才会将其保存到文件中。
# conn.commit()  # 在每次修改数据库后都进行提交，而不是仅在要关闭连接前才这样做.
# conn.close()  # 关闭连接。
#
# # 13.2.2 数据库应用程序示例
# # line.split('^')，行分解成字段；以波浪字符打头，field.strip('~')来获取其内容；
# # 对于其他字段（即数字字段），使用float(field)就能获取其内容，但字段为空时不能这样做
# # 通过调用curs.execute来执行一条SQL INSERT语句，从而将字段中的值插入数据库中。
import sqlite3

def convert(value):
    if value.startswith('~'):  # 查找带有~的字段
        return value.strip('~')  # 将~删除
    if not value:  # 匹配数字字段
        value = '0'  # 空字段什么都不返回
    return float(value)  # 返回浮点数

conn = sqlite3.connect('food1.db')
curs = conn.cursor()  # 返回连接的游标对象

curs.execute('''  
CREATE TABLE food (
id TEXT PRIMARY KEY,
desc TEXT,
water FLOAT,
kcal FLOAT,
protein FLOAT,
fat FLOAT,
ash FLOAT,
carbs FLOAT,
fiber FLOAT,
sugar FLOAT
)
''')
# 通过调用curs.execute来执行一条SQL INSERT语句，从而将字段中的值插入数据库中。
query = 'INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?)'
field_count = 10
for line in open("DEL_ABBR.txt"):  # 遍历每行数据
    fields = line.split('^')  # 以^为分割标识，获取字段
    vals = [convert(f) for f in fields[:field_count]]
    curs.execute(query, vals)

conn.commit()
conn.close()

import sqlite3, sys

conn = sqlite3.connect('food.db')
curs = conn.cursor()

query = 'SELECT * FROM food WHERE ' + sys.argv[1]
print(query)
curs.execute(query)
names = [f[0] for f in curs.description]
for row in curs.fetchall():
    for pair in zip(names, row):
        print('{}:{}'.format(*pair))
    print()



# 例题
# import sqlite3
# conn = sqlite3.connect('somedatabase.db')
# curs = conn.cursor()
# conn.commit()
# conn.close()
#
# import sqlite3
#
# def convert(value):
#     if value.startswith('~'):
#         return value.strip('~')
#     if not value:
#         value = '0'
#     return float(value)
#
# conn = sqlite3.connect('food.db')
# curs = conn.cursor()
#
# curs.execute('''
# CREATE TABLE food (
#     id         TEXT PRIMARY KEY,
#     desc       TEXT,
#     water      FLOAT,
#     kcal       FLOAT,
#     protein    FLOAT,
#     fat        FLOAT,
#     ash        FLOAT,
#     carbs      FLOAT,
#     fiber      FLOAT,
#     sugar      FLOAT
# )
# ''')
#
# query = 'INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?)'
# field_count = 10
#
# for line in open('DEL_ABBR.txt'):
#     fields = line.split('^')
#     vals = [convert(f) for f in fields[:field_count]]
#     curs.execute(query, vals)
#
# conn.commit()
# conn.close()

# import sqlite3, sys
#
# conn = sqlite3.connect('food2.db')
# curs = conn.cursor()
#
# query = 'SELECT * FROM food WHERE ' + sys.argv[1]
# print(query)
# curs.execute(query)
# names = [f[0] for f in curs.description]
# for row in curs.fetchall():
#     for pair in zip(names, row):
#         print('{}: {}'.format(*pair))
#     print()
