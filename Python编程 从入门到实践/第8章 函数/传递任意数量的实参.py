#Python允许函数从调用语句中手机任意数量的实参
#形参名中的星号创建了一个名为toppings的元组，该元组包含函收到的所有值
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
print("----------------------------分割线---------------------------")

#要让函数接受不同类型的实参，必须在函数定义中将接受任意数量实参的形参放在最后
#Python 先匹配位置实参和关键字实参，再将余下的实参收集到最后一个形参中
def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')
#通用形参名 *args，可以收集任意数量的位置实参
print("----------------------------分割线---------------------------")

#使用任意数量的关键字实参
#用两个星号创建一个字典
def bulid_profile(first, last, **user_info):
    """创建一个字典， 其中包含我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = bulid_profile('albert', 'einstein', 
                            location='princeton', 
                            field='physics')
print(user_profile)
#通用形参名 **kwargs, 可以收集任意数量的关键字实参
