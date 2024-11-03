#继承：编写的类是一个既有的类的特殊版本，子类自动获得父类的所有属性和方法
#子类的__init__()的方法
class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
#给属性指定默认值:添加以下属性，使其初始值为0
        self.odometer_reading = 0

    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
                  
    def increment_odometer(self, miles):
        """让里程表读数增加指定的量"""
        self.odometer_reading += miles

class Battery:
    """一次模拟电动起策划电池的简单尝试"""
    def __init__(self, battery_size=40):
        """初始化电池的属性"""
        self.battery_size = battery_size
    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")
        #将实例用作属性：将类的一部分提取出来，作为一个独立的类，组合：大型类拆分为多个协同
    def get_range(self):
        """打印一条消息，指出电池的续航里程"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """电动汽车的独特之处"""
    
    def __init__(self, make, model, year):
        """先初始化父类的属性，再初始化电动汽车特有的属性"""
        #给子类定义属性与方法
        """添加属性"""
        self.battery = Battery()

        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

#重写父类中的方法：父类的方法满足不了子类的需求
    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't have a gas tank!")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
#创建子类时，父类必须包含在当前文件中。
#super()函数可以调用父类的方法，父类称为超类(superclass)
print("---------")

my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

#模拟实物，解决上述问题时往往考虑的不是Python，而是如何使用代码来表示事物