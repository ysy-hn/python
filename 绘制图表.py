# 知识
# 创建一个PDF文件，其中包含的图表对从文本文件读取的数据进行了可视化。
# ReportLab包的基本知识，它让你能够像创建纯文本一样轻松地创建PDF格式（和其他格式）的图形和文档。
# 1、从网上下载数据文件；
# 2、对数据文件进行解析，并提取感兴趣的内容。
# 3、根据这些数据创建PDF图形。
# 如果你不想只是蜻蜓点水，可考虑使用图形包PYX（http://pyx.sf.net），其功能非常强大，并支持基于TEX排版。

# 21.4.1 使用 ReportLab 绘图
# ReportLab由很多部分组成，让你能够以多种方式生成输出。生成PDF,最基本的模块是pdfgen，
# Canvas类包含多个低级绘图方法，例如，要在名为c的Canvas上绘制直线，可调用方法c.line。
# 使用更高级的图形框架（reportlab.graphics包及其子模块），它能让我们创建各种形状，
# 将其添加到Drawing对象中，再将Drawing对象输出到PDF文件中。

# 代码清单21-1 一个简单的ReportLab程序（hello_report.py）
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF
d = Drawing(600, 600)
s = String(300, 300, 'Hello, world!', textAnchor='middle', fontSize=18, fillColor=colors.red)

d.add(s)
renderPDF.drawToFile(d, 'hello1.pdf', 'A simple PDF file')
# 创建一个指定尺寸的Drawing对象，再创建具有指定属性的图形元素（这里是一个String对象），
# 然后将图形元素添加到Drawing对象中。最后，以PDF格式渲染Drawing对象，并将结果保存到文件中。

# 21.4.2 绘制折线,PolyLine:绘制多条相连的直线.
# 要绘制折线图，必须为数据集中的每列数据绘制一条折线。
# 这些折线上的每个点都由时间（年和月）和值（从相关列获取的太阳黑子数）组成。
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF

a = Drawing(100, 100)
b = PolyLine([(0, 0), (10, 0), (10, 10), (0, 10)])
a.add(b)
renderPDF.drawToFile(a, '1.pdf')

# 21.4.3 编写原型
# 代码清单21-2 太阳黑子图形程序的第一个原型（sunspots_proto.py）
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF

data = [
# Year Month Predicted High Low
 (2007, 8, 113.2, 114.2, 112.2),
 (2007, 9, 112.8, 115.8, 109.8),
 (2007, 10, 111.0, 116.0, 106.0),
 (2007, 11, 109.8, 116.8, 102.8),
 (2007, 12, 107.3, 115.3, 99.3),
 (2008, 1, 105.2, 114.2, 96.2),
 (2008, 2, 104.1, 114.1, 94.1),
 (2008, 3, 99.9, 110.9, 88.9),
 (2008, 4, 94.8, 106.8, 82.8),
 (2008, 5, 91.2, 104.2, 78.2),
        ]
drawing = Drawing(200, 150)
pred = [row[2]-40 for row in data]
high = [row[3]-40 for row in data]
low = [row[4]-40 for row in data]
times = [200*((row[0] + row[1]/12.0) -2007)-110 for row in data]

drawing.add(PolyLine(list(zip(times, pred)), strokeColor=colors.blue))
drawing.add(PolyLine(list(zip(times, high)), strokeColor=colors.red))
drawing.add(PolyLine(list(zip(times, low)), strokeColor=colors.green))

drawing.add(String(65, 115, 'sunsports', fontSize=18, fillColor=colors.red))
renderPDF.drawToFile(drawing, 'report2.pdf', 'sunsports')

# 21.5.1 获取数据,使用标准模块urllib.
# 打开文件并读取其内容后，需要将不需要的内容剔除。
# 这里使用的文件包含空行（只有空白的行），还包含以特殊字符（#和:）打头的行。
# from urllib.request import urlopen
#
# data = []
# for line in urlopen(URL).readlines():
#  line = line.decode()
#  if not line.isspace() and not line[0] in COMMENT_CHARS:
#   data.append([float(n) for n in line.split()])

# 21.5.2 使用 LinePlot 类
# 快速设计原型时，秉承的理念是手头有什么就用什么，并看看能使用它们做什么。之后再进行优化重构。

# 代码清单21-3 最终的太阳黑子程序（sunspots.py）
from urllib.request import urlopen
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF

URL = 'ftp://ftp.swpc.noaa.gov/pub/weekly/Predict.txt'
COMMENT_CHARS = '#:'


drawing = Drawing(400, 200)
data = []
for line in urlopen(URL).readlines():
    line = line.decode()
    if not line.isspace() and line[0] not in COMMENT_CHARS:
        data.append([float(n) for n in line.split()])

pred = [row[2] for row in data]
high = [row[3] for row in data]
low = [row[4] for row in data]
times = [row[0] + row[1]/12.0 for row in data]

lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = [list(zip(times, pred)),
           list(zip(times, high)),
           list(zip(times, low))]
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green

drawing.add(lp)

drawing.add(String(250, 150, 'Sunspots',
            fontSize=14, fillColor=colors.red))


renderPDF.drawToFile(drawing, 'report2.pdf', 'Sunspots')

# 读取本地文件程序
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics import renderPDF

data = []
COMMENT_CHARS = '#:'
with open('sun.txt') as f:
    for line in f.readlines():
        line = line
        if not line.isspace() and line[0] not in COMMENT_CHARS:
            data.append([float(n) for n in line.split()])

pred = [row[2] for row in data]
high = [row[3] for row in data]
low = [row[4] for row in data]
times = [row[0] + row[1]/12.0 for row in data]

drawing = Drawing(400, 200)
lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = [list(zip(times, pred)),
           list(zip(times, high)),
           list(zip(times, low))]
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green

drawing.add(lp)

drawing.add(String(250, 150, 'Sunspots',
            fontSize=14, fillColor=colors.red))

renderPDF.drawToFile(drawing, 'report3.pdf', 'Sunspots')
