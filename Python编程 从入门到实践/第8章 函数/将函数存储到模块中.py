#函数优点：将代码块与主程序分离，也可将函数存储在称为模块的独立文件中，再将模块import导入主程序
#import语句可以让你在当前运行的程序文件中使用模块中的代码
#模块的扩展名是.py的文件
import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
"""
可用下列语法使用其中任意一个函数:
module_name.function_name()
也可以导入模块中特定函数,用逗号分隔函数名(此时无需使用句点):
from module_name import function_0, function_1, function_2...
"""
#使用as函数给函数指定别名(alias)
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
#也可以用as函数给模块指定别名
"""
import module_name as mn
"""
#使用星号可以导入模块中所有函数：
"""
from pizza import *
"""
#由于导入每个函数，可通过名称来调用每个函数，无需使用点号,如果不是自己编写的大型模块，慎用！

#函数编写指南
"""
给函数指定描述性名称时，只使用小写字母和下划线
给形参指定默认值时等号两边不要有空格
def function_name(parameter_0, parameter_1='default value')
调用关键字实参一样：function_name(value_0,parameter_1='value')
"""