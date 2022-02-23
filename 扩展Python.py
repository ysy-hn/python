# # 知识
# # 需要进一步提升速度的方法：1、使用Python开发原型；2、对程序进行性能分析以找出瓶颈；
# # 3、使用C（或者C++、C#、Java、Fortran等）扩展重写瓶颈部分。
# # 既能获得使用高级语言（Python）开发复杂系统的好处，又能使用低级语言（C）来开发较小但速度至关重要的组件。
# # 将潜在的瓶颈封装起来。
#
# # 17.2 简单易行的方式：Jython 和 IronPython
# # Jython，底层语言为Java；IronPython，为C#和其他.NET语言;
# # 在Jython中，可直接访问Java标准库；而在IronPython中，可直接访问C#标准库。
#
# # 代码清单17-1 一个简单的Java类（JythonTest.java）
# # public class JythonTest{
# #     public void greeting(){
# #         System.out.println('Hello, world!');
# #     }
# # }
# # 使用java编译器编译，javac JythonTest.java命令。cmd不识别javac时，重装java并配置好环境。
# # 编译这个类后，启动Jython（并将.class文件放到当前目录或Java CLASSPATH包含的目录中）。
# # CLASSPATH=JythonTest.class jython；就可以正常使用python方法导入这个由jython编写的类。
# # import JythonTest
# # test = JythonTest()
# # print(test.greeting())
#
# # 代码清单17-2 一个简单的C#类（IronPythonTest.cs）
# # using System;
# # namespace FePyTest {
# #    public class IronPythonTest {
# #
# #       public void greeting() {
# #          Console.WriteLine("Hello, world!");
# #       }
# #
# #    }
# # }
# # 对于Microsoft .NET编译, csc.exe /t:library IronPythonTest.cs命令；
# # 将其编译为动态链接库（DLL；参阅C#文档），并根据需要修改相关的环境变量（如PATH），然后导入。
# # import clr
# # clr.AddReferenceToFile("IronPythonTest.dll")
# # import FePyTest
# # f = FePyTest.IronPythonTest()
# # print(f.greeting() )
#
# # 17.3 编写C语言扩展,扩展Python通常意味着扩展CPython——使用编程语言C实现的Python标准版
# # 使用C语言编写Python扩展时，必须遵循严格的API,因为动态性和易读性不强。
# # SWIG：简单包装器和接口生成器；一种简化c语言扩展的编写过程。
# # SWIG是一款自动为C语言库生成包装代码的工具。包装代码自动处理Python CAPI，
# # 使你不必自己去做这样的工作。使用SWIG是最简单、最流行的扩展Python的方式之一。
#
# # 17.3.1 SWIG
# # 一、安装：官网下载压缩包，直接解压，在配置.exe文件的环境变量配置，即可使用；
# # 可使用命令行工具（cmd）查看，swig -version/-help,查看版本和命令等。
# # 二、用法：1、为代码编写一个接口文件。
# # 2、对接口文件运行SWIG，以自动生成一些额外的C语言代码（包装器代码）。
# # 3、将原来的C语言代码和生成的包装器代码一起编译，以生成共享库。
#
# # 三、回文：是忽略空格、标点等后正着读和反着读一样的句子.
# # 代码清单17-3 一个简单的检测回文的C语言函数（palindrome.c）
# # #include <string.h>
# #
# # int is_palindrome(char *text) {
# #     int i, n = strlen(text);
# #     for (i = 0; i <= n/2; ++i) {
# #         if (text[i] != text[n-i-1]) return 0;
# #     }
# #     return 1;
# # }
#
# # 代码清单17-4 检测回文的Python函数
# def is_palindrome(text):
#     n = len(text)
#     for i in range(len(text) // 2):
#         if text[i] != text[n-i-1]:
#             return False
#     return True
#
# # 代码清单17-5 回文检测库的接口（palindrome.i）
# # %module palindrome
# #
# # %{
# # #include <string.h>
# # %}
# #
# # extern int is_palindrome(char *text);
# #
# # extern int is palindrome(char *text);
# # 四、接口文件,声明要导出的函数（和变量），就像在头文件中一样;
# # 在接口文件的开头，有一个由%{和%}界定的部分，可在其中指定要包含的头文件（这里为string.h）。
# # 在这个部分的前面，还有一个%module声明，用于指定模块名。
#
# # 五、运行SWIG,swig -help可查看命令。
# # 使用开关-python就可让SWIG对C语言代码进行包装，以便能够在Python中使用。
# # 另一个可能很有用的开关是-c++，可用于包装C++库。
# # 运行SWIG时，需要将接口文件（也可以是头文件）作为参数，
# # swig -python palindrome.i,将生成2个新文件.c和.py。
#
# # 六、 编译、链接和使用，比较难懂可使用简易方法，越编译器“魔法森林”的捷径，18.3章的内容
# # 18.3 编译扩展,Setuptools也可用来完成这种任务.
# from setuptools import setup, Extension
#
# setup(name='palindrome',
#       version='1.0',
#       ext_modules=[
#             Extension('palindrome', ['palindrom2.c'])
#       ])
# # 构造函数Extension将一个名称和一个相关文件列表作为参数
# # 运行命令install，将自动编译扩展模块palindrome再安装它.
# # python setup.py build_ext --inplace(UNIX系统）:只就地编译扩展，不安装。
# # 能够让Setuptools使用SWIG并直接将其作为Python扩展确实非常方便；
# # 只需将接口文件的名称加入到Extension实例的文件列表中即可。
# # from setuptools import setup, Extension
# #
# # setup(name='palindrome',
# #       version='1.0',
# #       ext_modules=[
# #             Extension('_palindrome', ['palindrome.c',
# #                                       'palindrome.i'])
# #       ])
#
# # 17.3.2 手工编写扩展
# # 1. 引用计数，一个对象只要被代码引用（在C语言中是有指向它的指针），就不应将其释放。
# # 将对象的引用计数加1或减1时，正在被引用，不能释放；引用计数变成0后，对象将被自动释放。
# # Python中，内存管理是自动完成的：你只管创建对象，当你不再使用时它们就会消失。
# # C语言中，你必须显式地释放不再使用的对象（更准确地说是内存块），否则程序占用的内存将越来越多，为内存泄漏（memory leak）。
#
# # Py_INCREF：将obj的引用计数加1；Py_DECREF：将obj的引用计数减1。
# # 一些要点：
# # 1、对象不归你所有，但指向它的引用归你所有。一个对象的引用计数是指向它的引用的数量。
# # 2、对于归你所有的引用，必须负责在不再需要它时调用Py_DECREF。
# # 3、对于你暂时借用的引用，不应在借用完后调用Py_DECREF，因为这是引用所有者的职责。
# # 4、可通过调用Py_INCREF将借来的引用变成自己的。将创建一个新引用，而借来的引用依然归原来的所有者所有。
# # 5、通过参数收到对象后，要转移所有权（如将其存储起来）还是仅仅借用完全由你决定，但应清楚地说明。
# # 如果函数将在Python中调用，完全可以只借用，因为对象在整个函数调用期间都存在。
# # 如果在C语言中调用，就无法保证对象在函数调用期间都存在，因此应该创建自己的引用，并在使用完毕后将其释放。
#
# # 引用计数是一种垃圾收集方式，“垃圾”指的是程序不再使用的对象。垃圾收集器
#
# # 2. 扩展框架，必须先包含头文件Python.h，再包含其他标准头文件。头文件，#include <Python.h>。
# # 给函数指定什么样的名称都可以，但它必须是静态的；
# # 返回一个指向PyObject对象的指针（归你所有的引用）并接受两个参数（都是指向PyObject的指针）；
# # 将这两个参数分别命名为self和args（self：当前对象或NULL，args：由参数组成的元组）。
# #include <Python.h>
# # static PyObject *somename(PyObject *self, PyObject *args){
# #     PyObject *result;
# #     /* 在这里执行操作，包括分配result*/
# #
# #     Py_INCREF(result);/* 仅当需要时才这样做！*/
# #     return result;
# # }
# # 参数self仅用于关联的方法中。在其他函数中，这个参数为NULL指针。
# # 参数args包含传递给函数的所有参数（参数self除外）。
# # PyArg_ParseTuple(args, fmt, ...) ：提取位置参数。
# # PyArg_ParseTupleAndKeywords(args, kws, fmt, kwlist) ：提取位置参数和关键字参数。
#
# # # 代码清单17-6 手工编写的模块palindrome的Python C API版回文检查（palindrome2.c）
# # #include <Python.h>
# #
# # static PyObject *is_palindrome(PyObject *self, PyObject *args) {
# #     int i, n;
# #     const char *text;
# #     int result;
# #     /* "s"表示一个字符串：*/
# #     if (!PyArg_ParseTuple(args, "s", &text)) {
# #         return NULL;
# #     }
# #     /* 与旧版的代码大致相同：*/
# #     n=strlen(text);
# #     result = 1;
# #     for (i = 0; i <= n/2; ++i) {
# #         if (text[i] != text[n-i-1]) {
# #             result = 0;
# #             break;
# #         }
# #     }
# #     /* "i"表示一个整数：*/
# #     return Py_BuildValue("i", result);
# # }
# #
# # /* 方法/函数列表：*/
# # static PyMethodDef PalindromeMethods[] = {
# #
# #     /*名称、函数、参数类型、文档字符串 */
# #     {"is_palindrome", is_palindrome, METH_VARARGS, "Detect palindromes"},
# #     /* 列表结束标志：*/
# #     {NULL, NULL, 0, NULL}
# #
# # };
# #
# # static struct PyModuleDef palindrome =
# # {
# #     PyModuleDef_HEAD_INIT,
# #     "palindrome",  /* 模块名 */
# #     "",            /* 文档字符串 */
# #     -1,            /*存储在全局变量中的信号状态 */
# #     PalindromeMethods
# # };
# #
# #
# # /* 初始化模块的函数：*/
# # PyMODINIT_FUNC PyInit_palindrome(void)
# # {
# #     return PyModule_Create(&palindrome);
# # }
#
# # 新增的大部分内容都是模板代码。可将palindrome替换为模块名，将is_palindrome替换为函数名。
# # 如果还有其他函数，只需在数组PyMethodDef中将它们列出。初始化函数必须为initmodule，module为模块名.
# # 然后编译，可使用18.3章的简易方法，生成.so的文件，再放在PYTHONPATH包含的目录（如当前目录）中，可以使用。
# from palindrome import is_palindrome
# print(is_palindrome('foobar') )
#
