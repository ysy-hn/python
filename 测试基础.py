# # 知识
# # 测试驱动的编程:测试在先，编码在后.
# # 16.1.1 准确的需求说明,开发软件时，必须先知道软件要解决什么问题——要实现什么样的目标.
# # 要阐明程序的目标，可编写需求说明，也就是描述程序必须满足何种需求的文档（或便条）。
# # 先编写测试再编写代码并不是为了发现bug，而是为了检查代码是否管用。
# # 除非有相应的测试，否则该功能就并不存在，或者说不是真正意义上的功能。
# # 这样你就能名正言顺地证明它确实存在，而且做了它应该做的。
#
# # 代码清单16-1 简单的测试程序,计算矩形面积
# from area import rect_area
# height = 3
# width = 4
# correct_answer = 12
# answer = rect_area(height, width)
# if answer == correct_answer:
#     print('通过')
# else:
#     print('失败')
#
# # 16.1.2 做好应对变化的准备
# # 如果程序设计良好（使用了合适的抽象和封装），修改带来的影响将是局部的，只会影响很小一段代码。
# # 这意味着你能够确定bug的范围，因此调试起来更容易。
# # 优秀测试套件的目标之一是确保较高的覆盖率，为此可使用覆盖率工具，它们测量测试期间实际运行的代码所占的比例。
#
# # 16.1.3 测试四步曲
# # 1、 确定需要实现的新功能。可将其记录下来，再为之编写一个测试。
# # 2、编写实现功能的框架代码，让程序能够运行，但测试依然无法通过。确定测试失败后，再试图让它成功。
# # 3、编写让测试刚好能够通过的代码。
# # 4、改进（重构）代码以全面而准确地实现所需的功能，同时确保测试依然能够成功。
#
# # 16.2 测试工具，有两个杰出的模块可替你自动完成测试过程。
# # unittest：一个通用的测试框架。
# # doctest：一个更简单的模块，是为检查文档而设计的，但也非常适合用来编写单元测试。
#
# # 16.2.1 doctest
# # 交互式会话是一种很有用的文档，可将其放在文档字符串中。
#
# def square(x):
#     '''
#     计算平方并返回结果
#     >>> square(2)  # 注意格式一致包括空格。
#     4              # 注意格式一致包括顶格。
#     >>> square(3)
#     9
#     '''
#     return x * x
#
# if __name__ == '__main__':
#     import doctest, my_math   # my_math：模块名
#     doctest.testmod(my_math)  # testmod：对模块进行测试,检查文档字符串中的示例（还接受很多其他的参数）
# # cmd交互式运行代码，使用该命令可查看具体运行详情，python my_math.py -v
#
# # 16.2.2 unittest，更灵活、更强大；能够以结构化方式编写庞大而详尽的测试集。
# # 先使用模块unittest中的TestCase类编写一个测试。
#
# # 代码清单16-2 一个使用框架unittest的简单测试
# import unittest, my_math
#
# class ProductTestCase(unittest.TestCase):
#
#     def test_integers(self):
#         for x in range(-10,10):
#             for y in range(-10,10):
#                 p = my_math.product(x, y)
#                 self.assertEqual(p, x * y, 'Integer multiplication failed')
# # assertEqual:比较前两个数是否相等，第三个数为测试消息失败时显示的消息的字符串语句。
#     def test_floats(self):
#         for x in range(-10,10):
#             for y in range(-10,10):
#                 x = x / 10
#                 y = y / 10
#                 p = my_math.product(x, y)
#                 self.assertEqual(p, x * y, 'Integer multiplication failed')
#
# if __name__ == '__main__':
#     unittest.main()
# # unittest.main:负责替你运行测试：实例化所有的TestCase子类，并运行所有名称以test打头的方法。
# # 模块unittest区分错误和失败。错误指的是引发了异常，而失败是调用failUnless等方法的结果。
# # 接下来需要编写框架代码，以消除错误——只留下失败。
#
# # 16.3 超越单元测试
# # 源代码检查:一种发现代码中常见错误或问题的方式（有点像静态类型语言中编译器的作用，但做的事情要多得多）。
# # 性能分析:搞清楚程序的运行速度到底有多快。
#
# # 16.3.1 使用 PyChecker 和 PyLint 检查源代码
# # PyChecker（pychecker.sf.net）:能够找出诸如给函数提供的参数不对等错误。
# # PyLint（pylint.org）:支持PyChecker提供的大部分功能,变量名是否符合指定的命名约定、是否遵守了自己的编码标准等.
# # 使用pip安装，可以命令行脚本的方式运行它们，也可将其作为Python模块。
# # 要使用PyChecker来检查文件，可运行这个脚本并将文件名作为参数；pychecker file1.py ...
# # 使用PyLint检查文件时，需要将模块（或包）名作为参数：pylint module
# # 导入pychecker.checker时，它会检查后续代码（包括导入的模块），并将警告打印到标准输出。
#
# # 在Python中，可通过模块subprocess来使用命令行工具。
# # 代码清单16-3 使用模块subprocess调用外部检查器
#
# import unittest, my_math
# from subprocess import PIPE, Popen
#
# class ProductTestCase(unittest.TestCase):
#
#     def test_with_PyChecker(self):
#         cmd = 'pychecker', '-Q', my_math.__file__.rstrip('c')  # 指定了开关-Q（quiet，静默)
#         pychecker = Popen(cmd, stdout=PIPE, stderr=PIPE)
#         self.assertEqual(pychecker.stdout.read(), '')
#
#     def test_with_PyLint(self):
#         cmd = 'pylint', '-rn', 'my_math'  # 指定了开关-rn（n:no）以关闭报告，这意味着将只显示警告和错误
#         pylint = Popen(cmd, stdout=PIPE, stderr=PIPE)
#         self.assertEqual(pylint.stdout.read(), '')
#
# if __name__ == '__main__':
#     unittest.main()  # 运行当前模块中的单元测试
# # 为让pychecker正确地运行，我们需要获取文件名。为此，我使用了模块my_math的属性__file__，
# # 并使用rstrip将文件名末尾可能包含的c删掉（因为模块可能存储在.pyc文件中）。
#
# # 16.3.2 性能分析,如果程序的速度达不到你的要求，必须优化，就必须首先对其进行性能分析。
# # profile:一个卓越的性能分析模块;cProfile:一个速度更快C语言版本;只需调用其方法run并提供一个字符串参数
# import cProfile
# from my_math import product
# cProfile.run('product(1, 2)', 'my_math.text')
# # 输出：各个函数和方法被调用多少次以及执行它们花费了多长时间.
# import pstats
# p = pstats.Stats('my_math.text')
# # 通过使用这个Stats对象，可以编程方式研究分析结果。

