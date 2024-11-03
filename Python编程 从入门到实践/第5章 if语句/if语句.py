#简单if语句：一个条件测试+一个操作
#if conditional_test:
#    do something
#if-else语句，会执行两个操作中的一个
age = 17
if age >=18:
    print("You are old enough to vote!\nHave you registered to vote yet?")
else:
    print("Sorry,You are too young to vote.\nPlease register to vote as soon as you turn 18!")
print("----------------------------分割线---------------------------")
#if-elif-else，可以处理多个条件测试
age = 12
if age <4:
    print("Your admission cost is $0.")
elif age <18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is 40$.")
#可以对价格设定price为变量来统一输出，使代码更为简洁
#elif代码块可以使用多个，同时if-elif后面可以不跟else代码块。使处理更为清晰
#if-else和if-elif-else语句仅适用于只有一个条件满足的情况，如果必须检查你关心的所有条件，可以用不包含elif和else 的简单if语句
