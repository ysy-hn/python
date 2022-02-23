# 知识
# 6.2 访问字典中的值：即访问主键
# 6.2.2 添加键-值对：直接添加
# 6.2.4 修改字典中的值：直接通过主键修改
# 6.2.5 删除键—值对：del删除、pop删除、popitem删除
# 字典可以进行嵌套、切片（不直接对字典切片，间接切片可见下例）、迭代等操作
aliens = []
for alien_number in range(0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    print(alien)


# 例题
# 1
dict = {'first_name': 'li ning', 'last_name': 'china', 'age': '28', 'city': 'beijing'}
for k, v in dict.items():
    print(k, v)

# 2
numbers = {'li ning': '1', 'huanghe': '2', 'changjiang': '3', 'huangshan': '3', 'hefei': 4}
for k, v in numbers.items():
    print(k + ", {}是你喜欢的数字吗？".format(v))

# 3
numbers = {'li ning': '1', 'huanghe': '2', 'changjiang': '3', 'huangshan': '3', 'hefei': 4}
for k,v in numbers.items():
    print('{}:\n'.format(k), v)

# 4
numbers = {'li ning': '1', 'huanghe': '2', 'changjiang': '3', 'huangshan': '3', 'hefei': 4}
for k,v in numbers.items():
    print('{}:'.format(k), v)

# 5
dict = {'haunghe': 'china', 'changjiang': 'china', 'nile': 'egypt'}
for k, v in dict.items():
    print("The {1} runs through {0}".format(v.title(), k.title()))

# 6
user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }
user_1 = {
 'first': 'enrico',
 'last': 'fermi',
 }
for k, v in user_0.items():
    if k in user_1:
        print("谢谢参与，{}".format(v.title()))
    else:
        print("欢迎来参与，{}".format(v.title()))

# 7
dict = {'first_name': 'li ning', 'last_name': 'china', 'age': '28', 'city': 'beijing'}
people1 = {'li ning': '1', 'huanghe': '2'}
people2 = {'changjiang': '3', 'huangshan': '3', 'hefei': 4}
people = [dict, people1, people2]
for i in people:
    print(str(i) + ':')
    for k, v in i.items():
        print(k + ': ' + str(v))
    print('\n')

# 8
benben = {'li ning': 'dog'}
benben2 = {'san guo': 'zhuzhu'}
benben.update(benben2)
haha = {'shui hu': 'cat'}
lanlan = {'xi you': 'pig'}
pets = [benben, haha, lanlan]
for i in pets:
    for k, v in i.items():
        print("{}的宠物是：{}".format(k, v))

# 9
favorite_places = {
    'li ning': ['haung san', 'hefei'],
    'shui hu': ['cheng du', 'ma anshan'],
    'xi you': ['an qing', 'nan jing']
}
for k, v in favorite_places.items():
    print("{}喜欢{}、{}，还有喜欢的城市吗？".format(k.title(), v[0].title(), v[1].title()))
    a = input('y/n:')
    if a.lower() == 'y':
        print('好的，谢谢。')
    else:
        b = input('请输入你喜欢的城市：')
        print("{}还喜欢:".format(k.title()), b)

# 10
numbers = {'li ning': [0, 1, 2, 3], 'huanghe': [0, 1, 2], 'changjiang': [5, 1, 2, 3], 'huangshan': [0, 1, 2, 3, 8], 'hefei': [0, 1]}
for k, v in numbers.items():
    print(k + ':')
    for i in v:
        print(i)

# 11
numbers = {'li ning': [0, 1, 2, 3], 'huanghe': [0, 1, 2], 'changjiang': [5, 1, 2, 3], 'huangshan': [0, 1, 2, 3, 8], 'hefei': [0, 1]}
numbers.pop('hefei')
print(numbers)
numbers.popitem()
print(numbers)
numbers.setdefault('xi you')
print(numbers)
del numbers['li ning']
print(numbers)
numbers.clear()
print(numbers)
