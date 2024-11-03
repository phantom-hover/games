#range()函数可轻松生成一系列数
for value in range (1,5):
    print (value)
#其中,range()只打印1-4，第一个值是开始数，第二个值是停止数
print ("----------------分割线-------------------")
#可以用range()函数创建数值列表，通过将其作为list()的参数，输出数值列表
numbers = list(range(1,6))
print(numbers)
#range()函数可以设置步长，即第三个参数
even_numbers = list(range(2,11,2))
print(even_numbers)
#两个星号(**)代表乘方运算，可将前10个数乘方加入一个列表
squares = []
for value in range(1,11):
    squares.append(value** 2)
print(squares)
