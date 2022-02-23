# 迭代是Python最强大的功能之一，是访问集合元素的一种方式。
# 迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next()。

# # 字符串，列表或元组对象都可用于创建迭代器:
# list = [1, 2, 3, 4]
# it = iter(list)   # 创建迭代器对象
# print(next(it))   # 输出迭代器的下一个元素
# print(next(it))

# 迭代器对象可以使用常规for语句进行遍历:
list = [1, 2, 3, 4]
it = iter(list)
for x in it:
    print(x, end=' ')

# 也可以使用 next() 函数:
import sys

list = [1, 2, 3, 4]
it = iter(list)

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()  # 退出程序

# sys.exit(n) 退出程序引发SystemExit异常，可以捕获异常执行些清理工作。
# n默认值为0，表示正常退出，其他都是非正常退出。
# 还可以sys.exit(“sorry, goodbye!”); 一般主程序中使用此退出。
# os._exit(n)， 直接退出, 不抛异常, 不执行相关清理工作。常用在子进程的退出。
# exit()/quit()，跑出SystemExit异常。一般在交互式shell中退出时使用。
# python中exit(0) 和exit()1有什么功能？
# 在很多类型的操作系统里，exit(0)可以中断某个程序，其中的数字参数用来表示程序是否是碰到错误而中断。
# exit(1)表示发生了错误进行退出，exit(0)表示程序是正常退出的，退出代码是告诉解释器的（或操作系统）。
# 这和我们学的布尔逻辑0==False正好相反,不过你可以用不一样的数字表示不同的错误结果。
# 比如你可以用exit(100)来表示另一种和exit(2)或 exit(1)不同的错误。
import os
import re

# 执行jmeter脚本
cmd = "路径"
tmp = os.popen(cmd).read()
print(tmp)

# 输出执行结果
regex = re.compile('summary = .*?\(0.00%\)', re.S)
result = re.findall(regex, tmp)
if len(result) > 0:
    print("successed")
    exit(0)
else:
    print("failed")
    exit(1)


# 创建一个迭代器
# 把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
# 类都有一个构造函数，Python 的构造函数为 __init__(), 它会在对象初始化的时候执行。
# __iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过
# StopIteration 异常标识迭代的完成。
# __next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。
# 创建一个返回数字的迭代器，初始值为 1，逐步递增 1：
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myclass))
print(next(myclass))

# StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，
# 在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
# 在 20 次迭代后停止执行：
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)


# 生成器，使用了yield的函数被称为生成器（generator）
# 生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，
# 返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
# 调用一个生成器函数，返回的是一个迭代器对象。
# 以下实例使用 yield 实现斐波那契数列：
import sys
def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
print(f)

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()


# for循环简介：
# 一、当对象本身就是迭代器时，For循环工作机制：
# 调用 __iter__方法，返回自身self,也就是返回迭代器。不断地调用迭代器的next()方法，
# 每次按序返回迭代器中的一个值。迭代到最后没有元素时，就抛出异常 StopIteration
# 二、在可迭代对象中，for循环工作机制：
# 1、先判断对象是否为可迭代对象(等价于判断有没有__iter__或__getitem__方法)，
# 没有的话直接报错，抛出TypeError异常。有的话，调用 __iter__方法，返回一个迭代器。
# 在python内部不断地调用迭代器的__next__方法，每次按序返回迭代器中的一个值。
# 迭代到最后没有元素时，就抛出异常StopIteration，这个异常python自己会处理，不会暴露给开发者。
# 2、此外，还要注意，python中的for循环其实兼容了两种机制：
# （1）如果对象有__iter__会返回一个迭代器。如果对象没有__iter__，但是实现了__getitem__，
# 会改用下标迭代的方式。__getitem__可以帮助一个对象进行取数和切片操作。
# （2）当for发现没有__iter__但是有__getitem__的时候，会从0开始依次读取相应的下标，
# 直到发生IndexError为止，这是一种旧的迭代协议。iter方法也会处理这种情况，
# 在不存在__iter__的时候，返回一个下标迭代的iterator对象来代替。
# 一个重要的例子是str，字符串就是没有__iter__方法的，但是却依然可以迭代，
# 原因就是其在for循环时调用了__getitem__方法。


# 迭代器简介：
# 迭代器(iterator):迭代器对象必须同时实现__iter__和__next__方法才是迭代器。
# 对于迭代器来说，__iter__ 返回的是它自身self，__next__ 则是返回迭代器中的下一个值,
# 最后没有元素时，抛出异常(异常可以被开发者看到)。
# 1.迭代器一定是可迭代对象，因为它实现了__iter__()方法；
# 2.通过iter()方法(在类的内部就是__iter__)能够使一个可迭代对象返回一个迭代器。
# 3.迭代器的__iter__方法返回的是自身，并不产生新的迭代器对象。
# 第3点性质正是可迭代对象可以重复遍历的原因(每次返回一个独立的迭代器，
# 就可以保证不同的迭代过程不会互相影响)；而迭代器由于返回自身，因此只能遍历一次。
# _iter_(self)只会被调用一次,而_next_(self)会被调用 n 次，直到出现StopIteration异常。

# 迭代器是用来帮助我们记录每次迭代访问到的位置，当我们对迭代器使用next()函数的时候，
# 迭代器会向我们返回它所记录位置的下一个位置的数据。实际上，在使用next()函数的时候，
# 调用的就是迭代器对象的_next_方法。所以，我们要想构造一个迭代器，就要实现它的_next_方法。
# 但这还不够，python要求迭代器本身也是可迭代的，所以我们还要为迭代器实现_iter_方法，
# 而_iter_方法要返回一个迭代器，迭代器自身正是一个迭代器，所以迭代器的_iter_方法返回自身self即可。
#
# 一些术语的解释：
# 1，迭代器协议：对象需要提供next()方法，要么返回迭代中的下一项，要么就引起一个StopIteration异常，以终止迭代。
# 2，可迭代对象：实现了迭代器协议对象。list、tuple、dict都是Iterable（可迭代对象），
# 但不是Iterator（迭代器对象）。可以使用内建函数iter() ，把这些都变成Iterable（可迭代器对象）。
# 3，for item in Iterable 循环的本质就是先通过iter()函数获取可迭代对象Iterable的迭代器，
# 然后对获取到的迭代器不断调用next()方法来获取下一个值并将其赋值给item，
# 当遇到StopIteration的异常后循环结束。


# 生成器简介：
# 作用：延迟操作。也就是在需要的时候才产生结果，不是立即产生结果。
# 注意事项：生成器是只能遍历一次的；生成器是一类特殊的迭代器。
# 分类：
# 1、生成器函数：使用def定义函数，使用yield而不是return语句返回结果。
# yield语句一次返回一个结果，在每个结果中间，挂起函数的状态，以便下次从它离开的地方继续执行；
# 2、生成器表达式：类似于列表推导，只不过是把一对大括号[]变换为一对小括号()。
# 但是，生成器表达式是按需产生一个生成器结果对象，要想拿到每一个元素，就需要循环遍历。
# 生成器能做到迭代器能做的所有事,而且因为自动创建了 iter()和 next()方法,
# 生成器显得特别简洁,而且生成器也是高效的，使用生成器表达式取代列表解析可以同时节省内存。
# 除了创建和保存程序状态的自动方法,当发生器终结时,还会自动抛出 StopIteration 异常。
