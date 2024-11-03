#使用return 语句将值返回到调用函数的那行代码
#返回简单的值
def get_formatted_name(first_name, last_name):
    """返回标准格式的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
print("----------------------------分割线---------------------------")

#让实参变成可选的
def get_formatted_name(first_name, middle_name, last_name):
    """返回标准格式的姓名"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
#也可以将middle_name改为默认值进行可选化操作为，保证该函数亦可正常运行，将其放到形参列表末尾
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
#检查是否提供中间名，Python将非空字符串解读为True
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
print("----------------------------分割线---------------------------")

#返回字典
def build_person (first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)

#新增可选形参age，其默认值设置为特殊值None(表示变量没有值)，可视为占位值，相当于False
def build_person (first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] =age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)
print("----------------------------分割线---------------------------")

#结合使用函数和while循环
def get_formatted_name(first_name, last_name):
    """返回规范格式的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
#可以通过break语句提供退出循环的简单途径
while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name}!")