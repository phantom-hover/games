#位置实参：要求实参的顺序和形参顺序相同 
#关键字实参：每个实参都由变量名和值组成，还可以使用列表和字典
def describe_pet(animal_type,pet_name):
    """显示动物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')
#调用函数多次
describe_pet('dog','willie')
#位置实参的顺序很重要
print("----------------------------分割线---------------------------")

#关键字实参无需考虑实参顺序，而清楚指出函数调用各个值的用途
describe_pet(animal_type='hamster',pet_name='harry')
print("----------------------------分割线---------------------------")

#默认值：简化函数调用
def describe_pet(pet_name,animal_type='dog'):
    """显示动物的信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')
#此函数定义修改了形参的排列顺序，这个实参视为位置实参，需要放到开头
#使用时，必须在形参列表中先列出没有默认值的形参，再列出有默认值的形参
