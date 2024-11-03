#检查特殊元素
requested_toppings = ['mushrooms' , 'green peppers' , 'extra cheese ']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry , we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")
print("----------------------------分割线---------------------------")

#确认列表非空
requested_toppings =[]
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza")
print("----------------------------分割线---------------------------")

#使用多个列表
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(F"Adding {requested_topping}.")
    else:
        print(f"Sorry,we don't have {requested_topping}.")
print("\nFinished making your pizza")