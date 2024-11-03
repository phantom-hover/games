#sort()方法可以对列表进行按字母的永久排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print (cars)
#或进行传递参数 reverse=True 可以进行反向排序
cars.sort(reverse=True)
print (cars)
print("------------------分割线--------------------")

#sorted()函数在保留原排列顺序的同时，以特定顺序呈现它们
print ('Here is the original list:')
print (cars)
print ('\nHere is the sorted list:')
print (sorted(cars))
print ('\nHere is the original list again:')
print (cars)
print("------------------分割线--------------------")

#reverse()函数可以反转列表元素排列顺序
cars.reverse()
print (cars)
#并非按字母顺序相反排列，而是翻转列表元素的排列顺序，永久修改也可再次使用reverse()复原
print("------------------分割线--------------------")
#len()函数可以快速获悉列表的长度
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
