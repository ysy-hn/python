# # 知识
# # 11.1 打开文件：open，位于自动导入的模块io中。
# # 函数open的参数mode的最常见取值
# # 'r' 读取模式（默认值）
# # 'w' 写入模式，在写入模式下打开文件时，既有内容将被删除（截断），并从文件开头处开始写入。
# # 'x' 独占写入模式；在文件已存在时引发FileExistsError异常。
# # 'a' 附加模式，在既有文件末尾继续写入，可使用附加模式。
# # 'b' 二进制模式（与其他模式结合使用）
# # 't' 文本模式（默认值，与其他模式结合使用）
# # '+' 读写模式（与其他模式结合使用）
#
# # 11.2.1 读取和写入：在文本和二进制模式下，基本上分别将str和bytes类用作数据。
# f = open('somefile.txt', 'w')
# print(f.write('Hello, '))
# print(f.write('World!'))  # 再次写入，接上次写入位置
# f.close()
# f = open('somefile.txt', 'r')
# print(f.read(4))
# print(f.read())  # 再次读取，接上次读取位置
#
# # 11.2.2 使用管道重定向输出：在bash等shell中，可依次输入多个命令，并使用管道将它们链接起来。
# # sys.stdin：一个标准数据输入源。
# # $ cat somefile.txt | python somescript.py | sort
# # cat somefile.txt：将文件somefile.txt的内容写入到标准输出（sys.stdout）。
# # python somescript.py：执行Python脚本somescript。这个脚本从其标准输入中读取，并将结果写入到标准输出。
# # sort：读取标准输入（sys.stdin）中的所有文本，将各行按字母顺序排序，并将结果写入到标准输出。
#
# f = open('somefile.txt')
# print(f.tell())
# print(f.read(4))
# print(f.tell())
# # tell():返回当前位于文件的什么位置，文件指针的位置
# fo = open("somefile.txt", "rb")
# print("文件名为: ", fo.name)
# line = fo.readline()
# print("读取的数据为: %s" % (line))
# print(fo.tell())
# fo.seek(-3, 2)
# line = fo.readline()
# print("读取的数据为: %s" % (line))
# print(fo.tell())
# fo.close()
# # 随机存取：seek(offset[, whence])：将当前位置（执行读取或写入的位置）移到offset和whence指定的地方。
# # offset指定了字节（字符）数；whence：默认io.SEEK_SET（0/1/2）： 0，（偏移量是相对于文件开头的，偏移量不能为负数）；
# # 1，相对于当前位置进行移动，偏移量可以为负；2、相对于文件末尾进行移动;要使用第二个参数，方式必须带b模式。
#
# # 11.2.3 读取和写入行
# # readline:成行地读取,默认读取一行，也可提供一个非负整数，指定readline最多可读取多少个字符。
# # readlines：读取文件中的所有行并且包括换行符，并以列表的方式返回它们。
# # writelines：接受一个字符串列表（可以是任何序列或可迭代对象），并将这些字符串都写入到文件（或流）中，
# # 写入时不会添加换行符，因此你必须自行添加。
#
# # 11.2.4 关闭文件：写入过的文件，一定要将其关闭，因为Python可能缓冲你写入的数据。
# # 如果要重置缓冲，让所做的修改反映到磁盘文件中，但又不想关闭文件，可使用方法flush。
# # with open("somefile.txt") as somefile:
# #     do_something(somefile)
# # 尽量使用with open结构，不需要考虑文件开关，结束后自动关闭。
#
# # # 在这里打开文件
# # try:
# #     # 将数据写入到文件中
# # finally:
# #     file.close()
# # 要确保文件得以关闭，可使用一条try/finally语句，并在finally子句中调用close。
#
# # 11.3 迭代文件内容：一种常见的文件操作是迭代其内容，并在迭代过程中反复采取某种措施。
# with open('somefile.txt') as f:
#     while True:
#         char = f.read(21)
#         if not char:
#             break
#         print(char)
# # 11.3.1 每次一个字符（或字节）：在while循环中使用方法read，指定要读取的字符（字节）数。
# with open('somefile.txt') as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         print(line)
# # 11.3.2 每次一行,也可提供一个非负整数，指定readline最多可读取多少个字符
# with open('somefile.txt') as f:
#     for line in f.readlines():
#         print(line)
# with open('somefile.txt') as f:
#     print(f.readlines()[2])
# # # 11.3.3 读取所有内容;可对字符串应用正则表达式，还可将列表存储到某种数据结构中供以后使用。
# import fileinput
# for line in fileinput.input('somefile.txt'):
#     print(line)
# # 11.3.4 使用fileinput实现延迟行迭代;延迟是因为它只读取实际需要的文本部分。
# # 迭代大型文件中的行时，太占内存，可使用for循环和延迟行迭代的方法。
# with open('somefile.txt') as f:
#     for line in f:
#         print(line)
#         for i in line:
#             print(i)
# # 一般常用的文件迭代方法
#
# import sys
# for line in sys.stdin:
#     print(line)
# sys.stdin也是可迭代的

# f = open('somefile.txt', 'w')
# print('First', 'Line', file=f)
# print('Second', 'line', file=f)
# print('Third', 'and final', 'line', file=f)
# f.close()
# lines = list(open('somefile.txt'))
# print(lines)
# first, second, third = open('somefile.txt')
# print(first)
# print(second)
# print(third)
# # 可对迭代器做的事情基本上都可对文件做，如（使用list(open(filename))）将其转换为字符串列表，其效果与使用readlines相同
# # 11.3.5 文件迭代器，最常用的方法。



# # 例题
# f = open('somefile.txt', 'w')
# print(f.write('hello, '))
# print(f.write('world!'))
# f.close()
# f = open('somefile.txt', 'r')  # 默认是读取模式
# print(f.read(4))
# print(f.read())
#
# f = open('somefile.txt')
# print(f.read(7))
# print(f.read(4))
# f.close()
#
# f = open('somefile.txt')
# print(f.read())
# f.close()
#
# f = open('somefile.txt')
# for i in range(3):
#     print(str(i) + ': ' + f.readline(), end='')
# f.close()
#
# import pprint
# pprint.pprint(open('somefile.txt').readlines())
#
# f = open('somefile.txt', 'w')
# f.write('this\nis no\nhaiku')
# f.close()
#
# f = open('somefile.txt')
# lines = f.readlines()
# f.close()
# lines[1] = "isn't a\n"
# f = open('somefile.txt', 'w')
# f.writelines(lines)
# f.close()
#
# with open(filename) as f:
#     while True:
#         char = f.read(1)
#         if not char:
#             break
#         process(char)
#
# with open(filename) as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         process(line)
#
# with open(filename) as f:
#     for char in f.read():
#         process(char)
#
# with open(filename) as f:
#     for line in f.readlines():
#         process(line)
#
# import fileinput
# for line in fileinput.input(filename):
#     process(line)
#
# with open(filename) as f:
#     for line in f:
#         process(line)
#
# for line in open(filename):
#     process(line)
#
# import sys
# for line in sys.stdin:
#     process(line)
#
# f = open('somefile.txt', 'w')
# print('First', 'Line', file=f)
# print('Second', 'line', file=f)
# print('Third', 'and final', 'line', file=f)
# f.close()
#
# lines = list(open('somefile.txt'))
# print(lines)
# first, second, third = open('somefile.txt')
# print(first)
# print(second)
# print(third)
