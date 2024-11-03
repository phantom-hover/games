cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())
print("----------------------------分割线---------------------------")
#检查是否相等，使用“==”相等运算符,忽略大小写需要用upper(),lower()
#检查是否不相等，使用不等运算符（!=）
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies")
#数学比较符号都可以成为if语句的一部分
print("----------------------------分割线---------------------------")
#and、or检查多个条件,其中and的多个条件必须全部满足，而or只需要满足其中一个
age_0=22
age_1=18
if age_0 >=20 and age_1>=20:
    print (True)
else:
    print (False)
print("----------------------------分割线---------------------------")
#in 和 not in 可以检查特定的值是否在列表中
requested_topping = ['mushrooms','onions','pineapple']
food = 'mushrooms'
if food in requested_topping:
    print(f'We have {food.title()}!')
else:
    print(f"Sorry ,{food.title()} was sold out")
#布尔表达式，常用于记录条件，其结果为"True" 或者 "False"