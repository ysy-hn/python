# 转换标志，跟在叹号后面的单个字符括r（表示repr）、s（表示str）和a（表示ascii）。
print("{pi!s} {pi!r} {pi!a}".format(pi="π"))  # r（表示repr）、s（表示str）和a（表示ascii）
print("{num:10}".format(num=3))  # :值，宽度
print("{pi:10.2f}".format(pi=3.1415926) )  # .2f，精度
print('One googol is {:,}'.format(10**100))  # ，千位分隔符
print( '{:010.2f}'.format(3.14159) )  # 0填充
print("{:$^15}".format(" WIN BIG "))  # 其它字符填充

from math import pi
print('{0:<10.2f}\n{0:^10.2f}\n{0:>10.3f}'.format(pi))
# 宽度：10，精度.2f，左对齐：<,居中：^,右对齐：>。
print('{0:10.2f}\n{1:10.2f}'.format(pi, -pi))
# 0 1:format中的参数序列。
print('{0:10.2f}\n{1:=10.2f}'.format(pi, -pi))
# =：将填充字符放在符号和数字之间，该代码填充字符为空格。
print('{0:-.2}\n{1:-.2}'.format(pi, -pi))  # 默认设置
print('{0:+.2}\n{1:+.2}'.format(pi, -pi))
print('{0: .2}\n{1: .2}'.format(pi, -pi))
# 宽度位置加入其它字符时，对于负数还是保持原样；对于正数，添加+和空格，直接填充，其它保持原样。

# 根据指定的宽度打印格式良好的价格列表
width = int(input('Please enter width: '))
price_width = 10
item_width = width - price_width
header_fmt = '{{0:{}}} {{1:>{}}}'.format(item_width, price_width)
fmt = '{{0:{}}} {{1:>{}.2f}}'.format(item_width, price_width)
# 分两次设置了字符串的格式，格式定义字符串本身又包括占位符，两层花括号变成花括号，一对花括号变成宽度数值。
# 格式化字符本身包含字符，fmt格式化2次；print('{:{}}'.format('Item', item_width))，格式化1次。
# print('{{:{}}}'.format(10))，格式化1次，输出：{：10}。
print('=' * width)
print(header_fmt.format('Item', 'Price'))
print('-' * width)
print(fmt.format('Apples', 0.4))
print(fmt.format('Pears', 0.5))
print(fmt.format('Cantaloupes', 1.92))
print(fmt.format('Dried Apricots (16 oz.)', 8))
print(fmt.format('Prunes (4 lbs.)', 12))
print('=' * width)


# 3.4
print( "The Middle by Jimmy Eat World".center(39, "*"))
# center：在两边添加填充字符（默认为空格）让字符串居中
print('With a moo-moo here, and a moo-moo there'.find('moo'))
subject = '$$$ Get rich now!!! $$$'
print(subject.find('!!!', 0, 16))
# find：在字符串中查找子串。如果找到，就返回子串的第一个字符的索引，否则返回-1；还可指定搜索的起点和终点（它们都是可选的）
seq = ['1', '2', '3', '4', '5']
sep = '+'
print(sep.join(seq))  # 尝试合并一个数字列表
print('1+2+3+4+5'.split('+'))  # 将字符串拆分为序列
print('This is a test'.replace('is', 'eez') )  # 替换字符串
# translate与replace一样替换字符串的特定部分，它只能单字符替换；但能够同时替换多个字符，因此效率比replace高。
print( ' internal whitespace is kept '.strip() )
# strip：将字符串开头和末尾的空白（但不包括中间的空白）删除或字符串，并返回删除后的结果
# lstrip：删除开头，如上；rstrip：删除结尾，如上。

a = "AAD Ssd  asf asf "
print(a.title())  # 单词首字母大写
s = 'a, B'
print(s.capitalize())  # 将字符串的第一个字母变成大写,其他字母变小写。
print(a.upper())  # 全部大写
print(a.lower())  # 全部小写

c = 'that Is All, folks,2'
d = '   '
e = '1112'
f = 'ASDF SAF 1'
a = 'asd asd asf'
print(c.isspace())
print(c.isdigit())
print(c.isupper())
print(d.isspace())  # 判断字符串中全部为空格，是为真，否为假
print(e.isdigit())  # 判断字符串中全部为数字，是为真，否为假
print(f.isupper())  # 判断字符串中的字母全部大写，是为真，否为假
print(a.islower())  # 判断字符串中的字母全部小写，是为真，否为假


