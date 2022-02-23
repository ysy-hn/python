# 知识
# 7.1.2 使用 int()来获取数值输入
# 7.1.3 求模运算符,处理数值信息时，求模运算符（%）是一个很有用的工具，它将两个数相除并返回余数：
# 7.2.3 使用标志,action = True,while。。。action = False,很常用。


# 例题
# 1
user = input('你想要租什么样的汽车？')
print('我想要租{}'.format(user))

# 2
user = int(input('请问，有多少人吃饭：'))
if user > 8:
    print('没有空桌了。')
else:
    print('有位子。')

# 3
user = int(input('请输入一个数字，查看是否是10的整数倍：'))
if user % 10 == 0:
    print('是整数倍！')
else:
    print('不是整数倍。')

# 4
while True:
    user = input('请输入你喜欢的披萨配料：')
    if user.lower() == 'quit':
        break
    else:
        print('我们会加入{}配料的。'.format(user))

# 5
action = True
while action:
    user = input('请问你多大了？')
    if user.lower() == 'quit':
        action = False
    elif int(user) <= 3:
        print('免费')
    elif 3 < int(user) <= 12:
        print('收费10元。')
    else:
        print('收费15元。')

# 6
action = True
while action:
    user = input('请输入你喜欢的披萨配料：')
    if user.lower() == 'quit':
        break
    else:
        print('我们会加入{}配料的。'.format(user))

# 7
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# 8
sandwich_oreders = ['番茄', '牛肉', '猪肉', '原味']
finished_sandwiches = []
while sandwich_oreders:
    a = sandwich_oreders.pop()
    print("我喜欢吃{}口味的三明治".format(a))
    finished_sandwiches.append(a)
print(finished_sandwiches)

# 9
sandwich_oreders = ['番茄', '牛肉', '猪肉', '原味', '牛肉', '牛肉']
finished_sandwiches = []
print('{}卖完了'.format('牛肉'))
while '牛肉' in sandwich_oreders:
    sandwich_oreders.remove('牛肉')
while sandwich_oreders:
    a = sandwich_oreders.pop()
    print("我喜欢吃{}口味的三明治".format(a))
    finished_sandwiches.append(a)
print(finished_sandwiches)

# 10
responses = {}
polling_active = True

while polling_active:
    name = input('你的名字：')
    response = input('你喜欢旅游的地方名称：')
    responses[name] = response
    repeat = input('还有人想要填写吗？(Y/N)')
    if repeat.upper() == 'N':
        polling_active = False
print('调查结果如下：')
for name, response in responses.items():
    print('{}喜欢去{}旅游.'.format(name, response))