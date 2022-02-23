# # # 知识
# # 10.1.1 模块就是程序
# # import sys
# # sys.path.append("文件位置")
# # 要告诉解释器去哪里查找这个模块，可执行如下命令（以Windows目录为例）
#
# # 10.1.2 模块是用来下定义的
# # 模块在首次被导入程序时执行;可使用if __name__ == '__main__':来进行导入模块时自动被调用的控制。
# import hello
#
# # 10.1.3 让模块可用
# import sys, pprint
# pprint.pprint(sys.path)
# # 模块sys的变量path中找到目录列表（即搜索路径）。如果要让解释器能够找到模块，
# # 可将其放在其中任何一个位置中。但目录site-packages是最佳的选择，因为它就是用来放置模块的。
# # 除使用环境变量PYTHONPATH外，还可使用路径配置文件。
#
# # 10.1.4 包
# # 为组织模块，可将其编组为包（package）。模块存储在扩展名为.py的文件中，而包则是一个目录。
# # 要被Python视为包，目录必须包含文件__init__.py。
# # 一种简单的包布局
# # ~/python/ PYTHONPATH中的目录
# # ~/python/drawing/ 包目录（包drawing）
# # ~/python/drawing/__init__.py 包代码（模块drawing）
# # ~/python/drawing/colors.py 模块colors
# # ~/python/drawing/shapes.py 模块shapes
# import constants
# import drawing  # 导入包后即可使用__init__.py模块的内容,要使用其他模块需要导入
# import drawing.colors
# from drawing import shapes
# print((constants.PI))
#
# # 10.2.1 模块包含什么
# import copy
# print(dir(copy))
# # dir:要查明模块包含哪些东西，列出对象的所有属性（对于模块，列出所有的函数、类、变量等）。
# # 可与列表推导配合使用，过滤不需要的内容。
# print([n for n in dir(copy) if not n.startswith('_')])
#
# print(copy.__all__)
# # __all__:1、它是在模块copy中像下面这样设置的（这些代码是直接从copy.py复制而来的）;
# # 2、旨在定义模块的公有接口,它告诉解释器从这个模块导入所有的名称意味着什么。
# # 编写模块时，像这样设置__all__也很有用。因为模块可能包含大量其他程序不需要的变量、函数和类，比较周全的做法是将它们过滤掉。
# # 如果不设置__all__，则会在以import *方式导入时，导入所有不以下划线打头的全局名称。
#
# # 10.2.2 使用 help 获取帮助
# import copy
# help(copy.copy)  # help:可提供你通常需要的所有信息
# print(copy.copy.__doc__)  # __doc__:前面的帮助信息是从函数copy的文档字符串中提取的.
# print(range.__doc__)
#
# # 10.2.4 使用源代码
# print(copy.__file__)  # __file__：打开源代码位置；如果列出的文件名以.pyc结尾，可打开以.py结尾的相应文件
#
# # 10.3.1 sys:访问与Python解释器紧密相关的变量和函数
# # 模块sys中一些重要的函数和变量
# # argv 命令行参数，包括脚本名
# # exit([arg]) 退出当前程序，可通过可选参数指定返回值或错误消息
# # modules 一个字典，将模块名映射到加载的模块
# # path 一个列表，包含要在其中查找模块的目录的名称
# # platform 一个平台标识符，如sunos5或win32
# # stdin 标准输入流——一个类似于文件的对象
# # stdout 标准输出流——一个类似于文件的对象
# # stderr 标准错误流——一个类似于文件的对象
# import sys
# print(len(sys.argv))
# print(str(sys.argv))
# args = sys.argv[1:]
# print(args)
# args.reverse()
# print(' '.join(args))  # 不能打印这个操作的返回值，因为它就地修改列表并返回None
# print(' '.join(reversed(sys.argv[1:])))
#
# # 10.3.2 os:访问多个操作系统服务。
# # 模块os中一些重要的函数和变量
# # environ 包含环境变量的映射
# # system(command) 在子shell中执行操作系统命令
# # sep 路径中使用的分隔符
# # pathsep 分隔不同路径的分隔符
# # linesep 行分隔符（'\n'、'\r'或'\r\n'）
# # urandom(n) 返回n个字节的强加密随机数据
#
# # 10.3.3 fileinput:迭代一系列文本文件中的所有行。
# # 模块fileinput让你能够轻松地迭代一系列文本文件中的所有行。
# # 模块fileinput中一些重要的函数
# # input([files[, inplace[, backup]]]) 帮助迭代多个输入流中的行
# # filename() 返回当前文件的名称
# # lineno() 返回（累计的）当前行号
# # filelineno() 返回在当前文件中的行号
# # isfirstline() 检查当前行是否是文件中的第一行
# # isstdin() 检查最后一行是否来自sys.stdin
# # nextfile() 关闭当前文件并移到下一个文件
# # close() 关闭序列
# import fileinput
# for line in fileinput.input(inplace=True):
#     line = line.rstrip()
#     num = fileinput.lineno()
#     print('{:<50} # {:2d}'.format(line, num))
# # fileinput.input是其中最重要的函数，它返回一个可在for循环中进行迭代的对象。
# # 务必慎用参数inplace，因为这很容易破坏文件。
#
# # 10.3.4 集合、堆和双端队列
# # 1、集合
# print(set(range(10)))
# # set:直接创建集合；集合主要用于成员资格检查，因此将忽略重复的元素；
# # 还可执行各种标准集合操作，如并集和交集，为此可使用对整数执行按位操作的运算符。
# # 集合是可变的，因此不能用作字典中的键。
# # frozenset（不可变的集合）：创建给定集合的副本。在需要将集合作为另一个集合的成员或字典中的键时。
# a = {1, 2, 3}
# b = {2, 3, 4}
# print(a.union(b))    # union：并集
# print(a | b)         # 并集
# c = a & b            # 交集
# print(c)
# print(a.intersection(b))  # 交集
# print(a & b)
# print(c.issubset(a)) # 小于等于
# print(c <= a)
# print(c.issuperset(a)) # 大于等于
# print(c >= a)
# print(a.difference(b))  # 余集
# print(a - b)
# print(a.symmetric_difference(b))  # 并集的余集
# print(a ^ b)
#
# # 2、堆：一种优先队列；heapq：堆操作函数的模块。
# # 优先队列让你能够以任意顺序添加对象，并随时（可能是在两次添加对象之间）找出（并删除）最小的元素。
# # 模块heapq中一些重要的函数
# # heappush(heap, x) 将x压入堆中
# # heappop(heap) 从堆中弹出最小的元素
# # heapify(heap) 让列表具备堆特征
# # heapreplace(heap, x) 弹出最小的元素，并将x压入堆中
# # nlargest(n, iter) 返回iter中n个最大的元素
# # nsmallest(n, iter) 返回iter中n个最小的元素
# # 堆特征：位置i处的元素总是大于位置i // 2处的元素（反过来说就是小于位置2 * i和2 * i + 1处的元素）；这是底层堆算法的基础，
# from heapq import *
# from random import shuffle
# data = list(range(10))
# shuffle(data)
# heap = []
# for i in data:
#     heappush(heap, i)
# print(heap)
# heappush(heap, 0.5)
# print(heap)
# print(heappop(heap))
# print(heapreplace(heap, 0.5))
# print(heap )
#
# # 3、双端队列（及其他集合）：需要按添加元素的顺序进行删除时。
# # 支持在队首（左端）高效地附加和弹出元素；高效地旋转元素（将元素向右或向左移，并在到达一端时环绕到另一端）
# # extend：类似于相应的列表方法；
# # extendleft：类似于appendleft，可迭代对象中的元素将按相反的顺序出现在双端队列中
# from collections import deque
# a = deque(range(5))
# a.append(5)
# a.appendleft(6)
# print(a)
# print(a.pop())
# print(a.popleft())
# a.rotate(3)
# print(a)
# a.rotate(-1)
# print(a)
#
# # 10.3.5 time:获取当前时间、操作时间和日期、从字符串中读取日期、将日期格式化为字符串的函数。
# # Python日期元组中的字段
# # 0 年 如2000、2001等
# # 1 月 范围1~12
# # 2 日 范围1~31
# # 3 时 范围0~23
# # 4 分 范围0~59
# # 5 秒 范围0~61
# # 6 星期 范围0~6，其中0表示星期一
# # 7 儒略日 范围1~366
# # 8 夏令时 0、1或-1
# # 元组(2008, 1, 21, 12, 2, 56, 0, 21, 0)表示2008年1月21日12时2分56秒
# # 秒(0~61)，考虑到闰一秒和闰两秒的情况。夏令时数字是一个布尔值.
# # 模块time中一些重要的函数
# # asctime([tuple]) 将时间元组转换为字符串
# # localtime([secs]) 将秒数转换为表示当地时间的日期元组
# # mktime(tuple) 将时间元组转换为当地时间
# # sleep(secs) 休眠（什么都不做）secs秒
# # strptime(string[, format]) 将字符串转换为时间元组
# # time() 当前时间（从新纪元开始后的秒数，以UTC为准）
# import time
# print(time.asctime())
# print(time.mktime((2016, 1, 1, 0, 0, 0, -1, -1, -1)))
# print(time.strptime('Sat Jul  3 13:49:01 2021'))
# print(time.localtime(1625291408.250623))
# print(time.time())
# # datetime:日期和时间算术支持.
# from timeit import timeit
# def func():
#     s = 0
#     for i in range(1000):
#         s += i
# # timeit(函数名_字符串，运行环境_字符串，number=运行次数)
# t = timeit('func()', 'from __main__ import func', number=1000)
# print(t)
# print(timeit('x=1', number=1000))
# # timeit:计算代码段的执行时间。
# # repeat和timeit用法相似，多了一个repeat参数，表示重复测试的次数(可以不写，默认值为3.)，返回值为一个时间的列表。
#
# # 10.3.6 random:生成伪随机数的函数，有助于编写模拟程序或生成随机输出的程序。
# # 真正的随机（如用于加密或实现与安全相关的功能），应考虑使用模块os中的函数urandom。
# # 模块random中的SystemRandom类基于的功能与urandom类似，可提供接近于真正随机的数据。
#
# # 模块random中一些重要的函数
# # random() 返回一个0~1（含）的随机实数
# # getrandbits(n) 以长整数方式返回n个随机的二进制位
# # uniform(a, b) 返回一个a~b（含）的随机实数
# # randrange([start], stop, [step]) 从range(start, stop, step)中随机地选择一个数
# # choice(seq) 从序列seq中随机地选择一个元素
# # shuffle(seq[, random]) 就地打乱序列seq
# # sample(seq, n) 从序列seq中随机地选择n个值不同的元素
# from random import *
# from time import *
# date1 = (2016, 1, 1, 0, 0, 0, -1, -1, -1)
# time1 = mktime(date1)
# date2 = (2017, 1, 1, 0, 0, 0, -1, -1, -1)
# time2 = mktime(date2)
# random_time = uniform(time1, time2)
# print(asctime(localtime(random_time)))  # 转换为易于理解的日期
# print(random())
# print(uniform(1, 6))
# a = [0, 1, 2, 3, 4]
# print(choice(a))
# shuffle(a)
# print(a)
# print(sample(a, 2))
#
# # 10.3.7 shelve 和 json
# # shelve:简单的存储方案,这个函数将一个文件名作为参数，并返回一个Shelf对象，供你用来存储数据。
# import shelve
# s = shelve.open('test.dat',flag='c', protocol=None, writeback=False)
# s['x'] = ['a', 'b', 'c']
# s['y'] = {'x': 'a', 'y': 'b', 'z': 'c', 'd': 'e'}
# s['x'].append('d')
# print(s['x'])
# temp = s['x']  # 临时变量
# temp.append('d')
# s['x'] = temp
# print(s['x'])
# s.close()
# flag:默认为‘c’，如果数据文件不存在，就创建，允许读写;protocol:None/1/2，表示以二进制的形式序列化;
# writeback：默认False。True:shelf将会将所有从DB中读取的对象存放到一个内存缓存。
# 当我们close()打开的shelf的时候，缓存中所有的对象会被重新写入DB。
# 优点：减少了出错的概率，并且让对象的持久化对用户更加的透明了；缺点：增加额外的内存消耗，带来额外的等待时间。
# # # 潜在的陷阱,helve.open返回的对象并非普通映射;
# # 1、要正确地修改使用模块shelve存储的对象，必须将获取的副本赋给一个临时变量，并在修改这个副本后再次存储.
# # 2、或者将函数open的参数writeback设置为True。
#
# # 10.3.8 re：支持正则表达式，正则表达式是可匹配文本片段的模式。
# # 一、通配符：句点与除换行符外的任何字符都匹配('.ython')。
# # 对特殊字符进行转义：\\解释器执行的转义和模块re执行的转义（'python\\.org'）;y也可使用原始字符串（r'python\.org'）。
# # 字符集：用方括号将一个子串括起，创建一个字符集（'[pj]ython'）。排除字符集，可在开头添加一个^字符（'[^abc]'）。
# # 二选一：管道字符|（'python|perl'）；子模式：只想将其用于模式的一部分，可将这部分（子模式）放在圆括号内（'p(ython|erl)'）
# # 可选模式：子模式后面加上问号，可将其指定为可选的，（r'(http://)?(www\.)?python\.org）。
# # 重复模式：*：pattern可重复0、1或多次；+：pattern可重复1或多次；{m,n}：模式可从父m~n次。
# # 开头：也可查找与模式匹配的子串，开头是否与模式'ht+p'匹配，为此可使用脱字符（'^'）来指出这一点。末尾：（$）
# #
# # 二、模块re中一些重要的函数
# # compile(pattern[, flags]) 根据包含正则表达式的字符串创建模式对象
# # search(pattern, string[, flags]) 在字符串中查找模式
# # match(pattern, string[, flags]) 在字符串开头匹配模式
# # split(pattern, string[, maxsplit=0]) 根据模式来分割字符串
# # findall(pattern, string) 返回一个列表，其中包含字符串中所有与模式匹配的子串
# # sub(pat, repl, string[, count=0]) 将字符串中与模式pat匹配的子串都替换为repl
# # escape(string) 对字符串中所有的正则表达式特殊字符都进行转义
# #
# # 三、匹配对象和编组
# # 编组：包含与模式匹配的子串的信息，还包含模式的哪部分与子串的哪部分匹配的信息；
# # 通常，编组包含诸如通配符和重复运算符等特殊字符
# # re匹配对象的重要方法
# # group([group1, ...]) 获取与给定子模式（编组）匹配的子串
# # start([group]) 返回与给定编组匹配的子串的起始位置
# # end([group]) 返回与给定编组匹配的子串的终止位置（与切片一样，不包含终止位置）
# # span([group]) 返回与给定编组匹配的子串的起始和终止位置
# import re
# m = re.match(r'www\.(.*)\..{3}', 'www.python.org')
# print(m.group(1))
# print(m.end(1))
# print(m.span(1))
# # 重复运算符默认是贪婪的，这意味着它们将匹配尽可能多的内容。
# #
# # 6. 模板系统示例
# # 模板（template）是一种文件，可在其中插入具体的值来得到最终的文本。



