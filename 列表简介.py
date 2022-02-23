# 知识


# 例题
# 1
names = ['li ning', 'chana chdu', 'anhui hefei']
print(names[0].title())
print(names[1].capitalize())
print(names[2].title())

# 2
names = ['li ning', 'chana chdu', 'anhui hefei']
message = ', 你好！'
print(names[0] + message)
print('{}'.format(names[1] + message))
print(names[2], message)  # 逗号连接会出现空格

# 3
交通 = ['电动车', '地铁', '汽车']
message = 'i would like to own a Honda '
print(message.capitalize() + 交通[0])
print(message.capitalize(),交通[1])
print(message.capitalize() + '{}'.format(交通[2]))

# 4
names = ['li ning', 'chana chdu', 'anhui hefei']
message = 'can you dianner, '
for i in names:
    print(message + i.title() + '!')

# 5
names = ['li ning', 'chana chdu', 'anhui hefei']
message = 'can you dianner, '
message1 = ":”sorry,i can't“ "
for i in names:
    if len(i) == 10:
        print(i.title() + ' said' + message1)
        names.append('anhui hecsfe')
    else:
        print(message + i.title() + '!')

# 6
names = ['li ning', 'chana chdu', 'anhui hefei']
message = 'can you dianner, '
message1 = ":”sorry,i can't“ "
message2 = '我找到了更大的餐桌，可以请更多的盆友！'
names.append('anhui hecsfe')
names.insert(0, 'anhui huangshan')
names.insert(2, 'ma anshan')
for i in names:
    if len(i) == 10:
        print(i.title() + ' said' + message1)
        print(message2)
    else:
        print(message + i.title() + '!')

# 7
names = ['li ning', 'chana chdu', 'anhui hefei']
message = 'can you dianner, '
message1 = ":”sorry,i can't“ "
message2 = '我找到了更大的餐桌，可以请更多的盆友！'
message3 = '新餐桌无法及时送达，抱歉晚上不能聚餐了。'
names.append('anhui hecsfe')
names.insert(0, 'anhui huangshan')
names.insert(2, 'ma anshan')
print(message2)
for i, name in enumerate(names):  # enumerate:列表索引和元素
    if i < 2:
        print(message + name.title())
    else:
        print(name.title() + message3)
        print(names.pop().title() + message3)

# 8
place = ['anhui', '1hefei', 'wuhu', 'maanshan', 'najing']
print(place)
print(sorted(place))
print(place)
place.reverse()
print(place)
place.reverse()
print(place)
place.sort()
print(place)
place.sort(reverse=True)
print(place)

# 9
names = ['li ning', 'chana chdu', 'anhui hefei']
message = 'can you dianner, '
message1 = ":”sorry,i can't“ "
message2 = '我找到了更大的餐桌，可以请更多的盆友！'
message3 = '新餐桌无法及时送达，抱歉晚上不能聚餐了。'
names.append('anhui hecsfe')
names.insert(0, 'anhui huangshan')
names.insert(2, 'ma anshan')
print(len(names))

# 10
names = ['li ning', 'chana chdu', 'anhui hefei']
交通 = ['电动车', '地铁', '汽车']
names.append('西游')
names.extend(交通)
print(names)
# names.append(交通)
# print(names)
names.insert(0,'游戏')
names.pop()
names.pop(-2)
print(names)
print(len(names))
names.remove('地铁')
print(names)
print(sorted(names))
print(names)
names.sort()
print(names)
names.reverse()
print(names)
print(names[0], names[1])
del names[0]
print(names)
