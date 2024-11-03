#在列表之间移动元素
#首先创建一个待验证用户列表，和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
#验证每个用户，直到没有未验证用户为止，将每个经过验证的用户都移动到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    #用方法pop()从列表删除一个未验证的用户
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
#显示所有已经验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
print("----------------------------分割线---------------------------")

#删除为特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
    #Python删除第一个'cat'返回while代码行，然后发现'cat'，则再次进入循环并不断删除
print(pets)
print("----------------------------分割线---------------------------")

#使用用户输入填充字典
responses = {}
#设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    #提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    #将回答存储到字典中
    responses[name] = response

    #看看是否还有人需要参与调查
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False

#调查结束，显示结果
print("\n--- Poll Results --- ")
for name, response in responses.items():
    print(f"{name} would like to climb {response}")