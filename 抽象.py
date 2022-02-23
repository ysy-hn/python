# 知识
fibs = [0, 1]
for i in range(8):
    fibs.append(fibs[-2]+fibs[-1])
print(fibs)
fibs = [0, 1]
num = int(input('输入你想要的数字:'))
for i in range(num-2):
    fibs.append(fibs[-2]+fibs[-1])
print(fibs)
# 斐波那契数：fibs[-2]+fibs[-1]:一种数列，其中每个数都是前两个数的和。

import math
x = 1
y = math.sqrt
print(callable(x))
print(callable(y))
# callable: 判断某个对象是否被调用

def square(x):
    """Calculates the square of the number x."""
    return x * x
print(square(1))
print(square.__doc__)
print(help(square))
# 文档字符串（docstring），将作为函数的一部分存储起来.
# __doc__：访问文档字符串，可访问注释;
# help：访问文档字符串，可访问注释。


# 6.4.5 在定义和调用函数时都使用*或**，将只传递元组或字典。
# 6.5 作用域
x = 1
scope = vars()
print(scope['x'])  # 变量实际类似于字典，变量名为键，值为元素。vars:返回这个不可见的字典；这种“看不见的字典”称为命名空间或作用域
def multiplier(factor):
    def multiplyByFactor(number):
        return number * factor
    return multiplyByFactor
# 一个函数位于另一个函数中，且外面的函数返回里面的函数。存储其所在作用域的函数称为闭包。

# 6.6 递归:返回本身函数进行递归迭代
def recursion():
    return recursion()

# 一般实现
def power(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result
# 递归实现
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

import math
a = list(map(math.sqrt, [1,4,9,16,25]))
print(a)
# map(function, iterable, ...):简单的map（函数，序列）：会根据提供的函数对指定序列做映射
# function -- 函数,iterable -- 一个或多个序列

def is_odd(n):
    return n % 2 == 1
a = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(a)
# filter(function, iterable): 用于过滤序列，过滤掉不符合条件的元素， Python3中返回到是一个filter类,
# 提升了性能, 可以节约内存。该接收两个参数，第一个为函数，第二个为序列.

from functools import reduce
def add(x, y) :            # 两数相加
    return x + y
sum1 = reduce(add, [1,2,3,4,5])   # 计算列表和：1+2+3+4+5
sum2 = reduce(lambda x, y: x+y, [1,2,3,4,5])  # 使用 lambda 匿名函数
print(sum1)
print(sum2)
# reduce(function, iterable[, initializer])：function -- 函数，有两个参数，iterable -- 可迭代对象
# initializer -- 可选，初始参数。function（有两个参数）先对集合中的第 1、2 个元素进行操作，
# 得到的结果再与第三个数据用 function 函数运算，最后得到一个结果


# 例题
def hello(name):
    return 'hello, ' + name + '!'
print(hello('yan'))
def fibs(num):
    result = [0, 1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])
    return result
print(fibs(2))
# 自定义函数

def test():
    print('this is printed')
    return
x = test()
print(x)
# return 后无返回时，返回None。

def asfd(n):
    n = 'yan'
    return n
name = 'shao'
print(asfd(name))
print(name)
# 字符串（以及数和元组）是不可变的（immutable），这意味着你不能修改它们（即只能替换为新值）。
n = 1
print(asfd(n))

def change(n):
    n[0] = 'yan'
    return n
names = ['yanshao', 'you']
print(change(names))
print(names)
# 将同一个列表赋给两个变量时，这两个变量将同时指向这个列表。列表是可变的。
names = ['yanshao', 'you']
print(change(names[:]))
print(names)

def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}
storage = {}
init(storage)
print(storage)

def lookup(data, label, name):
    return data[label].get(name)
def store(data, full_name):
    names = full_name.split()
    if len(names) == 2:
        names.insert(1, '')
    labels = 'first', 'middle', 'last'

    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]
