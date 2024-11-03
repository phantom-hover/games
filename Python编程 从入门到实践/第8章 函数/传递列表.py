#传递列表给函数后，函数能直接访问其内容
def greet_users(names):
    """向列表中的每个用户发出简单的问候"""
    for name in names:
        msg = f"Hello {name.title()}!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
#将greet_users()定义成接受一个名字列表，并将其赋给形参names，这个函数收到遍历列表，并对其中每个用户打印，调用greet_users()并这个列表传递
print("----------------------------分割线---------------------------")

#在函数中修改列表
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其转移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print (completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
#每个函数都应只负责一项具体工作

#可以禁止函数修改列表
"""切片表示法[:]创建列表的副本"""
print_models(unprinted_designs[:], completed_models)