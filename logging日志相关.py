# logging.info(): 输出日志
# logging.debug(): 输出更详细的日志
# warnings.warn()/logging.warning(): 发出有关特定事件的警告
# logging.error()/logging.exception()/logging.critical(): 在不引发异常的情况下报告错误
# 级别	        级别数值	      使用时机
# DEBUG	        10	      详细信息，常用于调试。
# INFO	        20	      程序正常运行过程中产生的一些信息。
# WARNING      	30	      警告用户，虽然程序还在正常工作，但有可能发生错误。
# ERROR	        40	      由于更严重的问题，程序已不能执行一些功能了。
# CRITICAL	    50	      严重错误，程序已不能继续运行。
# 默认级别是WARNING

# # 简单范例
# import logging
# logging.warning('你好')  # 默认级别，会打印
# logging.info('你好')  # 级别低，不打印

# # 记录到文件内，使用basicConfig
# import logging
# logging.basicConfig(filename='日志.log', level=logging.DEBUG)
# logging.debug('详细信息，级别最低')
# logging.info('信息，级别倒数第2')
# logging.warning('警告，级别高')
# level=参数，设定了日志记录的门槛。
# logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
# # 通过写入操作，使之前的日志被删除

# 可以通过下面的方法来获取用户输入的日志级别参数：
# numeric_level = getattr(logging, loglevel.upper(), None)
# if not isinstance(numeric_level, int):
#     raise ValueError('Invalid log level: %s' % loglevel)
# logging.basicConfig(level=numeric_level, ...)

# # 通过百分符%方式的格式化控制，生成消息字符串，类同于字符串数据类型的格式化输出，但也有不同之处。
# import logging
# logging.warning('%s before you %s', 'Look', 'leap!')

# # 1.6 消息格式
# # 要控制消息格式，获得更多的花样，可以提供format参数：
# import logging
# logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
# logging.debug('This message should appear on the console')
# logging.info('So should this')
# logging.warning('And this, too')
# # 对于%(levelname)s这种东西，是logging模块内置的，可以被输出到日志中的对象。

# # 1.7 附加时间信息
# # 要在日志内容中附加时间信息，可以在format字符串中添加%(asctime)s。
# import logging
# logging.basicConfig(format='%(asctime)s %(message)s')
# logging.warning('打印时间')
#
# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# logging.warning('打印其它格式时间')

# logging模块采用了模块化设计，主要包含四种组件：
# 1、Loggers：记录器，提供应用程序代码能直接使用的接口；
# 2、Handlers：处理器，将记录器产生的日志发送至目的地；
# 3、Filters：过滤器，提供更好的粒度控制，决定哪些日志会被输出；
# 4、Formatters：格式化器，设置日志内容的组成结构和消息字段

import logging
# 一、Loggers记录器:
# 获取一个Logger类的实例: logger = logging.getLogger(__name__)
# 在使用debug()，info()，warn()，error()，critical()等方法之前必须先创建一个Logger的实例，
# 即创建一个记录器，如果没有显式的进行创建，则默认创建一个root logger，并应用默认的日志级别(WARN)，
# logger对象有三重功能。首先，提供应用程序调用的接口；其次，决定日志记录的级别；最后，将日志内容传递到相关联的handlers中。
# 总结logger对象的用法，可以分成两类：配置和消息发送。
# 下面是最常用的配置方法：
# Logger.setLevel()：设置日志记录级别
# Logger.addHandler()和Logger.removeHandler()：为logger对象添加或删除handler处理器对象。
# Logger.addFilter()和Logger.removeFilter()：为为logger对象添加或删除filter过滤器对象。
# 配置好logger对象后，就可以使用下面的方法创建日志消息了：
# Logger.debug(), Logger.info(), Logger.warning(), Logger.error(), and Logger.critical()：创建对应级别的日志，但不一定会被记录。
# Logger.exception()：创建一个类似Logger.error()的日志消息。不同的是Logger.exception()保存有一个追踪栈。该方法只能在异常handler中调用。
# Logger.log()：显式的创建一条日志，是前面几种方法的通用方法。
# 注意，getLogger()方法返回一个logger对象的引用，并以你提供的name参数命名，如果未提供名字，那么默认为‘root’。使用同样的name参数，多次调用getLogger()，将返回同样的logger对象。

