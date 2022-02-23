# 知识
# 10.1 从文件中读取数据,with open('pi_digits.txt') as file_object:contents = file_object.read()句式
# 10.1.2 文件路径，Windows，在文件路径中使用反斜杠（\）；绝对文件路径，相对文件路径。
# 10.1.3 逐行读取，对整个文件使用for循环；
# 10.1.4 创建一个包含文件各行内容的列表，使用关键字with时，open()返回的文件对象只在with代码块内可用。
# 可在with代码块内将文件的各行存储在一个列表中，并在with代码块外使用该列表：可以立即处理文件的各个部分，也可推迟到程序后面再处理。
# readlines():读取文件所有行；strip删除两边空格或字符串；:rstrip:删除右边空格或字符串；lstrip:删除左边空格或字符串。
# 中文文档是‘gbk’的编码方式，我们需要将‘gbk’转化为utf-8
# 10.2 写入文件,保存数据的最简单的方式之一是将其写入到文件中。
# w:写入模式，需要手动添加换行符，删除原内容写入;a:附加模式，在既有文件末尾继续写入。
# 10.3 异常,try-except;try-except-else;try-except-else-finally;raise;pass;
# warnings.filterwarnings(action,category=Warning, ...) 用于过滤警告
# warnings.warn(message, category=None) 用于发出警告
# 10.4.1 使用 json.dump()存储和 json.load()读取；
# json.dump()接受两个实参：要存储的数据以及可用于存储数据的文件对象。
# 10.4.2 保存和读取用户生成的数据，对于用户生成的数据，使用json保存它们大有裨益，
# 因为如果不以某种方式进行存储，等程序停止运行时用户的信息将丢失。
# 将代码划分为一系列完成具体工作的函数；重构让代码更清晰、更易于理解、更容易扩展。


# 例题
# 1
with open('learning_python.txt', encoding='utf-8') as f:
    file = f.read()
    print(file)

with open('learning_python.txt', encoding='utf-8') as f:
    for line in f:
        print(line)

with open('learning_python.txt', encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())

# 2
with open('learning_python.txt', encoding='utf-8') as f:
    lines = f.readlines()
for line in lines:
    line = line.replace('python', 'c语言')
    print(line.rstrip())

# 3
user = input('请输入您的名字：')
filename = 'guest.txt'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(user + '\n')

# 4
while True:
    filename = 'guest_book.txt'
    users = input('请输入您的名字(或N退出）：')
    if users.upper() == "N":
        break
    print('欢迎您登录，{}'.format(users))
    with open(filename, 'a', encoding='utf-8') as f:
        f.write('{},登录成功。\n'.format(users))

# 5
filename = '原因.txt'
while True:
    users = input('你为何喜欢编程？（退出N）')
    if users.upper() == "N":
        break
    print(users)
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(users + '\n')

# 6
while True:
    try:
        a = int(input('请输入数值：'))
        b = int(input('请输入数值：'))
        c = a + b
        print(c)
        d = str(input('是否继续?（Y/N）'))
        if d.upper() == 'N':
            break
    except ValueError:
        print('输入错误，请输入数字。')

# 7
while True:
    users = eval(input('请输入想要运算的数值：'))
    try:
        if users == 0:
            break
        print('结果：' + str(users))
    except NameError:
        print('输入错误，请输入数字：')
    except SyntaxError:
        print('输入错误，请输入数字：')

while True:
    num1 = input('Please enter the fiest number:')
    if num1 == 'q':
        break
    num2 = input('Please enter the second number:')
    if num2 == 'q':
        break
    """判断数据是否为字符串"""
    try:
        sum = int(num1) + int(num2)
    except ValueError:
        print("Sorry,you can't input a string!")
    else:
        print('The answer is ' + str(sum))

# 8
filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    print(filename + ':')
    try:
        with open(filename, encoding='utf-8') as f:
            line = f.read()
            print(line)
    except FileNotFoundError:
        print('您好，文件不存在。')

# 9
filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    print(filename + ':')
    try:
        with open(filename, encoding='utf-8') as f:
            line = f.read()
            print(line)
    except FileNotFoundError:
        pass

# 10
def count_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("Sorry,the file " + filename + ' does not exist.')
    else:
        number = contents.lower().count('the')
        print("The number of 'the' is " + str(number))

filenames = ['book.txt', 'book2.txt']
for filename in filenames:
    count_words(filename)

# 11
import json
numbers = input('请输入你喜欢的数字：')
filename = 'numbers.json'
with open(filename, 'w+', encoding='utf-8') as f:
    json.dump(numbers, f)

with open(filename) as f:
    numbers = json.load(f)
print(numbers)

# 12
import json
filename = 'numbers.json'
try:
    with open(filename) as f:
        numbers = json.load(f)
        print(numbers)
except json.decoder.JSONDecodeError:
    numbers = input('请输入你喜欢的数字：')
    with open(filename, 'w+', encoding='utf-8') as f:
        json.dump(numbers, f)
        print(numbers)
else:
    print("Welcome back, " + numbers + "!")

# 13
# import json
#
# def get_stored_username():
#     """如果存储了用户名，就获取它"""
#     filename = 'username.json'
#     try:
#         with open(filename) as f_obj:
#             username2 = json.load(f_obj)
#     except json.decoder.JSONDecodeError:
#         return None
#     else:
#         return username2
#
# def get_new_username():
#     """提示用户输入用户名"""
#     username1 = input("你的名字？ ")
#     filename = 'username.json'
#     with open(filename, 'w') as f_obj:
#         json.dump(username1, f_obj)
#         return username1
#
# def greet_user():
#     """问候用户，并指出其名字"""
#     username2 = get_stored_username()
#     username1 = get_new_username()
#     if username1 == username2:
#         print("欢迎回来, " + username1 + "!")
#     else:
#         print(username1 + "，用户名不对!请重新输入正确的用户名。")
#
# greet_user()
# # 初次登陆失败，多次登陆账号会变化问题。
import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except json.decoder.JSONDecodeError:
        return None
    else:
        return username

def get_new_username():
    username = input('你的名字?')
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    username = get_stored_username()  # 运行读取
    if username:
        print('你的名字是：' + username + '？')
        result = input('是否正确（Y/N）：')
        if result.upper() == 'Y':
            print('欢迎回来, ' + username + '!')
        else:
            username = get_new_username()  # 运行写入
            print(username + "，用户名不对!请重新输入正确的用户名。")
    else:
        username = get_new_username()  # 运行写入
        print(username + "，欢迎初次登陆！")

greet_user()
