#用def定义函数
def greet_user(username): 
    #显示简单的问候语
    print(f"Hello,{username.title()}!")
#向函数传递信息，给username指定一个值，调用greet_user可以传递名字
greet_user('jesse')
#变量username是一个形参，即函数完成工作所需的信息
#而值'jesse'是一个实参，即在调用函数时，传递给函数的信息
