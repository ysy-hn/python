months = [
 'January',
 'February',
 'March',
 'April',
 'May',
 'June',
 'July',
 'August',
 'September',
 'October',
 'November',
 'December'
]
# 一个列表，其中包含数1～31对应的结尾
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
 + ['st', 'nd', 'rd'] + 7 * ['th'] \
 + ['st']
year = input('Year: ')
month = input('Month (1-12): ')
day = input('Day (1-31): ')
month_number = int(month)
day_number = int(day)
# 别忘了将表示月和日的数减1，这样才能得到正确的索引
month_name = months[month_number-1]
ordinal = day + endings[day_number-1]
print(month_name + ' ' + ordinal + ', ' + year)

# 列表操作：索引、切片、相加、相乘和成员资格
# 反向切片
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print( numbers[8:3:-1])
print(numbers[10:0:-2] )
print(numbers[0:10:-2] )
print( numbers[::-2] )
print( numbers[5::-2] )
print(numbers[:5:-2] )  # 从右向左时，第一个索引要大于第二索引。

sentence = input("Sentence: ")
text_width = len(sentence)
box_width = text_width + 6
screen_width = 2*box_width
left_margin = screen_width // 2
print(' ' * left_margin + '+' + '-' * (box_width-2) + '+')
print(' ' * left_margin + '|' + ' ' * (box_width-2) + '|')
print(' ' * left_margin + '|  ' + sentence + '  |')
print(' ' * left_margin + '|' + ' ' * (box_width-2) + '|')
print(' ' * left_margin + '+' + '-' * (box_width-2) + '+')

# 2.3.2 列表基本操作
# 修改：根据索引直接修改；删除：del删除；赋值：根据索引直接赋值
# 2.3.3 列表方法
lst = [1, 2, 3]
lst.append(4)  # 在列表末尾加值
print(lst)

lst.clear()
print(lst)  # 清空列表信息

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

x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
print(x.count(1) )  # 计算指定的元素在列表中出现了多少次。

a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)  # 同时将多个值附加到列表末尾，为此可将这些值组成的序列作为参数提供给方法extend。

knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
print(knights.index('who'))  # 返回索引

numbers = [1, 2, 3, 5, 6, 7]
numbers.insert(3, 'four')  # 将一个对象插入列表,也可以切片完成
print(numbers)

x = [1, 2, 3]
x.pop()  # 从列表中删除一个元素（默认为最后一个元素）,可选择索引，并返回这一元素。
print(x) # pop是唯一既修改列表又返回一个非None值的列表方法。

x = ['to', 'be', 'or', 'not', 'to', 'be']
x.remove('be')  # 删除第一个为指定值的元素
print(x)

x = [1, 2, 3]
x.reverse()  # 按相反的顺序排列列表中的元素
print(x)
x = [1, 2, 3]
print(list(reversed(x)))

x = [4, 6, 2, 1, 7, 9]
x.sort()  # 就地排序,直接操作原列表，sort：有key和reverse可选参数，按关键字排序
print(x)

x = [4, 6, 2, 1, 7, 9]
print(sorted(x))  #  另外生成一个列表并排序,原列表不变
print(x)

x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
x.sort(key=len)   # 按key排序
print(x)

x = [4, 6, 2, 1, 7, 9]
x.sort(reverse=True)  # 按相反顺序排序
print(x)

a = 'hello'
print(list(a))
print(''.join(a))

print(tuple([1, 2, 3]))  # 将序列（列表）、字符串等，变成元组，元组不可修改
print(tuple('sa'))

