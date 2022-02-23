# 知识
# 4.3.4 列表解析，简单的说就是多行代码合成一行代码
squares = [value**2 for value in range(1, 11)]
print(squares)
my_foods = ['pizza', 'falafel', 'carrot cake']

import copy
a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象
b = a                       # 赋值，传对象的引用，关联
c = copy.copy(a)            # 对象拷贝，浅拷贝，一层独立，二层关联
e = a[:]                    # 对象拷贝，浅拷贝，一层独立，二层关联;与copy类似
d = copy.deepcopy(a)        # 对象拷贝，深拷贝，独立
a.append(5)  # 修改对象a
a[4].append('c')  # 修改对象a中的['a', 'b'],数组对象
print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)
print('e = ', e)


# 例题
# 1
pizza = ['番茄味', '鸡翅味', '原味']
for i, val in enumerate(pizza):
    print(i, val)

for i in pizza:
    print('I like {} pizza'.format(i))
print("I really love pizza!")

# 2
anamin = ['小狗', '小猫', '小鸡']
for i, val in enumerate(anamin):
    print("“{},  A {} would make a great pet”".format(i,val))
print("“Any of these animals would make a great pet!”")

# 3
for i in range(1, 21):
    print(i)

# 4
list = list(range(1, 101))
print(list)
for i in list:
    print(i)

list = []
for i in range(1, 101):
    list.append(i)
    print(i)
print(list)

# 5
list = []
for i in range(1, 101):
    list.append(i)
    print(i)
print(list)
print(min(list))
print(max(list))
print(sum(list))

# 6
list = []
for i in range(1,21,2):
    list.append(i)
    print(i)
print(list)

# 7
list = []
for i in range(3,31,3):
    list.append(i)
    print(i)
print(list)

# 8
list = []
for i in range(1,11):
    i = i**2
    list.append(i)
    print(i)
print(list)

# 9
list = [i**2 for i in range(1,11)]
print(list)

# 10
anamin = ['小狗', '小猫', '小鸡', '番茄味', '鸡翅味', '原味']
for i, val in enumerate(anamin[:3]):
    print(i, val)
for i, val in enumerate(anamin[1:4]):
    print(i, val)
for i, val in enumerate(anamin[-3:]):
    print(i, val)

# 11
pizza = ['番茄味', '鸡翅味', '原味']
friend_pizzas = pizza[:]
pizza.append('香辣味')
friend_pizzas.append('牛肉味')
for i, val in enumerate(pizza):
    print(str(i) + "， My favorite pizzas are:" + val)
for i, val in enumerate(friend_pizzas):
    print(i,  " My friend’s favorite pizzas are:" + val)

# 12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
for i, val in enumerate(my_foods):
    print(i, val)
for i in friend_foods:
    print(i)

# 13
foods = ('pizza', 'falafel', 'carrot cake', '奶茶', '土豆')
for i in foods:
    print(i)
# foods[-1] = 'as'
print(foods[-1])
foods = ('pizza', 'falafel', 'carrot cake', '咖啡', '雪糕')
for i in foods:
    print(i)