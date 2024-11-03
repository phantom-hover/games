#input()函数让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其赋给一个变量
message = input("Tell me something, and I will repeat it back to you:")
print(message)
#编写清晰的提示，通过在提示末尾添加空格，将提示与用户输入分开
name = input ("Please enter your name: ")
print(f"\nHello, {name}!")
#提示若超过一行，需要指出获取输入的原因，这种情况可以先将提示赋予一个变量，再将这个变量传递给input()函数
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")
#多行字符串：第一行消息的前半部分赋给变量prompt，第二行中，运算符+=在赋给变量prompt的字符串末尾追加一个字符串
print("----------------------------分割线---------------------------")

#用int()来获取数值输入
#使用input()函数会将用户输入解读为字符串
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

#求模运算符：验证一个数是奇数还是偶数
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")