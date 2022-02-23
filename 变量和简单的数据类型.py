# 知识
# 2.3.3 制表符
print('\tPython')  # 开头出现制表符，即空格
# 换行符
print('Python\nsda')

# 2.3.4 删除空白:
# strip:删除两端空白或字符串；rstrip：删除结尾空白或字符串；lstrip：删除开头空白或字符串。


# 例题
# 1
a = 'hello, wolrd!'
print(a.title())

# 2
a = 'hello, wolrd!'
print(a.title())
b = a + ' Python!'
print(b)

# 3
name = "Eric"
print('Hello ' + name + ",would you like to learn some Python today?")
name2 = 'Hello {},would you like to learn some Python today?'.format('Eric')
print(name2)

# 4
name = 'li Ning chinA'
print(name.lower())
print(name.upper())
print(name.title())
print(name.capitalize())

# 5
name = 'albert einstein'
a = "once said, “A person who never made a mistake never tried anything new.”"
print(name.title() + ' ' + a)

# 6
famous_person = 'albert einstein'
message = "a person who never made a mistake never tried anything new.”"
print(famous_person.title() + ' once said, “' + message.capitalize())

# 7
famous_person = ' \tli ning chang       \n    LI Chana      '
famous_person1 = 'li ning chang       \nLI Chana  '
print(famous_person)
print(famous_person.strip())
print(famous_person.rstrip())
print(famous_person.lstrip())
print(famous_person1.strip('na'))
print(famous_person1.lstrip('li '))
print(famous_person1.rstrip('hana '))

# 8
print(2 + 4 + 2)
print(10 - 2)
print(2 * 4)
print(16 / 2)
print(2 ** 3)

# 9
number = '5'
print('你最喜欢的数字是：', number)

