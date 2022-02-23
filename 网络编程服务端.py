# # 知识
# # 14.1.1 模块 socket，基本含义
# # 网络编程中的一个基本组件是套接字（socket）;套接字分为两类：服务器套接字和客户端套接字。
# # 套接字是模块socket中socket类的实例。实例化套接字时最多可指定三个参数：
# # 1、一个地址族（默认为socket.AF_INET）；
# # 2、是流套接字（socket.SOCK_STREAM，默认设置）还是数据报套接字（socket.SOCK_DGRAM）；
# # 3、协议（使用默认值0就好）,创建普通套接字时，不用提供任何参数。
# # 套接字，传输数据：send，发送数据；
# # recv（表示receive）：接收数据，最多接收多少个字节的数据，1024是个不错的选择。
# # 服务器套接字先调用bind，再调用listen监听特定的地址。可使用socket.gethostname获取当前机器的主机名。
# # 客户端套接字连接服务器，调用connect并提供调用方法bind时指定的地址.
# # 地址为(host, port)的元组，host是主机名（如www.example.com），port是端口号。
# # 调用accept方法来接受客户端连接，将阻断（等待）到客户端连接到来为止，
# # 然后返回一个格式为(client, address)的元组，client是一个客户端套接字，而address是前面解释过的地址。
#
# # 代码清单14-1 最简单的服务器
# import socket
# s = socket.socket()
#
# host = socket.gethostname()
# port = 1234
# s.bind(host, port)
#
# s.listen(5)
# while True:
#     c, addr = s.accept()
#     print('Got connection from', addr)
#     c.send('Thank you for connecting')
#     c.close()

# import socket
#
# #创建套接字
# s = socket.socket()
#
# #获取主机名
# host = socket.gethostname()
# #端口号
# port = 1234
# address = (host, port)
# #创建连接
# s.bind(address)
#
# #监听:最大连接数为5
# s.listen(5)
# while True:
#     #等待连接
#     client, addr = s.accept()
#     #接收消息
#     str = bytes.decode(client.reve(1024))
#     #发送消息
#     client.send(str.encode('我是服务端!','utf-8'))

# # 代码清单14-2 最简单的客户端
# import socket
# s = socket.socket()
#
# host = socket.gethostname()
# port = 1234
#
# s.connect((host, port))
# print(s.recv(1024))

# import socket
# s = socket.socket()
#
# #连接服务端地址
# host = socket.gethostname()
# port = 8080
# address = (host, port)
# #连接
# s.connect(address)
# #接收消息
# str = bytes.decode(s.reve(1024))
# #发送消息
# s.sent(str.encode('我是客户端！','utf-8'))

