# # 知识
# # 9.2.2
# class Bird:
#     def __init__(self):
#         self.hungry = True
#     def eat(self):
#         if self.hungry:
#             print('Aaaah...')
#             self.hungry = False
#         else:
#             print('No, thanks!')
# class SongBird(Bird):
#     def __init__(self):
#         Bird.__init__(self)  # 关联父类方法，可以直接使用父类方法
#         self.sound = 'Squawk!'
#     def sing(self):
#         print(self.sound)
# sb = SongBird()
# sb.sing()
# sb.eat()
# # 在子类中添加，父类.__init__(self)：关联父类方法，可以直接使用父类方法
#
# class SongBird(Bird):
#     def __init__(self):
#         super().__init__()  # super().__init__():关联父类方法，可以直接使用父类方法;
#         self.sound = 'Squawk!'
#     def sing(self):
#         print(self.sound)
# sb = SongBird()
# sb.sing()
# sb.eat()
#
# # 9.3.1 基本的序列和映射协议
# def check_index(key):
#     if not isinstance(key, int):
#         raise TypeError
#     if key < 0:
#         raise IndexError
#
# class ArithmeticSequnce:
#     def __init__(self, start=0, step=1):
#         self.start = start  # 存储起始值
#         self.step = step    # 存储步长值
#         self.changed = {}   # 内衣任何元素被修改
#
#     def __getitem__(self, key):
#         check_index(key)
#         try:
#             return self.changed[key]             # 修改过？
#         except KeyError:                         # 如果没有修改过，
#             return self.start + key * self.step  # 就计算元素的值
#
#     def __setitem__(self, key, value):
#         check_index(key)
#         self.changed[key] = value   # 存储修改后的值
# s = ArithmeticSequnce(1, 2)
# print(s[4])
# s[4] = 2
# print(s[4])
# print(s[5])
# print(s[3])
# print(s['four'])
# print(s[-4])
# # 在子类中添加，super().__init__()：关联父类方法，可以直接使用父类方法
# # super：可返回多个父类的方法或实例，尽量使用super而非父类.__init__(self)。
#
# # __len__(self)：返回集合包含的项数。
# # 对序列来说为元素个数，对映射来说为键-值对数。如果__len__返回零（且没有实现覆盖这种行为的__nonzero__），对象在布尔上下文中将被视为假（就像空的列表、元组、字符串和字典一样）。
# #
# # __getitem__(self, key)：返回与指定键的值。
# # 对序列来说，键应该是0~n-1的整数（也可以是负数，这将在后面说明），其中n为序列的长度。对映射来说，键可以是任何类型。
#
# # __setitem__(self, key, value)：存储键的值，以便以后能够使用__getitem__来获取。
#
# # __delitem__(self, key)：对对象的组成部分使用__del__语句时被调用，应删除与key相关联的值。
# # 同样，仅当对象可变（且允许其项被删除）时，才需要实现这个方法。
#
# # 对于序列，如果键为负整数，应从末尾往前数。换而言之，x[-n]应与x[len(x)-n]等效。
# # 如果键的类型不合适（如对序列使用字符串键），可能引发TypeError异常。
# # 对于序列，如果索引的类型是正确的，但不在允许的范围内，应引发IndexError异常。
#
# # 9.5.1 函数 property
# class CLanguage:
#     def __init__(self,n):
#         self.__name = n
#     def setname(self,n):
#         self.__name = n
#     def getname(self):
#         return self.__name
#     def delname(self):
#         self.__name = "xxx"
#     name = property(getname, setname, delname, '指明出处')
# # property(fget, fset, fdel, doc):所有参数都是可选的
# # fget -- 获取属性值的函数；
# # fset -- 设置属性值的函数；
# # fdel -- 删除属性值函数；
# # doc -- 属性描述信息。
#
# clang = CLanguage("C语言中文网")
# # 调取说明文档的 2 种方式
# print(CLanguage.name.__doc__)
# help(CLanguage.name)
# # 调用 getname() 方法
# print(clang.name)
# # 调用 setname() 方法
# clang.name = "Python教程"
# print(clang.name)
# # 调用 delname() 方法
# del clang.name
# print(clang.name)
#
# # 9.5.2 静态方法和类方法
# # 静态方法:包装在staticmethod类的对象中;静态方法的定义中没有参数self，可直接通过类来调用。
# # 类方法：包装在classmethod类的对象中;包含类似于self的参数，通常被命名为cls。
# class MyClass:
#     def smeth():  # 静态方法
#         print('This is a static method')
#     smeth = staticmethod(smeth)  # 手工包装和替换方法有点繁琐
#
#     def cmeth(cls):  # 类方法
#         print("This is a class method of", cls)
#     cmeth = classmethod(cmeth)  # 手工包装和替换方法有点繁琐
#
# class MyClass:
#     @staticmethod  # 静态方法
#     def smeth():
#         print('This is a static method')
#
#     @classmethod  # 类方法
#     def cmeth(cls):
#         print("This is a class method of", cls)
# MyClass.smeth()
# MyClass.cmeth()
# # 使用装饰器，再访问静态方法和类方法并使用它们（无需实例化类）。
#
# # 9.5.3 __getattr__、__setattr__等方法，在可以使用property时，尽量优先使用。
# class Rectangle:
#     def __init__(self):
#         self.width = 0
#         self.height = 0
#     def __setattr__(self, name, value):
#         if name == 'size':
#             self.width, self.height = value
#         else:
#             self.__dict__[name] = value
#     def __getattr__(self, name):
#         if name == 'size':
#             return self.width, self.height
#         else:
#             raise AttributeError()
# # __getattribute__(self, name)：在属性被访问时自动调用（只适用于新式类）。
# # __getattr__(self, name)：在属性被访问而对象没有这样的属性时自动调用。
# # __setattr__(self, name, value)：试图给属性赋值时自动调用。
# # __delattr__(self, name)：试图删除属性时自动调用。
#
# # 9.6.1 迭代器协议
# # 方法__iter__返回一个迭代器，它是包含方法__next__的对象，而调用这个方法时可不提供任何参数。
# class Fibs:
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         return self.a
#     def __iter__(self):
#         return self
# a = Fibs()
# for f in a:
#     if f > 1000:
#         print(f)
#         break
#
# it = iter([1, 2, 3])  # iter(obj)：从可迭代对象创建一个迭代器
# print(next(it))  # next(it)：让迭代器前进一步并返回下一个元素
#
# class TestIterator:
#     value = 0
#     def __next__(self):
#         self.value += 1
#         if self.value > 10: raise StopIteration
#         return self.value
#     def __iter__(self):
#         return self
# ti = TestIterator()
# print(list(ti))
#
# # 9.7.1 创建生成器
# nested = [[1, 2], [3, 4], [5]]
# def flatten(nested):
#     for sublist in nested:
#         for element in sublist:
#             yield element  # yield:生成器标志，
# # 生成器不是使用return返回一个值，而是可以生成多个值，每次一个。每次使用yield生成一个值后，
# # 函数都将冻结，即在此停止执行，等待被重新唤醒。被重新唤醒后，函数将从停止的地方开始继续执行。
# print(list(flatten(nested)))
#
# # 9.7.2 递归式生成器
# def flatten(nested):
#     try:
#         try:
#             nested + ''
#         except TypeError:
#             pass
#         else:
#             raise TypeError
#         for sublist in nested:
#             for element in flatten(sublist):  # 这里迭代的，但会引发TypeError异常，所以使用异常忽略。
#                 yield element
#     except TypeError:
#         yield nested
# print(list(flatten(['foo', ['bar', ['baz']]])))
#
# # 9.7.3 通用生成器
# # yield意味着应生成一个值，而return意味着生成器应停止执行。
# # 组成：生成器的函数和生成器的迭代器。生成器的函数是由def语句定义的，其中包含yield。生成器的迭代器是这个函数返回的结果。
# def simple_generator():
#     yield 1
# print(list(simple_generator()))
#
# # 9.7.4 生成器的方法
# def repeater(value):
#     while True:
#         new = (yield value)
#         if new is not None:
#             value = new
# r = repeater(42)
# # next(r)
# print(r.send("Hello, world!"))   # ?
# # send:外部世界可访问生成器的方法;类似于next;仅当生成器被挂起（即遇到第一个yield）后，使用send（而不是next）才有意义。
# # throw:用于在生成器中（yield表达式处）引发异常，调用时可提供一个异常类型、一个可选值和一个traceback对象。
# # close:用于停止生成器，调用时无需提供任何参数。
#
# # 9.8.5 基线条件
# # 基线条件（针对最小的问题）：满足这种条件时函数将直接返回一个值。
# # 递归条件：包含一个或多个调用，这些调用旨在解决问题的一部分。
#
# # 9.8.4 检测冲突
# def conflict(state, nextX):                            #state为已摆放的棋子的位置的元组，比如（1,3,0）
#     nextY = len(state)                                 #获取当前行号
#     for i in range(nextY):                             #检查每一个已摆放的棋子和当前行要摆放的棋子的位置（nextX, nextY）是否冲突
#         if abs(state[i] - nextX) in (0, nextY - i):    #关键！若是两个棋子 行差值 的绝对值 出现在元组 （0，行差值）中，则冲突发生，返回True
#             return True
#     return False                                       #无冲突，可行的摆放位置
#
#
# # 9.8.5 基线条件
# def queens(num, state):  # num：皇后数量
#     if len(state) == num-1:  # 检查是否最后一行，如果是最后一行，则执行终极操作，不再递归
#         for pos in range(num):  # pos从0到 棋盘行数-1
#             if not conflict(state, pos):  # 如果没有冲突，产生当前皇后的位置信息
#                 yield pos
# print(list(queens(4, (1, 3, 0))))
#
# # 9.8.6 递归条件
# def queens(num=8, state=()):  # #num为棋盘的行数，state为已摆放的棋子的列数汇总，类型为元组
#     for pos in range(num):
#         if not conflict(state, pos):
#             if len(state) == num - 1:  # 若是最后一行，对于pos in range(num)调用conflict(state, num) ,
#                 yield (pos,)  # 如果没有冲突,生成元组
#             else:
#                 for result in queens(num, state + (pos,)):
#                     yield (pos,) + result
# # 若不是最后一行 对于pos in range(num)调用conflict(state, pos),
# # 如果没有冲突,state更新,递归调用queens(num, state) state将更新
# # result这个变量代表的是quees返回的元组
# # queens(...)返回的是一个迭代器（生成器 更准确！生成器就是一种迭代器！），因此，下面代码中的result是一个元组，而不是一个数值：
# print(list(queens(4)) )
# print(len(list(queens(8))))
#
# # 9.8.7 扫尾工作
# def prettyprint(solution):
#     def line(pos, length=len(solution)):
#         return '. ' * (pos) + 'X ' + '. ' * (length-pos-1)
#     for pos in solution:
#         print(line(pos))
#
# import random
# prettyprint(random.choice(list(queens(8))))


