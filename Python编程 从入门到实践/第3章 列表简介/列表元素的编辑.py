#修改元素
motorcycles = ['honda' , 'yamaha' , 'suzuki']
print('1',motorcycles)

motorcycles[2]= 'ducati'
print('2',motorcycles)

#append()函数，将元素追加到列表末尾
motorcycles.append('suzuki')
print('3',motorcycles)
#可以创造一个空列表，再在其中通过append()来输入新值

#insert()函数，在任意列表位置添加新元素
motorcycles.insert(1,'kaqila')
print ('4',motorcycles)
#该操作使每个既有元素向右移动一个位置

#del语句，删除列表中的元素
del motorcycles [1]
print ('5',motorcycles)
#该语句删除即无法访问

#pop()函数删除元素，并可接着使用删除的值，其中括号里可以指定索引，其余默认为最后一个元素
popped_motorcycles = motorcycles.pop(2)
print ('6', motorcycles)
print (popped_motorcycles)

#remove()函数可以删除元素的值，并可以继续使用它的值
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print('7', motorcycles)
print (f'The reason:\nA {too_expensive.title()} is too expensive for me.')