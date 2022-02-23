# 知识
# 9.1.1 创建 Dog 类，1. 方法__init__()，开头和末尾各有两个下划线，这是一种约定，
# 旨在避免Python默认方法与普通方法发生名称冲突。self为前缀的变量都可供类中的所有方法使用。
# 9.2.2 给属性指定默认值(可在类属性里直接赋默认值）,1. 直接修改属性的值;2. 通过方法修改属性的值,更新属性的方法;
# 3. 通过方法对属性的值进行递增,对方法的设计编写。
# 9.3 继承,1、创建子类时，父类必须包含在当前文件中，且位于子类前面。
# 2、定义子类时，必须在括号内指定父类的名称（子类名称命名一般接父类名称）。
# 3、super().__init__(self删除，父类形参保留）父类形参有默认值的只继承形参，默认值不继承，
# 可在子类中形参设置默认值,要添加其它形参直接添加（推荐），或不添加形参在下面添加属性并赋初始值，调用时要引用该属性并赋值（较麻烦）。
# 9.3.3 给子类定义属性和方法，直接定义；9.3.4 重写父类的方法，直接重写父类同名的方法，调用时不会调用父类方法。
# 9.3.5 将实例用作属性，类太长时可拆分成其它的类，便于优化。
# 9.4 导入类，创建的每个模块都编写文档字符串；9.4.2 在一个模块中存储多个类；9.4.3 从一个模块中导入多个类；
# 9.4.4 导入整个模块；9.4.5 导入模块中的所有类；9.4.6 在一个模块中导入另一个模块。
# 9.5 Python 标准库；OrderedDict：创建有序字典，要创建字典并记录其中的键—值对的添加顺序。
# 9.6 类编码风格：
# 1、类名应采用驼峰命名法，即将类名中的每个单词的首字母都大写，而不使用下划线；
# 2、实例名和模块名都采用小写格式，并在单词之间加上下划线；
# 3、每个类，都应紧跟在类定义后面包含一个文档字符串；
# 4、每个模块也都应包含一个文档字符串，对其中的类可用于做什么进行描述；
# 5、可使用空行来组织代码，但不要滥用。在类中，可使用一个空行来分隔方法；而在模块中，可使用两个空行来分隔类；
# 6、需要同时导入标准库中的模块和你编写的模块时，先编写导入标准库模块的import语句，再添加一个空行，然后编写导入你自己编写的模块的import语句。


# 例题
# 1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('餐馆位于合肥，名称是{}。'.format(self.restaurant_name))
    def open_restaurant(self):
        print('餐馆正在{}。'.format(self.cuisine_type))
a = Restaurant('庐州太太', '营业')
print(a.restaurant_name)
print(a.cuisine_type)
a.describe_restaurant()
a.open_restaurant()

# 2
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('餐馆位于合肥，名称是{}。'.format(self.restaurant_name))
    def open_restaurant(self):
        print('餐馆正在{}。'.format(self.cuisine_type))
b = Restaurant('饭店', '歇业')
b.describe_restaurant()
c = Restaurant('酒店', '打样')
c.describe_restaurant()
d = Restaurant('旅馆', '营业')
d.describe_restaurant()

# 3
class User:
     def __init__(self, first_name, last_name, age, height):
         self.first_name = first_name
         self.last_name = last_name
         self.age = age
         self.height = height

     def describe_user(self):
         full_name = self.first_name + self.last_name
         print("{}, 年龄是{}，身高是{}.".format(full_name, self.age, self.height))

     def greet_user(self):
         print('您好!')
a = User('齐天', '大圣', '500', '1.5')
a.greet_user()
a.describe_user()

# 4
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print('餐馆位于合肥，名称是{}。'.format(self.restaurant_name))

    def open_restaurant(self):
        print('餐馆正在{}。'.format(self.cuisine_type))

    def set_number_served(self):
        print('今天目前有{}人来吃饭。'.format(self.number_served))

    def increment_number_served(self, numbers):
        self.number_served += numbers
        print('今天可能共有{}人来吃饭。'.format(self.number_served))

