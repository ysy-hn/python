# # 知识
# # 8.1 异常是什么：
# # Python使用异常对象来表示异常状态，并在遇到错误时引发异常。异常对象未被处理（或捕获）时，
# # 程序将终止并显示一条错误消息（traceback）。
# # 8.2.1 raise语句：引发异常，并将一个类（必须是Exception的子类）或实例作为参数。
# raise Exception
# raise Exception('hyperdrive overload')
# # Exception         几乎所有的异常类都是从它派生而来的
# # AttributeError    引用属性或给它赋值失败时引发
# # OSError           操作系统不能执行指定的任务（如打开文件）时引发，有多个子类
# # IndexError        使用序列中不存在的索引时引发，为LookupError的子类
# # KeyError          使用映射中不存在的键时引发，为LookupError的子类
# # NameError         找不到名称（变量）时引发
# # SyntaxError       代码不正确时引发
# # TypeError         将内置操作或函数用于类型不正确的对象时引发
# # ValueError        将内置操作或函数用于这样的对象时引发：其类型正确但包含的值不合适
# # ZeroDivisionError 在除法或求模运算的第二个参数为零时引发
#
# # 8.2.2 自定义的异常类
# class SomeCustomException(Exception): pass
# raise  SomeCustomException
# # 就像创建其他类一样，但务必直接或间接地继承Exception（这意味着从任何内置异常类派生都可以）。
#
# # 8.3 捕获异常：try/except语句
# try:
#     x = int(input('Enter the first number: '))
#     y = int(input('Enter the second number: '))
#     print(x / y)
# except ZeroDivisionError:
#     print('第二个数请输入非0实数.')
#
# # 8.3.1 不用提供参数
# # 捕获异常后，如果要重新引发它（即继续向上传播），可调用raise且不提供任何参数。
# class MuffledCalculator:
#     muffled = False
#     def calc(self, expr):
#         try:
#             return eval(expr)
#         except ZeroDivisionError:
#             if self.muffled:
#                 print('Division by zero is illegal')
#             else:
#                 raise
#                 # raise ValueError  # 有时你可能想引发别的异常,可直接添加
#                 # raise ValueError from None  # raise ... from ...：来提供自己的异常上下文，也可用None来禁用上下文
# calculator = MuffledCalculator()
# calculator.calc('10 / 0') # 关闭了抑制功能
# calculator.muffled = True  # 开启了抑制功能
# calculator.calc('10 / 0')
# # 如果无法处理异常，在except子句中使用不带参数的raise通常是不错的选择，但有时你可能想引发别的异常。
#
# # 8.3.3 异常可能有多个，可以使用多个except子句；也可以使用元组将多个异常放在一起；
# # 也可以直接使用except不接异常，会将所有异常捕获，但可能会隐藏你没考虑到的异常，一般不建议。
# try:
#     x = int(input('Enter the first number: '))
#     y = int(input('Enter the second number: '))
#     print(x / y)
# except (ZeroDivisionError, TypeError, NameError):
#     print('Your numbers were bogus ...')
# # 异常捕获后，可以返回异常提示而不用自己输入提示：as 。
# try:
#     x = int(input('Enter the first number: '))
#     y = int(input('Enter the second number: '))
#     print(x / y)
# except (ZeroDivisionError, TypeError) as e:
#     print(e)
#
# # 8.3.6 在没有出现异常时执行一个代码块很有用，像条件语句和循环一样，给try/except语句添加else子句。
# try:
#     print('A simple task')
# except:
#     print('What? Something went wrong?')
# else:
#     print('Ah ... It went as planned.')
# # try/except/else语句，没有异常跳到else语句并执行。
#
# # 8.3.7
# # finally：用于在发生异常时执行清理工作，这个子句是与try子句配套的。
# # finally子句非常适合用于确保文件或网络套接字等得以关闭。
# try:
#     1 / 0
# except NameError:
#     print("Unknown variable")
# else:
#     print("That went well!")
# finally:
#     print("Cleaning up.")
#
# # 8.5 异常之禅
# def describe_person(person):
#     print('Description of', person['name'])
#     print('Age:', person['age'])
#     if 'occupation' in person:
#         print('Occupation:', person['occupation'])
# a = {'name': 'Throatwobbler Mangrove', 'age': '42', 'occupation': 'camper'}
# b = describe_person(a)
# # 2次查找，效率低
# def describe_person(person):
#     print('Description of', person['name'])
#     print('Age:', person['age'])
#     try:
#         print('Occupation:', person['occupation'])
#     except KeyError: pass
# a = {'name': 'Throatwobbler Mangrove', 'age': '42', 'occupation': 'camper'}
# b = describe_person(a)
# # 检查对象是否包含特定的属性时，try/except也很有用,并且效率高.
# try:
#     obj.write
# except AttributeError:
#     print('The object is not writeable')
# else:
#     print('The object is writeable')
# # 该解决方案可替代7.2.9节介绍的使用getattr的解决方案，而且更自然。
#
# # 8.6 不那么异常的情况
# from warnings import warn
# # warn("I've got a bad feeling about this.")
# # warn:如果你只想发出警告，指出情况偏离了正轨,警告只显示一次。如果再次运行最后一行代码，什么事情都不会发生.
#
# from warnings import filterwarnings
# filterwarnings('ignore')  # filterwarnings：忽略异常
# warn("Anyone out there?")  # 此时警告不起作用。
# filterwarnings("error")   # filterwarnings：异常
# warn("Something is very wrong!")  # 此时发出警告
# # filterwarnings：来抑制你发出的警告（或特定类型的警告）类似于开关，并指定采取的措施，如"error"或"ignore"
# # warnings.filterwarnings(action,category=Warning, ...):用于过滤警告；前面的warnings是引用类。
# import warnings
# a, b = 1, 23
# class Twarnings(Warning):
#     pass
# try:
#     assert a == 2
# except Exception as e:
#     warnings.warn('wrong!', Twarnings)
# # warnings.warn(message, category=None):用于发出警告;前面的warnings是引用类。


