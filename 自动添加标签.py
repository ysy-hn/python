# 知识
# 20.1 问题描述，给纯文本文件添加格式。
# 定义一些目标：1、输入无需包含人工编码或标签；
# 2、程序需要能够处理不同的文本块（如标题、段落和列表项）以及内嵌文本（如突出的文本和URL）。
# 3、虽然这个实现添加的是HTML标签，但应该很容易对其进行扩展，以支持其他标记语言。

# 20.2 有用的工具
# 1、肯定需要读写文件（参见第11章），至少要从标准输入（sys.stdin）读取以及使用print进行输出。
# 2、可能需要迭代输入行（参见第11章）
# 3、需要使用一些字符串方法（参见第3章）。
# 4、可能用到一两个生成器（参见第9章）。
# 5、可能需要模块re（参见第10章）。

# 20.4 初次实现，首先要做的事情之一是将文本分成段落。比段落更准确的说法是块（block），因为块也可以指标题和列表项。
# 20.4.1 找出文本块，收集空行前的所有行并将它们返回。
# 代码清单20-2 一个文本块生成器（util.py）
def lines(file):
    for line in file:
        yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []

# 20.4.2 添加一些标记,使用代码清单20-2提供的基本功能，可创建简单的标记脚本.
# 1、打印一些起始标记；2、对于每个文本块，在段落标签内打印它；3、打印一些结束标记。
# 第一个文本块使用一级标题，星号括起的文本改成突出文本（使用标签em）。
# 代码清单20-3 一个简单的标记程序（simple_markup.py）
import sys, re
from util import *

print('<html><head><title>...</title><body>')
title = True
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*', r'<em>\1<em>', block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')
print('</body></html>')
# python simple_markup.py < test_input.txt > test_output.html

# 20.5 再次实现,为了提高可扩展性，需提高程序的模块化程度（将功能放在独立的组件中）
# 要提高模块化程度，方法之一是采用面向对象设计（参见第7章）。你需要找出一些抽象，让程序在变得复杂时也易于管理。
# 1、解析器：添加一个读取文本并管理其他类的对象。
# 2、规则：对于每种文本块，都制定一条相应的规则。这些规则能够检测不同类型的文本块并相应地设置其格式。
# 3、过滤器：使用正则表达式来处理内嵌元素。
# 4、处理程序：供解析器用来生成输出。每个处理程序都生成不同的标记。

# 20.5.1 处理程序，理程序负责生成带标记的文本，并从解析器那里接受详细指令。
# 假设对于每种文本块，它都提供两个处理方法：一个用于添加起始标签，另一个用于添加结束标签。
class HTNLRenderer:
    def start_paragraph(self):
        print('<p>')
    def end_paragraph(self):
        print('</p>')
# 要添加其他类型的标记，只需再创建相应的处理程序（或渲染程序），并在其中包含添加相应起始标签和结束标签的方法。
def sub_emphasis(self, match):
    return '<em>{}</em>'.format(match.group(1))  # 处理要突出的内容
def feed(self, data):
    print(data)  # 向处理程序提供实际文本

# 20.5.2 处理程序的超类,为提高灵活性，我们来添加一个Handler类，它将是所有处理程序的超类，负责处理一些管理性细节。
class Hander:
    def callbcak(self,prefix,name,*args):
        method = getattr(self, prefix + name, None)
        if callable(method):
            return method(*args)
# getattr(object, name[, default]):object：对象，name：字符串，对象属性；
# default：默认返回值，如果不提供该参数，在没有对应属性时，将触发 AttributeError。
# callable：调用返回True，否返回False。
    def start(self,name):
        self.callbcak('start_', name)
    def end(self,name):
        self.callbcak('end_', name)
    def sub(self,name):
        def substitution(match):
            result = self.callbcak('sub_', name, match)
            if result is None:
                match.group(0)
            return result
        return substitution

from handlers import HTMLRenderer
handler = HTMLRenderer()
# print(handler.sub('emphasis'))
import re
print(re.sub(r'\*(.+?)\*', handler.sub('emphasis'), 'This *is* a test'))
print(re.sub(r'\*(.+?)\*', handler.sub('emphasis'), 'This *is* a test'))

# 20.5.3 规则,是供主程序（解析器）使用的。
# 主程序必须根据给定的文本块选择合适的规则来对其进行必要的转换。
# 1、知道自己适用于那种文本块（条件）；2、对文本块进行转换（操作）。
# 因此每个规则对象都必须包含两个方法：condition（待处理的文本块）和
# action（访问处理器对象；返回一个布尔值，指出是否就此结束对当前文本块的处理。）。
# class HeadlineRule:
#     def condition(self, block):
#         如果文本块符合标题的定义，就返回True；
#         否则返回False。
# def action(self, block, handler):
#         调用诸如handler.start('headline')、handler.feed(block）
#         和handler.end('headline')等方法。
#         我们不想尝试其他规则，因此返回True，以结束对当前文本块的处理。
# 20.5.4 规则的超类,但多个规则可能执行相同的操作.
class Rule:
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True
#
# 你无需实现独立的过滤器类。由于Handler类包含方法sub，每个过滤器都可用一个正则表达
# 式和一个名称（如emphasis或url）来表示。

# 20.5.6 解析器，应用程序的核心部分：Parser类。
# 它使用一个处理程序以及一系列规则和过滤器将纯文本文件转换为带标记的文件（这里是HTML文件）。
class Parser:
    """
     读取文本文件、应用规则并控制处理程序的解析器
    """
    def __init__(self, handler):
        self.handler = handler
        self.rules = []  # 规则列表
        self.filters = []  # 过滤器列表
    def addRule(self, rule):
        self.rules.append(rule)  # 在规则列表中添加一个规则
    def addFilter(self, pattern, name):
        def filter(block, handler):  # 在过滤器列表中添加一个过滤器
            return re.sub(pattern, handler.sub(name), block)
# 调用re.sub并将参数指定为合适的正则表达式（模式）和处理程序中的替换函数（handler.sub(name)）。
        self.filters.append(filter)
    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):  # if语句来检查它是否适用—
                    last = rule.action(block, self.handler)
                    if last:break
# 为结束对文本块的处理，将方法action的返回值赋给变量last，再在这个变量为True时退出for循环。
        self.handler.end('document')