restaurant = Restaurant('庐州太太', '营业', 30)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served()
restaurant.increment_number_served(50)
restaurant.increment_number_served(70)

# 5
class User:
    def __init__(self, first_name, last_name, age, height, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.login_attempts = login_attempts

    def describe_user(self):
        full_name = self.first_name + self.last_name
        print("{}, 年龄是{}，身高是{}.".format(full_name, self.age, self.height))

    def greet_user(self):
        print('您好!')

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)
a = User('齐天', '大圣', 500, 1.5, 20)
a.increment_login_attempts()
a.increment_login_attempts()
a.increment_login_attempts()
a.reset_login_attempts()
a.increment_login_attempts()

# 6
class IcerCreamStandRestaurant(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        super().__init__(restaurant_name, cuisine_type, number_served)

    def flavors_names(self, flavors):
        self.flavors = flavors
        for i in flavors:
            print(i + '是我比较喜欢的口味。')
        print(flavors)
a = IcerCreamStandRestaurant('庐州太太', '营业', 30)
a.describe_restaurant()
a.open_restaurant()
a.set_number_served()
a.increment_number_served(20)
b = ['原味', '水果', '牛奶']
a.flavors_names(b)

# 7
class AdminUser(User):
    def __init__(self, first_name, last_name, age, height, privileges, login_attempts=0,):
        super().__init__(first_name, last_name, age, height, login_attempts)
        self.privileges = privileges

    def show_privileges(self):
        for i in self.privileges:
            print('管理员有这些权限：' + i)
        print(self.privileges)

a = ["删除", "新建", "保存"]
b = AdminUser('齐天', '大圣', 500, 1.5, a, 20)
b.greet_user()
b.describe_user()
b.increment_login_attempts()
b.reset_login_attempts()
b.increment_login_attempts()
b.show_privileges()

# 8
class Pivileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for i in self.privileges:
            print('管理员有这些权限：' + i)
        print(self.privileges)

class AdminUser(User):
    def __init__(self, first_name, last_name, age, height, privileges, login_attempts=0,):
        super().__init__(first_name, last_name, age, height, login_attempts)
        self.privileges = Pivileges(privileges)

a = ["删除", "新建", "保存"]
b = AdminUser('齐天', '大圣', 500, 1.5, a, 20)
b.greet_user()
b.describe_user()
b.increment_login_attempts()
b.reset_login_attempts()
b.increment_login_attempts()
b.privileges.show_privileges()  # 调用privileges属性关联的show_privileges方法

# 9
# 10
from restaurant import IcerCreamStandRestaurant
a = IcerCreamStandRestaurant('庐州太太', '营业', 30)
a.describe_restaurant()
a.open_restaurant()
a.set_number_served()
a.increment_number_served(20)
b = ['原味', '水果', '牛奶']
a.flavors_names(b)

# 11
from admin import *
a = ["删除", "新建", "保存"]
b = AdminUser('齐天', '大圣', 500, 1.5, a, 20)
b.greet_user()
b.describe_user()
b.increment_login_attempts()
b.reset_login_attempts()
b.increment_login_attempts()
b.privileges.show_privileges()

# 12
from admin2 import *
a = ["删除", "新建", "保存"]
b = AdminUser('齐天', '大圣', 500, 1.5, a, 20)
b.privileges.show_privileges()

# 13
from collections import OrderedDict
numbers = OrderedDict()
numbers['li ning'] = 1
numbers['huanghe'] = 2
numbers['changjiang'] = 3
numbers['huangshan'] = 4
for name, value in numbers.items():
    print(name.title(), value)

# 14
from random import randint

class Die():
    def __init__(self, size=6, frequency=10):
        self.size = size
        self.frequency = frequency
        self.rolls = []

    def roll_die(self):
        for i in range(0, self.frequency):
            roll = str(randint(1, self.size))
            print(roll + '点')
            self.rolls.append(roll)
        print(self.rolls)

a = Die()
a.roll_die()
b = Die(10)
b.roll_die()
c = Die(20)
c.roll_die()