# # 例题
# try:
#     x = int(input("输入第一个值:"))
#     y = int(input("输入第二个值:"))
#     print(x / y)
# except ZeroDivisionError:
#     print("第二个值不能是0.")
#
# class MuffledCalculator:
#     muffed = True  # 打开了抑制功能
#     def calc(self, expr):
#         try:
#             return eval(expr)
#         except ZeroDivisionError:
#             if self.muffed:
#                 print("按零划分是非法的")
#             else:
#                 raise
# calculator = MuffledCalculator()
# print(calculator.calc('10 / 2'))
# calculator.calc('10 / 0')
#
# try:
#     1/0
# except ZeroDivisionError:
#     raise ValueError from None
#
# try:
#     x = int(input("输入第一个值:"))
#     y = int(input("输入第二个值:"))
#     print(x / y)
# except ZeroDivisionError:
#     print("第二个值不能是0.")
# except ValueError:
#     print("That wasn't a number, was it?")
#
# try:
#     x = int(input("输入第一个值:"))
#     y = int(input("输入第二个值:"))
#     print(x / y)
# except (ZeroDivisionError, ValueError):
#     print("第二个值必须是非0整数.")
#
# try:
#     x = int(input("输入第一个值:"))
#     y = int(input("输入第二个值:"))
#     print(x / y)
# except (ZeroDivisionError, ValueError) as e:
#     print(e)
#
# try:
#     x = int(input("输入第一个值:"))
#     y = int(input("输入第二个值:"))
#     print(x / y)
# except :
#     print("第二个值必须是非0整数.")
#
# try:
#     print('A simple task')
# except:
#     print('What? Something went wrong?')
# else:
#     print('AH...It went as planned.')
#
# while True:
#     try:
#         x = int(input('Enter the first number: '))
#         y = int(input('Enter the second number: '))
#         value = x / y
#         print('{} = x / y '.format(value))
#     except:
#         print('Invalid input. Please try again.')
#     else:
#         break
#
# while True:
#     try:
#         x = int(input('Enter the first number: '))
#         y = int(input('Enter the second number: '))
#         value = x / y
#         print('{} = x / y '.format(value))
#     except Exception as e:
#         print('Invalid input:', e)
#         print('Please try again')
#     else:
#         break
#
# x = None
# try:
#     x = 1 / 0
# finally:
#     print('Cleaning up ...')
#     del x
#
# try:
#     1 / 0
# except ZeroDivisionError:
#     print('Unknown variable')
# else:
#     print('that went well!')
# finally:
#     print('Cleaning up.')
#
# def faulty():
#     raise Exception('something is wrong')
# def ignore_exception():
#     faulty()
# def handle_exception():
#     try:
#         faulty()
#     except:
#         print('Excepting handled')
# # print(ignore_exception())
# handle_exception()
#
# def describe_person(person):
#     print('Description of', person['name'])
#     print('Age:', person['age'])
#     if 'occupation' in person:
#         print('Occupation:', person['occupation'])
# describe_person({'name': 'Throatwobbler Mangrove', 'age': '42'})
# describe_person({'name': 'Throatwobbler Mangrove', 'age': '42', 'occupation': 'camper'})
# def describe_person(person):
#     print('Description of', person['name'])
#     print('Age:', person['age'])
#     try:
#         print('Occupation:', person['occupation'])
#     except KeyError as e:
#         print(e)
# describe_person({'name': 'Throatwobbler Mangrove', 'age': '42'})
# describe_person({'name': 'Throatwobbler Mangrove', 'age': '42', 'occupation': 'camper'})
#
# from warnings import warn
# warn("I've got a bad feeling about this.")
# from warnings import filterwarnings
# # filterwarnings("ignore")
# # warn('Anyone out there?')
# # filterwarnings('error')
# # warn('Something is very wrong!')
#
# filterwarnings("error")
# warn("This function is really old...", DeprecationWarning)
# filterwarnings("ignore", category=DeprecationWarning)
# warn("Another deprecation warning.", DeprecationWarning)
# warn("Something else.")
# # warnings.filterwarnings(action,category=Warning, ...) 用于过滤警告
# # warnings.warn(message, category=None) 用于发出警告