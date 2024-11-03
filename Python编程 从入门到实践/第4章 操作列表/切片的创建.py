#复制列表：创建一个包含整个列表的切片，即省略起始索引和终止索引([:])
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
#不加[:]会使得两个变量指向同一个列表而并非复制列表
my_foods.append('ice cream')
friend_foods.append('cannoli')
print("My favorite foods are:",my_foods)
print("My friend's foods are:",friend_foods)