# doctest.testmod(module):检查文档字符串中的示例（还接受很多其他的参数）
# unittest.main():运行当前模块中的单元测试
# profile.run(stmt[,filename]):执行语句并对其进行性能分析；可将分析结果保存到参数filename指定的文件中
#
#
#
# # 例题
# # from area import rect_area
# # height = 3
# # width = 4
# # corrent_answer = 12
# # answer = rect_area(height, width)
# # if answer == corrent_answer:
# #     print('Test passed')
# # else:
# #     print("Test failed")
# #
# # def square(x):
# #     return x * x
# #
# # def square(x):
# #     return x ** x
# # if __name__ =='__main__':
# #     import doctest, my_math
# #     doctest.testmod(my_math)
# #
# # import unittest, my_math
# # from subprocess import Popen, PIPE
# #
# # class ProductTestCase(unittest.TestCase):
# #
# #     def test_with_PyChecker(self):
# #         cmd = 'pychecker', '-Q', my_math.__file__.rstrip('c')
# #         pychecker = Popen(cmd, stdout=PIPE, stderr=PIPE)
# #         self.assertEqual(pychecker.stdout.read(), '')
# #
# #     def test_with_PyLint(self):
# #         cmd = 'pylint', '-rn', 'my_math'
# #         pylint = Popen(cmd, stdout=PIPE, stderr=PIPE)
# #         self.assertEqual(pylint.stdout.read(), '')
# #
# # if __name__ == '__main__': unittest.main()
# #
# # import cProfile
# # from my_math import product
# # cProfile.run('product(1,2)')
# #
# # import pstats
# # p = pstats.Stats('my_math.profile')
