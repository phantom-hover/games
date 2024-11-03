#异常是使用try-except代码块处理的，try-except代码块让Python执行指定的操作，同时告诉出现异常时候的做法
#处理ZeroDivisionError异常
#print(5/0)得到的Traceback：
"""
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    print(5/0)
          ~^~
ZeroDivisionError: division by zero
"""

#使用try-except代码块:如果try中代码运行无问题，将跳过except代码块，反之则运行
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

#使用异常避免崩溃:else代码块
#简单除法计算器
print("Give me two number, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
        #运行异常的做法
    else:
        print(answer)
    #只有try代码成功运行的代码需要放进else代码块中

#处理FileNotFoundError异常:
from pathlib import Path

path = Path('D:\\Desktop\\python_work\\Python编程 从入门到实践\\text_files\\alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
    #如果系统的默认代码与要读取的文件编码不一致，需要参数encoding
except FileExistsError:
    print(f"Sorry, the file {path} does not exist.")
#分析文本
else:
    #计算文件大致包含多少个单词
    words = contents.split()
    #对变量contents调用split()方法，生成一个列表包含所有单词
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")
