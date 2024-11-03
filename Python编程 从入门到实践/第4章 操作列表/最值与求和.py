#通过min(),max(),sum()函数分别找出该列表的最小值、最大值和总和
digit = [1,2,3,4,5,6,7,8,9,0]
print(sum(digit),max(digit),min(digit))
print ("----------------分割线-------------------")
#列表推导式将for循环和创建新元素的代码合成一行
squares=[value**2 for value in range (1,11)]
print(squares)
print ("----------------分割线-------------------")
#练习一：创建一个包含1~1 000 000的列表，并进行打印（按住Ctrl +C ）可停止输出，并对这些数求和
numbers = [number for number in range(1,1000000)]
print (min(numbers),sum(numbers))
#练习二：在1~100里面找出能被3整除的数并打印出来(拓展：可用if语句进行)
numbers = []
for number in range(1,100):
    if number%3==0:
        value = number
        numbers.append(value)
    else:
        number=number+1
print(numbers)