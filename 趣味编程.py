# # 知识
# # 1、原型设计：Python的优点之一是让你能够快速地编写程序；要更深入地了解面临的问题，编写原型程序是一种很好的办法。
# # 2、配置：灵活性形式多样；配置旨在让程序的某些方面修改起来更容易——对你和用户来说都如此。
# # 3、自动化测试：要能够轻松地修改程序，这绝对必不可少。
#
# # 19.3 原型设计，原型（prototype）指的是尝试性实现，即一个模型。
# # 对程序的结构（如需要哪些类和函数）有一定的想法后，建议你实现一个功能可能极其有限的简单版本。
# # 然后添加新功能，修改不喜欢的方面，等等。
# # 第一个实现是摸着石头过河：拼凑出一个能够解决问题（或部分问题）的程序，以便了解需要的组件以及对优秀解决方案的要求。
# # 在这个过程中，最重要的可能就是看到程序的各种缺陷。基于这些新的认识，再次尝试解决面临的问题，而此时我的判断力和洞察力可能更强。
# # 务必对推倒重来持谨慎态度，尽量对原型进行重构和修改。
#
# # 19.4 配置
# # 第6章和第7章介绍了如何提高代码的抽象程度，这是通过将代码放在函数和方法中并将较大的结构隐藏在类中实现的。
# # 更简单的一种提高程序抽象程度的方式：提取代码中的符号常量。
# # 常量，指的是内置的字面量值，如数、字符串和列表。可将其存储在全局变量中，而不在程序中反复输入它们。
# # 容易修改的值不要设为全局变量，容易出错。
# # 要指出变量被视为符号常量，可遵循一种特殊的命名约定：只在变量名中使用大写字母并用下划线分隔单词。
# # 请牢记下面一点：每当你需要输入常量（如数字42或字符串Hello, world!）多次时，都应考虑将其存储在全局变量中。
#
# # 19.4.2 配置文件
# # 1、将有关用户容易接触的配置变量放在独立的文件中，而不将它们放在模块开头。然后将配置放在特定的配置文件中。
# # 2、使用标准库模块configparser，从而可在配置文件中使用标准格式。
# greeting = 'Hello, world!'
# greeting: 'Hello, World!'
# # 必须使用[files]、[colors]等标题将配置文件分成几部分
#
# # 代码清单19-1 一个简单的配置文件
# # [numbers]
# # pi: 3.1415926535897931
# # [messages]
# # greeting: Welcome to the area calculation program!
# # question: Please enter the radius:
# # result_message: The area is
#
# # 代码清单19-2 一个使用ConfigParser的程序
# from configparser import ConfigParser
# CONFIGFILE = "config.cfg"
#
# config = ConfigParser()
# # 读取配置文件：
# config.read(CONFIGFILE)
#
# # 打印默认问候语（greeting）：
# # 在messages部分查找问候语：
# print(config['messages'].get('greeting'))
#
# # 使用配置文件中的提示（question）让用户输入半径：
# radius = float(input(config['messages'].get('question') + ' '))
#
# # 打印配置文件中的结果消息（result_message）；
# # 以空格结束以便接着在当前行打印：
# print(config['messages'].get('result_message'), end=' ')
#
# # getfloat()将获取的值转换为浮点数：
# print(config['numbers'].getfloat('pi') * radius**2)
# # 考虑让程序是可配置的,用户就可根据自己的偏好修改程序，可能让他们使用程序时的心情更为愉悦.
#
# # 19.5 日志,大致上就是收集与程序运行相关的数据，供你事后进行研究或积累。
# # print语句是一种简单的日志形式.
# import urllib
# log = open('logfile.txt', 'w')
# print('Downloading file from URL', url, file=log)
# text = urllib.urlopen(url).read()
# print('File successfully downloaded', file=log)
# # 如果程序在下载期间崩溃，这种方法的效果就不会很好。
# # 更安全的做法是，在每条日志语句前后都打开和关闭文件（至少应该在写入后刷新文件）。
# # 即便程序崩溃，也将看到日志文件的最后一行为“Downloading file from URL”，从而知道下载失败了。
#
# # 正确的做法是使用标准库中的模块logging。
# # 代码清单19-3 一个使用模块logging的程序
# import logging
#
# logging.basicConfig(level=logging.INFO, filename='mylog.log')
# logging.info('开始项目')
# logging.info('尝试将1除以0')
# print(1 / 1)
# logging.info('该功能成功了')
# logging.info('项目最后')
# #
