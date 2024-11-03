#定义元组:可以使用索引访问其元素
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
#无法修改元组，若定义只包含一个元素的元组，需要在这个元素后面加上逗号
print ('------------------------------分割线-------------------------')
#遍历元组所有值，可用for循环语句
for dimension in dimensions:
    print(dimension)
print ('------------------------------分割线-------------------------')
#可以给表示元组的变量赋值,来修改元组
dimensions=(199,400)
for dimension in dimensions:
    print(dimension)
#代码缩进一般都使用四格
  