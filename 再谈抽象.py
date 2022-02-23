# # 知识
# # 7.1.1 多态：不知道变量指向的是哪种对象，也能够对其执行操作，且操作的行为将随对象所属的类型（类）而异。
# # 7.1.3 封装：向外部隐藏不必要的细节。
# # 多态让你无需知道对象所属的类（对象的类型）就能调用其方法，而封装让你无需知道对象的构造就能使用它。
# # 7.1.4 继承
# # 7.2.1 每个对象都属于特定的类，并被称为该类的实例。“云雀”为“鸟类”的子类，而“鸟类”为“云雀”的超类
# # 7.2.3 属性、函数和方法：方法和函数的区别表现在前一节提到的参数self上。
# # 方法（更准确地说是关联的方法）将其第一个参数关联到它所属的实例，因此无需提供这个参数。
# # 私有的：要让方法或属性成为私有的（不能从外部访问），只需让其名称以两个下划线打头即可。
# class Secretive:
#     def __inaccessible(self):
#         print("Bet you can't see me ...")
#     def accessible(self):
#         print("The secret message is:")
#         self.__inaccessible()
# s = Secretive()
# # s.__inaccessible()
# s.accessible()
# s._Secretive__inaccessible()
# # 在开头加上一个下划线和类名，就能从类外访问私有方法，然而不应这样做。
#
# # 7.2.6 指定超类：要指定超类，可在class语句中的类名后加上超类名，并将其用圆括号括起。
class Filter:
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]
class SPAMFilter(Filter): # SPAMFilter是Filter的子类
    def init(self): # 重写超类Filter的方法init
        self.blocked = ['SPAM']
