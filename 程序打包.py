# # 知识
# # Setuptools：轻松地编写安装脚本，用于生成可发布的归档文档，供用户用来编译和安装你编写的库，还可用于编译扩展。
# # 18.1 Setuptools 基础
# # 代码清单18-1 简单的Setuptools安装脚本（setup.py）
# from setuptools import setup
#
# setup(name='Hello',
#       version='1.0',
#       description='A simple example',
#       author='Magnus Lie Hetland',
#       py_modules=['hello'])

# # 也可以填写其它信息或不填。
# # python setup.py:从输出可知，要获得更多的信息，可使用开关--help或--help-commands.
# # python setup.py build：打包命令；
# # Setuptools创建了一个名为build的目录，其中包含子目录lib；同时将hello.py复制到了这个lib中。
# # 目录build相当于工作区，Setuptools在其中组装包（以及编译扩展库等）。
# # 安装时不需要执行命令build，因为当你执行命令install时，如果需要，命令build会自动运行。
# # Python setup.py install:一般安装，安装模块、包和扩展的标准机制；
# # 会安装到python的site-packages目录下；可以直接导入使用了。
# # python setup.py uninstall:卸载指令；
# # python setup.py develop：开发方式安装（频繁变更，安装前需卸载很麻烦，使用开发方式可以避免）。
#
# # 18.2 打包,编写让用户能够安装模块的脚本setup.py后，就可使用它来创建归档文件了.
# # python setup.py sdist :创建源代码归档文件。
# # 创建了dist的目录，有Hello-1.0.tar.gz的文件；可将其解压缩，再使用脚本setup.py进行安装。
# # --formats：设置分发格式，为复数形式，可指定多种用逗号分隔的格式，这样将一次性创建多个归档文件。
# # --help-formats：获悉可使用的格式列表。
#
# # python setup.py --help
# #   --name              包名称
# #   --version (-V)      包版本
# #   --author            程序的作者
# #   --author_email      程序的作者的邮箱地址
# #   --maintainer        维护者
# #   --maintainer_email  维护者的邮箱地址
# #   --url               程序的官网地址
# #   --license           程序的授权信息
# #   --description       程序的简单描述
# #   --long_description  程序的详细描述
# #   --platforms         程序适用的软件平台列表
# #   --classifiers       程序的所属分类列表
# #   --keywords          程序的关键字列表
# #   --packages  需要打包的目录列表
# #   --py_modules  需要打包的python文件列表
# #   --download_url  程序的下载地址
# #   --cmdclass
# #   --data_files  打包时需要打包的数据文件，如图片，配置文件等
# #   --scripts  安装时需要执行的脚步列表
#
# # python setup.py --help-commands
# #   --python setup.py build     # 仅编译不安装
# #   --python setup.py install    #安装到python安装目录的lib下
# #   --python setup.py sdist      #生成压缩包(zip/tar.gz)
# #   --python setup.py bdist_wininst  #生成NT平台安装包(.exe)
# #   --python setup.py bdist_rpm #生成rpm包
#
# # python setup.py bdist --help-formats
# #   --formats=rpm      RPM distribution
# #   --formats=gztar    gzip'ed tar file
# #   --formats=bztar    bzip2'ed tar file
# #   --formats=ztar     compressed tar file
# #   --formats=tar      tar file
# #   --formats=wininst  Windows executable installer
# #   --formats=zip      ZIP file
#
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
# from setuptools import setup, Extension
#
# setup(name='palindrome',
#       version='1.0',
#       ext_modules=[
#             Extension('_palindrome', ['palindrome.c',
#                                       'palindrome.i'])
#       ])

# # 18.4 使用 py2exe 创建可执行程序,py2exe是Setuptools的一个扩展,使用pip安装。
# # 1、能够创建可执行的Windows程序（.exe文件）；
# # 2、在你不想给用户增加单独安装Python解释器的负担时很有用；
# # 3、py2exe包可用来创建带GUI（参见第12章）的可执行文件。
# print('hello, world!')
# input('Press<enter>')
# # 创建一个空目录，再将这个文件（hello.py）放到这个目录中。
#
# from distutils.core import setup
# import py2exe
#
# setup(console=['hello1.py'])
# # python setup.py py2exe:运行这个脚本。
# # 创建一个控制台应用程序（hello.exe），还将在子目录dist中创建其他几个文件。

# # 要让别人能够使用pip安装你开发的包，必须向Python Package Index（PyPI）注册它；
# # python setup.py register（UNIX），这将打开一个菜单，让你能够登录或注册。
# # 注册包后，就可使用命令upload将其上传到PyPI；python setup.py sdist upload。

# # 在电脑没有python环境时，可打包成可执行程序。
# # python -m pip install --upgrade pip,更新pip；
# # pip install pyinstaller，安装pyinstaller；pyinstaller -F --onefile 名称.py，打包成可执行程序。

# 例题
# from setuptools import setup
#
# setup(name='Hello',
#       version='1.0',
#       description='A simple example',
#       author='Magnus Lie Hetland',
#       py_modules=["hello"])