# 二、Handlers处理器
# logging模块使用较多的handlers有两个，StreamHandler和FileHandler。
# 1、StreamHandler:标准输出stdout（如显示器）分发器。
# 创建方法: sh = logging.StreamHandler(stream=None)
# 2、FileHandler:将日志保存到磁盘文件的处理器。
# 创建方法: fh = logging.FileHandler(filename, mode='a', encoding=None, delay=False)
# setLevel()：和logger对象的一样，设置日志记录级别。handlers的日志级别只对自己接收到的logger传来的日志有效，进行了更深一层的过滤。
# setFormatter()：设置当前handler对象使用的消息格式。
# addFilter() 和 removeFilter()：配置或删除一个filter过滤对象

# 三、Formatter对象用来最终设置日志信息的顺序、结构和内容。
# ft = logging.Formatter.__init__(fmt=None, datefmt=None, style=’%’)
# 如果不指定datefmt，那么它默认是%Y-%m-%d %H:%M:%S样式的。
# style参数默认为百分符%，这表示前面的fmt参数应该是一个%(<dictionary key>)s格式的字符串，而可以使用的logging内置的keys，如下表所示：
# 属性	            格式	        描述
# asctime	    %(asctime)s 	日志产生的时间，默认格式为2003-07-08 16:49:45,896
# created	    %(created)f	    time.time()生成的日志创建时间戳
# filename	    %(filename)s	生成日志的程序名
# funcName	    %(funcName)s	调用日志的函数名
# levelname	    %(levelname)s	日志级别 ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
# levelno	    %(levelno)s	    日志级别对应的数值
# lineno	    %(lineno)d	    日志所针对的代码行号（如果可用的话）
# module	    %(module)s	    生成日志的模块名
# msecs	        %(msecs)d	    日志生成时间的毫秒部分
# message	    %(message)s	    具体的日志信息
# name	        %(name)s	    日志调用者
# pathname	    %(pathname)s	生成日志的文件的完整路径
# process	    %(process)d 	生成日志的进程ID（如果可用）
# processName	%(processName)s	进程名（如果可用）
# thread	    %(thread)d	    生成日志的线程ID（如果可用）
# threadName	%(threadName)s	线程名（如果可用）

# 四、Filter过滤器
# Handlers和Loggers可以使用Filters来完成比日志级别更复杂的过滤。
# 比如我们定义了filter = logging.Filter('a.b.c')，并将这个Filter添加到了一个Handler上，
# 则使用该Handler的Logger中只有名字带a.b.c前缀的Logger才能输出其日志。
# 创建方法: filter = logging.Filter(name='')
# 例如：
# filter = logging.Filter('mylogger.child1.child2')
# fh.addFilter(filter)

# 配置日志模块
# 有三种配置logging的方法：
# 1、创建loggers、handlers和formatters，然后使用Python的代码调用上面介绍过的配置函数。
# 2、创建一个logging配置文件，然后使用fileConfig()方法读取它。
# 3、创建一个配置信息字典然后将它传递给dictConfig()方法。

# # 第一种
# import logging
# # 创建logger记录器
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)
# 创建一个控制台处理器，并将日志级别设置为debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# 创建formatter格式化器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 将formatter添加到ch处理器
ch.setFormatter(formatter)
# 将ch添加到logger
logger.addHandler(ch)
# 然后就可以开始使用了！
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

# # 第二种
# import logging
# import logging.config
#
# logging.config.fileConfig('logging.conf') # 读取config文件
#
# # 创建logger记录器
# logger = logging.getLogger('simpleExample')
#
# # 使用日志功能
# logger.debug('debug message')
# logger.info('info message')
# logger.warn('warn message')
# logger.error('error message')
# logger.critical('critical message')

# # 第三种，推荐掌握
# import logging
# import logging.config
# import yaml
# # 通过yaml文件配置logging
# f = open("logging.conf.yaml")
# dic = yaml.load(f)
# f.close()
# logging.config.dictConfig(dic)
# # 创建logger
# logger = logging.getLogger('simpleExample')
# logger.debug('debug message')
# logger.info('info message')
# logger.warn('warn message')
# logger.error('error message')
# logger.critical('critical message')

