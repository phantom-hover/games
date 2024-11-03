#Python允许你将类存储在模块中，然后在主程序中导入所需的模块
from car import Car

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
print("---------")

#在一个模块中存储多个类
from car import ElectricCar
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
print("---------")

#从一个模块导入多个类
from car import Car, ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
print("---------")

#导入整个模块
import car
my_mustang = car.Car('ford', 'mustang', 2024)

my_leaf = car.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

#导入模块中的所有类
"""
要导入模块中的每个类，可使用下面的语法
from module_name import *
#该导入方式不推荐
"""

#在一个模块中导入另一个模块
"""
将A类存储在一个模块中,并将B和C类存储到另一个模块中
如在BC中:from module_name(A) import A
B类需要访问其父类A,因此将A类导入该模块,更新A类,使其只包含A类
"""

#使用别名
from car import ElectricCar as EC
#使用别名
my_leaf = EC('nissan', 'leaf', 2024)
#给模块指定别名
import car as c
#现在可以结合使用模块别名和完整的类名
my_leaf = c.ElectricCar('nissan', 'leaf', 2024)

#找到合适的工作流程
