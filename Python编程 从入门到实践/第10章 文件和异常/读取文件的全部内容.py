#打开并读取文件，要使用文件的内容，需要将其路径告知Python(文件或文件夹在系统中的准确位置)
from pathlib import Path
#pathlib模块可以在各种操作系统中处理文件和目录，提供特定功能的模块称为库
#Path对象指向一个文件。让你在使用文件前核实它是否存在，并将其赋予变量path


path = Path('D:\\Desktop\\python_work\\Python编程 从入门到实践\\text_files\\pi_digits.txt')
#由于换行符\t的原因特殊情况需要打\\
contents = path.read_text().rstrip()
#方法链式调用：先对当前文件调用方法，再对返回的字符串调用另一个方法，然后将整理好的字符串赋给变量
contents = contents.rstrip()
print(contents)

#read_text()在到达文件末尾时会返回一个空字符串，而这个空字符串会被显示为一个空行
#若删除这个多出来的空行，可对字符串变量contents调用rstrip()
"""
相对文件路径:让Python到相对于当前运行程序的所在目录的指定位置去查找
绝对文件路径:以系统的根文件夹为起点,告诉Python文件所在的准确位置
"""
#访问文件中的各行：使用splitlines()将冗长的字符串转换为一系列行，再使用for循环以每次一行的方式检查文件中的各行

lines = contents.splitlines()
pi_string = ''
for line in lines:
    #使用文件中的内容:创建变量存储文件里面的值
    pi_string += line.lstrip()
    #lstrip()可删除空格
print(pi_string)
print(len(pi_string))
#读取文件时,Python将其中的所有文本都解释为字符串
print('--------')

#包含100万位的大型文件
path = Path('D:\\Desktop\\python_work\\Python编程 从入门到实践\\text_files\\pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")