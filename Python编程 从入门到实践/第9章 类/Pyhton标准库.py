#标准库的函数
#模块random中的函数randint()
#它将两个整数作为一个参数，并随机返回一个位于这两个整数之间的整数
from random import randint
print(randint(1,6))

#choice()函数：它将一个列表或元组作为参数，并随机返回其中某个元素
from random import choice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)

#大驼峰式命名法：将类名中的每个单词的首字母都大写，并且不使用下划线。而实例名和模块名都采用全小写格式，并在单词之间加上下划线。
