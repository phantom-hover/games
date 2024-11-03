#使用while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
#代码current_number += 1 是current_number = current_number + 1 的简写
#让用户选择何时退出，定义退出值
prompt = "\n退出值_Tell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
#将“quit”进行隐去
    if message != 'quit':
        print(message)

#使用标志，充当程序的交通信号灯，在while语句中检查标志当前值是否为True
active = True
messages = ''
while active:
    messages = input(prompt)

    if messages == 'quit':
        active = False
    else:
        print ()