# # 例题
# import sys
# sys.path.append('E:\You\G\python\python基础教程\代码')
# import hello
# import hello2
# import hello3
# hello3.hello()
# import hello4
# hello4.test()
# import another_hello
# another_hello.hello()
#
# import copy
# print(dir(copy))
# print([n for n in dir(copy) if not n.startswith('_')])
# print(copy.__all__)
#
# help(copy.copy)
# print(copy.copy.__doc__)
#
# import copy
# print(range.__doc__)
# print(copy.__file__)
#
# print(set(range(10)))
# print({0, 1, 2, 3, 0, 1, 2, 3, 4, 5})
# print({'fee', 'fie', 'foe'})
# a = {1, 2, 3}
# b = {2, 3, 4}
# print(a.union(b))    # 并集
# print(a | b)         # 并集
#
# c = a & b            # 交集
# print(c)
# print(a.intersection(b))  # 交集
# print(a & b)
#
# print(c.issubset(a)) # 小于等于
# print(c <= a)
#
# print(c.issuperset(a)) # 大于等于
# print(c >= a)
#
# print(a.difference(b))  # 余集
# print(a - b)
#
# print(a.symmetric_difference(b))  # 并集的余集
# print(a ^ b)
#
# print(a.copy())          # 浅复制
# print(a.copy() is a)
#
# a = set()
# b = set()
# print(a.add(frozenset(b)))
#
# from heapq import *
# from random import shuffle
# data = list(range(10))
# shuffle(data)
# heap = []
# for n in data:
#     heappush(heap, n)
# print(heap)
# heappush(heap, 0.5)
# print(heap)
# print(heappop(heap))
# print(heappop(heap))
# print(heappop(heap))
# print(heap)
# heap = [5, 8, 0, 3, 6, 7, 9, 1, 4, 2]
# heapify(heap)
# print(heap)
# print(heapreplace(heap, 0.5))
# print(heap)
# print(heapreplace(heap, 10))
# print(heap)
#
# from collections import deque
# q = deque(range(5))
# print(q)
# q.append(5)
# print(q)
# q.appendleft(6)
# print(q)
# print(q.pop())
# print(q.popleft())
# q.rotate(3)    # rotate：整体右移，最右边数字循环到最左边；-号，左移。
# print(q)
# q.rotate(-1)
# print(q)
#
# from time import asctime
# print(asctime())
#
# from random import *
# from time import *
# date1 = (2016, 1, 1, 0, 0, 0, -1, -1, -1)
# time1 = mktime(date1)
# date2 = (2017, 1, 1, 0, 0, 0, -1, -1, -1)
# time2 = mktime(date2)
# random_time = uniform(time1, time2)
# print(asctime(localtime(random_time)))
#
# from random import randrange
# num = int(input('How many dice?几个骰子'))
# sides = int(input('How many sides per die?每个骰子多少边'))
# sum = 0
# for i in range(num):
#     sum += randrange(sides) + 1
# print("The result is", sum)
#
# values = list(range(1,11)) + 'Jack Queen King'.split()
# suits ='diamonds clubs hearts spades'.split()
# deck = ['{} of {}'.format(v, s) for v in values for s in suits]
# from pprint import pprint
# # print(pprint(deck[:12]))
# from random import shuffle
# shuffle(deck)
# print(pprint(deck[:12]))
# # diamonds，spades， hearts，clubs：钻石，黑桃，红心，梅花
#
# import shelve
# s = shelve.open('test.dat', writeback=True)
# s['x'] = ['a', 'b', 'c']
# s['x'].append('d')
# print(s['x'])
#
# temp = s['x']
# temp.append('d')
# s['x'] = temp
# print(s['x'])
#
# import sys, shelve
#
# def store_person(db):
#     """ 让用户输入数据并将其存储到shelf对象中"""
#     pid = input('Enter unique ID number:')
#     person = {}
#     person['name'] = input('Enter name:')
#     person['age'] = input('Enter age:')
#     person['phone'] = input('Enter phone number:')
#     db[pid] = person
#
# def lookup_person(db):
#     """让用户输入ID和所需的字段，并从shelf对象中获取相应的数据"""
#     pid = input("Enter ID number:")
#     field = input("What would you like to know?(name, age, phone")
#     field = field.strip().lower()
#     print(field.capitalize() + ':',db[pid][field])
#
# def print_help():
#     print('The available commands are:')
#     print('store: Stores information about a person')
#     print("lookup: looks up a person from ID number" )
#     print("quit: Save changes and exit")
#     print('?:Prints this message')
#
# def enter_command():
#     cmd = input("Enter command (? for help):")
#     cmd = cmd.strip().lower()
#     return cmd
#
# def main():
#     database =shelve.open("E:\You\G\python\python基础教程\代码\10\database.py")
#     try:
#         while True:
#             cmd = enter_command()
#             if cmd == 'store':
#                 store_person(database)
#             elif cmd == 'lookup':
#                 lookup_person(database)
#             elif cmd == "?":
#                 print_help()
#             elif cmd == "quit":
#                 return
#     finally:
#         database.close()
#
# if __name__ == '__main__': main()
#
# import re
# some_text = 'alpha, beta,,,,gamma delta'
# print(re.split('[, ]+', some_text) )
# print(re.split('[, ]+', some_text, maxsplit=2))
# print(re.split('[, ]+', some_text, maxsplit=1))
# pat = '[a-zA-Z]+'
# text = '"Hm... Err -- are you sure?" he said, sounding insecure.'
# print(re.findall(pat, text) )
# pat = r'[.?\-",]+'
# print(re.findall(pat, text) )
# pat = '{name}'
# text = 'Dear {name}...'
# print(re.sub(pat, 'Mr. Gumby', text) )
# print( re.escape('www.python.org') )
# print( re.escape('But where is the ambiguity?') )
#
# import re
# m = re.match(r'www\.(.*)\..{3}', 'www.python.org')
# print(m.group(0))
# print(m.group(1))
# print(m.start(0))
# print(m.start(1))
# print(m.end(0))
# print(m.end(1))
# print(m.span(0))
# print(m.span(1))
#
# import re
# emphasis_pattern = r'\*([^\*]+)\*'
# print(re.sub(emphasis_pattern, r'<em>\1</em>', 'Hello,*world**!'))
#
# import re
# emphasis_pattern = r'\*\*(.+?)\*\*'
# print(re.sub(emphasis_pattern, r'<em>\1</em>', '**This** is **it**!') )
#
#
#
