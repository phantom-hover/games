#类可以模拟任何东西，基于这些创建对象成为实例化，这让你能够使用类的实例
#创建Dog类：赋予每条小狗sit 和 roll over 的能力
from typing import Any


class Dog:
#定义一个名为Dog的类，首字母大写的名称指的是类
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
    #类中的函数称为方法，__init__是一种特殊方法，每当根据Dog类创建新实例时Python会自动运行它。
    #定义成包含三个形参，其中self必不可少且位于其他形参前面，实参self会自动传递，只需给后面的形参提供值
        """初始化属性name 和 age"""
        self.name = name
        self.age = age
        #两个变量皆有前缀self，可供类中的所有方法使用，可以通过类的任意实例进行访问，这样通过实例访问的变量称为属性

    def sit(self):
        """模拟小狗收到命令时坐下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")
    #Dog类定义另外两个方法：sit()和roll_over()，仅仅是打印一条信息，指出小狗正在坐下或打滚

#下面根据类
my_dog = Dog('Willie', 6)
#处理此代码时，Python调用Dog类的__init__的方法，并传入实参'Willie'和6
#首字母大写的名称指的是类，全小写的名称指的是根据类创建的实例

my_dog.name
#访问属性：使用点号来访问my_dog的属性name的值

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()
#调用方法：Python在类Dog中查找方法sit()并运行其代码
print("------------------------------------")

#创建多个实例：
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"My dog's name is {your_dog.name}.")
print(f"My dog is {your_dog.age} years old.")
your_dog.sit()

