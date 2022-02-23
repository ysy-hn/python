# 知识
# 8.1.2 实参和形参，函数参数为形参，调用函数时需提供实参。
# 8.2.1 位置实参,可调用多次，位置顺序很重要，还可以指定实参顺序调用。
# 8.2.2 关键字实参，调用实参时可使用关键字参数，不分顺序。
# 8.2.3 默认值，调用时没有使用关键字参数就默认使用默认值。
# 8.2.4 等效的函数调用，可混合使用位置实参、关键字实参和默认值，通常有多种等效的函数调用方式
# 8.2.5 避免实参错误，提供的实参多于或少于函数完成其工作所需的信息时，将出现实参不匹配错误。
# 8.3 返回值，return返回简单值。
# 8.3.2 让实参变成可选的，使用if/else；返回字典。
# 8.3.4 结合使用函数和 while 循环，while True/break；while 标识。
# 8.4 传递列表，for循环; 在函数中修改列表;禁止函数修改列表(使用[:]复制一个副本，对副本进行操作，保留原本。
# 8.5 传递任意数量的实参,使用*形参形式；
# 8.5.1 结合使用位置实参和任意数量实参，*形参放在最后；
# 8.5.2 使用任意数量的关键字实参，**形参形式，放在最后。
# 8.6.1 导入整个模块,导入特定的函数,使用 as 给函数指定别名,使用 as 给模块指定别名,导入模块中的所有函数
# 8.7 函数编写指南


# 例题
# 1
def display_message():
    print('学习函数知识')
a = display_message()

# 2
def  favorite_book(title):
    print('我最喜欢的一本书是{}'.format(title))
a = favorite_book('西游记')

# 3
def  make_shirt(size, font):
    print('T恤的尺寸是{},T恤的字体是{}。'.format(size, font))
make_shirt('2xl', '中国')
make_shirt('xl', font='合肥')

# 4
def make_shirt(size, font='Python'):
    print('T恤的尺寸是{},T恤的字体是{}。'.format(size, font))
make_shirt('大号')
make_shirt('中号')
make_shirt('大号', font='中国')

# 5
def describe_city(name, country='中国'):
    print('{}位于{}.'.format(name, country))
describe_city('马鞍山')
describe_city('合肥')
describe_city('伦敦', country='英国')

# 6
def city_country(city, country):
    city_country = city + ',' + country
    return city_country
print(city_country('合肥', '中国'))

# 7
def make_album(name, music):
    album = {'name': name, 'music': music}
    return album
a = make_album('许嵩', '山水之间')
b = make_album('徐良', '素颜')
c = make_album('陈奕迅', '十年')
print(a, b, c)

def make_album(name, music, numbers=''):
    if numbers:
        album = {'name': name, 'music': music, 'numbers': numbers}
    else:
        album = {'name': name, 'music': music}
    return album
c = make_album('陈奕迅', '十年')
d = make_album('徐良', '素颜', '10万')
print(c, d)

# 8
def make_album(name, music):
    album = {'name': name, 'music': music}
    return album
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    name = input('请输入你喜欢的专辑歌手：')

    if name == 'q':
        break
    music = input('请输入你喜欢的专辑名称：')
    if music == 'q':
        break

    album = make_album(name, music)
    print(album)

def make_album(name, music, numbers=''):
    album = {'name': name, 'music': music}
    return album
while True:
    action = input('是否开始？（Y/N）')
    if action.upper() == 'N':
        break
    name = input('请输入你喜欢的专辑歌手：')
    music = input('请输入你喜欢的专辑名称：')
    album = make_album(name, music)
    print(album)

# 9
def show_magicians(names):
    for name in names:
        print(name)
names = ['猴子', '行者', '大圣']
show_magicians(names)

# 10
def make_great(names_design, names):
    while names_design:
        name_design = names_design.pop()
        print('伟大的' + name_design)
        names.append(name_design)

def show_magicians(names):
    for name in names:
        print(name)

names_design = ['猴子', '行者', '大圣']
names = []
make_great(names_design, names)
show_magicians(names)

# 11
def make_great(names_design, names):
    while names_design:
        name_design = '伟大的' + names_design.pop()
        print(name_design)
        names.append(name_design)

def show_magicians(names):
    for name in names:
        print(name)

names_design = ['猴子', '行者', '大圣']
names = []
make_great(names_design[:], names)
show_magicians(names)
print(names_design, names)

# 12
def sandwich(*others):
    for other in others:
        print('{}味的三明治'.format(other))
sandwich('番茄', '牛肉', '猪肉', '原味', '牛肉', '牛肉')
sandwich('番茄', '牛肉', '猪肉')
sandwich('番茄', '牛肉')

# 13
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('闫', '少友', 职业='工程师', 年龄='25')
print(user_profile)

# 14
def make_car(maked, size, **other_size):
    car = {}
    car['maked'] = maked
    car['size'] = size
    for key, value in other_size.items():
        car[key] = value
    return car
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)