# # 14.1.2 模块 urllib 和 urllib2,能够通过网络访问文件，进行下载、数据提取等操作。
# # 如果实现HTTP身份验证或Cookie，抑或编写扩展来处理自己的协议，urllib2可能是更好的选择。
# # 1. 打开远程文件，只能使用读取模式，以及使用模块urllib.request中的函数urlopen，而不是open（或file）。
# from urllib.request import urlopen
# # urlopen返回的类似于文件的对象，方法close、read、readline和readlines，还支持迭代等。
# webpage = urlopen('http://www.python.org')
# # 访问网页；如果没网，可使用file，访问本地file:c:\text\somefile.txt
# import re
# text = webpage.read()
# m = re.search(b'<a href="([^"]+)" .*?>about</a>', text, re.IGNORECASE)
# print(m.group(1) )
# # 还可使用正则表达式，进行数据提取等操作。
#
# # 2. 获取远程文件，urlretrieve下载到本地，返回(filename, headers)元组；
# # filename：本地文件的名称，headers：有关远程文件的信息。
# # urlretrieve(url, filename=None, reporthook=None, data=None):
# # finename:指定了保存本地路径（如果参数未指定，urllib会生成一个临时文件保存数据。）
# # reporthook:是一个回调函数，当连接上服务器、以及相应的数据块传输完毕时会触发该回调，我们可以利用这个回调函数来显示当前的下载进度。
# # data:指post到服务器的数据，返回一个(filename, headers)元组，filename:保存到本地的路径，header:服务器的响应头.
# # import urllib
# # urllib.urlretrieve('http://www.python.org', 'C:\\python_webpage.html')
#
# # 其他实用的函数
# # quote(string[, safe])：返回一个字符串，其中所有的特殊字符（在URL中有特殊意义的字符）
# # 都已替换为对URL友好的版本（如将~替换为%7E）。如果要将包含特殊字符的字符串用作URL，这很有用。
# # 参数safe是一个字符串（默认为'/'），包含不应像这样对其进行编码的字符.
# # quote_plus(string[, safe])：类似于quote，但也将空格替换为加号。
# # unquote(string)：与quote相反。
# # unquote_plus(string)：与quote_plus相反。
# # urlencode(query[, doseq])：将映射（如字典）或由包含两个元素的元组（形如(key, value)）
# # 组成的序列转换为“使用URL编码的”字符串。
#
# # 14.2 SocketServer 及相关的类，模块SocketServer是标准库提供的服务器框架的基石。
# # SocketServer包含4个基本的服务器：TCPServer（支持TCP套接字流）这个最重要、
# # UDPServer（支持UDP数据报套接字）、UnixStreamServer、UnixDatagramServer，这3个可能用不到。
# # 基本请求处理程序类BaseRequestHandler将所有操作都放在一个方法中——服务器调用的方法handle。
# # handle：使用属性self.request来访问客户端套接字；处理的是流(使用TCPServer时很可能如此)，
# # 可使用StreamRequestHandler类；还有其他属性self.rfile（用于读取）和self.wfile（用于写入）。

# # 代码清单14-3 基于SocketServer的极简服务器
# from socketserver import TCPServer, StreamRequestHandler
#
# class Handler(StreamRequestHandler):  # StreamRequestHandler:负责在使用完连接后将其关闭
#     def handle(self):
#         addr = self.request.getpeername()  # getpeername():获取与某个套接字关联的外地协议地址
#         print('Got connection from', addr)
#         self.wfile.write('Thank you for connecting')
# server = TCPServer(('', 1234), Handler)
# server.serve_forever()

# # 14.3 多个连接,处理多个连接的主要方式有三种:分叉（forking）、线程化和异步I/O.
# # 分叉：对进程（运行的程序）进行分叉时，基本上是复制它，而这样得到的两个进程都将从当前位置开始继续
# # 往下执行，且每个进程都有自己的内存副本（变量等）。原来的进程为父进程，复制的进程为子进程。
# # 在分叉服务器中，对于每个客户端连接，都将通过分叉创建一个子进程。父进程继续监听新连接，
# # 而子进程负责处理客户端请求。客户端请求结束后，子进程直接退出。
# # 分叉占用的资源较多，且在客户端很多时可伸缩性不佳。
# # 线程是轻量级进程（子进程），都位于同一个进程中并共享内存。线程化可能带来同步问题（数据混乱，相互干扰）。

# # 代码清单14-4 分叉服务器
# from socketserver import TCPServer, ForkingMixIn, StreamRequestHandler
#
# class Server(ForkingMixIn, TCPServer):
#     pass
#
# class Handler(StreamRequestHandler):
#     def handle(self):
#         addr = self.request.getpeername()
#         print('Got connection from', addr)
#         self.wfile.write('Thank you for connecting')
#
# server = Server(('', 1234), Handler)
# server.serve_forever()

# # 代码清单14-5 线程化服务器
# from socketserver import TCPServer, ThreadingMixIn, StreamRequestHandler
#
# class Server(ThreadingMixIn, TCPServer):
#     pass
#
# class Handler(StreamRequestHandler):
#     def hancle(self):
#         addr = self.request.getpeername()
#         print('Got connection from', addr)
#         self.wfile.write('Thank you for connecting')
# server = Server(('', 1234), Handler)
# server.serve_forever()

