# 5.2.1 序列解包：多个变量赋值或多个值赋给变量
# 注意一点*号在多个变量中的使用
a, b, *rest = [1, 2, 3, 4]  # *号可在任意变量中使用
print(rest)

# 5.2.2 链式赋值:x = y = 1
# 5.2.3 增强赋值：x += 1

# 5.4.1
# 布尔值：False None 0 "" () [] {} 都为假，其它为真包括负值。
# 5.4.2
name = input('What is your name? ')
if name.endswith('Gumby'):  # endswith：结束的字符
    print('Hello, Mr. Gumby')

# 5.4.6 运算符作为比较时，值相同则相同；is not等作为比较时，除了值相同，地址也要相同，才是同一对象。
# 字符串、数字、列表等比较时，按字母、数字顺序比较，而不是按长度比较。
print( "alpha" < "beta" )
print([2, [1, 4, 5]] < [2, [1, 5]] )
# 布尔运算有短路逻辑（延迟求值）的特征；比如x and y，x为假不看y；x or y，x为真不看y。

# 5.4.7 断言：让程序在错误条件出现时立即崩溃胜过以后再崩溃。
# 如果知道必须满足特定条件，程序才能正确地运行，可在程序中添加assert语句充当检查点；
# 还可在条件后面添加一个字符串，对断言做出说明。
age = -1
assert 0 < age < 100, '数值必须在0-100.'

# 5.5 循环：while、for、迭代字典、一些迭代工具
# 5.5.4 迭代工具
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
for i in range(len(names)):  # 这种迭代技巧常用
    print(names[i], 'is', ages[i], 'years old')
print(list(zip(names, ages)))
for name, age in zip(names, ages):
    print(name, 'is', age, 'years old')
# zip:并行迭代工具，缝合任意数量的序列,在最短的序列用完后停止“缝合”.
# enumerate:迭代时获取索引和值
# reversed：反转，不修改对象;带上反转前的序列类型，不然会输出地址
# sorted：排序，不修改对象。
a = [ 3, 6, 8, 3]
print(sorted(a))
print(list(reversed(a)))  # 带上反转前的序列数据类型，不然会输出地址
print(a)

# 5.5.5 跳出循环:break:直接跳出循环；continue：结束当前迭代，并跳到下一次迭代开头； while True/break成例
while True:
    word = input('请输入一个单词： ')
    if not word:
        break
    print('这个单词是：', word)

# 5.6 简单推导
print([(x, y) for x in range(3) for y in range(3)])  # 使用[]进行列表推导。
squares = {i:"{} squared is {}".format(i, i**2) for i in range(10)}  # 使用{}进行字典推导
print(squares[8])

# 5.7.1 pass：直接通过
y = x = ["Hello", "world"]
print(x, y)
del x  # del:只删除了x，没有删除列表本身
print(y)

# 5.7.3
exec("print('Hello, world!')")  # 将字符串作为语句执行，exec什么都不返回，因为它本身是条语句。
print(eval(input("Enter an arithmetic expression: ")))
# eval:计算并返回字符串表示的表达式的结果。
a = {}
a['x'] = 2
a['y'] = 3
print(eval('x * y', a))
print(ord("🙈"))   # 接受一个只包含一个字符的字符串，并返回这个字符的顺序值（一个整数），类似地址
print(chr(128584))  # 返回一个字符串，其中只包含一个字符，这个字符对应于传入的顺序值n（0 ≤n < 256）


# 例题
name = 'Gumby'
salutation = 'Mr.'
greeting = 'Hello'
print(greeting, ',', salutation, name)
print(greeting + ',', salutation, name)

# 序列解包，将一个序列（或任何可迭代对象）解包，并将得到的值存储到一系列变量中；简单的说就是把一个包分解成一个个变量。
x , y , z = 1, 2, 3
print(x, y, z)
x, y = y, x
print(x, y, z)
values = 1, 2, 3
print(values)
x, y, z = values
print(x, y, z)
scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'}
key, value = scoundrel.popitem()
print(key, value)
a, *b, c = "abc"
print(a, b, c)

name = input("what is your name?")
if name.endswith('yan'):
    print('你好，' + name)
else:
    print('不好意思')
age = -1
assert 0 < age < 100, '年龄必须是整数'
print(age)
name = ''
while not name.strip():
    name = input('请输入您的名字')
print('您好，{}！'.format(name))
words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
    print(word)
print(range(0,10))
print(list(range(0,10)))
for number in range(0,10):
    print(number)
d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
    print(key, 'corresponds to', d[key])
for key, value in d.items():
    print(key, 'corresponds to', value)
names = ['anne', 'beth', 'georpe', 'damon', 'yan']
ages = [22, 45,32, 102]
print(list(zip(names, ages)))
for name, age in zip(names, ages):
    print(name, 'is', age, 'years old')
# 创建一个适合用于并行迭代的新序列,缝合。
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(list(y))
strings = {'x': 1, 'y': 2, 'z': 3, 'yan': '9'}
for index, string in enumerate(strings):
    print(index, string)
    if 'yan' in string:
        strings[string] = '[censored]'
        strings[index] = '[censored]'
        print(strings)

a = [4, 3, 6, 8, 3]
print(sorted(a))
b = 'Hello, World!'
print(sorted(b))
print(list(reversed(b)))
print(sorted(b, key=str.lower))
# sorted:返回一个列表，其中包含seq中的所有值且这些值是经过排序的,
# reversed:按相反的顺序返回seq中的值，以便用于迭代
from math import sqrt
for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break

word = 'dummy'
while word:
    word = input('Please enter a word: ') # 使用这个单词做些事情：
    print('The word was', word)

while True:
    word = input('Please enter a word: ')
    if not word:
        break
from math import sqrt
for n in range(99, 80, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
    else:
        print("Didn't find it!")

result = []
for x in range(3):
    for y in range(3):
        result.append((x, y))
        print(result)
# range:创建一个由整数组成的列表
squares = {i: "{} squared is {}".format(i, i**2) for i in range(10)}
print(squares[8])
x = ['hello', 'world']
y = x
del x
print(y)
exec("print('hello,world!')")
from math import sqrt
scope = {}
exec('sqrt = 4', scope)
print(scope['sqrt'])
print(sqrt(9))
print(len(scope))
print(scope.keys())
print(eval(input("Enter an arithmetic expression: ")))
scope = {}
scope['x'] = 2
scope['y'] = 3
print(eval('x*y', scope))
exec('x = 9', scope)
print(scope['x'])
print(ord("🙈"))   # 接受一个只包含一个字符的字符串，并返回这个字符的顺序值（一个整数）
print(chr(128584))  # 返回一个字符串，其中只包含一个字符，这个字符对应于传入的顺序值n（0 ≤n < 256）
