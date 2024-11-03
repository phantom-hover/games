from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name:")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first,last)
    print(f"\tNeatly formatted name: {formatted_name}.")
#可每次修改函数进行测试，通过pytest提供了一种自动测试函数输出的高效方式
#单元测试,用于核实函数的某个方面没有问题
#测试用例是一组单元测试,这些单元测试一道核实函数在各种情况下的行为都符合要求
#全覆盖测试包含一整套单元测试

#可通过的测试
from name_function import get_formatted_name

def test_first_last_name():
    """能够正确地处理像 Janis Joplin这样的姓名吗?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
    #断言(assertion):声称满足特定的条件
#通过pytest调用这个函数，在终端窗口执行命令python -m pytest
#使用终端命令cd,使用命令dir可以显示当前目录中的所有文件