# # 14.3.2 使用 select 和 poll 实现异步 I/O
# # 分叉和线程化：一个进程（线程）等待数据时，其他进程（线程）可继续处理其客户端。
# # I/O异步：只处理当前正在通信的客户端。你甚至无需不断监听，只需监听后将客户端加入队列即可。
# # 基石是函数select/poll（UNIX系统），这两个函数都位于模块select中，其中poll的可伸缩性更高。
# # select:前三个参数为序列(输入、输出、发生异常（错误等）的连接，而第四个参数为超时时间（单位为秒）。
# # 这些序列也可包含文件对象（Windows不支持）或套接字。
# #
# # 代码清单14-6 使用select的简单服务器
# import socket, select
#
# s = socket.socket()
#
# host = socket.gethostname()
# port = 1234
# s.bind((host, port))
# s.listen(5)
# inputs = [5]
# while True:
#     # 方法select返回三个参数，通过序列解包赋值
#     rs, ws, es = select.select(inputs, [], [])
#     for r in rs:
#         if r is s:
#             c, addr = s.accept()
#             print('Got connection from', addr)
#             inputs.append(c)
#     else:
#         try:
#             data = r.recv(1024)
#             disconnected = not data
#         except socket.error:
#             disconnected = True
#         if disconnected:
#             # 1.getpeername()：用于获取与某个套接字关联的外地协议地址
#             # 2.getsockname()：用于获取与某个套接字关联的本地协议地址
#             print(r.getpeername(), 'disconnected')
#             inputs.remove(r)
#         else:
#             print(data)

# # 代码清单14-7 使用poll的简单服务器
# import socket, select
#
# s = socket.socket()
#
# host = socket.gethostname()
# port = 1234
# s.bind((host, port))
#
# fdmap = {s.fileno(): s}
#
# s.listen(5)
# p = select.poll()
# p.register(s)
# while True:
#     events = p.poll()
#     for fd, event in events:
#         if fd in fdmap:
#             c, addr = s.accept()
#             print('Got connection from', addr)
#             p.register(c)
#             fdmap[c.fileno()] = c
#         elif event & select.POllIN:
#             data = fdmap[fd].recv(1024)
#             if not data:  # 没有数据 --连接已关闭
#                 print(fdmap[fd].getpeername(), 'disconnected')
#                 p.unregister(fd)
#                 del fdmap[fd]
#             else:
#                 print(data)

# # 14.4 Twisted,事件驱动的Python网络框架,Twisted与多个常用的GUI工具包（Tk、GTK、Qt和wxWidgets）配合得天衣无缝
# # 处理程序必须显式地读取数据;客户端发起连接，有数据到来，客户端断开连接（以及众多其他的事件）。
# # 只想创建自定义协议类的实例时，可使用twisted.internet.protocol中的Factory；
# # 编写自定义协议时，将模块twisted.internet.protocol中的Protocol作为超类。
# # 有新连接到来时，将调用事件处理程序connectionMade；连接中断时，将调用connectionLost。
# # 来自客户端的数据是通过处理程序dataReceived接收的。
# # 1、protocol：实例化Factory，并设置其属性protocol（使用哪种协议与客户端通信。）；
# # 2、reactor.listenTCP：监听指定的端口，让工厂通过实例化协议对象来处理连接（调用reactor中的listenTCP）；
# # 3、reacto.run：调用模块reactor中函数run启动这个服务器

# # 代码清单14-8 使用Twisted创建的简单服务器
# from twisted.internet import reactor
# from twisted.internet.protocol import Factory, Protocol
#
# class SimpleLogger(Protocol):
#
#     def connectionMade(self):
#         print('Got connection from', self.transport.client)
#
#     def connectionLost(self, reason):
#         print(self.transport.client, 'disconnected')
#
#     def dataReceived(self, data):
#         print(data)
#
# factory = Factory()
# factory.protocol = SimpleLogger
#
# reactor.listenTCP(1234, factory)
# reactor.run()

