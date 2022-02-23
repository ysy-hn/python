# # 知识
# # 15.1 屏幕抓取，是通过程序下载网页并从中提取信息的过程，下载数据并对其进行分析。
# # 代码清单15-1 简单的屏幕抓取程序
# from urllib.request import urlopen
# import re
# p = re.compile('<a href="(/jobs/\\d+)/">(.*?)</a>')
# text = urlopen('http://python.org/jobs').read().decode()
# for url, name in p.findall(text):
#     print('{} ({})'.format(name, url))
# # 针对基于正则表达式的方法存在的问题：
# # 1、结合使用程序Tidy（一个Python库）和XHTML解析；
# # 2、使用专为屏幕抓取而设计的Beautiful Soup库。
#
# # 15.1.1 Tidy 和 XHTML 解析
# # Tidy是用于对格式不正确且不严谨的HTML进行修复的工具，还提供了极大的配置空间，让你能够开/关各种校正。
# from subprocess import Popen, PIPE
# text = open('messy.html').read()
# tidy = Popen('tidy', stdin=PIPE, stdout=PIPE, stderr=PIPE)
# tidy.stdin.write(text.encode())
# tidy.stdin.close()
# print(tidy.stdout.read().decode())
#
# # decode(encoding='UTF-8',errors='strict'):以指定的编码格式解码字符串。默认编码为字符串编码
# # encode(encoding='UTF-8',errors='strict'):以指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案
str = "this is string example....wow!!!"
str = str.encode('utf-8', 'strict')
print("Encoded String: ", str)
print("Decoded String: " + str.decode('utf-8', 'strict'))
#
# # 代码清单15-2 使用模块HTMLParser的屏幕抓取程序
# from urllib.request import urlopen
# from html.parser import HTMLParser
#
# def isjob(url):
#     try:
#         a, b, c, d = url.split('/')
#     except ValueError:
#         return False
#     return a == d == '' and b == 'jobs' and c.isdigit()
#
# class Scraper(HTMLParser):
#     in_link = False
#     def handle_starttag(self, tag, attrs):
#         attrs = dict(attrs)
#         url = attrs.get('href', '')
#         if tag == 'a' and isjob(url):
#             self.url = url
#             self.in_link = True
#             self.chunks = []
#
#     def handle_data(self, data):
#         if self.in_link:
#             self.chunks.append(data)
#
#     def handle_endtag(self, tag):
#         if tag == 'a' and self.in_link:
#             print('{} ({})'.format(''.join(self.chunks), self.url))
#             self.in_link = False
#
# text = urlopen('http://python.org/jobs').read().decode()
# parser = Scraper()
# parser.feed(text)
# parser.close()
#
# # 15.1.2 Beautiful Soup,一个小巧而出色的模块，用于解析你在Web上可能遇到的不严谨且格式糟糕的HTML。
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# text = urlopen('http://python.org/jobs').read()
# soup = BeautifulSoup(text, 'html.parser')
#
# jobs = set()
# for job in soup.body.section('h2'):  # soup.body来获取文档体，再访问其中的第一个section。返回其中的所有h2元素
#     jobs.add('{} ({})'.format(job.a.string, job.a['href']))
# # 第一个链接job.a。属性string是链接的文本内容，而a['href']为属性href。
# print('\n'.join(sorted(jobs, key=str.lower)))
# # set和sorted（通过将参数key设置为一个函数以忽略大小写）。旨在消除重复的职位并按字母顺序打印它们.
#
# # 15.2 使用CGI创建动态网页,通用网关接口（CGI）
# # CGI是一种标准机制，Web服务器可通过它将查询交给专用程序，并以网页的方式显示查询结果.
# # 要让CGI脚本能够通过Web进行访问（和运行），必须将其放在Web服务器能够访问的地方、添加!#行并设置合适的文件权限。
# # 15.2.1 第一步：准备 Web 服务器: $ python -m http.server --cgi
# # 15.2.2 第二步：添加!#行,将脚本放到正确的位置后，必须在其开头添加一个!#行。
# # 通过添加!#行，无需显式地执行Python解释器就能执行脚本。对CGI脚本来说,没有将不知道如何执行脚本。
# # 一般在开头添加，必须是第一行（之前没有空行）；#!/usr/bin/env python；
# # 如果有问题，先确定Python可执行文件的准确位置，并使用完整的目录，如#!C:\Python36\python.exe。
# # 15.2.3 第三步：设置文件权限，设置合适的文件权限。
# # 一般，CGI脚本不能修改计算机上的任何文件；要显式赋予权限，1、有root权限，2、设置文件权限。
# # UNIX中设置文件权限命令chmod：chmod 755（账号） somescript.cgi（脚本名）
#
# # 使用CGI程序存在一些安全风险。
# # 代码清单15-4 简单的CGI脚本
# #！/usr/bin/env python
# print('Content-type: text/plain')
# print()
# print('Hello, world!')
#
# # 15.2.6 使用 cgitb 进行调试,cgitb（用于CGI栈跟踪):返回有关什么地方出了问题的信息。
# # cgitb.enable() 在CGI脚本中启用栈跟踪
# # 代码清单15-5 显示栈跟踪的CGI脚本（faulty.cgi）
# #!/usr/bin/env python
# import cgitb; cgitb.enable()
# print('Content-type: text/html\n')
# print(1/0)
# print('Hello, world!')
# # 程序开发好后，应关闭这种cgitb功能，因为栈跟踪页面并非供程序的普通用户查看的.
#
# # 15.2.7 使用模块 cgi,在CGI脚本中，可使用模块cgi中的FieldStorage类来获取这些字段。
# # 当你创建FieldStorage实例（应只创建一个）时，它将从请求中取回输入变量（字段），并通过一个类似于字典的接口将它们提供给脚本。
# import cgi
# form = cgi.FieldStorage()
# name = form['name'].value
# # 使用getvalue方法更简单
# form = cgi.FieldStorage()
# name = form.getvalue('name', 'Unknown')
#
# # 代码清单15-6 从FieldStorage中获取单个值的CGI脚本
# #!/usr/bin/env python
# import cgi
# form = cgi.FieldStorage()
# name = form.getvalue('name', 'world')
#
# print('Content-type: text/plain\n')
# print('Hello, {}!'.format(name))
#
# # 代码清单15-7 包含HTML表单的问候脚本
# #!/usr/bin/env python
#
# import cgi
# form = cgi.FieldStorage()
#
# name = form.getvalue('name', 'world')
#
# print("""Content-type: text/html
#
# <html>
#   <head>
#     <title>Greeting Page</title>
#   </head>
#   <body>
#     <h1>Hello, %s!</h1>
#
#
#     <form action='simple3.cgi'>
#     Change name <input type='text' name='name' />
#     <input type='submit' />
#     </form>
#   </body>
# </html>
# """.format(name))
#
#
#
# # 例题
# # from urllib.request import urlopen
# # import re
# # p = re.compile('<a href="(/jobs/\\d+)/">(.*?)</a>')
# # text = urlopen('http://python.org/jobs').read().decode()
# # for url, name in p.findall(text):
# #     print('{} ({})'.format(name, url))
# #
# # from urllib.request import urlopen
# # from html.parser import HTMLParser
# #
# # def isjob(url):
# #     try:
# #         a, b, c, d = url.split('/')
# #     except ValueError:
# #         return False
# #     return a == d == '' and b == 'jobs' and c.isdigit()
# #
# # class Scraper(HTMLParser):
# #     in_link = False
# #     def handle_starttag(self, tag, attrs):
# #         attrs = dict(attrs)
# #         url = attrs.get('href', '')
# #         if tag == 'a' and isjob(url):
# #             self.url = url
# #             self.in_link = True
# #             self.chunks = []
# #
# #     def handle_data(self, data):
# #         if self.in_link:
# #             self.chunks.append(data)
# #
# #     def handle_endtag(self, tag):
# #         if tag == 'a' and self.in_link:
# #             print('{} ({})'.format(''.join(self.chunks), self.url))
# #             self.in_link = False
# #
# # text = urlopen('http://python.org/jobs').read().decode()
# # parser = Scraper()
# # parser.feed(text)
# # parser.close()
# #
# # from urllib.request import urlopen
# # from bs4 import BeautifulSoup
# #
# # text = urlopen('http://python.org/jobs').read()
# # soup = BeautifulSoup(text, 'html.parser')
# #
# # jobs = set()
# # for job in soup.body.section('h2'):
# #     jobs.add('{} ({})'.format(job.a.string, job.a['href']))
# #
# # print('\n'.join(sorted(jobs, key=str.lower)))
# #
# # #!/usr/bin/env python
# #
# # print('Content-type: text/plain')
# # print()  # Prints an empty line, to end the headers
# #
# # print('Hello, world!')
# #
# #
# # #!/usr/bin/env python
# #
# # import cgitb; cgitb.enable()
# #
# # print('Content-type: text/html\n')
# #
# # print(1/0)
# #
# # print('Hello, world!')
# #
# #
# # #!/usr/bin/env python
# #
# # import cgi
# # form = cgi.FieldStorage()
# #
# # name = form.getvalue('name', 'world')
# #
# # print('Content-type: text/plain\n')
# #
# # print('Hello, {}!'.format(name))
# #
# # #!/usr/bin/env python
# #
# # import cgi
# # form = cgi.FieldStorage()
# #
# # name = form.getvalue('name', 'world')
# #
# # print("""Content-type: text/html
# #
# # <html>
# #   <head>
# #     <title>Greeting Page</title>
# #   </head>
# #   <body>
# #     <h1>Hello, %s!</h1>
# #
# #
# #     <form action='simple3.cgi'>
# #     Change name <input type='text' name='name' />
# #     <input type='submit' />
# #     </form>
# #   </body>
# # </html>
# # """.format(name))
#
#
