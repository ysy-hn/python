# # 知识
# # GUI（图形用户界面）：包含按钮、文本框等控件的窗口；Tkinter是事实上的Python标准GUI工具包。
# # 12.1.1 初探：导入tkinter
# from tkinter import *
# top = Tk()
# # 要创建GUI，可创建一个将充当主窗口的顶级组件（控件）。为此，可实例化一个Tk对象。
# # mainloop() # 调用函数mainloop以进入Tkinter主事件循环
# btn = Button()  # 要创建按钮，可实例化Button类,目前不可见，使用布局管理器（几何管理器），pack。
# btn.pack()
# # btn['text'] = 'Click me!'
# def clicked():
#     print('I was clicked!')
# # btn['command'] = clicked
# # 控件包含各种属性，我们可以使用它们来修改控件的外观和行为。
# # btn.config(text='Click me!', command=clicked)  # 可以不分别给属性赋值，而使用方法config同时设置多个属性。
# Button(text='click me too!', command=clicked).pack()  # 还可使用控件的构造函数来配置控件。
#
# # 12.1.2 布局
# # Label(text="I'm in the first window!").pack()  # 构造函数的第一个可选参数，没有指定，将把顶级主窗口用作主控件
# second = Toplevel()
# Label(second, text="I'm in the second window!").pack()  # Toplevel类表示除主窗口外的另一个顶级窗口，而Label就是文本标签。
#
# for i in range(10):
#     Button(text=i).pack()
# # 没有提供任何参数时，pack从窗口顶部开始将控件堆叠成一列，并让它们在窗口中水平居中。
# # 可调整控件的位置和拉伸方式,side:LEFT、RIGHT、TOP、BOTTOM；可将参数fill设置为X、Y、BOTH；
# # 要让控件随父控件（这里是窗口）一起增大，可将参数expand设置为True。
# help(Pack.config)  # 交互式查看属性
# # grid管理器：排列控件：将它们放在不可见的表格单元格中。为此需要指定参数row和column，还可能要指定参数rowspan或columnspan——如果控件横跨多行或多列。
# # place管理器：手工放置控件——通过指定控件的x和y坐标以及高度和宽度来做到。
#
# # 12.1.3 事件处理,除了使用command进行事件处理，更通用的是bind。
# from tkinter import *
# top = Tk()
# def callback(event):
#     print(event.x, event.y)
# print(top.bind('<Button-1>', callback))  # <Button-1>是使用鼠标左按钮（按钮1）单击的事件名称。
# bind：要让控件对特定的事件进行处理，可对其调用方法bind，并指定事件的名称和要使用的函数。

# # 12.1.4 最终的程序
# from tkinter import *
# from tkinter.scrolledtext import ScrolledText
#
# def load():
#     with open(filename.get()) as file:
#         contents.insert(INSERT, file.read())  # 文本插入
#         print('打开成功！')
# # '1.0'来指定第1行的第0个字符（即第一个字符前面）；
# # 使用END来指定文本末尾，并使用INSERT来指定当前插入点。
# def save():
#     with open(filename.get(), 'w') as file:
#         file.write(contents.get('1.0', END))  # 文本保存
#         print('保存成功！')
# def delete():
#     with open(filename.get())as file:
#         contents.delete('1.0', END)
#         print('删除成功！')
#
# top = Tk()  # 创建主窗口
# top.title('文本')
#
# contents = ScrolledText()  # 创建可滚动的多行文本区域
# contents.pack(side=BOTTOM, expand=True, fill=BOTH)  # 文本内容编辑页配置
#
# filename = Entry()  # 创建单行文本框
# filename.pack(side=LEFT, expand=True, fill=X)  # 文本搜索框配置
#
# Button(text='打开', command=load).pack(side=LEFT)
# Button(text='保存', command=save).pack(side=LEFT)
# Button(text='删除', command=delete).pack(side=LEFT)
#
# mainloop()
# # Entry控件:创建单行文本框;使用get方法来提取Entry控件的内容。
# # 创建可滚动的多行文本区域，可结合使用控件Text和Scrollbar,但模块tkinter.scrolledtext已经提供了一种实现。
# # 对于ScrolledText对象，使用方法delete和insert来删除文本和插入文本。调用delete和insert时，需要使用合适的参数来指定文本的位置。

# from tkinter import *
# def main():
#     root = Tk()
#     # e输入框显示字符串:木芙蓉
#     def _show():
#         e.insert(0, '木芙蓉')
#     # 清空e输入框中的内容
#     def _clear():
#         e.delete(0, END)
#     content = StringVar()
#     e = Entry(root, textvariable=content).pack()
#     b_show = Button(root, text='显示木芙蓉', command=_show).pack()
#     b_clear = Button(root, text='清空', command=_clear).pack()
#     mainloop()
# if __name__ == '__main__':
#     main()



# 例题
# import tkinter as tk
# from tkinter import *
# top = Tk()
# mainloop()
#
# from tkinter import *
# # btn = Button()
# # btn.pack()
# # btn['text'] = 'Click me!'
# def clicked():
#     print('I was clicked!')
# # btn['command'] = clicked
#
# # btn.config(text='Click me1!', command=clicked)
#
# Button(text='Click me too!', command=clicked).pack()
#
# Label(text="I'm in the first window!").pack()
#
# # second = Toplevel()
# # Label(second, text="I'm in the second window！").pack()
#
# # 增加按钮默认居中，堆叠成一列
# # for i in range(10):
# #     Button(text=i).pack()
#
# # 模块功能解释
# # help(Pack.config)
# # help(Grid.configure)
# # help(Place.config)
# # help(Tk.bind)
#
# mainloop()
#
# from tkinter import *
# top = Tk()
# def callback(event):
#     print(event.x, event.y)
# print(top.bind('<Button-1>', callback))

# from tkinter import *
# from tkinter.scrolledtext import ScrolledText
#
# def load():
#     with open(filename.get()) as file:
#         contents.delete('1.0', END)
#         contents.insert(INSERT,file.read())
#
# def save():
#     with open(filename.get(), 'w') as file:
#         file.write(contents.get('1.0', END))
#
# top = Tk()
# top.title('文本')
#
# contents = ScrolledText()
# contents.pack(side=BOTTOM, expand=True, fill=BOTH)
#
# filename = Entry()
# filename.pack(side=LEFT, expand=True, fill=X)
#
# Button(text='打开', command=load).pack(side=LEFT)
# Button(text='保存', command=save).pack(side=LEFT)
#
# mainloop()