# # 代码清单14-9 使用协议LineReceiver改进后的日志服务器
# from twisted.internet import reactor
# from twisted.internet.protocol import Factory
# from twisted.protocols.basic import LineReceiver
#
# class SimpleLogger(LineReceiver):
#
#     def connectionMade(self):
#         print('Got connection from', self.transport.client)
#
#     def connectionLost(self, reason):
#         print(self.transport.client, 'disconnected')
#
#     def lineReceived(self, line):
#         print(line)
#
# factory = Factory()
# factory.protocol = SimpleLogger
# reactor.listenTCP(1234, factory)
# reactor.run()
# # 如果使用telnet连接到这个服务器以便测试它，每行输出可能只有一个字符，是否如此取决于缓冲等因素。
# # twisted.protocols.basic包含几个预定义的协议，LineReceiver,
# # 实现了dataReceived，并在每收到一整行后调用事件处理程序lineReceived。



# 例题
# import socket
# s = socket.socket()
#
# host = socket.gethostname()
# port = 1234
# s.bind((host, port))
#
# s.listen(5)
# while True:
#     c, addr = s.accept()
#     print('Got connection from', addr)
#     c.send('Thank you for connecting')
#     c.close()
#
# from socketserver import TCPServer, StreamRequestHandler
# class Handler(StreamRequestHandler):
#     def handle(self):
#         addr = self.request.getpeername()
#         print('Got connection from', addr)
#         self.wfile.write('Thanks you for connecting')
#
# server = TCPServer(('', 1234), Handler)
# server.servr_forever()
#
# from socketserver import TCPServer, ForkingMixIn, StreamRequestHandler
#
# class Server(ForkingMixIn, TCPServer):
#     pass
#
# class Handler(StreamRequestHandler):
#     def handle(self):
#         addr = self.request.getpeername()
#         print('Got connection from', addr)
#         self.wfile.write('Thanks you for connecting')
#
# server = TCPServer(('', 1234), Handler)
# server.servr_forever()
#
# from socketserver import TCPServer, ThreadingMixIn, StreamRequestHandler
#
# class Server(ThreadingMixIn, TCPServer):
#     pass
#
# class Handler(StreamRequestHandler):
#     def handle(self):
#         addr = self.request.getpeername()
#         print('Got connection from', addr)
#         self.wfile.write('Thanks you for connecting')
#
# server = TCPServer(('', 1234), Handler)
# server.servr_forever()
#
# import socket, select
#
# s = socket.socket()
#
# host = socket.gethostname()
# port = 1234
# s.bind((host, port))
# s.listen(5)
# inputs = [5]
# while True:
#     rs, ws, es = select.select(inputs, [], [])
#     for r in rs:
#         if r is s:
#             c, addr = s.accept()
#             print('Got connection from', addr)
#             inputs.append(c)
#     else:
#         try:
#             data = r.recv(1024)
#             disconnected = not data
#         except socket.error:
#             disconnected = True
#
#         if disconnected:
#             print(r.getpeername(), 'disconnected')
#             inputs.remove(r)
#         else:
#             print(data)
#
# import socket, select
#
# s = socket.socket()
#
# host = socket.gethostname()
# port = 1234
# s.bind((host, port))
#
# fdmap = {s.fileno(): s}
#
# s.listen(5)
# p = select.poll()
# p.register(s)
# while True:
#     events = p.poll()
#     for fd, event in events:
#         if fd in fdmap:
#             c, addr = s.accept()
#             print('Got connection from', addr)
#             p.register(c)
#             fdmap[c.fileno()] = c
#         elif event & select.POllIN:
#             data = fdmap[fd].recv(1024)
#             if not data:  # 没有数据 --连接已关闭
#                 print(fdmap[fd].getpeername(), 'disconnected')
#                 p.unregister(fd)
#                 del fdmap[fd]
#             else:
#                 print(data)


