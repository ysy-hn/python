# # 知识


# 例题
# 1
car = 'subaru'
if car == 'subar':
    print("Is car == 'subaru'? I predict True.")
    print(car == 'subaru')
else:
    print('False')

# 2
a = 12
b = 13
if a == b:
    print('True')
print('False')

# 3
alien_color = ['green', 'yellow', 'red']
for i in alien_color:
    if i == 'green':
        print('恭喜你获得5分！')

# 4
alien_color = ['green', 'yellow', 'red']
for i in alien_color:
    if i == 'green':
        print(i + ': 恭喜你获得5分！')
    else:
        print(i + ': 恭喜你获得10分！')

# 5
alien_color = ['green', 'yellow', 'red']
for i in alien_color:
    if i == 'green':
        print(i + ': 恭喜你获得5分！')
    elif i == 'yellow':
        print(i + ': 恭喜你获得10分！')
    else:
        print(i + ': 恭喜你获得15分！')

# 6
age = int(input('你现在几岁？'))
if 0 < age < 2:
    print('还是婴儿')
elif 2 <= age < 4:
    print('正在学习走路')
elif 4 <= age < 13:
    print('儿童')
elif 13 <= age < 20:
    print('青少年')
elif 20 <= age < 65:
    print('成年人')
else:
    print('老年人')

# 7
favorite_fruits = ['bananas', '番茄', '苹果', '西瓜']
for i in favorite_fruits:
    if i == 'bananas':
        print("You really like bananas!")

# 8
name = ['admin', 'bananas', '番茄', '苹果', '西瓜']
for i in name:
    if i == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello {}, thank you for logging in again".format(i))

# 9
name = ['admin', 'bananas', '番茄', '苹果', '西瓜']
name1 = ['桃子', '苹果']
for i in name1:
    if i in name:
        print("Hello {}, would you like to see a status report?".format(i))
    else:
        print("We need to find some users!")

# 10
current_uesrs = ['admin', 'bananas', '番茄', '苹果', '西瓜']
new_users = ['桃子', 'bAnanas', '西瓜', '草莓']
for i in new_users:
    if i.lower() in current_uesrs:
        print(i + "，需要输入别的用户名")
    else:
        print(i + ',该用户名未被使用')
        current_uesrs.append(i.lower())
print(current_uesrs)

# 11
a = list(range(1, 10))
for i in a:
    if i == 1:
        print('1st')
    elif i == 2:
        print('2nd')
    elif i == 3:
        print('3rd')
    else:
        print(str(i) + 'th')
