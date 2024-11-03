#Car类汇总
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
#def3    
    def increment_odometer(self, miles):
        """让里程表读数增加指定的量"""
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

print("--------------------")
#直接修改属性的值:直接访问并设置汽车的属性
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
#通过方法修改属性的值:无需直接访问属性，而是将值传递给方法，在内部进行更新
"""
    def update_odometer(self, mileage):
    将里程表读书设置为指定的值
    self.odometer_reading = mileage

my_new_Car.update_odometer(23)
"""
#也可以对此方法进行扩展，使其在修改里程表读数时做些额外的工作，如禁止将里程表读数往回调
"""
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can't roll back an odometer!')
"""

#通过方法让属性的值递增：将属性值递增特定的量，而不是将其设置为全新的值，见def#3
my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())
#首先创建一辆二手车my_used_car

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
#调用方法并传入23_500，将这辆二手车的里程表读数设置为23 500

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
#调用increment_odometer()并传入100，以增加从购买到登记期间行驶的100英里