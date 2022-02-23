# xmind使用方法：六项思考帽：
# 白色：客观信息；
# 红色：直觉感情；
# 黑色：逻辑判断；
# 黄色：积极乐观；
# 绿色：创新冒险；
# 蓝色：系统控制。


# pycharm使用技巧
# 打开settings：ctrl+alt+s
# 运行当前代码：ctrl+shift+F10
# 运行当前脚本：shift+F10
# 替换：ctrl+R
# 全局查找：ctrl+shift+F
# 全局替换：ctrl+shift+R
# 反撤销：ctrl+shift+Z
# 缩进：tab
# 反向缩进：shift+tab
# 翻页：PAGEUP和PAGEDOWN
# 行首：HOME
# 行尾：END

# 快速修正：alt+enter
# 复制代码：ctrl+D
# 删除代码：ctrl+Y
# 复写代码：ctrl+O
# 选中单词或代码块：ctrl+W
# 快速查看文档：ctrl+Q
# 模块或项目重命名：shift+F6
# 向下插入：shift+enter
# 向上插入：ctrl+alt+enter

# 查看项目视图：alt+1
# 查看结构视图：alt+7

# 快速进入代码：ctrl+左键或ctrl+B
# 快速查看历史：alt+左右方向 返回
# 快速切换方法：alt+上下

# 切换视图：ctrl+tab
# 查看资源文件，2次shift
# 查看方法在哪里调用：ctrl+alt+H
# 查看父类：ctrl+U
# 查看继承关系：ctrl+H

# 其它使用技巧
# Ctrl+N 按文件名搜索py文件
# Ctrl+shift+N 按文件名搜索所有类型的文件
# ctrl+shift+f 全局字符串搜索
# ctrl+shift+a
# 双shift搜索
# cd 路径：到某个路径中
# mkdir 文件名：创建文件夹
# python.exe -m pip install --upgrade pip：升级pip
# 补充知识：Django项目执行时No Module Named ‘ ‘ 问题的解决情况
# 出现这种问题的情况大致都是因为该模块未安装，使用 pip install xxx 进行安装，即可解决此类问题。
# 出现ModuleNotFoundError： No module named ‘rest_framework’ 时，
# 可以执行 pip install djangorestframework 命令进行安装。
# 出现ModuleNotFoundError： No module named ‘pymysql’ 时，
# 执行 pip install pymysql 完成安装
# 出现ModuleNotFoundError： No module named ‘import-export’ 时，
# 执行 pip install django-import-export 完成安装
# 查看django版本，py -m django --version

# 编辑python文件模板
# （a）shebang行
# #!/usr/bin/python3
# （b）预定义的变量要扩展为格式为$ {<variable_name>}的相应值。
# 可用的预定义文件模板变量为：
# $ {PROJECT_NAME} - 当前项目的名称。
# $ {NAME} - 在文件创建过程中在“新建文件”对话框中指定的新文件的名称。
# $ {USER} - 当前用户的登录名。
# $ {DATE} - 当前的系统日期。
# $ {TIME} - 当前系统时间。
# $ {YEAR} - 今年。
# $ {MONTH} - 当月。
# $ {DAY} - 当月的当天。
# $ {HOUR} - 目前的小时。
# $ {MINUTE} - 当前分钟。
# $ {PRODUCT_NAME} - 将在其中创建文件的IDE的名称。
# $ {MONTH_NAME_SHORT} - 月份名称的前3个字母。 示例：1月，2月等
# $ {MONTH_NAME_FULL} - 一个月的全名。 示例：1月，2月等