#
# # 7.2.7 深入探讨继承
print(issubclass(SPAMFilter, Filter))
# issubclass(A, B)：确定A是否是B的子类。
print(SPAMFilter.__bases__)
print(Filter.__bases__)
# __bases__:访问类的基类.
# s = SPAMFilter()
# print(isinstance(s, SPAMFilter))
# print(isinstance(s, Filter))
# print(isinstance(s, str))
# # isinstance(object, class)：确定对象是否是指定类的实例。
# print(s.__class__)
# # __class__：要获悉对象属于哪个类。
#
# # 7.2.8 多个超类
# class Calculator:
#     def calculate(self, expression):
#         self.value = eval(expression)
#
# class Talker:
#     def talk(self):
#         print('Hi, my value is', self.value)
#
# class TalkingCalculator(Calculator, Talker):
#     pass
# tc = TalkingCalculator()
# tc.calculate('1 + 2 * 3')
# tc.talk()
# # 多重继承，如果类的方法名相同需要认真排序，不然会覆盖方法。
# # 多个超类的超类相同时，查找特定方法或属性时访问超类的顺序称为方法解析顺序（MRO）。
#
# # 7.2.9 接口和内省
# # 只关心其接口（协议）——对外暴露的方法和属性。
# print(hasattr(tc, 'talk'))
# print(hasattr(tc, 'fnord'))
# # hasattr(object, name)：确定对象是否有指定的属性。
# print(callable(getattr(tc, 'talk', None)))
# print(callable(getattr(tc, 'fnord', None)))
# # callable(object)：判断对象是否是可调用的（如是否是函数或方法）。
# # getattr(object,name[,default])：获取属性的值，还可提供默认值。
# setattr(tc, 'name', 'Mr. Gumby')
# print(tc.name )
# # setattr(object, name, value):将对象的指定属性设置为指定的值;setattr与getattr功能相反.
#
# # 7.2.10 抽象基类
# from abc import ABC, abstractmethod
# class Talker(ABC):
#     @abstractmethod
#     def talk(self):
#         pass
# # 形如@this的东西被称为装饰器。
# Talker()
# # 抽象类（即包含抽象方法的类）最重要的特征是不能实例化。
# class Knigget(Talker):
#     def talk(self):
#         print("Ni!")
# # 你可重新编写这个类，使其实现要求的方法。
# k = Knigget()
# print(isinstance(k, Talker))
# k.talk()
#
# import random
# a = [1, 2, 6, 5]
# b = random.choice(a)
# print(b)
# # random.choice(sequence) 从一个非空序列中随机地选择一个元素
#
# print(type(a), type(b))
# # type(object) 返回对象的类型
#
#
# # # 例题
# # from random import choice
# # x = choice(['Hello, world!', [1, 2, 'e', 'e', 'e', 4]])
# # print(x.count('e'))
# # # random.choice(sequence) :从一个非空序列中随机地选择一个元素
# # def length_mseeage(x):
# #     print("the length of", repr(x), "is", len(x))
# # length_mseeage('Fnord')
# # length_mseeage([1, 2, 3])
# #
# # class Person:
# #     def set_name(self,name):
# #         self.name = name
# #
# #     def get_name(self):
# #         return self.name
# #
# #     def greet(self):
# #         print("Hello,world! I'm {}.".format(self.name))
# #
# # foo = Person()
# # bar = Person()
# # foo.set_name('yan shao')
# # bar.set_name('yan shaoyou')
# # foo.greet()
# # bar.greet()
# # print(foo.name)
# # print(foo.get_name())
# #
# # class MemberCounter:
# #     members = 0
# #     def init(self):
# #         MemberCounter.members += 1
# # m1 = MemberCounter()
# # m1.init()
# # print(MemberCounter.members)
# # print(m1.members)
# #
# # class Filter:
# #     def init(self):
# #         self.blocked = []
# #     def filter(self, sequence):
# #         return [x for x in sequence if x not in self.blocked]
# #
# # class SPAMFilter(Filter):   # SPAMFilter是Filter的子类
# #     def init(self):         # 重写超类Filter的方法init
# #         self.blocked = ['SPAM']
# # f = Filter()
# # f.init()
# # print(f.filter([1, 2, 3]))
# # s = SPAMFilter()
# # s.init()
# # print(s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM']) )
# #
# # print(issubclass(SPAMFilter, Filter))  # issubclass：确定A是否是B的子类
# # print(issubclass(Filter, SPAMFilter))
# # print(SPAMFilter.__bases__)            # __bases__：如果你有一个类，并想知道它的基类
# # print(Filter.__bases__)
# # s = SPAMFilter()
# # print(isinstance(s, SPAMFilter))       # isinstance:确定对象是否是指定类的实例
# # print(isinstance(s, Filter))
# # print(isinstance(s, str))
# # print(s.__class__)                     # __class__：获悉对象属于哪个类
# #
# # class Calculator:
# #     def calculate(self, expression):
# #         self.value = eval(expression)
# #
# # class Talker:
# #     def talk(self):
# #         print('Hi, my value is', self.value)
# #
# # class TalkingCalculator(Calculator, Talker):
# #     pass
# # tc = TalkingCalculator()
# # tc.calculate('1 + 2 * 3')
# # tc.talk()
# # print(hasattr(tc, 'talk'))  # hasattr：确定对象是否有指定的属性
# # print(hasattr(tc, 'fnord'))
# # print(callable((getattr(tc, 'talk', None))))  # callable：判断对象是否是可调用的（如是否是函数或方法）
# # # getattr:获取属性的值，还可提供默认值，然后对返回的对象调用callable。
# # print(callable(getattr(tc, 'fnord', None)))
# # setattr(tc, 'name', 'Mr. Gumby')  #  setattr与getattr功能相反，将对象的指定属性设置为指定的值
# # print(tc.name)
# #
# # from abc import ABC, abstractmethod
# # class Talker(ABC):
# #     @abstractmethod
# #     def talk(self):
# #         pass
# #
# # class Knigget(Talker):
# #     def talk(self):
# #         print("Ni!")
# #
# # k = Knigget()
# # print(isinstance(k, Talker))
# # k.talk()
# #
# # class Herring:
# #     def talk(self):
# #         print("Blub.")
# # h = Herring()
# # print(isinstance(h, Talker))
# # print(isinstance(h, Herring))
# # print(Talker.register(Herring))
# # print(isinstance(h, Talker))
