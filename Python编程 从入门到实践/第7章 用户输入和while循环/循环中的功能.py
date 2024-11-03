#使用break立即退出循环，不管条件测试的结果如何
#用于控制代码行的执行与否
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished)"
while True:
#True循环将不断运行，直至遇到break语句
    city = input()
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
#所有Python循环当中都可以使用break语句，如退出遍历列表或字典的for循环

#使用continue可以返回循环开头，并根据条件测试的结果决定是否继续执行循环
#让Python忽略余下的代码，并返回循环的开头
#下面例子为从1到10打出奇数循环，奇数continue并print,偶数忽略print并返回while循环开头+1
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 ==0:
        continue
    print(current_number)

#注意：避免无限循环，发成可以按Ctrl+C，或者关闭显示程序输出的终端窗口