# 例题
# class FooBar:
#     def __init__(self):
#         self.somevar = 42
# f = FooBar()
# print(f.somevar)
# class FooBar:
#     def __init__(self, value= 42):
#         self.somevar = value
# f = FooBar('This is a constructor argument')
# print(f.somevar)
#
# class A:
#     def hello(self):
#         print('hello, I am A.')
# class B(A):
#     pass
# a = A()
# b = B()
# a.hello()
# b.hello()
# class B(A):
#     def hello(self):
#         print('hello, I am B.')
# b = B()
# b.hello()
#
# class Bird:
#     def __init__(self):
#         self.hungry = True
#     def eat(self):
#         if self.hungry:
#             print('Aaaah...')
#             self.hungry = False
#         else:
#             print('No, thanks!')
# b = Bird()
# b.eat()
# b.eat()
# class SongBird(Bird):
#     def __init__(self):
#         self.sound = 'Squawk!'
#     def sing(self):
#         print(self.sound)
# sb = SongBird()
# sb.sing()
# class SongBird(Bird):
#     def __init__(self):
#         Bird.__init__(self)
#         self.sound = 'Squawk!'
#     def sing(self):
#         print(self.sound)
# sb = SongBird()
# sb.sing()
# sb.eat()
# sb.eat()
#
# class Bird:
#     def __init__(self):
#         self.hungry = True
#     def eat(self):
#         if self.hungry:
#             print('Aaaah...')
#             self.hungry = False
#         else:
#             print('No, thamks!')
#
#
# class SongBird(Bird):
#     def __init__(self):
#         super().__init__()  # super(class, obj): 返回一个超类的关联实例
#         self.sound = 'Squawk!'
#     def sing(self):
#         print(self.sound)
# sb = SongBird()
# sb.sing()
# sb.eat()
# sb.eat()
#
# def check_index(key):
#     """
#      指定的键是否是可接受的索引？
#      键必须是非负整数，才是可接受的。如果不是整数，
#      将引发TypeError异常；如果是负数，将引发Index
#      Error异常（因为这个序列的长度是无穷的）
#      """
#     if not isinstance(key, int):
#         raise TypeError
#     if key < 0:
#         raise IndexError
#
# class ArithmeticSequnce:
#     def __init__(self, start=0, step=1):
#         """
#         初始化这个算术序列
#          start -序列中的第一个值
#          step -两个相邻值的差
#          changed -一个字典，包含用户修改后的值
#         """
#         self.start = start  # 存储起始值
#         self.step = step    # 存储步长值
#         self.changed = {}   # 内衣任何元素被修改
#
#     def __getitem__(self, key):
#         """从算术序列中获取一个元素"""
#         check_index(key)
#         try:
#             return self.changed[key]             # 修改过？
#         except KeyError:                         # 如果没有修改过，
#             return self.start + key * self.step  # 就计算元素的值
#
#     def __setitem__(self, key, value):
#         """修改算术序列中的元素"""
#         check_index(key)
#         self.changed[key] = value   # 存储修改后的值
# s = ArithmeticSequnce(1, 2)
# print(s[4])
# s[4] = 2
# print(s[4])
# print(s[5])
# print(s[3])
# # print(s['four'])
# # print(s[-4])
#
# class CounterList(list):
#     def __init__(self, *args):
#         super().__init__(*args)
#         self.counter = 0
#
#     def __getitem__(self, index):
#         self.counter += 1
#         return super(CounterList,self).__getitem__(index)
#
# cl = CounterList(range(10))
# print(cl)
# cl.reverse()
# print(cl)
# del cl[3:6]
# print(cl)
# print(cl.counter)
# print(cl[4] + cl[2])
# print(cl.counter)
#
# class Rectangle:
#     def __init__(self):
#         self.width = 0
#         self.height = 0
#     def set_size(self, size):
#         self.width, self.height = size
#     def get_size(self):
#         return self.width, self.height
# r = Rectangle()
# r.width = 10
# r.height = 5
# print(r.get_size())
# r.set_size((150, 100))
# print(r.width)
#
# class Rectangle:
#     def __init__(self):
#         self.width = 0
#         self.height = 0
#     def set_size(self, size):
#         self.width, self.height = size
#     def get_size(self):
#         return self.width, self.height
#     size = property(get_size, set_size)  # property(fget, fset, fdel, doc):返回一个特性；所有参数都是可选的
# r = Rectangle()
# r.width = 10
# r.height = 5
# print(r.size)
# r.size = 150, 100
# print(r.width)
#
# class MyClass:
#     def smeth():
#         print('This is a static method')
#     smeth = staticmethod(smeth)
#
# def cmeth(cls):
#     print("This is a class method of", cls)
# cmeth = classmethod(cmeth)
#
# class MyClass:
#     @staticmethod
#     def smeth():
#         print('This is a static method')
#
#     @classmethod
#     def cmeth(cls):
#         print("This is a class method of", cls)
# MyClass.smeth()
# MyClass.cmeth()
#
# class Rectangle:
#     def __init__(self):
#         self.width = 0
#         self.height = 0
#     def __setattr__(self, name, value):
#         if name == 'size':
#             self.width, self.height = value
#         else:
#             self.__dict__[name] = value
#     def __getattr__(self, name):
#         if name == 'size':
#             return self.width, self.height
#         else:
#             raise AttributeError()
#
# class Fibs:
#     def __init__(self):
#         self.a = 0
#         self.b = 0
#     def __next__(self):   # next(it):  让迭代器前进一步并返回下一个元素
#         self.a, self.b = self.b, self.a + self.b
#         return self.a
#     def __iter__(self):   # iter(obj): 从可迭代对象创建一个迭代器
#         return self
# # fibs = Fibs()
# # for f in fibs:
# #     if f > 1000:
# #         print(f)
# #         break
# it = iter([1, 2, 3])
# print(next(it))
# print(next(it))
# print(next(it))
#
# class TestIterator:
#     value = 0
#     def __next__(self):
#         self.value += 1
#         if self.value > 10:
#             raise StopIteration
#         return self.value
#     def __iter__(self):
#         return self
# ti = TestIterator()
# print(list(ti))
#
# def flatten(nested):
#     for sublist in nested:
#         for element in sublist:
#             yield element
# nested = [[1, 2], [6, 4], [5]]
# for num in flatten(nested):
#     print(num)
# print(list(flatten(nested)))
#
# def flatten(nested):
#     try:
#         for sublist in nested:
#             for element in flatten(sublist):
#                 yield element
#     except TypeError:
#         yield nested
# print(list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8])))
#
# def flatten(nested):
#     try:
#         """不迭代类似字符串的对象"""
#         try:
#             nested + ''
#         except TypeError:
#             pass
#         else:
#             raise TypeError
#         for sublist in nested:
#             for element in flatten(sublist):
#                         yield element
#     except TypeError:
#         yield nested
# print(list(flatten(['foo', ['bar', ['baz']]])))
# print(list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8])))
#
# def simple_generator():
#     yield 1
# print(simple_generator)
# print(simple_generator())
#
# def repeater(value):
#     while True:
#         new = (yield value)
#         if new is not None:
#             value = new
# r = repeater(42)
# print(next(r))
# print(r.send("hello, world!"))
#
# def flatten(nested):
#     result = []
#     try:
#         """不迭代类似字符串的对象"""
#         try:
#             nested + ''
#         except TypeError:
#             pass
#         else:
#             raise TypeError
#         for sublist in nested:
#             for element in flatten(sublist):
#                         result.append(element)
#     except TypeError:
#         result.append(nested)
#     return result
#
# def conflict(state, nextX):
#     nextY = len(state)
#     for i in range(nextY):
#         if abs(state[i] - nextX) in (0, nextY - i):
#             return True
#     return False
#
# def queens(num, state):
#     if len(state) == num-1:
#         for pos in range(num):
#             if not conflict(state, pos):
#                 yield pos
# print(list(queens(4, (1, 3, 0))))
