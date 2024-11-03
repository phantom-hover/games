#列表：用【】表示列表，用逗号分隔其中元素
bicycles= ['trek' , 'cannondle' , 'redline' , 'specialized' ]
print (bicycles)
#列表指引，返回该元素,并加入title()
print (bicycles[1].title())
#注意：索引从0开始而非1

print(bicycles[-1])
#将索引指定为-1，则返回到最后一个列表元素，以此类推，-2、-3等

#f字符串根据列表中的值来创建消息
message=f'My first bicycle was a {bicycles[2].title()}'
print (message)