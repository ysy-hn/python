# 4.2.1 字典是不可变得，无序的。
items = [('name', 'Gumby'), ('age', 42)]
d = dict(items)  # dict：字典类型
print(d)

# 4.2.2
print(len(d))
print(d['age'])

# 4.2.4：clear：清空；copy：浅复制；deepcopy：深复制；fromkeys：创建新字典，指定键，键对应的值都是None。
items = [('name', 'Gumby'), ('age', 42)]
items.clear()  # 清空字典
print(items)

a = {}
b = a.fromkeys(['name', 'age'])  # fromkeys：创建新字典，指定键，键对应的值都是None;可指定值。
c = a.fromkeys(['name', 'age'], 'name')
print(b)
print(c)

d = {}
print(d.get('name'))  # get:访问字典没有的项，返回None，不引发错误。
print(a.setdefault('name'))  # setdefault:字典不包含指定的键时，在字典中添加指定的键-值对;如果没有指定，默认为None。
print(d.setdefault('name1', 'N/A'))

d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 1}
print(d.items())
# items：返回所有字典项的列表，其中每个元素都为(key, value)的形式。字典项在列表中的排列顺序不确定.
# 返回值属于一种名为字典视图的特殊类型。字典视图可用于迭代;
# 视图的一个优点是不复制，它们始终是底层字典的反映，即便你修改了底层字典亦如此.
print(d.keys())
# keys:返回字典视图，字典中的键。
d = {1: 1, 2: 2, 3: 3, 4: 1}
print(d.values())  # values:返回字典视图，字典中的值。

print(d.pop('spam'))  # pop:获取与指定键相关联的值，并将该键-值对从字典中删除.
print(d.popitem())  # popitem:随机地弹出（删除）一个字典项,一般弹出最后一项。

d = {
    'title': 'Python Web Site',
    'url': 'http://www.python.org',
    'changed': 'Mar 14 22:09:15 MET 2016'
    }
x = {'title': 'Python Language Website', 'spam': 1}
d.update(x)  # update:使用一个字典中的项来更新另一个字典,不存在，直接添加；存在，直接替换。
print(d)


# # 练习
x = [None]*10
x[9] = 'asd'
print(x)

# 一个简单的数据库
# 一个将人名用作键的字典。每个人都用一个字典表示，
# 字典包含键'phone'和'addr'，它们分别与电话号码和地址相关联
people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },
    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
    },
    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}
# 电话号码和地址的描述性标签，供打印输出时使用
labels = {
    'phone': 'phone number',
    'addr': 'address'
}
name = input("Name: ")
# 要查找电话还是地址？
request = input("Phone number(p) or address(a)?")
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'
if name in people:
    print("{}'s {} is {}.".format(name, labels[key], people[name][key]))

x = {}
y = x
x['key'] = 'value'
print(y)

print({}.fromkeys(['name', 'age']))
print(dict.fromkeys(['name', 'age']))
print(dict.fromkeys(['name', 'age'], '(ubkasdniw)'))

d = {}
print(d.get('name'))
print(d.setdefault('name', 'nad/'))
print(d)

d = {'a': 1, 'b': 2}
d.update({'1': 3})
print(d)

people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },
    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
    },
    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}
# 一个使用get()的简单数据库
# 在这里插入代码清单4-1中的数据库（字典people）
labels = {
 'phone': 'phone number',
 'addr': 'address'
}
name = input('Name: ')
# 要查找电话号码还是地址？
request = input('Phone number (p) or address (a)? ')
# 使用正确的键：
key = request # 如果request既不是'p'也不是'a'
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'
# 使用get提供默认值
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')
print("{}'s {} is {}.".format(name, label, result))