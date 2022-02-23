# 知识
# 不像HTML那样是一种特定的语言，XML是一组定义一类语言的规则,还可自定义标签名。
# 22.1 问题描述,要解决的通用问题是解析（读取并处理）XML文件.
# 本章要解决的具体问题是，根据一个XML文件生成完整的网站，而这个文件描述了网站的结构以及每个网页的基本内容。
# 1、整个网站由单个XML文件描述，该文件包含有关各个网页和目录的信息。
# 2、程序应根据需要创建目录和网页；3、应能够轻松地修改整个网站的设计并根据新的设计重新生成所有网页。
# 需要一个管用的SAX解析器。要确定是否已经有这样的SAX解析器.如果出现异常，就必须安装PyXML。
# 主要的概念包括网站、目录、页面、名称、标题和内容。
# 1、你不会存储有关网站本身的任何信息，因此网站只是一个顶级元素，包含所有的文件和目录。
# 2、目录主要用作文件和其他目录的容器；
# 3、页面是单个网页。
# 4、目录和网页都得有名称。这些名称就是目录名和文件名，将出现在文件系统和相应的URL中。
# 5、每个网页都必须有标题（不同于文件名）。
# 6、每个网页都包含一些内容。在这里，我们只使用普通的XHTML来表示内容。这样可直接将内容放在最终的网页中，并让浏览器进行解读。































# 例题
# from xml.sax.handler import ContentHandler
# from xml.sax import parse
#
# class TestHandler(ContentHandler):
#     pass
#
# parse("website.xml", TestHandler())
#
#
# def stratElement(self, name, attrs):
#     print(name, attrs.keys())
#
#
# from xml.sax.handler import ContentHandler
# from xml.sax import parse
#
# class HeadlineHandler(ContentHandler):
#
#     in_headline = False
#
#     def __init__(self, headlines):
#         super().__init__()
#         self.headlines = headlines
#         self.data = []
#
#     def startElement(self, name, attrs):
#         if name == 'h1':
#             self.in_headline = True
#
#     def endElement(self, name):
#         if name == 'h1':
#             text = ''.join(self.data)
#             self.data = []
#             self.headlines.append(text)
#             self.in_headline = False
#
#     def characters(self, string):
#         if self.in_headline:
#             self.data.append(string)
#
# headlines = []
# parse('website.xml', HeadlineHandler(headlines))
#
# print("The following <h1> elements were found:")
# for h in headlines:
#     print(h)
#
#
# class Dispatcher:
#     def startElement(self, name, attrs):
#         self.dispatch('start', name, attrs)
#     def endElement(self, name):
#         self.dispatch('end', name)
#
# def dispatch(self, prefix, name, attrs=None):
#     mname = prefix + name.capitalize()
#     dname = 'default' + prefix.capitalize()
#     method = getattr(self, mname, None)
#     if callable((method)):
#         args = ()
#     else:
#         method = getattr(self, dname, None)
#         args = name,
#     if prefix == 'start':
#         args += attrs,
#         if callable(method):
#             method(*args)
#
#
# class TestHandler(Dispatcher, ChildProcessError):
#     def startPage(self, attrs):
#         print('Beginning page', attrs['name'])
#     def endPage(self):
#         print('Ending page')
#
#
# def writeHeader(self, title):
#     self.out.write("<html>\n <head>\n <title>")
#     self.out.write(title)
#     self.out.write("</title>\n </head>\n <body>\n")
#
# def writeFooter(self):
#     self.out.write("\n </body>\n </html>\n")
#
# def defaultStart(self, name, attrs):
#     if self.passthrough:
#         self.out.write('<' + name)
#         for key, cal in attrs.items():
#             self.out.write(' {}="{}"'.format(key, vars))
#         self.out.write('>')
#
# def defaultEnd(self, name):
#     if self.passthrough:
#         self.out.write('</{}>'.format(name))
#
# import os
# def ensureDirectory(self):
#     path = os.path.join(*self.directory)
#     os.makedirs(path, exist_ok=True)
#
# def __init__(self, directory):
#     self.directory = [directory]
#     self.ensureDirectory()
#
#
# def startDirectory(self, attrs):
#     self.directory.append(attrs['name'])
#     self.ensureDirectory()
#
# def endDirectory(self):
#     self.directory.pop()
#
# def stratPage(self, attrs):
#     filename = os.path.join(*self.directory + [attrs['name'] + '.html'])
#     self.out = open(filename, 'w')
#     self.writeHeader(attrs['title'])
#     self.passthrough = True
#
# def endPage(self):
#     self.passthrough = False
#     self.writeFooter()
#     self.out.close()
#
#
#