MyNames = {}
init(MyNames)
store(MyNames, 'Magnus Lie Hetland')
print(lookup(MyNames, 'middle', 'Lie'))

store(MyNames, 'Robin Hood')
store(MyNames, 'Robin Locksley')
print(lookup(MyNames, 'first', 'Robin'))

store(MyNames, 'Mr. Gumby')
print(lookup(MyNames, 'middle', ''))

def inc(x):
    x[0] = x[0] + 1
foo = [10]
inc(foo)
print(foo)

def hello(name, greeting='hello', punctuation='!'):
    print('{}, {}{}'.format(greeting, name, punctuation))
hello('Mars', greeting='Top of the morning to ya',punctuation='.')
# 关键字和默认值参数

def print_params_2(title, *params):
    print(title)
    print(params)
print_params_2('Params:', 1, 2, 3)
print_params_2('Nothing:')
# 星号意味着收集余下的位置参数。如果没有可供收集的参数，params将是一个空元组。
def in_the_middle(x, *y, z):
    print(x, y, z)
in_the_middle(1,2,3,4,5,6,z=7)
# 带星号的参数也可放在其他位置（而不是最后）,使用名称来指定后续参数
def print_params_3(**params):
    print(params)
print_params_3(x=1, y=2, z=3)
# 要收集关键字参数，可使用两个星号,此时返回的是字典。
def print_params_4(x, y, z=3, *pospar):
    print(x, y, z)
    print(pospar)
print_params_4(1, 2, 3, 5, 6, 7)

def add(x, y):
    return x +y
params = (1, 2)
print(add(*params))

def story(**kwds):
    return 'Once upon a time, there was a ' \
           '{job} called {name}.'.format_map(kwds)

def power(x, y, *others):
    if others:
        print('Received redundant parameters:', others)
    return pow(x, y)

def interval(start, stop=None, step=1):
    'Imitates range() for step > 0'
    if stop is None:         # 如果没有给参数stop指定值，
       start, stop = 0, start   # 就调整参数start和stop的值
    result = []
    i = start                # 从start开始往上数
    while i < stop:          # 数到stop位置
       result.append(i)         # 将当前数的数附加到result末尾
       i += step                # 增加到当前数和step（> 0）之和
    return result

print(story(job='king', name='Gunby'))
print(story(name='Sir Robin', job='brave knight'))
params = {'job': 'language', 'name': 'Python'}
print(story(**params))
del params['job']
print(story(job='stroke of genius', **params))
print(power(2,3))
print(power(3,2))
print(power(y=3, x=2))
params = (5,) * 2
print(power(*params))
print(power(3,3,'hello, world!'))
print(interval(10))
print(interval(1,5))
print(interval(3,12,4))
print(power(*interval(3,7)))

x = 1
scope = vars()
print(scope['x'])
scope['x'] += 1
print(x)
def foo():
    x = 42
x = 1
foo()
print(x)
def chang_global():
    global x
    x = x+1
x = 1
chang_global()
print(x)
def output(x):
    print(x)
x = 1
y = 2
output(y)
print(x)
print(y)
def combine(parameter):
    print(parameter + external)
external = 'berry'
combine('Shrub')
def combine(parameter):
    print(parameter + globals()['parameter'])
parameter = 'berry'
combine('Shrub')
def foo():
    def bar():
        print('hello, world!')
    bar()
foo()
def multiplier(factor):
    def multiplyByFactor(number):
        return number * factor
    return multiplyByFactor
double = multiplier(2)
print(double(5))
triple = multiplier(3)
print(triple(3))
print(multiplier(5)(4))
def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result
n = 5
print(n)
print(factorial(n))
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
n = 5
print(n)
print(factorial(n))
def power(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result
n = 5
print(n)
print(power(2, n))
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
n = 5
print(n)
print(power(2, n))
def search(sequence, number, lower=0, upper=None):
    if upper is None:
        upper = len(sequence) - 1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)
seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()
print(seq)
print(search(seq, 34))
print(search(seq, 100))
