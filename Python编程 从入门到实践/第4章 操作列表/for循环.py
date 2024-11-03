#使用for循环语句，让python去处理每个元素
magicians = ['alice','david','carolina']
for magician in magicians:
    #定义一个for循环，使这行代码从列表magicians中取出元素，并将其与变量magician相关联
    print(magician)
print('-------------------分割线--------------------')
for magician in magicians:
    print(f"{magician.title()},that was a great trick!")
    print(f"I can't wait to see your next trick,{magician.title()}.\n")
#缩进一格，执行一次，结束for循环
print ('Thank you ,everyone.That was a great magic show!')
#一定要注意缩进的地方
